# Description
The `get_activity_modification` method to extract INDRA ActiveForm statements from a BioPAX model.

# Code
```
indra.statements import *
indra.util import flatten

def get_activity_modification(self):
    """Extract INDRA ActiveForm statements from the BioPAX model."""
    for agent, gained_mods, lost_mods, activity_change, ev in \
            self._conversion_no_control_iter():
        # We have to have both a modification change and an activity
        # change
        if not (gained_mods or lost_mods) or not activity_change:
            continue
        is_active = (activity_change == 'active')
        # NOTE: with the ActiveForm representation we cannot
        # separate static_mods and gained_mods. We assume here
        # that the static_mods are inconsequential and therefore
        # are not mentioned as an Agent condition, following
        # don't care don't write semantics. Therefore only the
        # gained_mods are listed in the ActiveForm as Agent
        # conditions.
        assert isinstance(agent, Agent)
        if gained_mods:
            ag = copy.deepcopy(agent)
            ag.mods = gained_mods
            stmt = ActiveForm(ag, 'activity', is_active, evidence=ev)
            self.statements.append(stmt)
        if lost_mods:
            ag = copy.deepcopy(agent)
            ag.mods = lost_mods
            stmt = ActiveForm(ag, 'activity', not is_active, evidence=ev)

```
