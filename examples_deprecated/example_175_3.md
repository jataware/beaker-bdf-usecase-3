# Description
Shows how to set the grounding of a given agent by re-grounding with Gilda. It modifies the agent in place.

# Code
```
import requests
from urllib.parse import urljoin
from indra.config import get_config, has_config
from indra.ontology.standardize import standardize_agent_name

logger = logging.getLogger(__name__)
grounding_service_url = get_config('GILDA_URL', failure_ok=True) if has_config('GILDA_URL') else 'http://grounding.indra.bio/'

def get_grounding(txt: str, context: Optional[str] = None, mode: Optional[str] = 'web') -> Tuple[Mapping[str, Any], List[Any]]:
    grounding = {}
    if mode == 'web':
        resp = requests.post(urljoin(grounding_service_url, 'ground'), json={'text': txt, 'context': context})
        results = resp.json()
        if results:
            grounding = {results[0]['term']['db']: results[0]['term']['id']}
    else:
        from gilda import ground
        results = ground(txt, context)
        if results:
            grounding = {results[0].term.db: results[0].term.id}
            results = [sm.to_json() for sm in results]

def ground_agent(agent, txt, context=None, mode='web'):
    """Set the grounding of a given agent, by re-grounding with Gilda.

    This function changes the agent in place without returning a value.

    Parameters
    ----------
    agent : indra.statements.Agent
        The Agent whose db_refs shuld be changed.
    txt : str
        The text by which the Agent should be grounded.
    context : Optional[str]
        Any additional text context to help disambiguate the sense
        associated with txt.
    mode : Optional[str]
        If 'web', the web service given in the GILDA_URL config setting or
        environmental variable is used. Otherwise, the gilda package is
        attempted to be imported and used. Default: web
    """
    gr, results = get_grounding(txt, context, mode)
    if gr:
        db_refs = {'TEXT': txt}
        db_refs.update(gr)
        agent.db_refs = db_refs
        standardize_agent_name(agent, standardize_refs=True)

```
