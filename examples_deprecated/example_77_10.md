# Description
Shows how to process the neighborhood of genes using BEL from the 'getting_started.rst' documentation.

# Code
```
from indra.sources import bel

@pytest.mark.slow
def test_getting_started5():
    # Chunk 5
    from indra.sources import bel
    bel_processor = bel.process_pybel_neighborhood(['KRAS', 'BRAF'])

```
