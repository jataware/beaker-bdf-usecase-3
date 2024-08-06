# Description
Test retrieving full text using a PMC ID

# Code
```
import time
from indra.literature import id_lookup, get_full_text
from indra.util import unicode_strs

@pytest.mark.webservice
def test_get_full_text_pmc():
    txt, txt_format = get_full_text('PMC4322985', 'pmcid')
    assert txt_format == 'pmc_oa_xml'
    assert len(txt) > 300000

```
