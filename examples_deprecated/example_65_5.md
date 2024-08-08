# Description
Test fetching CCLE lines with BRAF V600E mutations and ensuring the correct number of lines are returned.

# Code
```
import pytest

def test_get_ccle_lines_for_mutation():
    """Check how many lines have BRAF V600E mutations.

    Check that this returns a list greater than zero, and more specificially,
    equal to 55 cell lines.
    """
    cl_BRAF_V600E = cbio_client.get_ccle_lines_for_mutation('BRAF', 'V600E')

```
