# Description
Check PubMed ID (PMID) using s3_client's check_pmid function and validate the results.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import s3_client
from indra.util import unicode_strs
import zlib

def test_check_pmid():
    pmid = s3_client.check_pmid(12345)
    assert pmid == 'PMID12345'
    assert unicode_strs(pmid)
    pmid = s3_client.check_pmid('12345')
    assert pmid == 'PMID12345'
    assert unicode_strs(pmid)
    pmid = s3_client.check_pmid('PMID12345')
    assert pmid == 'PMID12345'

```
