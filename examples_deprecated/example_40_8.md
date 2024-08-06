# Description
Updating mappings from DrugBank to CHEBI/CHEMBL by using PyOBO to download and filter xrefs, then saving them.

# Code
```
os
logging
pyobo

def update_drugbank_mappings():
    """Update mappings from DrugBank to CHEBI/CHEMBL"""
    # Note that for this to work, PyOBO (https://github.com/pyobo/pyobo) has
    # to be installed and the DrugBank download
    # (https://www.drugbank.ca/releases/latest) put into ~/.obo/drugbank/
    # Note that the DrugBank download requires signing up for an account and
    # waiting for approval.
    import pyobo
    drugbank_chembl = pyobo.get_filtered_xrefs('drugbank', 'chembl.compound')
    drugbank_chebi = pyobo.get_filtered_xrefs('drugbank', 'chebi')
    chebi_drugbank = pyobo.get_filtered_xrefs('chebi', 'drugbank')
    drugbank_names = pyobo.get_id_name_mapping('drugbank')
    rows = []
    for drugbank_id, chembl_id in drugbank_chembl.items():
        rows.append([drugbank_id, 'CHEMBL', chembl_id, 'drugbank'])
    for drugbank_id, chebi_id in drugbank_chebi.items():
        rows.append([drugbank_id, 'CHEBI', chebi_id, 'drugbank'])
    for chebi_id, drugbank_id in chebi_drugbank.items():
        rows.append([drugbank_id, 'CHEBI', chebi_id, 'chebi'])
    for drugbank_id, name in drugbank_names.items():
        rows.append([drugbank_id, 'NAME', name, 'drugbank'])
    fname = os.path.join(path, 'drugbank_mappings.tsv')
    header = ['DRUGBANK_ID', 'NAMESPACE', 'ID', 'SOURCE']
    rows = [header] + sorted(rows)

```
