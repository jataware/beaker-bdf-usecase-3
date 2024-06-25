# Description
Example of querying a deprecated protein ID and fetching its gene name using the Uniprot client.

# Code
```
indra.databases import uniprot_client
indra.util import unicode_strs

@pytest.mark.webservice
def test_query_protein_deprecated():
    g = uniprot_client.query_protein('Q8NHX1')
    assert g is not None
    gene_name = uniprot_client.get_gene_name('Q8NHX1')
    assert gene_name == 'MAPK3'
    assert unicode_strs(gene_name)
    gene_name = uniprot_client.get_gene_name('Q8NHX1', web_fallback=False)
    assert gene_name == 'MAPK3'

```
