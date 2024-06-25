# Description
Gzip a string using s3_client's gzip_string function and verify decompressed content.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import s3_client
from indra.util import unicode_strs
import zlib

def test_gzip_string():
    content = 'asdf'
    content_enc = s3_client.gzip_string(content, 'content')
    content_dec = zlib.decompress(content_enc, 16+zlib.MAX_WBITS)
    content_dec_uni = content_dec.decode('utf-8')

```
