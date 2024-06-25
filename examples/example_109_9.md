# Description
Test distinguish path polarity with inhibition and dephosphorylation

# Code
```
pysb import Monomer, Parameter, Rule, Initial, Annotation
indra.statements import Agent, Phosphorylation, Dephosphorylation
indra.explanation.model_checker import PysbModelChecker, PathResult

@with_model
def test_distinguish_path_polarity2():
    """Test the ability to distinguish a positive from a negative regulation."""
    Monomer('A')
    Monomer('B', ['act'], {'act' : ['y', 'n']})
    Monomer('C', ['T185'], {'T185': ['u', 'p']})
    Parameter('k', 1)
    Rule('A_inhibit_B', A() + B(act='y') >> A() + B(act='n'), k)
    Rule('B_dephos_C', B(act='y') + C(T185='p') >>
                       B(act='y') + C(T185='u'), k)
    Initial(A(), k)
    Initial(B(act='y'), k)
    Initial(C(T185='p'), k)
    Annotation(A, 'https://identifiers.org/hgnc:1')
    Annotation(B, 'https://identifiers.org/hgnc:2')
    Annotation(C, 'https://identifiers.org/hgnc:3')
    Annotation('A_inhibit_B', 'A', 'rule_has_subject')
    Annotation('A_inhibit_B', 'B', 'rule_has_object')
    Annotation('B_dephos_C', 'B', 'rule_has_subject')
    Annotation('B_dephos_C', 'C', 'rule_has_object')
    C.site_annotations = [
            Annotation(('T185', 'p'), 'phosphorylation', 'is_modification'),
            Annotation('T185', 'T', 'is_residue'),
            Annotation('T185', '185', 'is_position'),
        ]
    # Create the model checker
    stmts = _path_polarity_stmt_list()
    mc = PysbModelChecker(model, stmts)
    results = mc.check_model()
    assert len(results) == len(stmts)
    assert isinstance(results[0], tuple)
    assert results[0][1].paths == [(('A_inhibit_B', 0), ('B_dephos_C', 1),
                                    ('C_T185_p_obs', 0))]
    assert results[1][1].paths == []
    assert results[2][1].paths == [(('A_inhibit_B', 0), ('B_dephos_C', 1),
                                    ('C_T185_p_obs', 0))], results[2][1].paths

```