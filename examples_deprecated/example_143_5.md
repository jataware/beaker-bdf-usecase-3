# Description
Parsing source IDs using 'parse_source_ids' function and validating the returned dictionary.

# Code
```

def test_parse_source_ids():
    sd = parse_source_ids('virhostnet-rid:2564|virhostnet-nrid:2199')
    assert sd == {'virhostnet-rid': '2564',

```
