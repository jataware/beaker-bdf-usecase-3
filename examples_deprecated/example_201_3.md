# Description
Process remote SIF files to get statements.

# Code
```
import requests
import logging
from .processor import SifProcessor
from .minerva_client import get_sif_filenames_to_ids, default_map_name

logger = logging.getLogger(__name__)
base_url = ('https://git-r3lab.uni.lu/covid/models/-/raw/master/'
            'Executable%20Modules/SBML_qual_build/sif/')

def process_sif_strs(model_id_to_sif_strs, map_name=default_map_name):
    sp = SifProcessor(model_id_to_sif_strs, map_name=map_name)
    sp.extract_statements()

def process_from_web(filenames='all', map_name=default_map_name):
    """Get statements by processing remote SIF files.

    Parameters
    ----------
    filenames : list or str('all')
        Filenames for models that need to be processed (for full list of
        available models see
        https://git-r3lab.uni.lu/covid/models/-/tree/master/
        Executable%20Modules/SBML_qual_build/sif). If set to 'all'
        (default), then all available models will be processed.
    map_name : str
        A name of a disease map to process.

    Returns
    -------
    sp : indra.source.minerva.SifProcessor
        An instance of a SifProcessor with extracted INDRA statements.
    """
    filenames_to_ids = get_sif_filenames_to_ids(map_name=map_name)
    if filenames == 'all':
        filenames = list(filenames_to_ids.keys())
    model_id_to_sif_strs = {}
    for fname in filenames:
        model_id = filenames_to_ids[fname]
        url = base_url + fname
        res = requests.get(url)
        if res.status_code == 200:
            sif_strs = res.text.split('\n')
            model_id_to_sif_strs[model_id] = sif_strs
        else:
            logger.warning('Could not get content from file %s, skipping '
                           'model %d' % (fname, model_id))

```
