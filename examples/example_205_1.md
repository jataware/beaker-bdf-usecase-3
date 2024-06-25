# Description
Query the OmniPath web API to get PTMs and ligand-receptor interactions, process them using an OmniPathProcessor, and return the processor object.

# Code
```
import logging
import requests
from .processor import OmniPathProcessor

logger = logging.getLogger(__name__)


def process_from_web():
    """Query the OmniPath web API and return an OmniPathProcessor.

    Returns
    -------
    OmniPathProcessor
        An OmniPathProcessor object which contains a list of extracted
        INDRA Statements in its statements attribute.
    """
    ptm_json = _get_modifications()
    ligrec_json = _get_interactions()
    op = OmniPathProcessor(ptm_json=ptm_json, ligrec_json=ligrec_json)
    op.process_ptm_mods()
    op.process_ligrec_interactions()

```
