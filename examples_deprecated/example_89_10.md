# Description
This example demonstrates how to check if a gene belongs to a specific category (kinase, phosphatase, transcription factor) using the `hgnc_client`.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.databases import hgnc_client
indra.util import unicode_strs

def test_is_category():
    assert hgnc_client.is_kinase('MAPK1')
    assert not hgnc_client.is_kinase('EGF')
    assert hgnc_client.is_phosphatase('PTEN')
    assert not hgnc_client.is_phosphatase('KRAS')
    assert hgnc_client.is_transcription_factor('FOXO3')

```
