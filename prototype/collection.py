"""Read the editable collection; frozen identities are independent of hierarchy."""
import xml.etree.ElementTree as ET
C='{http://cnx.rice.edu/collxml}';M='{http://cnx.rice.edu/mdml}'
def read_sections(root,identities):
    registry={s['id'].split(':',1)[1]:s for s in identities}
    sections=[]
    def walk(content,parents):
        for e in content:
            if e.tag==C+'module':
                mid=e.get('document');identity=registry[mid]
                source=ET.parse(root/identity['source']).getroot()
                title=source.find('{http://cnx.rice.edu/cnxml}title')
                sections.append({'module_id':mid,'parents':parents,'title':''.join(title.itertext()),'source':identity['source'],'candidate_slug':identity['slug']})
            elif e.tag==C+'subcollection':
                walk(e.find(C+'content'),parents+[''.join(e.find(M+'title').itertext())])
            else:raise ValueError('Unsupported collection node '+e.tag)
    tree=ET.parse(root/'maintained/collections/introduction-to-physics.collection.xml')
    walk(tree.getroot().find(C+'content'),[])
    ids=[s['module_id'] for s in sections]
    if len(ids)!=len(set(ids)) or set(ids)!=set(registry):raise ValueError('Collection/identity registry mismatch')
    return sections
