# Description
Convert a JSON representation of a statement to a Statement object, get its agent list, and use a utility function to process it.

# Code
```
from indra.statements import Statement

def test_conversion_keying():
    stmt_json = {"type": "Conversion",
                 "subj": {"name": "inflammatory response", "db_refs": {}},
                 "obj_from": [{"name": "KNG1",
                               "db_refs": {"HGNC": "6383", "UP": "P01042"}}],
                 "obj_to": [{"name": "Kallidin",
                             "db_refs": {"SCHEM": "Kallidin"}}],
                 "id": "d2361669-dfe5-45e0-914a-c96a82ad25fb"}
    stmt_list = [Statement._from_json(stmt_json)]
    stmt_list[0].agent_list()
    list(_get_relation_keyed_stmts(stmt_list))

```
