# Description
Get PMID key using s3_client's get_pmid_key function and validate the results.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import s3_client
from indra.util import unicode_strs
import zlib

def test_get_pmid_key():
    pmid = '12345'
    pmid_key = s3_client.get_pmid_key(pmid)
    assert pmid_key == s3_client.prefix + 'PMID12345'

```
