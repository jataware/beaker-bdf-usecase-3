# Description
Test error raised when processing PTMs without sequence file.

# Code
```
from os.path import join, abspath, dirname
import pytest
from indra.sources import hprd

test_dir = join(abspath(dirname(__file__)), 'hprd_tests_data')

def test_process_ptms_no_seq():
    with pytest.raises(ValueError):
        ptm_file = join(test_dir, 'POST_TRANSLATIONAL_MODIFICATIONS.txt')

```
