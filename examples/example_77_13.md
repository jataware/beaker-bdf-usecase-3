# Description
Demonstrates using the IndraNet Assembler with collected statements and converting the IndraNet to signed graph.

# Code
```

def test_getting_started9_10():
    # Chunk 9
    # pa.export_model('sbml', file_name='model.sbml')

    # Chunk 10
    from indra.assemblers.indranet import IndraNetAssembler
    indranet_assembler = IndraNetAssembler(statements=_get_gene_network_stmts())
    indranet = indranet_assembler.make_model(method='df')
    assert len(indranet.nodes) > 0, 'indranet contains no nodes'
    assert len(indranet.edges) > 0, 'indranet contains no edges'

    # Chunk 11
    signed_graph = indranet.to_signed_graph()

```
