# Description
Match left-hand side (lhs) in rules

# Code
```
pysb import Monomer, Rule, Parameter
indra.explanation.model_checker.pysb import _match_lhs

def test__match_lhs():
    Monomer('A', ['other'], {'other': ['u', 'p']})
    Monomer('B', ['T185'], {'T185': ['u', 'p']})
    rule = Rule('A_phos_B', A() + B(T185='u') >> A() + B(T185='p'),
                Parameter('k', 1))
    matching_rules = _match_lhs(A(), model.rules)
    assert len(matching_rules) == 1
    assert matching_rules[0] == rule
    matching_rules = _match_lhs(A(other='u'), model.rules)

```
