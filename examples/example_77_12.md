# Description
Shows how to use the PysbAssembler with statements and export the model in SBML format.

# Code
```
from indra.assemblers.pysb import PysbAssembler

@pytest.mark.nogha
def test_getting_started7_8():
    # Chunk 7
    stmts = _get_gene_network_stmts()  # Added only in this test, not in docs
    from indra.assemblers.pysb import PysbAssembler
    pa = PysbAssembler()
    pa.add_statements(stmts)
    model = pa.make_model()
    assert model

    # Chunk 8
    sbml_model = pa.export_model('sbml')

```
