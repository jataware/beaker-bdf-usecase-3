# Description
Processing an NXML file using the ISI reader to extract INDRA statements

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

def process_nxml(nxml_filename, pmid=None, extra_annotations=None, **kwargs):
    """Process an NXML file using the ISI reader

    First converts NXML to plain text and preprocesses it, then runs the ISI
    reader, and processes the output to extract INDRA Statements.

    Parameters
    ----------
    nxml_filename : str
        nxml file to process
    pmid : Optional[str]
        pmid of this nxml file, to be added to the Evidence object of the
        extracted INDRA statements
    extra_annotations : Optional[dict]
        Additional annotations to add to the Evidence object of all extracted
        INDRA statements. Extra annotations called 'interaction' are ignored
        since this is used by the processor to store the corresponding
        raw ISI output.
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
        A processor containing extracted Statements
    """
    if extra_annotations is None:
        extra_annotations = {}

    cleanup = kwargs.get('cleanup', True)

    # Create a temporary directory to store the proprocessed input
    pp_dir = tempfile.mkdtemp('indra_isi_pp_output')

    pp = IsiPreprocessor(pp_dir)
    pp.preprocess_nxml_file(nxml_filename, pmid, extra_annotations)

    # Run the ISI reader and extract statements
    ip = process_preprocessed(pp, **kwargs)

    if cleanup:
        # Remove temporary directory with processed input
        shutil.rmtree(pp_dir)
    else:
        logger.info('Not cleaning up %s' % pp_dir)


```
