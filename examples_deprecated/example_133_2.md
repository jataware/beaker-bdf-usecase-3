# Description
Example of processing a valid XML string representing phosphorylation events and asserting various properties of the resulting statements using the `sparser` library.

# Code
```
from indra.sources import sparser

xml_str1 = '''
<article pmid="54321">
 <interpretation>
 <sentence-text>MEK1 phosphorylates ERK1</sentence-text>
 <sem>
     <ref category="phosphorylate">
         <var name="agent">
         <ref category="protein">
             <var name="name">MP2K1_HUMAN</var>
             <var name="uid">UP:MP2K1_HUMAN</var>
         </ref>
         </var>
         <var name="substrate">
            <ref category="protein">
                <var name="name">MK03_HUMAN</var>
                <var name="uid">UP:MK03_HUMAN</var>
            </ref>
         </var>
     <var name="present"><ref category="present"></ref></var>
     </ref>
 </sem>
 </interpretation>
</article>

def test_phosphorylation():
    sp = sparser.process_xml(xml_str1)
    assert len(sp.statements) == 1
    assert sp.statements[0].enz.name == 'MAP2K1'
    assert sp.statements[0].sub.name == 'MAPK3'
    assert len(sp.statements[0].evidence) == 1
    ev = sp.statements[0].evidence[0]
    assert ev.pmid == '54321'
    assert ev.text

```
