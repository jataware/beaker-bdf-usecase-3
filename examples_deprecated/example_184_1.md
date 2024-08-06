# Description
Extract chemical-disease relationship statements classified as 'therapeutic' from a DataFrame

# Code
```
import tqdm
from indra.statements import *
from indra.databases import hgnc_client
from indra.statements.validate import assert_valid_db_refs
from indra.ontology.standardize import standardize_db_refs, get_standard_agent

class CTDProcessor:
    """Parent class for CTD relation-specific processors."""
    def __init__(self, df):
        self.df = df
        self.statements = []

def get_disease_agent(name, disease_id):
    groundings = disease_id.split('|')
    db_refs = {}
    for gr in groundings:
        db_ns, db_id = gr.split(':')
        db_refs[db_ns] = db_id
    return get_standard_agent(name, db_refs)

def get_chemical_agent(name, mesh_id, cas_id):
    db_refs = {'MESH': mesh_id}
    if cas_id:
        db_refs['CAS'] = cas_id

class CTDChemicalDiseaseProcessor(CTDProcessor):
    """Processes chemical-disease relationships from CTD."""

    def extract_statements(self):
        df = self.df[self.df[5] == 'therapeutic']
        for _, row in tqdm.tqdm(df.iterrows(), total=len(df)):
            chem_name, chem_mesh_id, chem_cas_id, disease_name, disease_id,\
                direct_ev, inf_gene, inf_score, omim_ids, pmids = list(row)
            if not direct_ev:
                continue
            chem_agent = get_chemical_agent(chem_name, chem_mesh_id,
                                            chem_cas_id)
            disease_agent = get_disease_agent(disease_name, disease_id)
            anns = {'direct_evidence': 'therapeutic'}
            evs = [Evidence(source_api='ctd', pmid=pmid, annotations=anns)
                   for pmid in pmids.split('|')]
            stmt = Inhibition(chem_agent, disease_agent,
                              evidence=evs)

```
