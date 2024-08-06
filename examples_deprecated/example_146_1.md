# Description
Generate a PySB model based on a subset of given INDRA Statements.

# Code
```
import pickle
from indra.assemblers.pysb import PysbAssembler


def get_subnetwork(statements, nodes):
    filtered_statements = _filter_statements(statements, nodes)
    pa = PysbAssembler()
    pa.add_statements(filtered_statements)
    model = pa.make_model()
    return model


def _filter_statements(statements, agents):
    filtered_statements = []
    for s in statements:
        if all([a is not None for a in s.agent_list()]) and \
            all([a.name in agents for a in s.agent_list()]):
            filtered_statements.append(s)

if __name__ == '__main__':
    genes = ['EGF', 'EGFR', 'ERBB2', 'GRB2', 'SOS1', 'HRAS', 'RAF1',
             'MAP2K1', 'MAPK1']

    with open('models/rasmachine/rem/model.pkl', 'rb') as f:
        model = pickle.load(f)
    stmts = []
    for k, v in model.items():
        stmts += v


```
