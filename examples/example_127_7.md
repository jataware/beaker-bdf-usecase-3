# Description
Put full text content using s3_client's put_full_text function and validate the stored content.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import s3_client
from indra.util import unicode_strs
import zlib

def test_put_full_text():
    full_text = 'test_put_full_text'
    pmid_test = 'PMID000test1'
    s3_client.put_full_text(pmid_test, full_text, full_text_type='pmc_oa_txt')
    # Get the full text back
    (content, content_type) = s3_client.get_full_text(pmid_test)
    assert content == full_text
    assert content_type == 'pmc_oa_txt'

```
