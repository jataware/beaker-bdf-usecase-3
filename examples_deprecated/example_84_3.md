# Description
Example demonstrating the usage of GenewaysActionParser to parse actions data.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from os.path import join, dirname, abspath
from indra.sources.geneways.action_parser import GenewaysActionParser

# Path to the Geneways test/dummy data folder
path_this = dirname(abspath(__file__))

def test_geneways_action_parser():
    parser = GenewaysActionParser(data_folder)

    actions = parser.actions
    assert len(actions) == 3

    action0 = actions[0]
    action1 = actions[1]
    action2 = actions[2]

    assert action0.hiid == '1'
    assert action0.up == '2'
    assert action0.dn == '1'
    assert action0.actiontype == 'phosphorylate'
    assert action0.action_count == '1'
    assert action0.actionmention_count == '2'
    assert action0.plo == 'P'
    assert action0.max_score == '0.77'
    assert action0.max_prec == '0.88'
    assert len(action0.action_mentions) == 2

    assert action1.hiid == '2'
    assert action1.up == '3'
    assert action1.dn == '4'
    assert action1.actiontype == 'bind'
    assert action1.action_count == '1'
    assert action1.actionmention_count == '1'
    assert action1.plo == 'P'
    assert action1.max_score == '0.12'
    assert action1.max_prec == '0.34'
    assert len(action1.action_mentions) == 1

    assert action2.hiid == '3'
    assert action2.up == '5'
    assert action2.dn == '6'
    assert action2.actiontype == 'bind'
    assert action2.action_count == '1'
    assert action2.actionmention_count == '1'
    assert action2.plo == 'P'
    assert action2.max_score == '0.16'
    assert action2.max_prec == '0.17'

```
