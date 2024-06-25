# Description
Processing a text string using the ISI reader to extract INDRA statements

# Code
```
from datetime import datetime
import os
import glob
import json
import shutil
import logging
import tempfile
import subprocess
from indra.sources.isi.processor import IsiProcessor
from indra.sources.isi.preprocessor import IsiPreprocessor
logger = logging.getLogger(__name__)

class IsiRuntimeError(Exception):

def process_text(text, pmid=None, **kwargs):
    """Process a string using the ISI reader and extract INDRA statements.

    Parameters
    ----------
    text : str
        A text string to process
    pmid : Optional[str]
        The PMID associated with this text (or None if not specified)
    num_processes : Optional[int]
        Number of processes to parallelize over
    cleanup : Optional[bool]
        If True, the temporary folders created for preprocessed reading input
        and output are removed. Default: True
    add_grounding : Optional[bool]
        If True the extracted Statements' grounding is mapped
    molecular_complexes_only : Optional[bool]
        If True, only Complex statements between molecular entities are retained
        after grounding.

    Returns
    -------
    ip : indra.sources.isi.processor.IsiProcessor
        A processor containing statements
    """
    cleanup = kwargs.get('cleanup', True)

    # Create a temporary directory to store the proprocessed input
    pp_dir = tempfile.mkdtemp('indra_isi_pp_output')

    pp = IsiPreprocessor(pp_dir)
    extra_annotations = {}
    pp.preprocess_plain_text_string(text, pmid, extra_annotations)

    # Run the ISI reader and extract statements
    ip = process_preprocessed(pp, **kwargs)

    if cleanup:
        # Remove temporary directory with processed input
        shutil.rmtree(pp_dir)
    else:
        logger.info('Not cleaning up %s' % pp_dir)


```
