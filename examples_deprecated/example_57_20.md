# Description
Testing the belief engine's cycle detection in hierarchical evidence structures.

# Code
```
copy import deepcopy
pytest
indra.statements import Evidence, Agent, Phosphorylation

def test_cycle():
    with pytest.raises(AssertionError):
        st1 = Phosphorylation(Agent('B'), Agent('A1'))
        st2 = Phosphorylation(None, Agent('A1'))
        st1.supports = [st2]
        st1.supported_by = [st2]
        st2.supports = [st1]
        st2.supported_by = [st1]
        engine = BeliefEngine()

```
