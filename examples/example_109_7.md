# Description
Test dephosphorylation statement with different policies

# Code
```
indra.statements import Agent, Dephosphorylation
indra.assemblers.pysb.assembler import PysbAssembler

def test_dephosphorylation():
    dusp = Agent('DUSP6', db_refs={'HGNC':'1'})
    mapk1 = Agent('MAPK1', db_refs={'HGNC':'2'})
    stmt = Dephosphorylation(dusp, mapk1, 'T', '185')

    def check_policy(policy, result):
        pysba = PysbAssembler()
        pysba.add_statements([stmt])
        pysba.make_model(policies=policy)
        mc = PysbModelChecker(pysba.model, [stmt])
        checks = mc.check_model()
        assert len(checks) == 1
        assert isinstance(checks[0], tuple)
        assert checks[0][0] == stmt
        pr = checks[0][1]
        assert pr.paths == result

    check_policy('one_step', [(('DUSP6_dephosphorylation_MAPK1_T185', 0),
                               ('MAPK1_T185_p_obs', 1))])
    check_policy('two_step', [(('DUSP6_dephosphorylation_MAPK1_T185', 0),
                               ('MAPK1_T185_p_obs', 1))])

```
