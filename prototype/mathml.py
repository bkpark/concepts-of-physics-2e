import html, re
NS={'m':'http://www.w3.org/1998/Math/MathML'}
esc=lambda s:html.escape(str(s),quote=True)
local=lambda e:e.tag.rsplit('}',1)[-1]

class UnsupportedMath(Exception):pass
def M(tag,inner='',attrs=None):
    a=''.join(f' {esc(k)}="{esc(v)}"' for k,v in (attrs or {}).items())
    return f'<{tag}{a}>{inner}</{tag}>'
def fenced(s):return M('mrow',M('mo','(')+s+M('mo',')'))

def math_node(e):
    tag=local(e); attrs=dict(e.attrib)
    if tag=='apply':
        if not len(e):raise UnsupportedMath('Empty apply')
        op=local(e[0]); args=list(e)[1:]; vals=[math_node(x) for x in args]
        if op=='power':
            if len(vals)!=2:raise UnsupportedMath(f'power has {len(vals)} operands; expected 2')
            base=vals[0] if local(args[0]) in ('ci','cn','csymbol','mi','mn','msub') else fenced(vals[0])
            return M('msup',base+vals[1])
        if op=='divide' and len(vals)==2:return M('mfrac',''.join(vals))
        if op=='abs' and len(vals)==1:return M('mrow',M('mo','|')+vals[0]+M('mo','|'))
        operators={'eq':'=','gt':'&gt;','lt':'&lt;','times':'×','minus':'−','plus':'+','approx':'≈','scalarproduct':'⋅','vectorproduct':'×'}
        if op not in operators:raise UnsupportedMath('Unknown Content MathML operator '+op)
        if not vals:raise UnsupportedMath('Operator without operands '+op)
        if op=='minus' and len(vals)==1:return M('mrow',M('mo','−')+fenced(vals[0]))
        # Explicit grouping avoids changing precedence in mixed Content/Presentation input.
        vals=[fenced(v) if local(a)=='apply' and local(a[0]) in ('eq','plus','minus') else v for a,v in zip(args,vals)]
        if op=='times':
            out=vals[0]
            for i,v in enumerate(vals[1:],1):
                # Historical renderer uses juxtaposition for symbolic products.
                numeric=local(args[i-1]) in ('cn','mn') and (local(args[i]) in ('cn','mn') or (local(args[i])=='apply' and local(args[i][0])=='power'))
                out+=M('mo','×' if numeric else '&#x2062;')+v
            return M('mrow',out)
        return M('mrow',M('mo',operators[op]).join(vals))
    if tag=='cn' and attrs=={'type':'e-notation'}:
        # MathML 3 chapter 4: significand <sep/> decimal exponent.
        if len(e)!=1 or local(e[0])!='sep' or len(e[0]):raise UnsupportedMath('Malformed e-notation')
        significand=(e.text or '').strip();exponent=(e[0].tail or '').strip()
        if not significand or not re.fullmatch(r'[+\-−]?\d+',exponent):raise UnsupportedMath('Malformed e-notation exponent')
        return M('mrow',M('mn',esc(significand))+M('mo','×')+M('msup',M('mn','10')+M('mn',esc(exponent))))
    if tag in ('ci','cn','csymbol'):
        if set(attrs)-{'type'} or (attrs.get('type') and not(tag=='ci' and attrs['type']=='vector')):
            raise UnsupportedMath('Unsupported content-token attributes '+str(attrs))
        target={'ci':'mi','cn':'mn','csymbol':'mi'}[tag]
        body=esc(e.text or '')+''.join(math_node(x)+esc(x.tail or '') for x in e)
        if e.get('type')=='vector':return M('mi',body,{'mathvariant':'bold'})
        return M(target,body,{'mathvariant':'normal'} if tag=='csymbol' else {})
    if tag in ('annotation','annotation-xml'):
        return ''  # Original annotations retained in source sidecars; not display branches.
    allowed={'math','mrow','mi','mn','mo','mtext','mspace','mfrac','msqrt','mroot','msup','msub','msubsup','mover','munder','munderover','mtable','mtr','mtd','mstyle','mfenced','mmultiscripts','mprescripts','none','menclose','mpadded','semantics','sep'}
    if tag not in allowed:raise UnsupportedMath('Unknown MathML element '+tag)
    arity={'msup':2,'msub':2,'msubsup':3,'mfrac':2,'mroot':2,'mover':2,'munder':2,'munderover':3}.get(tag)
    if arity and len(e)!=arity:raise UnsupportedMath(f'{tag} has {len(e)} operands; expected {arity}')
    if tag=='semantics':tag='mrow'
    if tag=='mtr':
        # Renderer-only repair of direct mrow children; preserve row contents.
        return M('mtr',''.join(math_node(x) if local(x)=='mtd' else M('mtd',math_node(x)) for x in e),attrs)
    if 'width' in attrs:attrs['width']=re.sub(r'(?<=\d)\s+(?=em|ex|px)', '', attrs['width'])
    if tag=='math':attrs={'xmlns':NS['m'],'display':'block' if e.get('display') in ('block','display') else 'inline'}
    body=esc(e.text or '')+''.join(math_node(x)+esc(x.tail or '') for x in e)
    return M(tag,body,attrs)
