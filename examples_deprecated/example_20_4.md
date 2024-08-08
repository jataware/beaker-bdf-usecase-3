# Description
Get the MESH ID and name for a given MESH term using the NLM REST API.

# Code
```
import requests
import json
import re
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
    '''
def submit_sparql_query(query_body):
    url = MESH_URL + 'sparql'
    query = '%s\n%s' % (mesh_rdf_prefixes, query_body)
    args = {'query': query, 'format': 'JSON', 'inference': 'true'}
    resp = requests.get(url, params=args)
    if resp.status_code != 200:
        return None
    try:
        return resp.json()
    except Exception:

def get_mesh_id_name_from_web(mesh_term):
    """Get the MESH ID and name for the given MESH term using the NLM REST API.

    Parameters
    ----------
    mesh_term : str
        MESH Descriptor or Concept name, e.g. 'Breast Cancer'.

    Returns
    -------
    tuple of strs
        Returns a 2-tuple of the form `(id, name)` with the ID of the
        descriptor corresponding to the MESH label, and the descriptor name
        (which may not exactly match the name provided as an argument if it is
        a Concept name). If the query failed, or no descriptor corresponding to
        the name was found, returns a tuple of (None, None).
    """
    query_body = """
        SELECT ?d ?dName ?c ?cName
        FROM <http://id.nlm.nih.gov/mesh>
        WHERE {
          ?d a meshv:Descriptor .
          ?d meshv:concept ?c .
          ?d rdfs:label ?dName .
          ?c rdfs:label ?cName
          FILTER (REGEX(?dName,'^%s$','i') || REGEX(?cName,'^%s$','i'))
        }
        ORDER BY ?d
    """ % (mesh_term, mesh_term)
    mesh_json = submit_sparql_query(query_body)
    if mesh_json is None:
        return None, None
    try:
        # Choose the first entry (should usually be only one)
        id_uri = mesh_json['results']['bindings'][0]['d']['value']
        name = mesh_json['results']['bindings'][0]['dName']['value']
    except (KeyError, IndexError, json.decoder.JSONDecodeError) as e:
        return None, None

    # Strip the MESH prefix off the ID URI
    m = re.match('http://id.nlm.nih.gov/mesh/([A-Za-z0-9]*)', id_uri)
    assert m is not None
    id = m.groups()[0]

```
