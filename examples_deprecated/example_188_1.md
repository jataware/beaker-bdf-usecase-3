# Description
Define and create an instance of EidosBioProcessor, process Eidos output to extract INDRA statements and convert them to biologically-oriented statements.

# Code
```
from typing import Any, Callable, Mapping, Optional

from indra.statements import Agent
from indra.statements import Activation, Inhibition
from indra.ontology.standardize import standardize_agent_name

import json

GrounderResult = Mapping[str, str]
Grounder = Callable[[str, Optional[str]], GrounderResult]

class EidosProcessor:
    def __init__(self, json_dict):
        self.json_dict = json_dict
        self.statements = []

    def extract_causal_relations(self):
        # Dummy implementation to simulate extracting casual relations
        self.statements = [{'subj': Concept('entity1'), 'obj': Concept('entity2'), 'evidence': [{'text': 'Evidence text'}]}]

class Concept:
    def __init__(self, name):
        self.name = name

class EidosBioProcessor(EidosProcessor):
    """Class to extract biology-oriented INDRA statements from Eidos output
    in a way that agents are grounded to biomedical ontologies."""

    def __init__(self, json_dict, grounder: Optional[Grounder] = None):
        super().__init__(json_dict)
        if grounder:
            self.grounder = grounder
        else:
            self.grounder = default_grounder_wrapper

    def get_regulate_activity(self, stmt):
        context = stmt.evidence[0].text
        subj = self.get_agent_bio(stmt.subj.concept, context=context)
        obj = self.get_agent_bio(stmt.obj.concept, context=context)
        if not subj or not obj:
            return None
        pol = stmt.overall_polarity()
        stmt_type = Activation if pol == 1 or not pol else Inhibition
        bio_stmt = stmt_type(subj, obj, evidence=stmt.evidence)
        return bio_stmt

    def extract_statements(self):
        self.extract_causal_relations()
        bio_stmts = []
        for stmt in self.statements:
            bio_stmt = self.get_regulate_activity(stmt)
            if bio_stmt:
                bio_stmts.append(bio_stmt)

```
