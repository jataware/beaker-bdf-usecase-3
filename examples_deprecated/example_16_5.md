# Description
Return a valid GO label based on an ID, label, or synonym.

# Code
```
import re
import logging
from indra.databases.obo_client import OboClient

logger = logging.getLogger(__name__)

def get_valid_location(loc):
    """Return a valid GO label based on an ID, label or synonym.

    The rationale behind this function is that many sources produce
    cellular locations that are arbitrarily either GO IDs (sometimes
    without the prefix and sometimes outdated) or labels or synonyms.
    This function handles all these cases and returns a valid GO label
    in case one is available, otherwise None.

    Parameters
    ----------
    loc : txt
        The location that needst o be canonicalized.

    Returns
    -------
    str or None
        The valid location string is available, otherwise None.
    """
    if not loc:
        return None
    # If it's actually a GO ID, we do some validation and use it. If it is
    # a text label then we look up the GO ID for it
    if re.match(r'^(GO:)?\d+$', loc):
        if not loc.startswith('GO:'):
            loc = 'GO:' + loc
        go_id = loc
        prim_id = get_primary_id(go_id)
        if prim_id:
            go_id = prim_id
    else:
        go_id = get_go_id_from_label_or_synonym(loc)
        if not go_id:
            return None
    # If we managed to get a GO ID either way, we get its label and return it
    # with some extra caution to not return a None name under any
    # circumstances
    if go_id:
        loc = get_go_label(go_id)
        if loc:
            return loc

```
