# Description
Testing the random noise priors for evidence from various sources using the evidence random noise prior function and belief engine.

# Code
```
from copy import deepcopy
import pytest
from indra.statements import Evidence, Agent, Complex
from indra.belief import BeliefEngine, load_default_probs, SimpleScorer, evidence_random_noise_prior


def test_evidence_random_noise_prior():
    type_probs = {'biopax': 0.9, 'geneways': 0.2}
    biopax_subtype_probs = {
            'reactome': 0.4,
            'biogrid': 0.2}
    geneways_subtype_probs = {
            'phosphorylate': 0.5,
            'bind': 0.7}
    subtype_probs = {'biopax': biopax_subtype_probs,
                     'geneways': geneways_subtype_probs}

    ev_geneways_bind = Evidence(source_api='geneways', source_id=0,
                                pmid=0, text=None, epistemics={},
                                annotations={'actiontype': 'bind'})
    ev_biopax_reactome = Evidence(source_api='biopax', source_id=0,
                                  pmid=0, text=None, epistemics={},
                                  annotations={'source_sub_id': 'reactome'})
    ev_biopax_pid = Evidence(source_api='biopax', source_id=0,
                             pmid=0, text=None, epistemics={},
                             annotations={'source_sub_id': 'pid'})

    # Random noise prior for geneways bind evidence is the subtype prior,
    # since we specified it
    assert evidence_random_noise_prior(ev_geneways_bind, \
                                       type_probs, subtype_probs) == 0.7

    # Random noise prior for reactome biopax evidence is the subtype prior,
    # since we specified it
    assert evidence_random_noise_prior(ev_biopax_reactome, \
                                       type_probs, subtype_probs) == 0.4

    # Random noise prior for pid evidence is the subtype prior,
    # since we specified it
    assert evidence_random_noise_prior(ev_biopax_pid,
                                       type_probs, subtype_probs) == 0.9

    # Make sure this all still works when we go through the belief engine
    statements = []
    members = [Agent('a'), Agent('b')]
    statements.append(Complex(members, evidence=ev_geneways_bind))
    statements.append(Complex(members, evidence=ev_biopax_reactome))
    statements.append(Complex(members, evidence=ev_biopax_pid))
    p = {'rand': type_probs, 'syst': {'biopax': 0, 'geneways': 0}}

    scorer = SimpleScorer(p, subtype_probs)
    engine = BeliefEngine(scorer)
    engine.set_prior_probs(statements)
    assert statements[0].belief == 1 - 0.7
    assert statements[1].belief == 1 - 0.4

```
