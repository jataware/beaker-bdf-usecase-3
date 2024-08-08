# Description
Test handling of non-existing gzipped object keys using s3_client's get_gz_object function.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import s3_client
from indra.util import unicode_strs
import zlib

def test_get_gz_object_nosuchkey():
    obj = s3_client.get_gz_object('foobar')

```
