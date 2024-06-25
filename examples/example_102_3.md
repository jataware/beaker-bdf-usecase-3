# Description
Test retrieving a PubMed abstract using PMCID

# Code
```
import time
from indra.literature import id_lookup, get_full_text
from indra.util import unicode_strs

@pytest.mark.webservice
def test_get_full_text_pubmed_abstract():
    # DOI lookup in CrossRef fails for this one because of page mismatch
    txt, txt_format = get_full_text('27075779', 'pmid')
    assert txt_format == 'abstract'
    assert len(txt) > 800

```
