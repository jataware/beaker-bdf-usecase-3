# Description
Example demonstrating the usage of process_geneways_files to process Geneways data files.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from os.path import join, dirname, abspath
from indra.statements import Phosphorylation, Complex
from indra.sources.geneways.api import process_geneways_files

# Path to the Geneways test/dummy data folder
path_this = dirname(abspath(__file__))

def test_geneways_processor():
    processor = process_geneways_files(data_folder, get_evidence=False)

    statements = processor.statements
    assert len(statements) == 3

    statement0 = statements[0]
    statement1 = statements[1]
    statement2 = statements[2]

    assert isinstance(statement0, Phosphorylation)
    assert statement0.enz.db_refs['TEXT'] == 'c-Src'
    assert statement0.enz.name == 'A2M'
    assert statement0.sub.db_refs['TEXT'] == 'Akt'
    assert statement0.sub.name == 'A1BG'
    assert statement0.evidence[0].pmid == '19262695'
    assert statement0.evidence[0].epistemics['direct']

    assert isinstance(statement1, Phosphorylation)
    assert statement1.enz.db_refs['TEXT'] == 'c-Src'
    assert statement1.enz.name == 'A2M'
    assert statement1.sub.db_refs['TEXT'] == 'Akt'
    assert statement1.sub.name == 'A1BG'
    assert statement1.evidence[0].pmid == '2'
    assert statement1.evidence[0].epistemics['direct']

    assert isinstance(statement2, Complex)
    assert statement2.members[0].db_refs['TEXT'] == 'C'

```
