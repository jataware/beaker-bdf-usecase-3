# Description
Define a REST endpoint '/child_rel' to get the child relationships of a specified node in the ontology.

# Code
```
import argparse
from flask import Flask, request, jsonify
from indra.ontology.bio import bio_ontology

app = Flask(__name__)

bio_ontology.initialize()

@app.route('/child_rel', methods=['GET'])
def child_rel():
    ont = request.json.get('ontology')
    ontology = ontologies.get(ont)
    kwargs = ('ns', 'id', 'rel_types')
    return jsonify(list(ontology.child_rel(

```
