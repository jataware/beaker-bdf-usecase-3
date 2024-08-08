# Description
Parsing PSI-MI terms using 'parse_psi_mi' function and validating the returned values.

# Code
```

def test_parse_psi_mi():
    res = parse_psi_mi('psi-mi:"MI:0915"(physical association)')
    assert len(res) == 2, res
    assert res[0] == 'MI:0915', res

```
