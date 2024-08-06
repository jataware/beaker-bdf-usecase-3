# Description
Demonstrates how to get the top Gilda grounding for a given text using the Gilda grounding web service or local Gilda package.

# Code
```
import requests
from urllib.parse import urljoin
from indra.config import get_config, has_config

logger = logging.getLogger(__name__)

def get_grounding(
    txt: str,
    context: Optional[str] = None,
    mode: Optional[str] = 'web',
) -> Tuple[Mapping[str, Any], List[Any]]:
    """Return the top Gilda grounding for a given text.

    Parameters
    ----------
    txt : str
        The text to ground.
    context : Optional[str]
        Any context for the grounding.
    mode : Optional[str]
        If 'web', the web service given in the GILDA_URL config setting or
        environmental variable is used. Otherwise, the gilda package is
        attempted to be imported and used. Default: web

    Returns
    -------
    dict
        If no grounding was found, it is an empty dict. Otherwise, it's a
        dict with the top grounding returned from Gilda.
    list
        The list of ScoredMatches
    """
    grounding = {}
    if mode == 'web':
        resp = requests.post(urljoin(grounding_service_url, 'ground'),
                             json={'text': txt, 'context': context})
        results = resp.json()
        if results:
            grounding = {results[0]['term']['db']: results[0]['term']['id']}
    else:
        from gilda import ground
        results = ground(txt, context)
        if results:
            grounding = {results[0].term.db: results[0].term.id}
            results = [sm.to_json() for sm in results]

```
