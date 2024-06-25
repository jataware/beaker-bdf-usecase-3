# Description
Assembling a SIF model with a Phosphorylation statement and saving it to a file.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
indra.assemblers.sif import SifAssembler

def test_modification():
    st1 = Phosphorylation(Agent('BRAF'), Agent('MAP2K1'), 'S', '222')
    sa = SifAssembler([st1])
    sa.make_model(True, True, True)
    assert len(sa.graph.nodes()) == 2
    assert len(sa.graph.edges()) == 1
    sa.save_model('test_sif.sif', True)
    with open('test_sif.sif', 'rb') as fh:
        txt = fh.read().decode('utf-8')

```
