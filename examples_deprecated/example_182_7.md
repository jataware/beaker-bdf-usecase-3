# Description
The `get_conversions` method to extract Conversion INDRA Statements from a BioPAX model.

# Code
```
indra.statements import *
indra.util import flatten

    def get_conversions(self):
        """Extract Conversion INDRA Statements from the BioPAX model."""
        for subj, ev, control, conversion in \
                self._control_conversion_iter(bp.Conversion, 'primary'):
            # We only extract conversions for small molecules
            if not all(_is_small_molecule(pe)
                       for pe in (conversion.left + conversion.right)):
                continue
            # Since we don't extract location, this produces conversions where
            # the input and output is the same
            if isinstance(conversion, bp.Transport):
                continue

            # Assemble from and to object lists
            obj_from = []
            obj_to = []
            for participants, obj_list in ((conversion.left, obj_from),
                                           (conversion.right, obj_to)):
                for participant in participants:
                    agent = self._get_agents_from_entity(participant)
                    if isinstance(agent, list):
                        obj_list += agent
                    else:
                        obj_list.append(agent)

            # Make statements
            if not obj_from and not obj_to:
                continue
            st = Conversion(subj, obj_from, obj_to, evidence=ev)

```
