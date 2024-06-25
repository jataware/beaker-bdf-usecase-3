# Description
Test the `get_agent_bio` function from the `indra.sources.eidos.bio_processor` with different groundings to ensure it correctly creates agents with the expected properties.

# Code
```
from indra.sources.eidos.bio_processor import get_agent_bio

def test_get_agent_bio():
    # (raw text, normalized text, groundings, name)
    groundings = (
        ('xxx', 'yyy', {}, 'yyy'),
        ('xxx', 'checklist', {'MESH': 'D057189'}, 'Checklist'),
        ('checklist', 'yyy', {'MESH': 'D057189'}, 'Checklist'),
        ('checklist', 'life insurance', {'MESH': 'D057189'}, 'Checklist')
    )

    for raw_text, norm_text, groundings, name in groundings:
        concept = Concept(norm_text, db_refs={'TEXT': raw_text})
        agent = get_agent_bio(concept)
        assert agent.name == name, agent
        for ns, id in groundings.items():
            assert agent.db_refs.get(ns) == id, agent.db_refs
        assert agent.db_refs['TEXT'] == raw_text

```
