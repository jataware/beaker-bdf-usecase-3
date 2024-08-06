# Description
Query the INDRA DB for Phosphorylation statements whose substrate is one of the proteins whose phosphorylation appears in the site list and construct a dictionary of statements organized by specific sites making sure that phosphorylation of that specific site is described in the list of statements as values.

# Code
```
# Query the INDRA DB for Phosphorylation statements whose substrate is one
# of the proteins whose phosphorylation appears in the site list
from indra.sources.indra_db_rest import get_statements_from_query
from indra.sources.indra_db_rest.query import HasAgent, HasType

stmts_by_target = {}
unique_genes = {ms.gene_name for ms in valid_sites}

import tqdm
for gene in tqdm.tqdm(unique_genes):
    q = HasAgent(gene, role='OBJECT') & HasType('Phosphorylation')
    ip = get_statements_from_query(q)
    stmts_by_target[gene] = ip.statements


stmts_by_site = {}
for site in valid_sites:
    stmts = stmts_by_target[site.gene_name]
    stmts = [s for s in stmts if s.enz and 'HGNC' in s.enz.db_refs]
    stmts = [s for s in stmts
             if s.residue == site.orig_res and s.position == site.orig_pos]
    stmts_by_site[(site.gene_name, site.orig_res, site.orig_pos)] = stmts
stmts_by_site    
```
