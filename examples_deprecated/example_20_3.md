# Description
Submit a SPARQL query to the MESH RDF endpoint and parse the JSON response.

# Code
```
import requests
from functools import lru_cache
MESH_URL = 'https://id.nlm.nih.gov/mesh/'
mesh_rdf_prefixes = '''
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX meshv: <http://id.nlm.nih.gov/mesh/vocab#>
        PREFIX mesh: <http://id.nlm.nih.gov/mesh/>
        PREFIX mesh2019: <http://id.nlm.nih.gov/mesh/2019/>
        PREFIX mesh2018: <http://id.nlm.nih.gov/mesh/2018/>
        PREFIX mesh2017: <http://id.nlm.nih.gov/mesh/2017/>

@lru_cache(maxsize=1000)
def submit_sparql_query(query_body):
    url = MESH_URL + 'sparql'
    query = '%s\n%s' % (mesh_rdf_prefixes, query_body)
    args = {'query': query, 'format': 'JSON', 'inference': 'true'}
    resp = requests.get(url, params=args)
    # Check status
    if resp.status_code != 200:
        return None
    try:
        # Try to parse the json response (this can raise exceptions if we
        # got no response).
        return resp.json()
    except Exception:

```
