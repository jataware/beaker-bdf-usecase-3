# Description
Testing extraction of text from custom XML string.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
pytest
indra.literature import pmc_client

@pytest.mark.webservice
def test_extract_text2():
    xml_str = '<article><body><p><p>some text</p>a</p></body></article>'
    text = pmc_client.extract_text(xml_str)
    assert text == 'a\nsome text\n'

```
