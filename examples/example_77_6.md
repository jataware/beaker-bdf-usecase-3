# Description
Demonstrates processing a text description of a mechanism using TRIPS and assembling the model using PysbAssembler from the modeling.rst documentation.

# Code
```
from indra.sources import trips

def test_nl_modeling():
    # 1 code chunk
    from indra.sources import trips
    model_text = 'MAP2K1 phosphorylates MAPK1 and DUSP6 dephosphorylates MAPK1.'
    tp = trips.process_text(model_text)

    # 2nd code chunk
    for st in tp.statements:
        assert st.evidence[0].text  # Replaces a print statement in the doc

    # 3rd code chunk
    from indra.assemblers.pysb import PysbAssembler
    pa = PysbAssembler()
    pa.add_statements(tp.statements)
    pa.make_model(policies='two_step')

    # 4th code chunk
    for monomer in pa.model.monomers:
        assert monomer  # This replaces a print statements in the doc

    # 5th code chunk
    for rule in pa.model.rules:
        assert rule  # This replaces a print statements in the doc

    # 6th code chunk
    for parameter in pa.model.parameters:
        assert parameter  # This replaces a print statements in the doc

    # 7th code chunk
    for annotation in pa.model.annotations:
        assert annotation  # This replaces a print statements in the doc

    # 8th code chunk (this code is currently in a commented out section)
    pa.set_context('A375_SKIN')
    for monomer_pattern, parameter in pa.model.initial_conditions:
        assert monomer_pattern
        assert parameter.value

    # 9th code chunk
    _ = pa.export_model('sbml')
    assert _
    _ = pa.export_model('bngl')
    assert _

    # 10th code chunk

```
