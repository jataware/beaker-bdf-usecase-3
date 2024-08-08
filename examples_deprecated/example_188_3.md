# Description
Default grounder wrapper leveraging the Gilda grounding tool for text context.

# Code
```
from typing import Optional, Mapping


def default_grounder_wrapper(text: str, context: Optional[str]) -> GrounderResult:
    # Import here to avoid this when working in INDRA World context
    from indra.preassembler.grounding_mapper.gilda import get_grounding
    grounding, _ = get_grounding(text, context=context, mode='local')

```
