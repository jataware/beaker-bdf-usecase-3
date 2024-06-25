# Description
Test the `get_agent_bio` function with a custom grounding function to ensure it correctly applies the provided grounding information.

# Code
```
from indra.sources.eidos.bio_processor import get_agent_bio

def test_bio_custom_grounding():
    def my_grounder(txt, context):
        return {'MYDB': 'MYGROUNDING'}
    agent = get_agent_bio(Concept('x',
                                  {'TEXT': 'x'}),
                          grounder=my_grounder)

```
