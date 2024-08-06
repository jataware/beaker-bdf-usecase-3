# Description
Testing extraction of text from valid XML content for a given PMCID without prefix.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
pytest
indra.literature import pmc_client

@pytest.mark.webservice
def test_extract_text():
    pmc_id = '4322985'
    xml_str = pmc_client.get_xml(pmc_id)
    text = pmc_client.extract_text(xml_str)
    assert text is not None
    assert 'RAS VS BRAF ONCOGENES AND TARGETED THERAPIES' in text

```
