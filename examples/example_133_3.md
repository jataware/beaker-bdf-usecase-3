# Description
Example of processing another XML string involving phosphorylation with additional attributes, marking the test as slow and dependent on web services, and asserting various properties of the resulting statements using the `sparser` library.

# Code
```
from indra.sources import sparser
import pytest

xml_str2 = '''
<article pmid="12345">
<interpretation>
  <sentence-text>Hence ASPP2 can be phosphorylated at serine 827 by MAPK1 in vitro</sentence-text>
  <sem>
    <ref category="phosphorylate">
      <var name="subordinate-conjunction">
          <ref category="subordinate-conjunction"><var name="word">hence</var></ref></var>
      <var name="substrate">
          <ref category="protein">
              <var name="name">ASPP2_HUMAN</var>
              <var name="uid">UP:ASPP2_HUMAN</var>
          </ref>
      </var>
      <var name="agent">
        <ref category="protein">
          <var name="context">
            <ref category="in-vitro"></ref>
          </var>
          <var name="uid">UP:MK01_HUMAN</var>
          <var name="name">MK01_HUMAN</var>
        </ref>
      </var>
      <var name="site">
        <ref category="residue-on-protein">
          <var name="amino-acid">
            <ref category="amino-acid"><var name="name">serine</var></ref>
          </var>
          <var name="position"> 827</var>
        </ref>
      </var>
      <var name="modal"><ref category="can"></ref></var>
    </ref>
  </sem>
</interpretation>
</article>

def test_phosphorylation2():
    sp = sparser.process_xml(xml_str2)
    assert len(sp.statements) == 1
    assert sp.statements[0].enz.name == 'MAPK1'
    assert sp.statements[0].sub.name == 'TP53BP2'
    assert sp.statements[0].residue == 'S'
    assert sp.statements[0].position == '827'
    assert (len(sp.statements[0].evidence) == 1)
    ev = sp.statements[0].evidence[0]
    assert (ev.pmid == '12345')
    assert (ev.text)

```
