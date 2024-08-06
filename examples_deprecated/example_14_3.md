# Description
Retrieve the parents of a given enzyme class code using `get_parents`.

# Code
```
from typing import List
from indra.databases.obo_client import PyOboClient


from indra.databases import ec_client
ec_client.get_parents("1.1.1.1")

```
