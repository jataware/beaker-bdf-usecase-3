# Description
Loads phosphorylation statements from a pickle file, performs multiple filtering and mapping steps, and saves the final filtered phosphorylation statements to another pickle file.

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

logger = logging.getLogger('indra.benchmarks.phosphorylations')

def filter_belief(stmts):
    believed_stmts = []
    for stmt in stmts:
        if len(stmt.evidence) > 1:
            believed_stmts.append(stmt)
    return believed_stmts


def filter_direct(stmts):
    direct_stmts = []
    for stmt in stmts:
        if get_is_direct(stmt):
            direct_stmts.append(stmt)
    return direct_stmts


def filter_non_hypothesis(stmts):
    non_hyp_stmts = []
    for stmt in stmts:
        if get_is_not_hypothesis(stmt):
            non_hyp_stmts.append(stmt)
    return non_hyp_stmts


def filter_grounded(stmts):
    gm = default_mapper
    stmts_mapped = gm.map_agents(stmts, do_rename=True)

    stmts_grounded = []
    for stmt in stmts_mapped:
        all_grounded = True
        for agent in stmt.agent_list():
            if agent is not None:
                if set(agent.db_refs.keys()) == set(['TEXT']):
                    all_grounded = False
                    break
        if all_grounded:
            stmts_grounded.append(stmt)
    return stmts_grounded


def filter_enzkinase(stmts):
    kinase_activities = get_kinase_activities()
    stmts_enzkinase = []
    for stmt in stmts:
        is_kinase = False
        for kin in kinase_activities:
            if stmt.enz.entity_matches(kin.agent):
                is_kinase = True
                break
            if kin.agent.refinement_of(stmt.enz, bio_ontology):
                is_kinase = True
                break
        if is_kinase:
            stmts_enzkinase.append(stmt)

def extract_phos():
    with open(stmts_fname, 'rb') as fh:
        model = pickle.load(fh)

    stmts = []
    for pmid, pmid_stmts in model.items():
        for stmt in pmid_stmts:
            if isinstance(stmt, Phosphorylation):
                stmts.append(stmt)
    logger.info('%d phosphorylations in RAS Machine' % len(stmts))

    stmts = [s for s in stmts if s.enz is not None]
    logger.info('%d phosphorylations with enzyme in RAS Machine' % len(stmts))

    stmts_grounded = filter_grounded(stmts)
    logger.info('%d grounded phosphorylations in RAS Machine' % len(stmts_grounded))

    stmts_enzkinase = filter_enzkinase(stmts_grounded)
    logger.info('%d phosphorylations with kinase enzyme in RAS Machine' % len(stmts_enzkinase))

    sm = SiteMapper(default_site_map)
    stmts_valid, _ = sm.map_sites(stmts_enzkinase)
    logger.info('%d valid-sequence phosphorylations in RAS Machine' % len(stmts_valid))

    pa = Preassembler(bio_ontology, stmts_valid)
    stmts_unique = pa.combine_duplicates()
    logger.info('%d unique phosphorylations in RAS Machine' % len(stmts_unique))

    stmts_unique = pa.combine_related()
    logger.info('%d top-level phosphorylations in RAS Machine' % len(stmts_unique))

    with open('mapped_unique_phos.pkl', 'wb') as fh:
        pickle.dump(stmts_unique, fh)

    # Filter RAS Machine statements for direct and not hypothesis
    stmts = filter_direct(stmts_unique)
    logger.info('%d direct phosphorylations in RAS Machine' % len(stmts))
    stmts = filter_non_hypothesis(stmts)
    logger.info('%d non-hypothesis phosphorylations in RAS Machine' % len(stmts))

    with open('filtered_phos.pkl', 'wb') as fh:
        pickle.dump(stmts, fh)


```
