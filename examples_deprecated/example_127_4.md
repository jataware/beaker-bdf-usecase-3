# Description
Get gzipped objects using s3_client's get_gz_object function and validate the results.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import s3_client
from indra.util import unicode_strs
import zlib

def test_get_gz_object():
    # Get XML
    key = 'papers/PMID27297883/fulltext/txt'
    obj = s3_client.get_gz_object(key)
    assert unicode_strs(obj)
    # Get reach output
    key = 'papers/PMID27297883/reach'
    obj = s3_client.get_gz_object(key)

```
