# Description
Demonstrates creating a phosphorylation statement using INDRA's Phosphorylation and Agent classes.

# Code
```

def test_getting_started6():
    # Chunk 6
    from indra.statements import Phosphorylation, Agent
    braf = Agent('BRAF')
    map2k1 = Agent('MAP2K1')
    stmt = Phosphorylation(braf, map2k1)

```
