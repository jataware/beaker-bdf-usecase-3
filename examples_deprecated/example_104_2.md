# Description
Test for converting a Medscan entity into an Agent using `agent_from_entity` method.

# Code
```
__future__ import absolute_import, print_function, unicode_literals
builtins import dict, str
os.path import join, dirname

def test_agent_from_entity():
    mp = MedscanProcessor()

    # Test entity
    entity = MedscanEntity(name='kinesin-I',
                           urn='urn:agi-gocomplex:0016938',
                           type=None, properties={},
                           ch_start=0, ch_end=10)

    # Test relation
    tagged_sentence = '{ID{321=BRAF} is a protein, not a type of car.'
    relation = MedscanRelation(pmid=None,
                               uri=None,
                               sec=None,
                               entities={'123': entity},
                               tagged_sentence=tagged_sentence,
                               subj=None,
                               verb=None,
                               obj=None,
                               svo_type=None)

    # Test for when an entity is in the grounded entities list
    agent1, bounds = mp.agent_from_entity(relation, 'ID{123}')
    assert agent1.db_refs == {'TEXT': 'kinesin-I', 'GO': 'GO:0016938'}

    # Test for when an entity is in the tagged sentence but not the entity list
    agent2, bounds = mp.agent_from_entity(relation, 'ID{321}')
    assert agent2.db_refs == {'TEXT': 'BRAF'}  # No grounding

    # Test for when an entity is neither tagged in the sentence nor in the
    # grounded entities list
    agent3_res = mp.agent_from_entity(relation, 'ID{444}')

```
