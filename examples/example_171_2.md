# Description
Define a REST endpoint '/parent_rel' to get the parent relationships of a specified node in the ontology.

# Code
```
import argparse
from flask import Flask, request, jsonify
from indra.ontology.bio import bio_ontology

app = Flask(__name__)

bio_ontology.initialize()

@app.route('/parent_rel', methods=['GET'])
def parent_rel():
    ont = request.json.get('ontology')
    ontology = ontologies.get(ont)
    kwargs = ('ns', 'id', 'rel_types')
    return jsonify(list(ontology.parent_rel(

```
