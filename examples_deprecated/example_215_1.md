# Description
Process plain text with the Turku Event Extraction System (TEES) and convert its output to INDRA statements using a TEESProcessor.

# Code
```
import os
import codecs
import shutil
import subprocess
tempfile
from indra.sources.tees.processor import TEESProcessor
from indra import get_config

# Setup logger
import logging
logger = logging.getLogger(__name__)

# Define TEES installation paths
tees_candidate_paths = ['../TEES', '~/TEES', '~/Downloads/TEES']
tees_installation_files = ['batch.py', 'classify.py', 'train.py', 'visualize.py']

def process_text(text, pmid=None, python2_path=None):
    """Processes the specified plain text with TEES and converts output to
    supported INDRA statements. Check for the TEES installation is the
    TEES_PATH environment variable, and configuration file; if not found,
    checks candidate paths in tees_candidate_paths. Raises an exception if
    TEES cannot be found in any of these places.

    Parameters
    ----------
    text : str
        Plain text to process with TEES
    pmid : str
        The PMID from which the paper comes from, to be stored in the Evidence
        object of statements. Set to None if this is unspecified.
    python2_path : str
        TEES is only compatible with python 2. This processor invokes this
        external python 2 interpreter so that the processor can be run in
        either python 2 or python 3. If None, searches for an executible named
        python2 in the PATH environment variable.

    Returns
    -------
    tp : TEESProcessor
        A TEESProcessor object which contains a list of INDRA statements
        extracted from TEES extractions
    """
    # Try to locate python2 in one of the directories of the PATH environment
    # variable if it is not provided
    if python2_path is None:
        for path in os.environ["PATH"].split(os.pathsep):
            proposed_python2_path = os.path.join(path, 'python2.7')
            if os.path.isfile(proposed_python2_path):
                python2_path = proposed_python2_path
                print('Found python 2 interpreter at', python2_path)
                break
    if python2_path is None:
        raise Exception('Could not find python2 in the directories ' +
                        'listed in the PATH environment variable. ' +
                        'Need python2 to run TEES.')

    # Run TEES
    a1_text, a2_text, sentence_segmentations = run_on_text(text,
                                                                python2_path)

    # Run the TEES processor
    tp = TEESProcessor(a1_text, a2_text, sentence_segmentations, pmid)

```
