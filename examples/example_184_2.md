# Description
Extract gene-disease relationship statements classified as 'therapeutic' from a DataFrame

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

def get_gene_agent(name, gene_entrez_id):
    db_refs = {'EGID': gene_entrez_id}
    hgnc_id = hgnc_client.get_hgnc_id(name)
    if hgnc_id:
        db_refs['HGNC'] = hgnc_id

class CTDGeneDiseaseProcessor(CTDProcessor):
    """Processes gene-disease relationships from CTD."""

    def extract_statements(self):
        df = self.df[self.df[4] == 'therapeutic']
        for _, row in tqdm.tqdm(df.iterrows(), total=len(df)):
            gene_name, gene_entrez_id, disease_name, disease_id, direct_ev, \
                inf_chem, inf_score, omim_ids, pmids = list(row)
            if not direct_ev:
                continue
            disease_agent = get_disease_agent(disease_name, disease_id)
            gene_agent = get_gene_agent(gene_name, gene_entrez_id)
            anns = {'direct_evidence': 'therapeutic'}
            evs = [Evidence(source_api='ctd', pmid=pmid, annotations=anns)
                   for pmid in pmids.split('|')]
            stmt = Inhibition(gene_agent, disease_agent,
                              evidence=evs)

```
