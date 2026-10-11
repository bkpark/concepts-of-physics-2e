import unittest
import xml.etree.ElementTree as ET
from numbering import build_objects

class SummaryNumberingTests(unittest.TestCase):
    def test_alias_tracks_original_without_consuming_a_number(self):
        root=ET.fromstring('''<document xmlns="http://cnx.rice.edu/cnxml"><equation id="a"/><section><title>Section Summary</title><equation id="s"/></section><equation id="b"/></document>''')
        rules={'course':dict(scope='section',unnumbered_equation_ancestor_classes=[],relocated_ancestor_classes=[],relocated_exercise_types=[],backmatter_after_body=False,separate_exercise_counters=False,exercise_prefix=True,inline_exercise_prefix=True), 'overrides':{'course':{}},'summary_equation_aliases':{'m#s':'m#a'}}
        def run():return build_objects([{'module_id':'m','parents':[]}],{'m':root},'course',{'m':'1.2'},rules,lambda m,i:m+'-'+i)
        out=run()
        self.assertEqual(out['m','s']['label'],'1.2.1')
        self.assertEqual(out['m','b']['label'],'1.2.2')
        root.insert(0,ET.Element('{http://cnx.rice.edu/cnxml}equation',id='new'))
        out=run()
        self.assertEqual(out['m','s']['label'],'1.2.2')
        self.assertEqual(out['m','s']['anchor'],'m-s')
        self.assertEqual(out['m','b']['label'],'1.2.3')

if __name__=='__main__':unittest.main()
