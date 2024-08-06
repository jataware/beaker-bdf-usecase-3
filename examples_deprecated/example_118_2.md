# Description
Use the `get_pmids` method from the Pubchem client to retrieve PubMed IDs (PMIDs) associated with a given PubChem compound ID.

# Code
```

def test_get_pmids():
    pmids = pubchem_client.get_pmids('2244')
    example_pmid = '19036898'
    wrong_pmid = '17410596'
    assert example_pmid in pmids

```
