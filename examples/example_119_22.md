# Description
Fetching supplementary annotations for a PubMed article using the `get_mesh_annotations` method.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_supplementary_annotations():
    time.sleep(0.5)
    pmid = '30105248'
    anns = pubmed_client.get_mesh_annotations(pmid)
    assert len(anns) == 7, anns
    assert anns[0]['type'] == 'main'
    assert anns[0]['mesh'] == 'D053839'
    assert len(anns[0]['qualifiers']) == 1
    assert anns[0]['qualifiers'][0] == anns[0]['qualifier']
    supp_ann = anns[-1]
    assert supp_ann['type'] == 'supplementary'
    assert supp_ann['mesh'] == 'C000623891'

```
