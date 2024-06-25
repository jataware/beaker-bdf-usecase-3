# Description
Run Eidos on a set of text files and process output with INDRA.

# Code
```
import os
import glob
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
    subprocess.call(cmd)

# Existing function to extract from a directory
def extract_from_directory(path_in, path_out):
    path_in = os.path.realpath(os.path.expanduser(path_in))
    path_out = os.path.realpath(os.path.expanduser(path_out))
    logger.info('Running Eidos on input folder %s' % path_in)

def extract_and_process(path_in, path_out, process_fun):
    """Run Eidos on a set of text files and process output with INDRA.

    The output is produced in the specified output folder but
    the output files aren't processed by this function.

    Parameters
    ----------
    path_in : str
        Path to an input folder with some text files
    path_out : str
        Path to an output folder in which Eidos places the output
        JSON-LD files
    process_fun : function
        A function that takes a JSON dict as argument and returns an
        EidosProcessor.

    Returns
    -------
    stmts : list[indra.statements.Statements]
        A list of INDRA Statements
    """
    path_in = os.path.realpath(os.path.expanduser(path_in))
    path_out = os.path.realpath(os.path.expanduser(path_out))
    extract_from_directory(path_in, path_out)
    jsons = glob.glob(os.path.join(path_out, '*.jsonld'))
    logger.info('Found %d JSON-LD files to process in %s' %
                (len(jsons), path_out))
    stmts = []
    for json in jsons:
        ep = process_fun(json)
        if ep:
            stmts += ep.statements

```
