# Description
Demonstrates processing a PMC article using the REACH processor.

# Code
```
from indra.sources import reach

@pytest.mark.nogha  # This test takes 10+ minutes, stalling Travis
def test_readme_using_indra2():
    from indra.sources import reach
    reach_processor = reach.process_pmc('PMC8511698', url=reach.local_nxml_url)

```
