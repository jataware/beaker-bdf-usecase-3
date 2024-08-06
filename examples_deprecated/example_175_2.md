# Description
Illustrates how to retrieve a list of strings for entities that Gilda can disambiguate using the Gilda web service or local Gilda package.

# Code
```
import requests
from urllib.parse import urljoin
from indra.config import get_config, has_config


def get_gilda_models(mode='web'):
    """Return a list of strings for which Gilda has a disambiguation model.

    Parameters
    ----------
    mode : Optional[str]
        If 'web', the web service given in the GILDA_URL config setting or
        environmental variable is used. Otherwise, the gilda package is
        attempted to be imported and used. Default: web

    Returns
    -------
    list[str]
        A list of entity strings.
    """
    if mode == 'web':
        res = requests.post(urljoin(grounding_service_url, 'models'))
        models = res.json()
        return models
    else:
        from gilda import get_models

```
