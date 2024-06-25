# Description
Test retrieving full text using a DOI

# Code
```
import time
from indra.literature import id_lookup, get_full_text
from indra.util import unicode_strs

@pytest.mark.webservice
def test_get_full_text_doi():
    txt, txt_format = get_full_text('10.18632/oncotarget.2555', 'doi')
    assert txt_format == 'pmc_oa_xml'
    assert len(txt) > 300000

```
