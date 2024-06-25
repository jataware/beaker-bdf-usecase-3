# Description
Deserialize a single statement JSON into a Statement object.

# Code
```
import json
import logging
from indra.statements.statements import Statement

logger = logging.getLogger(__name__)

def stmts_from_json(json_in, on_missing_support='handle'):
    stmts = []
    uuid_dict = {}
    for json_stmt in json_in:
        try:
            st = Statement._from_json(json_stmt)
        except Exception as e:
            logger.warning("Error creating statement: %s" % e)
            continue
        stmts.append(st)
        uuid_dict[st.uuid] = st
    for st in stmts:
        _promote_support(st.supports, uuid_dict, on_missing_support)
        _promote_support(st.supported_by, uuid_dict, on_missing_support)

def stmt_from_json(json_in):
    """Deserialize a single statement JSON into a Statement object.

    Parameters
    ----------
    json_in : dict
        A JSON representation of the INDRA Statement.

    Returns
    -------
    stmt : :py:class:`Statement`
        The INDRA Statement.
    """
    stmt = stmts_from_json([json_in], on_missing_support='ignore')

```
