# Description
Test the extraction of a dephosphorylation sentence. This sentence is processed into two INDRA statements, at least one of which is correct.

# Code
```
import pytest
from indra.statements import *
from indra.sources.tees import api

@pytest.mark.slow
def test_process_dephosphorylation():
    # Test the extraction of a dephosphorylation sentence. This sentence is
    # processed into two INDRA statements, at least one of which is correct.

    # Text statement describing phosphorylation
    s = 'Here we show that febuxostat suppresses LPS-induced MCP-1 ' + \
            'production and mRNA expression via activating ' + \
            'MAPK phosphatase-1 (MKP-1) which, in turn, leads to ' + \
            'dephosphorylation and inactivation of JNK in macrophages.'
    tp = api.process_text(s)
    statements = tp.statements

    # We'll set this to true if at least one of the extracted statements meets
    # our criteria for correctness
    some_statement_correct = False

    # Extracting this particular sentence with TEES produces a couple
    # statements, at least one of which is correct
    for statement in statements:
        statement_correct = False
        enz = statement.enz.db_refs['TEXT']
        sub = statement.sub.db_refs['TEXT']

        # Does this statement have the entities named in the text?
        entities_correct = enz == 'MAPK phosphatase-1' and sub == 'JNK'

        # Is the statement a phosphorylation statement?
        type_correct = isinstance(statement, Dephosphorylation)

        # There should be an evidence object (properties of evidence tested in
        # other tests)
        assert len(statements[0].evidence) == 1

        # If yes to both, the correct statement was among those extracted
        statement_correct = type_correct and entities_correct
        some_statement_correct = statement_correct or some_statement_correct


```
