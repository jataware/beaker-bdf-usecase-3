# Description
Shows processing the neighborhood of specific genes using BioPAX.

# Code
```
from indra.sources import biopax

@pytest.mark.slow
def test_readme_using_indra5():
    from indra.sources import biopax
    # Process the neighborhood of BRAF and MAP2K1
    biopax_processor = biopax.process_pc_pathsfromto(['BRAF', 'RAF1'],
                                                     ['MAP2K1', 'MAP2K2'])

```
