# Description
Test looking up metadata with DOI and PMC ID

# Code
```
import time
from indra.literature import id_lookup, get_full_text
from indra.util import unicode_strs

@pytest.mark.webservice
def test_id_lookup_no_pmid():
    """Look up a paper that has a PMCID and DOI but not PMID."""
    time.sleep(0.5)
    res = id_lookup('10.1083/jcb.1974if', 'doi')
    assert res['pmcid'] == 'PMC3352949'
    res = id_lookup('PMC3352949', 'pmcid')
    assert res['doi'] == '10.1083/jcb.1974if'

```
