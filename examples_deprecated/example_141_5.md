# Description
Example of fetching synonyms (gene and protein) for a given protein ID using the Uniprot client.

# Code
```

def test_get_synonyms():
    upid = 'Q02750'  # This is MAP2K1
    gene_synonyms = uniprot_client.get_gene_synonyms(upid)
    assert gene_synonyms, gene_synonyms
    assert 'MEK1' in gene_synonyms
    protein_synonyms = uniprot_client.get_protein_synonyms(upid)
    assert protein_synonyms, protein_synonyms
    assert 'MKK1' in protein_synonyms
    all_synonyms = uniprot_client.get_synonyms(upid)
    assert set(gene_synonyms + protein_synonyms) == set(all_synonyms)

```
