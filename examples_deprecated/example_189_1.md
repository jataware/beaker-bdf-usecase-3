# Description
Run Eidos on a set of text files in a folder and produce JSON-LD files.

# Code
```
import os
import logging
from indra import get_config

# Configuration setup
EIDOSPATH = get_config('EIDOSPATH')
eidos_package = 'org.clulab.wm.eidos'
logger = logging.getLogger(__name__)

# Existing function to run Eidos endpoint
def run_eidos(endpoint, *args):
    call_class = '%s.%s' % (eidos_package, endpoint)
    cmd = ['java', '-Xmx12G', '-cp', EIDOSPATH, call_class] + list(args)
    logger.info('Running Eidos with command "%s"' % (' '.join(cmd)))

def extract_from_directory(path_in, path_out):
    """Run Eidos on a set of text files in a folder.

    The output is produced in the specified output folder but
    the output files aren't processed by this function.

    Parameters
    ----------
    path_in : str
        Path to an input folder with some text files
    path_out : str
        Path to an output folder in which Eidos places the output
        JSON-LD files
    """
    path_in = os.path.realpath(os.path.expanduser(path_in))
    path_out = os.path.realpath(os.path.expanduser(path_out))
    logger.info('Running Eidos on input folder %s' % path_in)

```
