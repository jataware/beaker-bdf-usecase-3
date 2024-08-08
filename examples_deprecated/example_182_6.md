# Description
The `get_regulate_amounts` method to extract INDRA RegulateAmount statements from a BioPAX model.

# Code
```
indra.statements import *
indra.util import flatten

def get_regulate_amounts(self):
    """Extract INDRA RegulateAmount Statements from the BioPAX model."""
    for subj, ev, control, conversion in \
            self._control_conversion_iter(bp.TemplateReaction, 'all'):
        stmt_type = IncreaseAmount if control.control_type == 'ACTIVATION' \
            else DecreaseAmount
        for product in conversion.product:
            product_agents = self._get_agents_from_entity(product)
            for obj in _listify(product_agents):
                stmt = stmt_type(subj, obj, evidence=ev)

```
