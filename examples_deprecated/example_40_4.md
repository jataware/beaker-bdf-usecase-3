# Description
Updating ChEBI references by downloading reference data, saving PubChem mappings, and processing duplicate mappings.

# Code
```
import os
import logging
import requests
import gzip
import pandas
from collections import defaultdict
from urllib.request import urlretrieve
from indra.util import write_unicode_csv, read_unicode_csv

def update_chebi_references():
    # The reference table contains all the automated mappings from ChEBI
    # IDs to IDs in other databases, except CAS, which only has manually
    # curated mappings available in the database_accession table
    # (see implementation in update_cas_to_chebi).
    logger.info('--Updating ChEBI entries----')
    url = 'ftp://ftp.ebi.ac.uk/pub/databases/chebi/' + \
        'Flat_file_tab_delimited/reference.tsv.gz'
    fname = os.path.join(path, 'reference.tsv.gz')
    urlretrieve(url, fname)
    with gzip.open(fname, 'rb') as fh:
        logger.info('Loading %s' % fname)
        df = pandas.read_csv(fh, sep='\t', index_col=None,
                             parse_dates=True, encoding='latin-1')
    # Save PubChem mapping
    fname = os.path.join(path, 'chebi_to_pubchem.tsv')
    logger.info('Saving into %s' % fname)
    df_pubchem = df[df['REFERENCE_DB_NAME']=='PubChem']
    df_pubchem.sort_values(['COMPOUND_ID', 'REFERENCE_ID'], ascending=True,
                           inplace=True)
    df_pubchem.to_csv(fname, sep='\t', columns=['COMPOUND_ID', 'REFERENCE_ID'],
                      header=['CHEBI', 'PUBCHEM'], index=False)

    # Process PubChem mapping to eliminate SID rows and strip CID: prefix
    # If the second column of the row starts with SID:, ignore the row
    # If the second column of the row starts with CID:, strip out the CID
    # prefix Otherwise, include the row unchanged
    original_rows = read_unicode_csv(fname, '\t')
    new_rows = []
    for original_row in original_rows:
        if original_row[1].startswith('CID:'):
            new_row = original_row
            new_row[1] = new_row[1][5:] # Strip out CID:
            new_rows.append(new_row)
        elif original_row[1].startswith('SID:'):
            # Skip SID rows
            continue
        else:
            # Include other rows unchanged
            new_rows.append(original_row)
    write_unicode_csv(fname, new_rows, '\t')

    # In another round of cleanup, we try dealing with duplicate mappings in a
    # principled way such that many-to-one mappings are allowed but one-to-many
    # mappings are eliminated
    original_rows = read_unicode_csv(fname, '\t')
    chebi_pubchem = defaultdict(list)
    pubchem_chebi = defaultdict(list)
    for chebi_id, pc_id in original_rows:
        chebi_pubchem[chebi_id].append(pc_id)
        pubchem_chebi[pc_id].append(chebi_id)
    # Looking for InChIKey matches for duplicates in the ChEBI -> PubChem
    # direction
    logger.info('Getting InChiKey matches for duplicates')
    ik_matches = set()
    for chebi_id, pc_ids in chebi_pubchem.items():
        if len(pc_ids) > 1:
            ck = chebi_client.get_inchi_key(chebi_id)
            for pc_id in pc_ids:
                pk = pubchem_client.get_inchi_key(pc_id)
                if ck == pk:
                    ik_matches.add((chebi_id, pc_id))
    # Looking for InChIKey matches for duplicates in the PubChem -> ChEBI
    # direction
    for pc_id, chebi_ids in pubchem_chebi.items():
        if len(chebi_ids) > 1:
            pk = pubchem_client.get_inchi_key(pc_id)
            for chebi_id in chebi_ids:
                ck = chebi_client.get_inchi_key(chebi_id)
                if ck == pk:
                    ik_matches.add((chebi_id, pc_id))
    rows = read_unicode_csv(fname, '\t')
    header = next(rows)
    header.append('IK_MATCH')
    new_rows = [header]
    for chebi_id, pc_id in rows:
        if (chebi_id, pc_id) in ik_matches:
            new_rows.append([chebi_id, pc_id, 'Y'])
        else:
            new_rows.append([chebi_id, pc_id, ''])

```
