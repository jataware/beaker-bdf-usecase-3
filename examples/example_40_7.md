# Description
Updating MeSH ID to name and tree number mappings by downloading and processing XML data from the MeSH FTP site.

# Code
```
import os
import logging
import gzip
from xml.etree import ElementTree as ET

def update_mesh_names():
    """Update Mesh ID to name and tree number mappings."""
    # The structure of the MeSH FTP site is a bit confusing -
    # the addresses used in the update_mesh_names() functions
    # only work for the current year's releases. If you want
    # a previous release, you need to change the following URL to be:
    # ftp://nlmpubs.nlm.nih.gov/online/mesh/<YEAR>/xmlmesh/desc<YEAR>.gz
    url = ('ftp://nlmpubs.nlm.nih.gov/online/mesh/MESH_FILES/'
           f'xmlmesh/desc{MESH_YEAR}.gz')
    desc_path = os.path.join(path, f'mesh_desc{MESH_YEAR}.gz')
    if not os.path.exists(desc_path):
        logging.info('Download %s MeSH descriptors from %s', MESH_YEAR, url)
        urlretrieve(url, desc_path)
        logging.info('Done downloading %s MeSH descriptors', MESH_YEAR)
    # Process the XML and find descriptor records
    with gzip.open(desc_path) as desc_file:
        logging.info('Parsing MeSH descriptors')
        et = ET.parse(desc_file)
    rows = []
    for record in et.iterfind('DescriptorRecord'):
        # We first get the ID and the name
        uid = record.find('DescriptorUI').text
        name = record.find('DescriptorName/String').text
        term_name_str = _get_term_name_str(record, name)
        tree_numbers = record.findall('TreeNumberList/TreeNumber')
        tree_numbers_str = '|'.join([t.text for t in tree_numbers])
        rows.append((uid, name, term_name_str, tree_numbers_str))

    fname = os.path.join(path, 'mesh_id_label_mappings.tsv')

```
