# Description
Retrieve genes associated with a specific Gene Ontology (GO) ID from the QuickGO API. This function demonstrates how to use the requests module to query an external API and process the resulting TSV data into a list of genes.

# Code
```
import sys
import logging
import csv
import requests


def get_genes_for_go_id(goid):
    quickgo_url = 'https://www.ebi.ac.uk/QuickGO/GAnnotation'
    params = {'goid': goid, 'format':'tsv', 'db':'UniProtKB', 'tax':'9606',
              'col':'proteinSymbol'
           }
    res = requests.get(quickgo_url, params)
    if not res.status_code == 200:
        logger.error('Could not retrieve proteins associated with GO ID %s'
                      % goid)
        return None
    genes = set([])
    # Python 3
    if sys.version_info[0] >= 3:
        tsv_reader = csv.reader(res.text.splitlines(), delimiter='\t')
        for row in tsv_reader:
            genes.add(row[0])
    # Python 2
    else:
        tsv_reader = csv.reader(res.content.splitlines(),
                                delimiter='\t'.encode('utf-8'))
        for row in tsv_reader:
            genes.add(row[0].decode('utf-8')) 

```
