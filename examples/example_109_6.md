# Description
Test embedding of complex pattern with Pervanadate

# Code
```
pysb import Monomer, Rule, Parameter, Annotation
indra.statements import Agent, Phosphorylation
indra.explanation.model_checker import PysbModelChecker

@with_model
def test_consumption_rule():
    pvd = Agent('Pervanadate', db_refs={'HGNC': '1'})
    erk = Agent('MAPK1', db_refs={'HGNC': '2'})
    stmt = Phosphorylation(pvd, erk, 'T', '185')
    # Now make the model
    Monomer('Pervanadate', ['b'])
    Monomer('DUSP', ['b'])
    Monomer('MAPK1', ['b', 'T185'], {'T185': ['u', 'p']})
    Rule('Pvd_binds_DUSP',
         Pervanadate(b=None) + DUSP(b=None) >>
         Pervanadate(b=1) % DUSP(b=1),
         Parameter('k1', 1))
    Rule('Pvd_binds_DUSP_rev',
         Pervanadate(b=1) % DUSP(b=1) >>
         Pervanadate(b=None) + DUSP(b=None),
         Parameter('k2', 1))
    Rule('DUSP_binds_MAPK1_phosT185',
         DUSP(b=None) + MAPK1(b=None, T185='p') >>
         DUSP(b=1) % MAPK1(b=1, T185='p'),
         Parameter('k3', 1))
    Rule('DUSP_binds_MAPK1_phosT185_rev',
         DUSP(b=1) % MAPK1(b=1, T185='p') >>
         DUSP(b=None) + MAPK1(b=None, T185='p'),
         Parameter('k4', 1))
    Rule('DUSP_dephos_MAPK1_at_T185',
         DUSP(b=1) % MAPK1(b=1, T185='p') >>
         DUSP(b=None) % MAPK1(b=None, T185='u'),
         Parameter('k5', 1))
    Annotation(Pervanadate, 'https://identifiers.org/hgnc:1')
    Annotation(MAPK1, 'https://identifiers.org/hgnc:2')
    Annotation('Pvd_binds_DUSP', 'Pervanadate', 'rule_has_subject')
    Annotation('Pvd_binds_DUSP', 'Pervanadate', 'rule_has_object')
    Annotation('Pvd_binds_DUSP', 'DUSP', 'rule_has_subject')
    Annotation('Pvd_binds_DUSP', 'DUSP', 'rule_has_object')
    Annotation('Pvd_binds_DUSP_rev', 'Pervanadate', 'rule_has_subject')
    Annotation('Pvd_binds_DUSP_rev', 'Pervanadate', 'rule_has_object')
    Annotation('Pvd_binds_DUSP_rev', 'DUSP', 'rule_has_subject')
    Annotation('Pvd_binds_DUSP_rev', 'DUSP', 'rule_has_object')
    Annotation('DUSP_dephos_MAPK1_at_T185', 'DUSP', 'rule_has_subject')
    Annotation('DUSP_dephos_MAPK1_at_T185', 'MAPK1', 'rule_has_object')
    MAPK1.site_annotations = [
            Annotation(('T185', 'p'), 'phosphorylation', 'is_modification'),
            Annotation('T185', 'T', 'is_residue'),
            Annotation('T185', '185', 'is_position'),
        ]
    # Now check the model against the statement
    mc = PysbModelChecker(model, [stmt])
    checks = mc.check_model()
    assert len(checks) == 1
    assert isinstance(checks[0], tuple)
    assert checks[0][0] == stmt
    pr = checks[0][1]
    assert pr.paths == [(('Pvd_binds_DUSP', 0),
                         ('DUSP_binds_MAPK1_phosT185', 1),
                         ('DUSP_dephos_MAPK1_at_T185', 1),

```
