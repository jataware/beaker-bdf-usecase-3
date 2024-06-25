# Description
Process one or more local SIF files to get statements.

# Code
```
import logging
from .processor import SifProcessor
from .minerva_client import get_sif_filenames_to_ids, default_map_name

logger = logging.getLogger(__name__)
base_url = ('https://git-r3lab.uni.lu/covid/models/-/raw/master/'
            'Executable%20Modules/SBML_qual_build/sif/')

def process_sif_strs(model_id_to_sif_strs, map_name=default_map_name):
    sp = SifProcessor(model_id_to_sif_strs, map_name=map_name)
    sp.extract_statements()

def process_files(ids_to_filenames, map_name=default_map_name):
    """Get statements by processing one or more local SIF files.

    Parameters
    ----------
    ids_to_file_names : dict
        A dictionary mapping model IDs to files containing model content as
        SIF. Model IDs are needed to find relevant references.
    map_name : str
        A name of a disease map to process.

    Returns
    -------
    sp : indra.source.minerva.SifProcessor
        An instance of a SifProcessor with extracted INDRA statements.
    """
    model_id_to_sif_strs = {}
    for model_id, filename in ids_to_filenames.items():
        with open(filename, 'r') as f:
            sif_strs = f.readlines()
        model_id_to_sif_strs[model_id] = sif_strs

```
