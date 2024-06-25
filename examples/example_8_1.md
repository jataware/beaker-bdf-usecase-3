# Description
Extracts human-human phosphorylation data from a CSV file, converts it to INDRA Phosphorylation statements, and saves the extracted statements to a pickle file.

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

psite_fname = 'phosphosite_kin_sub_2016.csv'
stmts_fname = 'model.pkl'


def phosphosite_to_indra():
    df = pandas.DataFrame.from_csv(psite_fname, index_col=None)
    df = df[df['KIN_ORGANISM'] == 'human']
    df = df[df['SUB_ORGANISM'] == 'human']
    stmts = []
    for _, row in df.iterrows():
        enz_name = row['GENE']
        enz_up = row['KIN_ACC_ID']
        sub_name = row['SUB_GENE']
        sub_up = row['SUB_ACC_ID']
        if not enz_name or not sub_name or \
            isinstance(enz_name, float) or isinstance(sub_name, float):
            continue
        enz = Agent(enz_name, db_refs={'UP': enz_up})
        sub = Agent(sub_name, db_refs={'UP': sub_up})
        site = row['SUB_MOD_RSD']
        if site[0] in ('S', 'T', 'Y'):
            residue = site[0]
            position = site[1:]
        else:
            residue = None
            position = None
        ev = Evidence('phosphosite')
        st = Phosphorylation(enz, sub, residue, position, ev)
        stmts.append(st)
    logger.info('%d human-human phosphorylations in Phosphosite' % len(stmts))
    with open('phosphosite_indra.pkl', 'wb') as fh:
        pickle.dump(stmts, fh)

```
