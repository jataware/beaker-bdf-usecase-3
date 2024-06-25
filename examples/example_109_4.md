# Description
One-step phosphorylation model check

# Code
```
pysb import Monomer, Rule, Parameter, Initial, Annotation
indra.statements import Agent, Phosphorylation
indra.explanation.model_checker import PysbModelChecker, PathResult

@with_model
def test_one_step_phosphorylation():
    # Create the statement
    a = Agent('A', db_refs={'HGNC': '1'})
    b = Agent('B', db_refs={'HGNC': '2'})
    st = Phosphorylation(a, b, 'T', '185')
    # Now create the PySB model
    Monomer('A')
    Monomer('B', ['T185'], {'T185': ['u', 'p']})
    Rule('A_phos_B', A() + B(T185='u') >> A() + B(T185='p'),
         Parameter('k', 1))
    Initial(A(), Parameter('A_0', 100))
    Initial(B(T185='u'), Parameter('B_0', 100))
    # Add annotations
    Annotation(A, 'https://identifiers.org/hgnc:1')
    Annotation(B, 'https://identifiers.org/hgnc:2')
    Annotation('A_phos_B', 'A', 'rule_has_subject')
    Annotation('A_phos_B', 'B', 'rule_has_object')
    B.site_annotations = [
        Annotation(('T185', 'p'), 'phosphorylation', 'is_modification'),
        Annotation('T185', 'T', 'is_residue'),
        Annotation('T185', '185', 'is_position'),
    ]
    mc = PysbModelChecker(model, [st])
    results = mc.check_model()
    assert len(results) == 1
    assert isinstance(results[0], tuple)
    assert results[0][0] == st
    pr = results[0][1]
    assert isinstance(pr, PathResult)

```
