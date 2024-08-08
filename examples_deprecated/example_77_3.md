# Description
Shows how to search for recent abstracts in PubMed, process abstracts using REACH, and collect extracted statements.

# Code
```
indra.sources import reach
indra.literature import pubmed_client

@pytest.mark.slow
@pytest.mark.nogha
def test_readme_using_indra3():
    from indra.sources import reach
    from indra.literature import pubmed_client
    # Search for 10 most recent abstracts in PubMed on 'BRAF'
    pmids = pubmed_client.get_ids('BRAF', retmax=10)
    all_statements = []
    for pmid in pmids:
        abs = pubmed_client.get_abstract(pmid)
        if abs is not None:
            reach_processor = reach.process_text(abs, url=reach.local_text_url)
            if reach_processor is not None:
                all_statements += reach_processor.statements

```
