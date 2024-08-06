# Description
Map INDRA Statements' db_refs to updated values using a provided mapping.

# Code
```
import logging
from indra.pipeline import register_pipeline
from indra.util import read_unicode_csv

def map_db_refs(stmts_in, db_refs_map=None):
    """Update entries in db_refs to those provided in db_refs_map.

    Parameters
    ----------
    stmts_in : list[indra.statements.Statement]
        A list of INDRA Statements to update db_refs in.
    db_refs_map : Optional[dict]
        A dictionary where each key is a tuple (db_ns, db_id) representing old
        db_refs pair that has to be updated and each value is a new db_id to
        replace the old value with. If not provided, the default db_refs_map
        will be loaded.
    """
    if not db_refs_map:
        db_refs_map = _load_db_refs_map()
    stmts_out = []

    def update_agent_db_refs(ag_db_refs, db_refs_map):
        for (db_ns, old_db_id), new_id in db_refs_map.items():
            if ag_db_refs.get(db_ns) == old_db_id:
                ag_db_refs[db_ns] = new_id
        return ag_db_refs

    for stmt in stmts_in:
        new_stmt = deepcopy(stmt)
        for ag in new_stmt.agent_list():
            if ag is not None:
                ag.db_refs = update_agent_db_refs(ag.db_refs, db_refs_map)
        stmts_out.append(new_stmt)

```
