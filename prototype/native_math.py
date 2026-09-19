"""Presentation-only adaptation of legacy MathML for native browser rendering."""
import xml.etree.ElementTree as ET
from mathml import math_node
NS='http://www.w3.org/1998/Math/MathML';M='{'+NS+'}'

def native_math(e):
    tree=ET.fromstring(math_node(e));changes=[]
    def walk(node,inherited_variant=None):
        tag=node.tag.split('}')[-1];variant=node.get('mathvariant',inherited_variant)
        for child in list(node):walk(child,variant)
        if tag=='mfenced':
            children=list(node);opening=node.get('open','(');closing=node.get('close',')')
            separators=''.join(node.get('separators',',').split());node.clear();node.tag=M+'mrow'
            def op(value):ET.SubElement(node,M+'mo',{'stretchy':'true'}).text=value
            if opening:op(opening)
            for i,child in enumerate(children):
                if i and separators:op(separators[min(i-1,len(separators)-1)])
                node.append(child)
            if closing:op(closing)
            changes.append('expand-mfenced')
        if variant in ('normal','bold') and tag in ('mi','mn','mo','mtext'):
            node.set('mathvariant','normal')
            if variant=='bold':node.set('style','font-weight:700');changes.append('bold-css')
        if node.get('fontstyle'):
            node.set('style',node.get('style','')+';font-style:'+node.get('fontstyle'));changes.append('fontstyle-css')
        if node.get('displaystyle')=='true':node.set('style',node.get('style','')+';math-style:normal')
        if node.text is not None and not node.text.strip():node.text=None
        if node.tail is not None and not node.tail.strip():node.tail=None
    walk(tree)
    # Avoid changing ElementTree's global namespace registry used for source evidence.
    xml=ET.tostring(tree,encoding='unicode')
    prefix=xml.split(':',1)[0][1:] if ':' in xml.split('>',1)[0].split(' ',1)[0] else None
    if prefix:xml=xml.replace('<'+prefix+':','<').replace('</'+prefix+':','</').replace('xmlns:'+prefix+'=', 'xmlns=')
    return xml,changes
