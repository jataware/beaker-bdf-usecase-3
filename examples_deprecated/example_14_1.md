# Description
Retrieve the enzyme name corresponding to a given enzyme class code using `get_name_from_id`.

# Code
```
from typing import Optional
from indra.databases.obo_client import PyOboClient


from indra.databases import ec_client
ec_client.get_name_from_id("1.1.1.1")

```
