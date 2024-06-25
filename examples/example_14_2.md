# Description
Retrieve the enzyme class code corresponding to a given enzyme name using `get_id_from_name`.

# Code
```
from typing import Optional
from indra.databases.obo_client import PyOboClient


    >>> from indra.databases import ec_client

    >>> ec_client.get_id_from_name("Alcohol dehydrogenase")

```
