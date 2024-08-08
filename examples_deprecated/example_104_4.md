# Description
Test for evidence object creation from `process_file` method.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname
indra.sources.medscan.api import process_file
indra.statements import IncreaseAmount

def test_evidence():
    # Test that evidence object is created correctly
    fname = os.path.join(data_folder, 'test_ExpressionControl_positive.csxml')
    mp = process_file(fname, None)

    statements = mp.statements
    assert len(statements) == 2
    s0 = statements[0]

    assert len(s0.evidence) == 1
    assert isinstance(s0, IncreaseAmount)
    assert s0.evidence[0].source_api == 'medscan'
    assert s0.evidence[0].source_id == 'info:pmid/23455322'
    assert s0.evidence[0].pmid == '23455322'
    assert s0.evidence[0].text == 'Finally, we show that parp-1(-/-) mice' + \
                                  ' display a significant reduction in the' + \
                                  ' circulating hypoxia-induced ' + \
                                  'erythropoietin levels, number of ' + \
                                  'red cells and hemoglobin concentration.', \
        s0.evidence[0].text
    coords = s0.evidence[0].annotations['agents']['coords']
    assert isinstance(coords, list), type(coords)
    assert len(coords) == 2, len(coords)
    assert coords[0] == (90, 97), coords[0]

```
