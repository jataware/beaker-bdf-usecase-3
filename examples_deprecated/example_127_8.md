# Description
Put abstract content using s3_client's put_abstract function and validate the stored content.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import s3_client
from indra.util import unicode_strs
import zlib

def test_put_abstract():
    abstract = 'test_put_abstract'
    pmid_test = 'PMID000test2'
    s3_client.put_abstract(pmid_test, abstract)
    # Get the abstract back
    (content, content_type) = s3_client.get_full_text(pmid_test)
    assert content == abstract
    assert content_type == 'abstract'

```
