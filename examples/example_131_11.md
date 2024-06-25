# Description
Testing site mapping with invalid position values.

# Code
```
protmapper import MappedSite
indra.statements import *
indra.util import unicode_strs
indra.preassembler.sitemapper import default_mapper as sm, MappedStatement

def test_invalid_position():
    stmt = Phosphorylation._from_json({
        'enz': {'name': 'CFD'},
        'sub': {'name': 'HP'},
        'residue': 'F',
        'position': '2.59'
    })
    valid, mapped = sm.map_sites(stmts=[stmt])
    assert not valid

```
