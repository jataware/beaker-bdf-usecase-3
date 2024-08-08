# Description
Updating the HMDB to ChEBI mapping by downloading and parsing HMDB metabolite data and saving valid mappings.

# Code
```
import os
import logging
import requests
from zipfile import ZipFile
from xml.etree import ElementTree as ET
from indra.util import write_unicode_csv
from indra.databases import chebi_client

def update_hmdb_chebi_map():
    logger.info('--Updating HMDB to ChEBI entries----')
    ns = {'hmdb': 'http://www.hmdb.ca'}
    url = 'http://www.hmdb.ca/system/downloads/current/hmdb_metabolites.zip'
    fname = os.path.join(path, 'hmdb_metabolites.zip')
    logger.info('Downloading %s' % url)
    urlretrieve(url, fname)
    mappings = []
    with ZipFile(fname) as input_zip:
        with input_zip.open('hmdb_metabolites.xml') as fh:
            for event, elem in ET.iterparse(fh, events=('start', 'end')):
                #print(elem.tag)
                if event == 'start' and \
                        elem.tag == '{%s}metabolite' % ns['hmdb']:
                    hmdb_id = None
                    chebi_id = None
                # Important: we only look at accession if there's no HMDB
                # ID yet, otherwise we pick up secondary accession tags
                elif event == 'start' and \
                        elem.tag == '{%s}accession' % ns['hmdb'] and \
                        not hmdb_id:
                    hmdb_id = elem.text
                elif event == 'start' and \
                        elem.tag == '{%s}chebi_id' % ns['hmdb']:
                    chebi_id = elem.text
                elif event == 'end' and \
                        elem.tag == '{%s}metabolite' % ns['hmdb']:
                    if hmdb_id and chebi_id:
                        name = chebi_client.get_chebi_name_from_id(chebi_id)
                        if not name:
                            print('Likely invalid ChEBI mapping: ',
                                  hmdb_id, chebi_id)
                            continue
                        mappings.append([hmdb_id, chebi_id])
                elem.clear()
    fname = os.path.join(path, 'hmdb_to_chebi.tsv')
    mappings = [['HMDB_ID', 'CHEBI_ID']] + sorted(mappings, key=lambda x: x[0])

```
