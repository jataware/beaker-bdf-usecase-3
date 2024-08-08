# Description
Reground texts using the Eidos reader.

# Code
```
import os
import json
import datetime
from indra import get_config
from indra.java_vm import autoclass

eidos_package = 'org.clulab.wm.eidos'

class EidosReader(object):
    def __init__(self):
        self.eidos_reader = None
        self.default_ontology = None

    def get_default_ontology(self):
        if self.default_ontology is None:
            from indra_world.ontology import world_ontology
            self.default_ontology = world_ontology.dump_yml_str()
        return self.default_ontology

    def initialize_reader(self):
        eidos = autoclass(eidos_package + '.EidosSystem')
        self.eidos_reader = eidos()

def _list_to_seq(lst):
    ml = autoclass('scala.collection.mutable.MutableList')()
    for element in lst:
        ml.appendElem(element)
    return ml

def _get_scored_grounding(tpl):
    ts = tpl.toString()
    parts = ts[1:-1].rsplit(',', maxsplit=1)

def reground_texts(self, texts, yaml_str=None, topk=10,
                   is_canonicalized=False, filter=True):
    if self.eidos_reader is None:
        self.initialize_reader()
    if yaml_str is None:
        yaml_str = self.get_default_ontology()
    text_seq = _list_to_seq(texts)
    raw_groundings = \
        self.eidos_reader.components().ontologyHandler().reground(
            'Custom',  # name
            yaml_str,  # ontologyYaml
            text_seq,  # texts
            filter,  # filter
            topk,  # topk
            is_canonicalized  # isAlreadyCanonicalized
        )
    # Process the return values into a proper Python representation
    groundings = [[_get_scored_grounding(entry) for entry in text_grounding]
                  for text_grounding in raw_groundings]

```
