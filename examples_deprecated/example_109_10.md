# Description
Test phosphorylation annotations in PySB model

# Code
```
pysb import Monomer, Rule, Parameter, Initial, Annotation
indra.statements import Agent, Phosphorylation
indra.explanation.model_checker import PysbModelChecker, PathResult

@with_model
def test_phosphorylation_annotations():
    # Create the statement
    a = Agent('MEK1', db_refs={'HGNC': '6840'})
    b = Agent('ERK2', db_refs={'HGNC': '6871'})
    st1 = Phosphorylation(a, b, 'T', '185')
    st2 = Phosphorylation(a, b, None, None)
    st3 = Phosphorylation(a, b, 'Y', '187')
    # Now create the PySB model
    Monomer('A_monomer')
    Monomer('B_monomer', ['Thr185', 'Y187'],
            {'Thr185': ['un', 'phos'], 'Y187': ['u', 'p']})
    Rule('A_phos_B', A_monomer() + B_monomer(Thr185='un') >>
                     A_monomer() + B_monomer(Thr185='phos'),
         Parameter('k', 1))
    Initial(A_monomer(), Parameter('A_0', 100))
    Initial(B_monomer(Thr185='un', Y187='u'), Parameter('B_0', 100))
    # Add agent grounding
    Annotation(A_monomer, 'https://identifiers.org/hgnc:6840')
    Annotation(B_monomer, 'https://identifiers.org/hgnc:6871')
    Annotation('A_phos_B', 'A_monomer', 'rule_has_subject')
    Annotation('A_phos_B', 'B_monomer', 'rule_has_object')
    # Add annotations to the sites/states of the Monomer itself
    B_annot = [
        Annotation('Thr185', 'T', 'is_residue'),
        Annotation('Thr185', '185', 'is_position'),
        Annotation(('Thr185', 'phos'), 'phosphorylation', 'is_modification'),
        Annotation('Y187', 'Y', 'is_residue'),
        Annotation('Y187', '187', 'is_position'),
        Annotation(('Y187', 'p'), 'phosphorylation', 'is_modification'),
    ]
    B_monomer.site_annotations = B_annot
    mc = PysbModelChecker(model, [st1, st2, st3])
    results = mc.check_model()
    assert len(results) == 3
    assert isinstance(results[0], tuple)
    assert results[0][0] == st1
    assert results[0][1].paths == [(('A_phos_B', 0),
                                    ('B_monomer_Thr185_phos_obs', 0))]
    assert results[1][0] == st2
    assert results[1][1].paths == [(('A_phos_B', 0),
                                    ('B_monomer_Thr185_phos_obs', 0))]
    assert results[2][0] == st3

```
