# Description
Define a REST endpoint '/get_xrefs' to get cross-references (or mappings) for a specified node in the ontology.

# Code
```
import argparse
from flask import Flask, request, jsonify
from indra.ontology.bio import bio_ontology

app = Flask(__name__)

bio_ontology.initialize()

@app.route('/get_xrefs', methods=['GET'])
def get_xrefs():
    ont = request.json.get('ontology')
    ontology = ontologies.get(ont)
    kwargs = ('ns', 'id')
    return jsonify(ontology.get_mappings(

```
