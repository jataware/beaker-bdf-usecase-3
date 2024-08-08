# Description
Shows how to fetch PubMed IDs for a specific gene, retrieve full text using INDRA, process content with REACH, and assemble corpus with various INDRA tools.

# Code
```
indra import literature
indra.sources import reach
indra.tools import assemble_corpus as ac
indra.assemblers.cx import CxAssembler
indra.databases import ndex_client
indra.assemblers.indranet import IndraNetAssembler
networkx as nx
indra.assemblers.pysb import PysbAssembler

@pytest.mark.slow
@pytest.mark.nogha
def test_gene_network():
    # Chunk 1: this is tested in _get_gene_network_stmts
    # from indra.tools.gene_network import GeneNetwork
    # gn = GeneNetwork(['H2AX'])
    # biopax_stmts = gn.get_biopax_stmts()
    # bel_stmts = gn.get_bel_stmts()

    # Chunk 2
    from indra import literature
    pmids = literature.pubmed_client.get_ids_for_gene('H2AX')

    # Chunk 3
    from indra import literature
    paper_contents = {}
    for pmid in pmids:
        content, content_type = literature.get_full_text(pmid, 'pmid')
        if content_type == 'abstract':
            paper_contents[pmid] = content
        if len(paper_contents) == 5:  # Is 10 in actual code
            break

    # Chunk 4
    from indra.sources import reach

    literature_stmts = []
    for pmid, content in paper_contents.items():
        rp = reach.process_text(content, url=reach.local_text_url)
        literature_stmts += rp.statements
    print('Got %d statements' % len(literature_stmts))
    assert literature_stmts  # replaces a print statements

    # Chunk 6
    from indra.tools import assemble_corpus as ac
    # stmts = biopax_stmts + bel_stmts + literature_stmts  # tested elsewhere
    stmts = _get_gene_network_stmts() + literature_stmts  # Added instead of above line
    stmts = ac.map_grounding(stmts)
    stmts = ac.map_sequence(stmts)
    stmts = ac.run_preassembly(stmts)
    assert stmts

    # Chunk 7
    from indra.assemblers.cx import CxAssembler
    from indra.databases import ndex_client
    cxa = CxAssembler(stmts)
    cx_str = cxa.make_model()
    assert cx_str

    # Chunk 8
    # ndex_cred = {'user': 'myusername', 'password': 'xxx'}
    # network_id = ndex_client.create_network(cx_str, ndex_cred)
    # print(network_id)

    # Chunk 9
    from indra.assemblers.indranet import IndraNetAssembler
    indranet_assembler = IndraNetAssembler(statements=stmts)
    indranet = indranet_assembler.make_model()
    assert len(indranet.nodes) > 0, 'indranet conatins no nodes'
    assert len(indranet.edges) > 0, 'indranet conatins no edges'

    # Chunk 10
    import networkx as nx
    paths = nx.single_source_shortest_path(G=indranet, source='H2AX',
                                           cutoff=1)
    assert paths

    # Chunk 11
    from indra.assemblers.pysb import PysbAssembler
    pysb = PysbAssembler(statements=stmts)
    pysb_model = pysb.make_model()

```
