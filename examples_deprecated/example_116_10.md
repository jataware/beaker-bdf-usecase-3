# Description
Testing retrieval of XML content for a given PMCID with prefix.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
pytest
indra.literature import pmc_client

@pytest.mark.webservice
def test_get_xml_PMC():
    pmc_id = 'PMC4322985'
    xml_str = pmc_client.get_xml(pmc_id)
    assert xml_str is not None

```
