# Description
Test fetching genetic profiles for 'paad_icgc', mutation type, and ensuring the data is retrieved correctly.

# Code
```
import pytest

@pytest.mark.webservice
def test_get_genetic_profiles():
    genetic_profiles = \
        cbio_client.get_genetic_profiles('paad_icgc', 'mutation')

```
