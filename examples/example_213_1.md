# Description
An example showing how to instantiate and use the SignorProcessor class to process a SIGNOR dataset.

# Code
```
import re
import logging
from copy import deepcopy
from collections import Counter
from os.path import join, dirname
import tqdm
from indra.statements import *
from indra.util import read_unicode_csv
from indra.resources import get_resource_path
from indra.ontology.standardize import standardize_name_db_refs, get_standard_agent
from indra.sources.reach.processor import parse_amino_acid_string
from indra.databases import hgnc_client, uniprot_client, chebi_client
from indra.databases.identifiers import ensure_prefix

logger = logging.getLogger(__name__)

def _read_famplex_map():
    fname = get_resource_path('famplex_map.tsv')
    raw_map = read_unicode_csv(fname, '\t')
    m = {}
    for row in raw_map:
        m[(row[0], row[1])] = row[2]
    return m

famplex_map = _read_famplex_map()

def _parse_residue_positions(residue_field):
    res_strs = [rs.strip() for rs in residue_field.split(';')]
    return [parse_amino_acid_string(rp) for rp in res_strs]

def get_ref_context(db_ns, db_id):
    db_id = db_id.strip()
    if db_ns in {'BTO'}:
        db_id = ensure_prefix(db_ns, db_id)
    standard_name, db_refs = standardize_name_db_refs({db_ns: db_id})
    return RefContext(standard_name, db_refs)

def process_uniprot_entry(up_id):
    if up_id == 'P17861_P17861-2':
        up_id = 'P17861-2'
    parts = up_id.split('-')
    if len(parts) == 1:
        return {'UP': up_id}
    elif parts[1].startswith('PRO'):
        return {'UP': parts[0], 'UPPRO': parts[1]}
    else:

class SignorProcessor(object):
    """Processor for Signor dataset, available at http://signor.uniroma2.it.

    Parameters
    ----------
    data : iterator
        Iterator over rows of a SIGNOR CSV file.
    complex_map : dict
        A dict containing SIGNOR complexes, keyed by their IDs.

    Attributes
    ----------
    statements : list[indra.statements.Statements]
        A list of INDRA Statements extracted from the SIGNOR table.
    stats : dict
        A dictionary containing statistics about the processing, useful
        for determining any unprocessed entries and debugging.
    """
    def __init__(self, data, complex_map=None):
        self._data = data
        if complex_map is None:
            self.complex_map = {}
        else:
            self.complex_map = complex_map
        self.stats = {}

        # Process into statements
        self.statements = []

        # Keys missing from FamPlex map
        self.stats['famplex_missing'] = []

        # Counter listing the frequency of different mechanisms that are
        # not handled by the processor.
        self.stats['unhandled_mech_ctr'] = Counter()

        # List of SignorRow namedtuples
        # List of rows where no mechanism statements were generated.
        self.stats['no_mech_rows'] = []

        for idx, row in enumerate(tqdm.tqdm(self._data,
                                            desc='Processing SIGNOR rows')):
            row_stmts, no_mech = self._process_row(row)
            if row_stmts is None:
                continue
            if no_mech:
                self.stats['no_mech_rows'].append(row)
            self.statements.extend(row_stmts)

        # Counter listing the frequency of different MECHANISM types in the
        # list of no-mechanism rows.
        # No-mechanism rows by mechanism type
        no_mech_ctr = Counter([row.MECHANISM
                               for row in self.stats['no_mech_rows']])
        self.stats['no_mech_ctr'] = \
            sorted([(k, v) for k, v in no_mech_ctr.items()],
                   key=lambda x: x[1], reverse=True)

        # Add a Complex statement for each Signor complex
        for complex_id in tqdm.tqdm(sorted(self.complex_map.keys()),
                                    desc='Processing SIGNOR complexes'):
            agents = self._get_complex_agents(complex_id)
            if len(agents) < 2:
                logger.info('Skipping Complex %s with less than 2 members' %
                            complex_id)
                continue
            # If we returned with None, we skip this complex
            if not agents:
                continue
            ev = Evidence(source_api='signor', source_id=complex_id,
                          text='Inferred from SIGNOR complex %s' % complex_id)
            s = Complex(agents, evidence=[ev])
            self.statements.append(s)

```
