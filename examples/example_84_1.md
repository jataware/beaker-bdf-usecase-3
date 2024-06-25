# Description
Example demonstrating the usage of GenewaysSymbols to parse symbols data.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from os.path import join, dirname, abspath
from indra.sources.geneways.symbols_parser import GenewaysSymbols
from indra.sources.geneways.api import process_geneways_files

# Path to the Geneways test/dummy data folder
path_this = dirname(abspath(__file__))
data_folder = join(path_this, 'geneways_tests_data')

def test_geneways_symbols_parser():
    symbols = GenewaysSymbols(symbols_file)

    print(symbols.symbol_to_id('Akt') == ['1'])
    assert symbols.symbol_to_id('Akt') == ['1']
    assert symbols.symbol_to_id('c-Src') == ['2']

    assert symbols.id_to_symbol('1') == 'Akt'
    assert symbols.id_to_symbol('2') == 'c-Src'


```
