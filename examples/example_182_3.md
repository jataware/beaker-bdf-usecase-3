# Description
The `get_modifications` method to extract INDRA Modification Statements from a BioPAX model.

# Code
```
indra.statements import *
indra.util import flatten

def get_modifications(self):
    """Extract INDRA Modification Statements from the BioPAX model."""
    for enz, sub, gained_mods, lost_mods, \
            activity_change, ev in self._conversion_state_iter():
        for mods, is_gain in ((gained_mods, True), (lost_mods, False)):
            for mod in mods:
                # We skip generic / unspecified modifications
                if mod.mod_type == 'modification':
                    continue
                stmt_class = modtype_to_modclass[mod.mod_type]
                if not is_gain:
                    stmt_class = modclass_to_inverse[stmt_class]
                stmt = stmt_class(enz, sub, mod.residue,
                                  mod.position, evidence=ev)
                stmt = _remove_redundant_mods(stmt)

```
