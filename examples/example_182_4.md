# Description
The `get_regulate_activities` method to extract Activation/Inhibition INDRA Statements from a BioPAX model.

# Code
```
indra.statements import *
indra.util import flatten

def get_regulate_activities(self):
    """Get Activation/Inhibition INDRA Statements from the BioPAX model."""
    for subj, obj, gained_mods, lost_mods, \
            activity_change, ev in self._conversion_state_iter():
        # We don't want to have gained or lost modification features
        if not activity_change or (gained_mods or lost_mods):
            continue
        stmt_class = Activation if activity_change == 'active' \
            else Inhibition
        stmt = stmt_class(subj, obj, 'activity',
                          evidence=ev)

```
