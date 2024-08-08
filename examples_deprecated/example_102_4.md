# Description
Test looking up metadata using a PMID

# Code
```
import time
from indra.literature import id_lookup, get_full_text
from indra.util import unicode_strs

@pytest.mark.webservice
def test_id_lookup():
    time.sleep(0.5)
    res = id_lookup('17513615', 'pmid')

```
