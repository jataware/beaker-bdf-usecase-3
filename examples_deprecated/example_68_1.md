# Description
A unit test for the citation count retrieving functionalities of the `coci_client` module from `indra.literature`. The test is skipped because the COCI web service is not currently working.

# Code
```
from unittest import skip

@skip('COCI web service not working currently')
def test_citation_count():
    pmid = '24624335'
    doi = '10.1016/J.redox.2013.12.020'
    assert coci_client.get_citation_count_for_pmid(pmid) > 200

```
