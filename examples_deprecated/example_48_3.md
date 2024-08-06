# Description
Sort and get the highest ranking compositional grounding entry from a list.

# Code
```
def compositional_sort_key(entry):
    concepts = [grounding[0] for grounding in entry if grounding is not None]
    scores = [grounding[1] for grounding in entry if grounding is not None]
    key1 = scores[0]
    key2 = len(scores)
    key3 = sum(scores) / len(scores)
    key4 = '|'.join(concepts)

def get_top_compositional_grounding(groundings):
    """Return the highest ranking compositional grounding entry."""
    return max(groundings, key=compositional_sort_key)


def get_sorted_compositional_groundings(groundings):
    """Return the compositional groundings sorted starting from the top."""

```
