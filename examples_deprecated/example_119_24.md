# Description
Checking if a PubMed article is retracted using the `is_retracted` method.

# Code
```
import time

def test_is_retracted():
    assert pubmed_client.is_retracted('35463694')

```
