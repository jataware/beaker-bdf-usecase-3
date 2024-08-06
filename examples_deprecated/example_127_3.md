# Description
Filter keys using s3_client's filter_keys function and validate the results.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import s3_client
from indra.util import unicode_strs
import zlib

def test_filter_keys():
    pmid_key = s3_client.get_pmid_key('1001287')
    key_list = s3_client.filter_keys(pmid_key)

```
