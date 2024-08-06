# Description
Testing the tagging of evidence subtypes across multiple sources.

# Code
```
copy import deepcopy
pytest
indra.statements import Evidence

def test_evidence_subtype_tagger():
    #Test for reach evidence
    evidence_reach = Evidence(source_api='reach', source_id=0,
            pmid=0, text=None, epistemics={},
            annotations={'found_by': 'Positive_early_activation'})
    (stype, subtype) = tag_evidence_subtype(evidence_reach)
    assert stype == 'reach'
    assert subtype == 'Positive_early_[^_]*'

    #Test for biopax evidence
    evidence_biopax = Evidence(source_api='biopax', source_id=0,
            pmid=0, text=None, epistemics={},
            annotations={'source_sub_id': 'reactome'})
    (stype, subtype) = tag_evidence_subtype(evidence_biopax)
    assert stype == 'biopax'
    assert subtype == 'reactome'

    #Test for geneways evidence
    evidence_geneways = Evidence(source_api='geneways', source_id=0,
            pmid=0, text=None, epistemics={},
            annotations={'actiontype': 'bind'})
    (stype, subtype) = tag_evidence_subtype(evidence_geneways)
    assert stype == 'geneways'
    assert subtype == 'bind'

    #Test for unsupported evidence
    evidence_donald_duck = Evidence(source_api='donald_duck', source_id=0,
            pmid=29053813, text=None, epistemics={'direct': True},
            annotations={'quack': 'quack',
                         'quack?' : 'QUAAAAAAAAACK!'})
    (stype, subtype) = tag_evidence_subtype(evidence_donald_duck)
    assert stype == 'donald_duck'

```
