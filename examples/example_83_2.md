# Description
Fix invalidities in evidence object using the `fix_invalidities_evidence` function.

# Code
```
from indra.statements import Evidence

def test_fix_evidence():
    ev = Evidence(pmid='123', text_refs={'pmcid': 'PMC1234'})
    fix_invalidities_evidence(ev)
    assert ev.pmid == '123'

```
