# Description
Test the assembly of sentences for complex formation statements.

# Code
```
import indra.assemblers.english.assembler as ea

def test_complex_more():
    a = Agent('MAP2K1')
    b = Agent('BRAF')
    c = Agent('RAF1')
    st = Complex([a, b, c])
    sb = ea._assemble_complex(st)
    print(sb.sentence)
    assert sb.sentence == 'MAP2K1 binds BRAF and RAF1.'
    assert _substring_by_coords(sb.sentence, sb.agents[0].coords) == 'MAP2K1'
    assert _substring_by_coords(sb.sentence, sb.agents[1].coords) == 'BRAF'

```
