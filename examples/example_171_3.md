# Description
Define a REST endpoint '/get_node_property' to get properties of a specified node in the ontology.

# Code
```
import argparse
from flask import Flask, request, jsonify
from indra.ontology.bio import bio_ontology

app = Flask(__name__)

bio_ontology.initialize()

@app.route('/get_node_property', methods=['GET'])
def get_node_property():
    ont = request.json.get('ontology')
    ontology = ontologies.get(ont)
    kwargs = ('ns', 'id', 'property')
    return jsonify(ontology.get_node_property(

```
