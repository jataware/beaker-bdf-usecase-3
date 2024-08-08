# Description
Test the translation of a phosphorylation statement to English.

# Code
```
import indra.assemblers.english.assembler as ea

def test_phos_enz():
    a = Agent('MAP2K1')
    b = Agent('BRAF')
    st = Phosphorylation(b, a, 'serine', '222')
    sb = ea._assemble_modification(st)
    print(sb.sentence)
    assert sb.sentence == 'BRAF phosphorylates MAP2K1 on S222.'
    assert _substring_by_coords(sb.sentence, sb.agents[0].coords) == 'BRAF'

```
