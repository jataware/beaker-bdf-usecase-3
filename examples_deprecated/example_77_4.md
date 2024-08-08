# Description
Demonstrates processing the neighborhood of specific genes using BEL.

# Code
```
from indra.sources import bel

@pytest.mark.slow
def test_readme_using_indra4():
    from indra.sources import bel
    # Process the neighborhood of BRAF and MAP2K1
    bel_processor = bel.process_pybel_neighborhood(['BRAF', 'MAP2K1'])

```
