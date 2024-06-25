# Description
Updating CAS to ChEBI mappings by downloading accessions data from ChEBI, processing specific mappings, and saving them.

# Code
```
import os
import logging
import requests
import pandas
from urllib.request import urlretrieve

def update_chebi_accessions():
    # The database_accession table contains manually curated mappings
    # between ChEBI and other databases. It only contains very few mappings
    # to e.g., PubChem, therefore the main resource for those mappings
    # is the reference table (see implementation in update_chebi_entries).
    # The only useful mappings we extract here from the database_accession
    # table are the ones to CAS which are not available in the reference
    # table.
    logger.info('--Updating CAS to ChEBI entries----')
    url = 'ftp://ftp.ebi.ac.uk/pub/databases/chebi/' + \
        'Flat_file_tab_delimited/database_accession.tsv'
    fname = os.path.join(path, 'database_accession.tsv')
    urlretrieve(url, fname)
    with open(fname, 'rb') as fh:
        logger.info('Loading %s' % fname)
        df = pandas.read_csv(fh, sep='\t', index_col=None,
                             dtype=str, na_filter=False)
    fname = os.path.join(path, 'cas_to_chebi.tsv')
    logger.info('Saving into %s' % fname)
    df_cas = df[df['TYPE'] == 'CAS Registry Number']
    df_cas.sort_values(['ACCESSION_NUMBER', 'COMPOUND_ID'], ascending=True,
                       inplace=True)
    # Here we need to map to primary ChEBI IDs
    from indra.databases.chebi_client import get_primary_id
    # This is a wrapper just to strip off the CHEBI prefix to
    # keep the existing conventions
    def _get_primary_id_wrapper(chebi_id):
        return get_primary_id(chebi_id)[6:]
    df_cas.COMPOUND_ID = df_cas.COMPOUND_ID.apply(_get_primary_id_wrapper)
    df_cas.ACCESSION_NUMBER = df_cas.ACCESSION_NUMBER.replace('0103-05-09',
                                                              '103-05-9')
    df_cas.drop_duplicates(subset=['ACCESSION_NUMBER', 'COMPOUND_ID'],
                           inplace=True)
    # Temporary fix, see https://github.com/ebi-chebi/ChEBI/issues/4149
    df_cas = df_cas[~df_cas['ACCESSION_NUMBER'].str.contains('/')]
    # This is to avoid some weird entries like
    # NMRShiftDB:60057454;PubChem:21593947...
    df_cas = df_cas[~df_cas['ACCESSION_NUMBER'].str.contains(':')]
    df_cas.to_csv(fname, sep='\t',
                  columns=['ACCESSION_NUMBER', 'COMPOUND_ID'],

```
