# Description
Get all valid element references for a map.

# Code
```
import requests
import re

default_map_name = 'covid19map'
base_url = 'https://%s.elixir-luxembourg.org/minerva/api/'


def get_latest_project_id(map_name=default_map_name):
    url = (base_url % map_name) + 'projects/'
    res = requests.get(url)
    projects = res.json()
    if '_' not in map_name:
        map_name = map_name.replace('map', '_map')
    p = '%s_\d{2}[a-zA-Z]{3}\d{2}$' % map_name
    latest_project = max(
        [pr for pr in projects if re.match(p, pr['projectId'])],
        key=lambda pr: pr['creationDate'])
    project_id = latest_project['projectId']
    return project_id


def get_models(project_id, map_name=default_map_name):
    url = (base_url % map_name) + ('projects/%s/models/' % project_id)
    res = requests.get(url)
    res.raise_for_status()
    return res.json()


def get_all_model_elements(models, project_id, map_name=default_map_name):
    all_elements = []
    for model in models:
        model_id = model['idObject']
        model_elements = get_model_elements(model_id, project_id, map_name)
        all_elements += model_elements
    return all_elements


def get_element_references(element):
    refs = element.get('references', [])
    references = [(ref.get('type'), ref.get('resource')) for ref in refs]
    if element.get('name'):
        references.append(('TEXT', element['name']))
    return references


def get_model_elements(model_id, project_id, map_name=default_map_name):
    url = (base_url % map_name) + \
        ('projects/%s/models/%s/' % (project_id, model_id)) + 'bioEntities/elements/?columns=id,name,type,elementId,complexId,references'
    res = requests.get(url)
    res.raise_for_status()

def get_all_valid_element_refs(map_name=default_map_name):
    project_id = get_latest_project_id(map_name)
    models = get_models(project_id, map_name)
    all_model_elements = get_all_model_elements(models, project_id,
                                                map_name)
    element_refs = [get_element_references(element) for element
                    in all_model_elements]
    valid_element_refs = [ref for ref in element_refs if ref]

```
