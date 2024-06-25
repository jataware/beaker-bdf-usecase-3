# Description
Identifies the overlap of phosphorylation statements between predicted data and reference data.

# Code
```
import os
import pickle
import pandas
import logging
from indra.databases import hgnc_client
from indra.statements import Phosphorylation, Agent, Evidence
from indra.preassembler import Preassembler
from indra.ontology.bio import bio_ontology
from indra.preassembler.grounding_mapper import default_mapper
from indra.preassembler.sitemapper import SiteMapper, default_site_map


def compare_overlap(stmts_pred, stmts_ref):
    # Ras Machine statements that are in Phosphosite
    found_stmts = []
    not_found_stmts = []
    for i, stmt_pred in enumerate(stmts_pred):
        found = False
        for stmt_ref in stmts_ref:
            if stmt_pred.matches(stmt_ref) or \
                stmt_ref.refinement_of(stmt_pred, bio_ontology):
                    found = True
                    break
        if found:
            found_stmts.append(stmt_pred)
        else:
            not_found_stmts.append(stmt_pred)

```
