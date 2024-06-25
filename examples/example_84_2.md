# Description
Example demonstrating the usage of GenewaysActionMentionParser to parse action mentions.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from os.path import join, dirname, abspath
from indra.sources.geneways.actionmention_parser import GenewaysActionMentionParser

# Path to the Geneways test/dummy data folder
path_this = dirname(abspath(__file__))
data_folder = join(path_this, 'geneways_tests_data')

def test_geneways_actionmention_parser():
    parser = GenewaysActionMentionParser(actionmention_file)

    assert len(parser.action_mentions) == 4
    mention0 = parser.action_mentions[0]
    mention1 = parser.action_mentions[1]
    mention2 = parser.action_mentions[2]
    mention3 = parser.action_mentions[3]

    #Make sure that the parser reads in the TSV file into the correct fields

    #First action mention
    assert mention0.hiid == '1'
    assert mention0.actionmentionid == '1'
    assert mention0.negative == '0'
    assert mention0.upstream == 'c-Src'
    assert mention0.actiontype == 'phosphorylate'
    assert mention0.downstream == 'Akt'
    assert mention0.pmid == '19262695'
    assert mention0.isFullText == '1'
    assert mention0.sentencenumber == '4'
    assert mention0.score == '0.56'
    assert mention0.prec == '0.78'

    #Second action mention
    assert mention1.hiid == '1'
    assert mention1.actionmentionid == '2'
    assert mention1.negative == '0'
    assert mention1.upstream == 'c-Src'
    assert mention1.actiontype == 'phosphorylate'
    assert mention1.downstream == 'Akt'
    assert mention1.pmid == '2'
    assert mention1.isFullText == '0'
    assert mention1.sentencenumber == '7'
    assert mention1.score == '0.23'
    assert mention1.prec == '0.34'

    #Third action mention
    assert mention2.hiid == '2'
    assert mention2.actionmentionid == '3'
    assert mention2.negative == '1'
    assert mention2.upstream == 'A'
    assert mention2.actiontype == 'bind'
    assert mention2.downstream == 'B'
    assert mention2.pmid == '0'
    assert mention2.isFullText == '0'
    assert mention2.sentencenumber == '0'
    assert mention2.score == '0.12'
    assert mention2.prec == '0.48'

    #Fourth action mention
    assert mention3.hiid == '3'
    assert mention3.actionmentionid == '4'
    assert mention3.negative == '0'
    assert mention3.upstream == 'C'
    assert mention3.actiontype == 'bind'
    assert mention3.downstream == 'D'
    assert mention3.pmid == '0'
    assert mention3.isFullText == '0'
    assert mention3.sentencenumber == '0'
    assert mention3.score == '0.22'

```
