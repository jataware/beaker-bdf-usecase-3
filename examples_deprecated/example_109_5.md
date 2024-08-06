# Description
Two-step phosphorylation model check

# Code
```
pysb import Monomer, Rule, Parameter, Initial, Annotation
indra.statements import Agent, Phosphorylation
indra.explanation.model_checker import PysbModelChecker, PathResult

@with_model
def test_two_step_phosphorylation():
    # Create the statement
    a = Agent('A', db_refs={'HGNC': '1'})
    b = Agent('B', db_refs={'HGNC': '2'})
    st = Phosphorylation(a, b, 'T', '185')
    # Now create the PySB model
    Monomer('A', ['b', 'other'], {'other': ['u','p']})
    Monomer('B', ['b', 'T185'], {'T185': ['u', 'p']})
    Rule('A_bind_B', A(b=None) + B(b=None, T185='u') >>
                     A(b=1) % B(b=1, T185='u'), Parameter('kf', 1))
    Rule('A_bind_B_rev', A(b=1) % B(b=1, T185='u') >>
                         A(b=None) + B(b=None, T185='u'), Parameter('kr', 1))
    Rule('A_phos_B', A(b=1) % B(b=1, T185='u') >>
                     A(b=None) + B(b=None, T185='p'),
                 Parameter('kcat', 1))
    Initial(A(b=None, other='p'), Parameter('Ap_0', 100))
    Initial(A(b=None, other='u'), Parameter('Au_0', 100))
    Initial(B(b=None, T185='u'), Parameter('B_0', 100))
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
    #with open('model_rxn.dot', 'w') as f:
    #    f.write(render_reactions.run(model))
    #with open('species_2step.dot', 'w') as f:
    #    f.write(species_graph.run(model))
    #generate_equations(model)
    # Now check the model
    mc = PysbModelChecker(model, [st])
    results = mc.check_model()
    assert len(results) == 1
    assert isinstance(results[0], tuple)
    assert results[0][0] == st
    pr = results[0][1]

```
