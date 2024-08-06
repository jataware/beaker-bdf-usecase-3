# Description
Parsing text references using 'parse_text_refs' function and validating the returned dictionary.

# Code
```

def test_parse_text_refs():
    tr = parse_text_refs('pubmed:22046132')
    assert tr['PMID'] == '22046132'

    tr = parse_text_refs('pubmed:https(//doi.org/10.1101/2020.03.22.002386)')

```
