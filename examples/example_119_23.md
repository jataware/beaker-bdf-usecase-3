# Description
Retrieving substance annotations for a PubMed article using the `get_substance_annotations` method and validating the presence of specific mesh IDs.

# Code
```
import time

def test_get_substance_annotations():
    pmid = '27959613'
    mesh_ids = pubmed_client.get_substance_annotations(pmid)
    example_mesh_id = 'D009570'
    wrong_mesh_id = 'D0074447'
    assert example_mesh_id in mesh_ids

```
