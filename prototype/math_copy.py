"""Copy formats derived from rendered MathML, never from stale annotations.

No renderer is shipped to readers. ASCIIMath uses named symbols when supported,
Unicode fallbacks otherwise, and an invisible matrix for multiline layout.
"""
import re
import xml.etree.ElementTree as ET
from functools import lru_cache

GREEK = dict(zip('αβγδζηθικλμνξπρστυχψωΓΔΘΛΞΠΣΦΨΩ',
    'alpha beta gamma delta zeta eta theta iota kappa lambda mu nu xi pi rho sigma tau upsilon chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Phi Psi Omega'.split()))
# These mappings follow the MathJax ASCIIMath parser, not visual similarity.
ASCII_SYMBOLS = {**GREEK, 'ε':'epsilon','φ':'varphi','ϕ':'phi','ϑ':'vartheta','*':'**',
    '×':'xx','⋅':'*','·':'*','−':'-','–':'-','±':'+-','∓':'-+', '≈':'~~','≃':'~=',
    '≠':'!=','≤':'<=','≥':'>=','∝':'prop','∞':'oo','∂':'del','∇':'grad',
    '→':'->','←':'larr','↔':'harr','⇒':'=>','⇔':'<=>','∑':'sum','∏':'prod',
    '∫':'int','∮':'oint','∈':'in','∉':'!in','∩':'nn','∪':'uu','∧':'^^','∨':'vv',
    '⊥':'_|_','∠':'/_','…':'...','⋯':'cdots','⊗':'ox','⊙':'o.',
    '′':"'",'″':"''",'‴':"'''",'÷':'-:',
    '\u2062':'','\u2061':'','\u200b':'','\u00a0':' '}
TEX_SYMBOLS = {c:'\\'+name for c,name in GREEK.items()}
TEX_SYMBOLS.update({'ε':r'\varepsilon','ϵ':r'\epsilon','φ':r'\varphi','ϕ':r'\phi','ϑ':r'\vartheta',
    'ℏ':r'\hbar','ℓ':r'\ell','Å':r'\text{\AA}','°':r'{}^{\circ}',
    '×':r'\times','⋅':r'\cdot','·':r'\cdot','−':'-','–':'-','±':r'\pm','∓':r'\mp',
    '≈':r'\approx','≃':r'\simeq','≠':r'\ne','≤':r'\le','≥':r'\ge','∝':r'\propto',
    '∞':r'\infty','∂':r'\partial','∇':r'\nabla','→':r'\to','←':r'\leftarrow',
    '↔':r'\leftrightarrow','⇒':r'\Rightarrow','⇔':r'\Leftrightarrow','∑':r'\sum',
    '∏':r'\prod','∫':r'\int','∮':r'\oint','∈':r'\in','∉':r'\notin','∩':r'\cap',
    '∪':r'\cup','⊥':r'\perp','∠':r'\angle','…':r'\ldots','′':r'\prime',
    '″':r'\prime\prime','‴':r'\prime\prime\prime','÷':r'\div',
    '\u2062':'','\u2061':'','\u200b':'','\u00a0':r'\,','{':r'\{','}':r'\}',
    '%':r'\%','$':r'\$','#':r'\#','&':r'\&','_':r'\_','\\':r'\backslash','’':r'\text{’}'})
FUNCTIONS = set('sin cos tan sec csc cot arcsin arccos arctan sinh cosh tanh exp log ln lim min max det'.split())

def tag(e): return e.tag.rsplit('}',1)[-1]
def text(e): return ''.join(e.itertext()).strip()
def escape_tex(s):
    return ''.join({'\\':r'\textbackslash{}','{':r'\{','}':r'\}','_':r'\_',
        '%':r'\%','$':r'\$','#':r'\#','&':r'\&','^':r'\textasciicircum{}','~':r'\textasciitilde{}'}.get(c,c) for c in s)

class Converter:
    def __init__(self, fmt):
        self.fmt=fmt
        self.notes=set()
        self.table_depth=0

    def token(self,e):
        s=re.sub(r'\s+',' ',text(e)); t=tag(e)
        if not s:return ''
        mapping=TEX_SYMBOLS if self.fmt=='latex' else ASCII_SYMBOLS
        if s in mapping:return mapping[s]
        if re.fullmatch(r'[+−-]?\d+(?:[.,]\d+)*|\.\d+',s):
            if self.fmt=='asciimath' and ',' in s:return '"'+s+'"'
            return s.replace('−','-')
        if s in FUNCTIONS:return '\\'+s if self.fmt=='latex' else s
        if t=='mo':
            if self.fmt=='asciimath' and self.table_depth and s in ('(',')','[',']','{','}'):
                # Literal fences cannot interfere with the matrix's row syntax,
                # even when the legacy source has an unmatched fence.
                return '"'+s+'"'
            if self.fmt=='asciimath' and s in (',',';'):return '"'+s+'"'
            return ' '.join(mapping.get(c,c) for c in s)
        if len(s)==1 and not s.isascii():
            self.notes.add('unicode')
            if self.fmt=='latex':self.notes.add('unicode-latex')
            return s
        if self.fmt=='latex':
            if t=='mtext' or (t=='mi' and e.get('mathvariant')=='normal'):
                return r'\mathrm{'+escape_tex(s)+'}' if re.fullmatch(r'[A-Za-z]+',s) else r'\text{'+escape_tex(s)+'}'
            if re.fullmatch(r'[A-Za-z]',s):return s
            # Preserve combined source text rather than guessing its algebra.
            return r'\mathit{'+escape_tex(s)+'}' if t=='mi' else r'\text{'+escape_tex(s)+'}'
        if t=='mi' and e.get('mathvariant')!='normal' and re.fullmatch(r'[A-Za-z]+',s):
            # Spaces prevent accidental reserved words (e.g. product of s,i,n).
            return ' '.join(s)
        if '"' in s:
            # ASCIIMath has no reliable quote escape; preserve quote as Unicode.
            self.notes.add('unicode');s=s.replace('"','″')
        return '"'+s+'"'

    def seq(self,children):
        children=list(children); out=[]; i=0
        while i<len(children):
            c=children[i]
            if self.fmt=='asciimath' and tag(c)=='mo' and text(c)=='/' and out and i+1<len(children):
                out[-1]='('+out[-1]+')/('+self.convert(children[i+1])+')';i+=2
            else:out.append(self.convert(c));i+=1
        return ' '.join(filter(None,out))

    def script(self,base,sub=None,sup=None):
        if self.fmt=='latex':
            return '{'+base+'}'+('_{'+sub+'}' if sub else '')+('^{'+sup+'}' if sup else '')
        simple=bool(re.fullmatch(r'[\w]+|"[^"]*"',base))
        grouped='""' if not base else base if simple or (base.startswith('(') and base.endswith(')')) else '{: '+base+' :}'
        return grouped+('_('+sub+')' if sub else '')+('^('+sup+')' if sup else '')

    def convert(self,e):
        t=tag(e); c=list(e)
        if t in ('annotation','annotation-xml','none','mprescripts'):return ''
        if t=='semantics':return self.convert(c[0]) if c else ''
        if t in ('mi','mn','mo','mtext'):
            out=self.token(e)
            if 'bold' in e.get('mathvariant','') or 'font-weight:700' in e.get('style',''):
                return r'\boldsymbol{'+out+'}' if self.fmt=='latex' else 'bb('+out+')'
            return out
        if t=='mspace':return r'\,' if self.fmt=='latex' else ' '
        if t in ('math','mrow','mstyle','mpadded','mtd','mtr'):
            return self.seq(c)
        if t=='mfrac':
            a,b=map(self.convert,c)
            return r'\frac{'+a+'}{'+b+'}' if self.fmt=='latex' else '('+a+')/('+b+')'
        if t in ('msup','msub','msubsup'):
            return self.script(self.convert(c[0]),self.convert(c[1]) if t!='msup' else None,
                self.convert(c[-1]) if t!='msub' else None)
        if t in ('msqrt','mroot'):
            a=self.seq(c) if t=='msqrt' else self.convert(c[0])
            if self.fmt=='latex':return r'\sqrt'+('['+self.convert(c[1])+']' if t=='mroot' else '')+'{'+a+'}'
            return ('root('+self.convert(c[1])+')' if t=='mroot' else 'sqrt')+'('+a+')'
        if t in ('mover','munder','munderover'):
            a=self.convert(c[0]); acc=text(c[-1])
            accents={'¯':('overline','bar'),'‾':('overline','bar'),'→':('vec','vec'),'⃗':('vec','vec'),
                '^':('hat','hat'),'ˆ':('hat','hat'),'~':('tilde','tilde'),'˜':('tilde','tilde'),
                '˙':('dot','dot'),'ˉ':('overline','bar'),'¨':('ddot','ddot')}
            if t=='mover' and acc in accents:
                latex,ascii=accents[acc]
                return '\\'+latex+'{'+a+'}' if self.fmt=='latex' else ascii+'('+a+')'
            if t=='munderover':return self.script(a,self.convert(c[1]),self.convert(c[2]))
            cmd='overset' if t=='mover' else 'underset';b=self.convert(c[1])
            return '\\'+cmd+'{'+b+'}{'+a+'}' if self.fmt=='latex' else cmd+'('+b+')('+a+')'
        if t=='mmultiscripts':
            base=self.convert(c[0]); post=[];pre=[];dest=post
            for child in c[1:]:
                if tag(child)=='mprescripts':dest=pre
                else:dest.append(self.convert(child))
            for i in range(0,len(post),2):base=self.script(base,*post[i:i+2])
            prefix=''
            for i in range(0,len(pre),2):prefix+=self.script('',*pre[i:i+2])+' '
            return prefix+base
        if t=='mtable':
            self.notes.add('multiline')
            self.table_depth+=1
            rows=[[self.convert(cell) for cell in row] for row in c]
            self.table_depth-=1
            if self.fmt=='latex':
                width=max(map(len,rows),default=1)
                align=e.get('columnalign','left').split();align=(align+[align[-1]]*width)[:width]
                spec=''.join({'left':'l','right':'r','center':'c'}.get(a,'l') for a in align)
                return r'\begin{array}{'+spec+'}\n'+' \\\\\n'.join(' & '.join(row+['']*(width-len(row))) for row in rows)+'\n'+r'\end{array}'
            # Invisible outer delimiters; cell and row commas are structural.
            return '{: '+',\n'.join('('+','.join(cell or '""' for cell in row)+')' for row in rows)+' :}'
        if t=='menclose':
            a=self.seq(c);notation=e.get('notation','longdiv')
            if notation=='updiagonalstrike':
                self.notes.add('cancel')
                return r'\cancel{'+a+'}' if self.fmt=='latex' else 'cancel('+a+')'
            raise ValueError('Unsupported enclosure: '+notation)
        raise ValueError('Unsupported copy element: '+t)

@lru_cache(maxsize=16000)
def copy_formats(rendered):
    root=ET.fromstring(rendered); result={}; notes=set()
    # Legacy importers split decimal digits across nested layout-only rows.
    # Rejoin these for readable copy text without rewriting textbook source.
    def tidy(e):
        for c in list(e):tidy(c)
        if tag(e) not in ('math','mrow','mtd'):return
        flattened=[]
        has_slash=any(tag(c)=='mo' and text(c)=='/' for c in e)
        for c in e:
            if tag(c)=='mrow' and not c.attrib and not has_slash and not any(tag(x)=='mo' and text(x)=='/' for x in c):flattened.extend(list(c))
            else:flattened.append(c)
        e[:]=flattened
        i=0
        while i+2<len(e):
            a,b,c=e[i:i+3]
            if (all(tag(x) in ('mn','mtext') for x in (a,b,c)) and
                re.fullmatch(r'\d+',text(a)) and text(b)=='.' and re.fullmatch(r'\d+',text(c))):
                n=ET.Element('{http://www.w3.org/1998/Math/MathML}mn');n.text=text(a)+'.'+text(c)
                e[i:i+3]=[n]
            else:i+=1
    tidy(root)
    for fmt in ('latex','asciimath'):
        cv=Converter(fmt)
        result[fmt]=cv.convert(root).strip();notes.update(cv.notes)
    result['notes']=sorted(notes)
    return result
