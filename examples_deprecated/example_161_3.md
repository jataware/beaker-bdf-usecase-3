# Description
Example of how to define and use a weight flattening function for preassembly method

# Code
```
import logging
import networkx as nx
import pandas as pd
from .net import IndraNet, default_sign_dict
from indra.statements import *
from indra.tools import assemble_corpus as ac
from indra.preassembler.custom_preassembly import agent_name_stmt_matches, agent_name_polarity_matches
from itertools import permutations
from collections import OrderedDict, defaultdict
from functools import partial

logger = logging.getLogger(__name__)
NS_PRIORITY_LIST = (
    'FPLX', 'HGNC', 'UP', 'CHEBI', 'GO', 'MESH', 'HMDB', 'PUBCHEM')

def get_ag_ns_id(ag):
    """Return a tuple of name space, id from an Agent's db_refs."""
    for ns in NS_PRIORITY_LIST:
        if ns in ag.db_refs:
            return ns, ag.db_refs[ns]
    return 'TEXT', ag.name

class IndraNetAssembler():
    def __init__(self, statements=None):
        self.statements = statements if statements else []
        self.model = None

def _get_source_counts(stmt):
    source_counts = defaultdict(int)
    for ev in stmt.evidence:
        source_counts[ev.source_api] += 1
    return dict(source_counts)

def _get_edge_data(stmt, extra_columns=None):
    stmt_type = type(stmt).__name__
    try:
        res = stmt.residue
    except AttributeError:
        res = None
    try:
        pos = stmt.position
    except AttributeError:
        pos = None
    edge_data = {
        'residue': res,
        'position': pos,
        'stmt_type': stmt_type,
        'evidence_count': len(stmt.evidence),
        'stmt_hash': stmt.get_hash(refresh=True),
        'belief': stmt.belief,
        'source_counts': _get_source_counts(stmt)
    }
    if extra_columns:
        for col_name, func in extra_columns:
            edge_data[col_name] = func(stmt)
    return edge_data

def _store_edge_data(stmts, extra_columns=None):
    for stmt in stmts:
        edge_data = _get_edge_data(stmt, extra_columns)
        for evid in stmt.evidence:
            evid.annotations['indranet_edge'] = edge_data

>>> def weight_flattening(G):
...     # Sets the flattened weight to the average of the
...     # inverse source count
...     for edge in G.edges:
...         w = [1/s['evidence_count']
...             for s in G.edges[edge]['statements']]
...         G.edges[edge]['weight'] = sum(w)/len(w)

```
