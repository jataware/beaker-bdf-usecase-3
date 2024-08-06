# Description
Process a single local SIF file to get statements.

# Code
```
import logging
from .processor import SifProcessor
from .minerva_client import get_sif_filenames_to_ids, default_map_name

logger = logging.getLogger(__name__)
base_url = ('https://git-r3lab.uni.lu/covid/models/-/raw/master/'
            'Executable%20Modules/SBML_qual_build/sif/')

def process_files(ids_to_filenames, map_name=default_map_name):
    model_id_to_sif_strs = {}
    for model_id, filename in ids_to_filenames.items():
        with open(filename, 'r') as f:
            sif_strs = f.readlines()
        model_id_to_sif_strs[model_id] = sif_strs
    return process_sif_strs(model_id_to_sif_strs, map_name)

def process_sif_strs(model_id_to_sif_strs, map_name=default_map_name):
    sp = SifProcessor(model_id_to_sif_strs, map_name=map_name)
    sp.extract_statements()

def process_file(filename, model_id, map_name=default_map_name):
    """Get statements by processing a single local SIF file.

    Parameters
    ----------
    filename : str
        A name (or path) of a local SIF file to process.
    model_id : int
        ID of a model corresponding to file content. Model ID is needed to
        find relevant references.
    map_name : str
        A name of a disease map to process.

    Returns
    -------
    sp : indra.source.minerva.SifProcessor
        An instance of a SifProcessor with extracted INDRA statements.
    """

```
