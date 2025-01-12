# Description
Get inhibition statements for a specific drug by querying ChEMBL, including activities of the drug interacting with protein targets

# Code
```
import os
import logging
import requests
from sympy.physics import units
from indra.databases import chebi_client, uniprot_client
from indra.statements import Inhibition, Agent, Evidence
from collections import defaultdict
from indra.util import read_unicode_csv

logger = logging.getLogger(__name__)

# Helper functions and initial setup

def send_query(query_dict):
    url = 'https://www.ebi.ac.uk/chembl/api/data/' + query_dict['query'] + '.json'
    r = requests.get(url, params=query_dict['params'])
    r.raise_for_status()
    return r.json()


 def activities_by_target(activities):
    targ_act_dict = defaultdict(lambda: [])
    for activity in activities:
        target_chembl_id = activity['target_chembl_id']
        activity_id = activity['activity_id']
        targ_act_dict[target_chembl_id].append(activity_id)
    for target_chembl_id in targ_act_dict:
        targ_act_dict[target_chembl_id] = list(set(targ_act_dict[target_chembl_id]))
    return targ_act_dict


def get_protein_targets_only(target_chembl_ids):
    protein_targets = {}
    for target_chembl_id in target_chembl_ids:
        target = query_target(target_chembl_id)
        if 'SINGLE PROTEIN' in target['target_type']:
            protein_targets[target_chembl_id] = target
    return protein_targets


def get_evidence(assay):
    kin = get_kinetics(assay)
    source_id = assay.get('assay_chembl_id')
    if not kin:
        return None
    annotations = {'kinetics': kin}
    chembl_doc_id = str(assay.get('document_chembl_id'))
    pmid = get_pmid(chembl_doc_id)
    return Evidence(source_api='chembl', pmid=pmid, source_id=source_id, annotations=annotations)


 def get_kinetics(assay):
    try:
        val = float(assay.get('standard_value'))
    except TypeError:
        logger.warning('Invalid assay value: %s' % assay.get('standard_value'))
        return None
    unit = assay.get('standard_units')
    if unit == 'nM':
        unit_sym = 1e-9 * units.mol / units.liter
    elif unit == 'uM':
        unit_sym = 1e-6 * units.mol / units.liter
    else:
        logger.warning('Unhandled unit: %s' % unit)
        return None
    param_type = assay.get('standard_type')
    if param_type not in ['IC50', 'EC50', 'INH', 'Potency', 'Kd']:
        logger.warning('Unhandled parameter type: %s' % param_type)
        logger.info(str(assay))
        return None
    return {param_type: val * unit_sym}


def get_pmid(doc_id):
    url_pmid = 'https://www.ebi.ac.uk/chembl/api/data/document.json'
    params = {'document_chembl_id': doc_id}
    res = requests.get(url_pmid, params=params)
    return str(res.json()['documents'][0]['pubmed_id'])


def query_target(target_chembl_id):
    query_dict = {'query': 'target', 'params': {'target_chembl_id': target_chembl_id, 'limit': 1}}
    res = send_query(query_dict)
    return res['targets'][0]


def get_target_chemblid(target_upid):
    url = 'https://www.ebi.ac.uk/chembl/api/data/target.json'
    params = {'target_components__accession': target_upid}
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()['targets'][0]['target_chembl_id']


def get_chembl_id(nlm_mesh):
    mesh_id = get_mesh_id(nlm_mesh)
    pcid = get_pcid(mesh_id)
    url_mesh2pcid = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/%s/synonyms/JSON' % pcid
    r = requests.get(url_mesh2pcid)
    res = r.json()
    synonyms = res['InformationList']['Information'][0]['Synonym']
    return [syn for syn in synonyms if 'CHEMBL' in syn and 'SCHEMBL' not in syn][0]

chembl_names = {}
resource_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources', 'chembl_tas.csv')
for chembl_id, chembl_name, _ in read_unicode_csv(resource_file, delimiter=',', skiprows=1):
    if chembl_name:

def get_drug_inhibition_stmts(drug):
    """Query ChEMBL for kinetics data given drug as Agent get back statements

    Parameters
    ----------
    drug : Agent
        Agent representing drug with MESH or CHEBI grounding

    Returns
    -------
    stmts : list of INDRA statements
        INDRA statements generated by querying ChEMBL for all kinetics data of
        a drug interacting with protein targets
    """
    chebi_id = drug.db_refs.get('CHEBI')
    mesh_id = drug.db_refs.get('MESH')
    if chebi_id:
        drug_chembl_id = chebi_client.get_chembl_id(chebi_id)
    elif mesh_id:
        drug_chembl_id = get_chembl_id(mesh_id)
    else:
        logger.error('Drug missing ChEBI or MESH grounding.')
        return None
    logger.info('Drug: %s' % (drug_chembl_id))
    query_dict = {'query': 'activity',
                  'params': {'molecule_chembl_id': drug_chembl_id,
                             'limit': 10000}
                  }
    res = send_query(query_dict)
    activities = res['activities']
    targ_act_dict = activities_by_target(activities)
    target_chembl_ids = [x for x in targ_act_dict]
    protein_targets = get_protein_targets_only(target_chembl_ids)
    filtered_targ_act_dict = {t: targ_act_dict[t]
                              for t in [x for x in protein_targets]}
    stmts = []
    for target_chembl_id in filtered_targ_act_dict:
        target_activity_ids = filtered_targ_act_dict[target_chembl_id]
        target_activites = [x for x in activities
                            if x['activity_id'] in target_activity_ids]
        target_upids = []
        targ_comp = protein_targets[target_chembl_id]['target_components']
        for t_c in targ_comp:
            target_upids.append(t_c['accession'])
        evidence = []
        for assay in target_activites:
            ev = get_evidence(assay)
            if not ev:
                continue
            evidence.append(ev)
        if len(evidence) > 0:
            for target_upid in target_upids:
                agent_name = uniprot_client.get_gene_name(target_upid)
                target_agent = Agent(agent_name, db_refs={'UP': target_upid})
                st = Inhibition(drug, target_agent, evidence=evidence)
                stmts.append(st)

```
