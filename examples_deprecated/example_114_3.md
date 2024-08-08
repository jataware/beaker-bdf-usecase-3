# Description
Test special cases for kinase names and ensure correct HGNC or FPLX identifiers are provided by _agent_from_str function.

# Code
```

def test_special_cases():
    # See http://phospho.elm.eu.org/kinases.html for list of kinases
    ag = _agent_from_str('Aurora A')
    assert ag.db_refs.get('HGNC') == '11393'

    ag = _agent_from_str('CCDPK')  # is non-human
    assert ag is None, ag

    ag = _agent_from_str('MAP2K_group')
    assert ag.db_refs.get('FPLX') == 'MAP2K'

    ag = _agent_from_str('PDHK4')
    assert ag.db_refs.get('HGNC') == '8812'

    # PDKC is probably a typo in the kinase table at
    # http://phospho.elm.eu.org/kinases.html but it is unclear what was
    # meant by the name from the source material: possibly PKC or SDK1.
    ag = _agent_from_str('PDKC')
    assert ag is None

    ag = _agent_from_str('PKA_alpha')
    assert ag.db_refs.get('HGNC') == '9380'

    ag = _agent_from_str('PKC_zeta')
    assert ag.db_refs.get('HGNC') == '9412'

    ag = _agent_from_str('RSK-5')
    assert ag.db_refs.get('HGNC') == '10434'

    ag = _agent_from_str('Titin kinase')

```
