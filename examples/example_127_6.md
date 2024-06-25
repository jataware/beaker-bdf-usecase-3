# Description
Get full text content using s3_client's get_full_text function and validate the results.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import s3_client
from indra.util import unicode_strs
import zlib

def test_get_full_text():
    (content, content_type) = s3_client.get_full_text('27297883')
    assert unicode_strs((content, content_type))
    assert content_type == 'txt'
    (content, content_type) = s3_client.get_full_text('1001287')
    assert unicode_strs((content, content_type))
    assert content_type == 'pmc_oa_xml'
    # TODO: Find a paper that has only abstract
    #(content, content_type) = s3_client.get_full_text('27653174')
    #assert unicode_strs((content, content_type))
    #assert content_type == 'abstract'
    (content, content_type) = s3_client.get_full_text('000000')

```
