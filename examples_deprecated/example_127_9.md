# Description
Put and get REACH output using s3_client's put_reader_output and get_reader_output functions, then validate the stored content.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.literature import s3_client
from indra.util import unicode_strs
import zlib

def test_reach_output():
    # Test put_reach_output
    reach_data = {'foo': 1, 'bar': {'baz': 2}}
    pmid = 'PMID000test3'
    reach_version = '42'
    source_text = 'pmc_oa_txt'
    s3_client.put_reader_output('reach', reach_data, pmid, reach_version, source_text)
    # Now get the data back
    retrieved_reach_data = s3_client.get_reader_output('reach', pmid)
    assert retrieved_reach_data == reach_data
    assert unicode_strs(retrieved_reach_data)
    # Get the reach version of the key we created
    ret_reach_version, ret_source_text = \
        s3_client.get_reader_metadata('reach', pmid)
    assert ret_reach_version == reach_version

```
