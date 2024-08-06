# Description
Get upload content using s3_client's get_upload_content function and validate results based on abstract or full text availability.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import s3_client
from indra.util import unicode_strs
import zlib

def test_get_upload_content():
    pmid_s3_no_content = 'PMID000foobar'
    (ct, ct_type) = s3_client.get_upload_content(pmid_s3_no_content)
    assert ct is None
    assert ct_type is None

    pmid_s3_abstract_only = 'PMID000test4'
    s3_client.put_abstract(pmid_s3_abstract_only, 'foo')
    (ct, ct_type) = s3_client.get_upload_content(pmid_s3_abstract_only)
    assert ct == 'foo'
    assert ct_type == 'abstract'

    pmid_s3_fulltext = 'PMID000test5'
    s3_client.put_full_text(pmid_s3_fulltext, 'foo', full_text_type='txt')
    (ct, ct_type) = s3_client.get_upload_content(pmid_s3_fulltext)
    assert ct == 'foo'

```
