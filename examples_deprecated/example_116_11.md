# Description
Testing retrieval of XML content for an invalid PMCID and expecting None.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import pytest

@pytest.mark.webservice
def test_get_xml_invalid():
    pmc_id = '9999999'
    xml_str = pmc_client.get_xml(pmc_id)

```
