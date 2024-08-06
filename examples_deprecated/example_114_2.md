# Description
Test processing JSON data using the PhosphoElmProcessor and confirm that it processes phosphorylation events correctly when skip_empty is set to True.

# Code
```
from indra.statements import Phosphorylation
from indra.sources.phosphoelm.processor import PhosphoElmProcessor
from indra.sources.phosphoelm.api import _get_json_from_entry_rows

columns = ['acc', 'sequence', 'position', 'code', 'pmids', 'kinases', 'source', 'species', 'entry_date']
non_human_no_kinase = ['O08539', 'FAKEGSKG', '6', 'S', '17114649', '', 'HTP', 'Mus musculus', '2005-03-14 12:16:11.108314+01']
human_no_kinase = ['O14543', 'FAKESEQUENCESRPLDTSLRLKTFSSKSEYQL', '31', 'Y', '12783885', '', 'LTP', 'Homo sapiens', '2006-10-17 12:06:48.271076+02']
human_kinase1 = ['O14543', 'FAKESEQUENCESRPLDTSLRLKTFSSKSEYQL', '31', 'Y', '12783885', 'Lck', 'LTP', 'Homo sapiens', '2006-10-17 12:06:48.16767+02']
human_kinase2 = ['O14746', 'FAKEPRCRAVRSLL', '12', 'S', '10224060', 'PKB_group', 'LTP', 'Homo sapiens', '2004-12-31 00:00:00+01']


def test_skip_empty():
    pep = PhosphoElmProcessor(
        phosphoelm_data=_get_json_from_entry_rows(iter(raw_data))
    )
    pep.process_phosphorylations(skip_empty=True)
    stmts = pep.statements

```
