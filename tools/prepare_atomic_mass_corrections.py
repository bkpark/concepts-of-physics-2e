from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as E
from decimal import Decimal,ROUND_HALF_UP
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'reports/1.1/atomic-masses-audit';P=ROOT/'maintained/modules/m42699/index.cnxml'
C='{http://cnx.rice.edu/cnxml}';M='{http://www.w3.org/1998/Math/MathML}'
rows=json.loads((D/'comparison.json').read_text('utf-8')); base=P.read_bytes();source=base.decode('utf-8')
def math(x):return '<m:math>'+x+'</m:math>'
def number(x):return '<m:mn>'+x+'</m:mn>'
def sci(coef,power,unit):return math('<m:mrow>'+number(coef)+'<m:mo>×</m:mo><m:msup>'+number('10')+number(str(power))+'</m:msup><m:mspace width="0.167em"/><m:mtext>'+unit+'</m:mtext></m:mrow>')
def fmtmass(ref):
 v=Decimal(str(ref['mass']));u=Decimal(str(ref['uncertainty_u']))
 rounded_u=u.quantize(Decimal(1).scaleb(u.adjusted()-1),rounding=ROUND_HALF_UP) if u else u
 places=6 if not u else min(6,max(0,1-rounded_u.adjusted()))
 quantum=Decimal(1).scaleb(-places);value=format(v.quantize(quantum,rounding=ROUND_HALF_UP),'f');un=(u/quantum).quantize(Decimal(1),rounding=ROUND_HALF_UP)
 return value+('('+str(un)+')' if un else '')+('<sup>#</sup>' if ref['estimated'] else '')
def half(n):
 if n['half_life']=='stbl':return 'Stable'
 v=Decimal(n['half_life']);u=Decimal(n['uncertainty']);unit=n['unit'];power=0
 if unit in ['ky','My','Gy','Ty','Py','Ey','Zy']:
  scale={'ky':3,'My':6,'Gy':9,'Ty':12,'Py':15,'Ey':18,'Zy':21}[unit];power=v.adjusted()+scale;factor=Decimal(10)**(scale-power);v*=factor;u*=factor;unit='y'
 if unit=='m':unit='min'
 if unit=='ms' and v>=100:v/=1000;u/=1000;unit='s'
 places=max(0,-v.as_tuple().exponent,-u.as_tuple().exponent);q=Decimal(1).scaleb(-places);value=format(v.quantize(q),'f');unc=str((u/q).quantize(Decimal(1)))
 # Parenthetical uncertainty refers to the final quoted digits.
 coef=value+'('+unc+')'
 return sci(coef,power,unit) if power else coef+'\u00a0'+unit
beta_minus=math('<m:msup><m:mi>β</m:mi><m:mo>−</m:mo></m:msup>');beta_plus=math('<m:msup><m:mi>β</m:mi><m:mo>+</m:mo></m:msup>');alpha=math('<m:mi>α</m:mi>')
def modes(n):
 raw=n['decay_abundance'];parts=[];separate='e+=' in raw or ('B+=' in raw and 'EC=' in raw)
 for branch in raw.split(';'):
  m=re.match(r'([A-Za-z0-9+\-]+)(=|~)([0-9.eE+\-]+)',branch)
  if not m:continue
  mode,op,amount=m.groups()
  if mode=='IS' or Decimal(amount)<Decimal('0.1'):continue
  if mode=='B+' and separate:continue
  label={'A':alpha,'B-':beta_minus,'B+':'EC/'+beta_plus,'e+':beta_plus,'EC':'EC','SF':'SF','2B-':'double '+beta_minus,'IT':'IT'}.get(mode)
  if label is None:raise ValueError(branch)
  parts.append(label)
 return ', '.join(parts)
def abundance(r):
 raw=r.get('ciaaw2024_fraction')
 if raw is None:return ''
 raw=re.sub(r'\s+','',raw)
 if raw.startswith('['):
  a,b=raw[1:-1].split(',');return format(Decimal(a).scaleb(2),'f')+'–'+format(Decimal(b).scaleb(2),'f')+'%'
 m=re.fullmatch(r'(\d+(?:\.\d+)?)(?:\((\d+)\))?',raw);assert m,raw
 v=Decimal(m[1]);unc=m[2];v*=100
 if not unc:return format(v,'f')+'%'
 decimals=max(0,len(m[1].split('.')[1])-2) if '.' in m[1] else 0
 # At very coarse source precision retain explicit percentage uncertainty.
 u=Decimal(unc)*Decimal(10)**(-len(m[1].split('.')[1]))*100
 if decimals==0 and u<1:decimals=-u.as_tuple().exponent
 q=Decimal(1).scaleb(-decimals);return format(v.quantize(q),'f')+'('+str((u/q).quantize(Decimal(1)))+')%'
def text(e):
 if e.tag==M+'annotation':return ''
 return (e.text or '')+''.join(text(c)+(c.tail or '') for c in e)
def plain(xml):return ' '.join(text(E.fromstring('<root xmlns:m="'+M[1:-1]+'">'+xml+'</root>')).split())
updates=[];index=0
entry_re=r'<entry\b[^>]*?/>|<entry\b[^>]*>.*?</entry>'
def replace_row(match):
 global index
 old=match.group();entries=list(re.finditer(entry_re,old,re.S))
 if len(entries)!=7:return old
 cells=[plain(x.group()) for x in entries]
 if not cells[2].isdigit():return old
 r=rows[index];index+=1;assert int(cells[2])==r['A']
 vals={4:fmtmass(r['ame2020']),5:', '.join(x for x in [abundance(r),modes(r['nubase2020'])] if x),6:half(r['nubase2020'])}
 if r['Z']==71:vals[1]='Lutetium'
 new=old
 for i in sorted(vals,reverse=True):
  e=entries[i];attrs=re.match(r'<entry\b([^>]*?)(?:/?>)',e.group())[1].rstrip('/')
  new=new[:e.start()]+'<entry'+attrs+'>'+vals[i]+'</entry>'+new[e.end():]
 updates.append({'Z':r['Z'],'A':r['A'],'state':'ground','before':cells,'after':[plain(x.group()) for x in re.finditer(entry_re,new,re.S)]})
 if (r['Z'],r['A'])==(104,261):
  # NUBASE2020 isomer mass excess 101390(120)# keV and excitation 70(100)# keV.
  ref={'mass':r['ame2020']['mass']+70/931494.10242,'uncertainty_u':120/931494.10242,'estimated':True}
  vals2=['','Rutherfordium (metastable)','261',math('<m:mmultiscripts><m:mtext>Rf</m:mtext><m:mprescripts/><m:none/><m:mrow><m:mn>261</m:mn><m:mtext>m</m:mtext></m:mrow></m:mmultiscripts>'),fmtmass(ref),alpha,half({'half_life':'74','uncertainty':'5','unit':'s'})]
  add='<row id="atomic-masses-rf261m">'+''.join('<entry align="center">'+v+'</entry>' for v in vals2)+'</row>'
  updates.append({'Z':104,'A':261,'state':'metastable','before':None,'after':[plain(v) for v in vals2]});new+='\n'+add
 return new
out=re.sub(r'<row\b[^>]*>.*?</row>',replace_row,source,flags=re.S);assert index==160
out=out.replace('Percent Abundance or Decay Mode','Natural Abundance / Principal Decay Mode(s)')
notes='''<caption><para id="atomic-masses-data-sources">Masses are for neutral atoms in their nuclear ground states, except for the free neutron and the explicitly labeled metastable state. Sources: <link url="https://doi.org/10.1088/1674-1137/abddaf">AME2020</link> (atomic masses), <link url="https://doi.org/10.1088/1674-1137/abddae">NUBASE2020</link> (half-lives and decay modes), and <link url="https://www.ciaaw.org/isotopic-abundances.htm">CIAAW 2024</link> (natural isotopic compositions). Only selected isotopes are listed, so an element’s listed abundances need not sum to 100%.</para>
<para id="atomic-masses-precision">Masses are rounded to at most six decimal places. Parentheses give the uncertainty in the last quoted digits; for example, 3.52(18) min means 3.52 ± 0.18 min. Mass uncertainties smaller than half the last displayed unit are omitted. A superscript # marks a mass estimated from systematic trends. Carbon-12 has mass exactly 12 u by definition. Ranges describe natural variation in normal terrestrial materials; other abundances are representative values with their quoted uncertainties. Unusual materials can fall outside these ranges.</para>
<para id="atomic-masses-decay-notes">Only confirmed decay branches with evaluated fractions of at least 0.1% are listed. EC means electron capture, SF means spontaneous fission, and double <m:math><m:msup><m:mi>β</m:mi><m:mo>−</m:mo></m:msup></m:math> means double-beta decay. EC/<m:math><m:msup><m:mi>β</m:mi><m:mo>+</m:mo></m:msup></m:math> denotes a combined electron-capture/positron-emission branch when NUBASE does not separate the two contributions; it does not establish a separate branching fraction for each. “Stable” follows the evaluation and does not imply that every energetically possible decay has been excluded.</para>
<para id="atomic-masses-isomer-notes">The superscript m identifies a metastable nuclear state. For rutherfordium-261, the 2.1(2) s and 74(5) s entries follow the ground-state and isomer assignments in NUBASE2020, which flags their ordering as uncertain. Ground-state/isomer ordering is also uncertain for lawrencium-257 and seaborgium-263; the rows here follow the evaluation’s ground-state assignments. The rutherfordium-261m mass is estimated from the AME2020 ground-state mass and the NUBASE2020 excitation energy, with uncertainty based on the evaluated isomer mass excess.</para></caption>'''
out=out.replace('</tgroup>','</tgroup>\n'+notes,1)
intro='<para id="atomic-masses-reading-table">This table lists selected isotopes. Numbers in parentheses give uncertainties in the last quoted digits; for example, 3.52(18) means 3.52 ± 0.18. Abundance ranges show natural variation. See the <link target-id="atomic-masses-data-sources">table notes</link> for sources, decay-mode conventions, and metastable-state assignments.</para>\n'
out=out.replace('<table id="import-auto-id1169737762674"',intro+'<table id="import-auto-id1169737762674"',1);E.fromstring(out)
(D/'corrected-candidate.cnxml').write_bytes(out.encode('utf-8'))
(D/'proposed-row-changes.json').write_text(json.dumps(updates,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'rows':len(updates),'source_unchanged':P.read_bytes()==base,'candidate':str(D/'corrected-candidate.cnxml')}))
