# Description
Retrieving MeSH annotations from the full XML of a PubMed article using `get_full_xml` and `get_metadata_from_xml_tree` methods.

# Code
```
import time
from indra.literature import pubmed_client

@pytest.mark.webservice
def test_get_annotations():
    time.sleep(0.5)
    pmid = '30971'
    tree = pubmed_client.get_full_xml(pmid)
    results = pubmed_client.get_metadata_from_xml_tree(tree,
                                                       mesh_annotations=True)
    assert len(results) == 1, len(results)
    assert 'mesh_annotations' in results[pmid], results[pmid]
    me_ans = results[pmid]['mesh_annotations']
    assert len(me_ans) == 9, len(me_ans)
    assert all(d['mesh'].startswith('D') for d in me_ans)

```
