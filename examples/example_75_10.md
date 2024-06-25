# Description
Test the sorting of statements by belief score.

# Code
```
import pytest

@pytest.mark.nonpublic
def test_sort_by_belief():
    p = dbr.get_statements(object="MEK", stmt_type="Inhibition",
                                  sort_by='belief', limit=10)
    assert p.statements
    beliefs = [s.belief for s in p.statements]
    assert beliefs == sorted(beliefs, reverse=True), \
        f"Beliefs mis-ordered!\nbeliefs: {beliefs}\n" \

```
