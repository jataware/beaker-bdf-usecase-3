# Description
Explains how to set grounding for Agents in a given Statement using the Gilda grounding web service or local Gilda package.

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
    return grounding, results

def ground_agent(agent, txt, context=None, mode='web'):
    gr, results = get_grounding(txt, context, mode)
    if gr:
        db_refs = {'TEXT': txt}
        db_refs.update(gr)
        agent.db_refs = db_refs
        standardize_agent_name(agent, standardize_refs=True)

def ground_statement(stmt, mode='web', ungrounded_only=False):
    """Set grounding for Agents in a given Statement using Gilda.

    This function modifies the original Statement/Agents in place.

    Parameters
    ----------
    stmt : indra.statements.Statement
        A Statement to ground
    mode : Optional[str]
        If 'web', the web service given in the GILDA_URL config setting or
        environmental variable is used. Otherwise, the gilda package is
        attempted to be imported and used. Default: web
    ungrounded_only : Optional[str]
        If True, only ungrounded Agents will be grounded, and ones that
        are already grounded will not be modified. Default: False
    """
    if stmt.evidence and stmt.evidence[0].text:
        context = stmt.evidence[0].text
    else:
        context = None
    for agent in stmt.agent_list():
        if agent is not None and 'TEXT' in agent.db_refs:
            txt = agent.db_refs['TEXT']
            gr = agent.get_grounding()
            if not ungrounded_only or gr[0] is None:

```
