# Description
Example demonstrating the processing of multiple texts to ensure no shared objects are created between statements

# Code
```
from os.path import dirname, join
import indra.statements as ist
from indra.sources import trips
from indra.util import unicode_strs
import pytest

test_small_file = join(dirname(__file__), 'test_small.xml')

def assert_if_hgnc_then_up(st):
    agents = st.agent_list()
    for a in agents:
        if a is not None:
            up_id = a.db_refs.get('UP')
            hgnc_id = a.db_refs.get('HGNC')
            if hgnc_id and not up_id:
                assert False


def assert_grounding_value_or_none(st):
    agents = st.agent_list()
    for a in agents:
        if a is not None:
            for k, v in a.db_refs.items():
                if not v:

@pytest.mark.webservice
@pytest.mark.slow
def test_no_shared_objects():
    """Make sure shared objects are not being created between statements"""
    verbs = ('phosphorylates', 'binds', 'activates',
             ' causes activation of ', 'increases', 'degrades', 'synthesizes',
             'transcribes', 'ubiquitinates')
    for verb in verbs:
        text = 'HEDGEHOG %s SMURF1 and SMURF2' % verb
        tp = trips.process_text(text)
        stmts = tp.statements
        assert len(stmts) == 2
        stmt1, stmt2 = stmts
        # assert stmt1.evidence[0] is not stmt2.evidence[0]
        hedgehog1 = stmt1.agent_list()[0]
        hedgehog2 = stmt2.agent_list()[0]
        assert hedgehog1 is not hedgehog2
    # autophosphorylation
    text = 'HEDGEHOG phosphorylates itself at Ser1337 and Tyr99'
    tp = trips.process_text(text)
    stmts = tp.statements
    assert len(stmts) == 2
    stmt1, stmt2 = stmts
    assert stmt1.evidence[0] is not stmt2.evidence[0]
    hedgehog1 = stmt1.agent_list()[0]
    hedgehog2 = stmt2.agent_list()[0]

```
