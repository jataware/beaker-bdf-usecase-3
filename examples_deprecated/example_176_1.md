# Description
How to load a grounding map from a CSV file

# Code
```
import os
import csv
import json
import logging
from copy import deepcopy
from indra.util import read_unicode_csv
logger = logging.getLogger(__name__)

def replace_hgnc_symbols(gmap):
    """Replace HGNC symbols with IDs in a grounding map."""
    for txt, mapped_refs in deepcopy(gmap).items():
        hgnc_sym = mapped_refs.get('HGNC')
        if hgnc_sym:
            hgnc_id = hgnc_client.get_hgnc_id(hgnc_sym)
            # Override the HGNC symbol entry from the grounding
            # map with an HGNC ID
            if hgnc_id:
                mapped_refs['HGNC'] = hgnc_id
            else:
                logger.error('No HGNC ID corresponding to gene '
                             'symbol %s in grounding map.' % hgnc_sym)
                # Remove the HGNC symbol in this case
                mapped_refs.pop('HGNC')
        # In case the only grounding was eliminated, we remove the entry
        # completely
        if mapped_refs:
            gmap[txt] = mapped_refs

def load_grounding_map(grounding_map_path, lineterminator='\r\n',
                       hgnc_symbols=True):
    """Return a grounding map dictionary loaded from a csv file.

    In the file pointed to by grounding_map_path, the number of name_space ID
    pairs can vary per row and commas are
    used to pad out entries containing fewer than the maximum amount of
    name spaces appearing in the file. Lines should be terminated with \r\n
    both a carriage return and a new line by default.

    Optionally, one can specify another csv file (pointed to by ignore_path)
    containing agent texts that are degenerate and should be filtered out.

    It is important to note that this function assumes that the mapping file
    entries for the HGNC key are symbols not IDs. These symbols are converted
    to IDs upon loading here.

    Parameters
    ----------
    grounding_map_path : str
        Path to csv file containing grounding map information. Rows of the file
        should be of the form <agent_text>,<name_space_1>,<ID_1>,...
        <name_space_n>,<ID_n>
    lineterminator : Optional[str]
        Line terminator used in input csv file. Default: \r\n
    hgnc_symbols : Optional[bool]
        Set to True if the grounding map file contains HGNC symbols rather than
        IDs. In this case, the entries are replaced by IDs. Default: True

    Returns
    -------
    g_map : dict
        The grounding map constructed from the given files.
    """
    gmap = {}
    map_rows = read_unicode_csv(grounding_map_path, delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL,
                                lineterminator=lineterminator)
    for row in map_rows:
        txt = row[0]
        keys = [entry for entry in row[1::2] if entry]
        values = [entry for entry in row[2::2] if entry]
        if not keys or not values:
            logger.warning('Missing grounding entries for %s, skipping.' % txt)
            continue
        if len(keys) != len(values):
            logger.warning('Mismatched keys and values in row %s, skipping.' %
                           str(row))
            continue
        gmap[txt] = dict(zip(keys, values))
    if hgnc_symbols:
        gmap = replace_hgnc_symbols(gmap)

```
