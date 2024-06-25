# Description
Define a REST endpoint '/get_id_from_name' to get the ID of a node by specifying its name in the ontology.

# Code
```
import argparse
from flask import Flask, request, jsonify
from indra.ontology.bio import bio_ontology

app = Flask(__name__)

bio_ontology.initialize()

@app.route('/get_id_from_name', methods=['GET'])
def get_id_from_name():
    ont = request.json.get('ontology')
    ontology = ontologies.get(ont)
    kwargs = ('ns', 'name')
    return jsonify(ontology.get_id_from_name(

```
