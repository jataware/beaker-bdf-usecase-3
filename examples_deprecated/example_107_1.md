# Description
Test the processing of SIF strings using the SifProcessor and verify the resulting statements.

# Code
```
import os
from indra.sources.minerva.api import *
from indra.sources.minerva.processor import SifProcessor
from indra.sources.minerva.minerva_client import get_model_ids
from indra.statements import Activation, Inhibition

models_to_ids = get_model_ids()
tgfb_id = models_to_ids['TGFbeta signalling']
apopt_id = models_to_ids['Apoptosis pathway']
model_id_to_sif_strs = {
    tgfb_id: ['sa44 POSITIVE csa5', 'sa18 NEGATIVE csa3'],
    apopt_id: ['sa18 POSITIVE sa15', 'csa2 POSITIVE sa9']

def test_process_sif_strs():
    sp = process_sif_strs(model_id_to_sif_strs)
    assert sp
    assert isinstance(sp, SifProcessor)
    assert len(sp.statements) == 4
    # Correct statement types
    assert isinstance(sp.statements[0], Activation)
    assert isinstance(sp.statements[1], Inhibition)
    assert isinstance(sp.statements[2], Activation)
    assert isinstance(sp.statements[3], Activation)
    # Using the same code ('sa18'), get different agents depending on model
    assert sp.statements[1].subj.name == 'MAPK3'
    assert sp.statements[1].subj.get_grounding() == ('HGNC', '6877')
    assert sp.statements[2].subj.name == 'CASP9'
    assert sp.statements[2].subj.get_grounding() == ('HGNC', '1511')
    # If possible, get FamPlex family
    # "sa44 POSITIVE csa5" is "ACVR1 POSITIVE SMAD2/3_complex"
    assert sp.statements[0].obj.name == 'SMAD2_3'
    assert sp.statements[0].obj.get_grounding() == ('FPLX', 'SMAD2_3')
    # Otherwise create Agent with BoundConditions
    # "csa2 POSITIVE sa9" is "csa2 POSITIVE sa9"
    assert sp.statements[3].subj.name == 'FAS'
    assert sp.statements[3].subj.bound_conditions
    assert sp.statements[3].subj.bound_conditions[0].agent.name == 'FASLG'
    # Both main agent and BoundCondition agent have groundings
    assert sp.statements[3].subj.get_grounding() == ('HGNC', '11920')
    assert sp.statements[3].subj.bound_conditions[0].agent.get_grounding() == (
        'HGNC', '11936')
    # Statements have evidence
    assert sp.statements[0].evidence
    assert sp.statements[0].evidence[0].source_api == 'minerva'
    assert sp.statements[0].evidence[0].annotations['sif_str'] == \
        'sa44 POSITIVE csa5'
    assert sp.statements[0].evidence[0].annotations['minerva_model_id'] == \

```
