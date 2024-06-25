# Description
This example demonstrates how to load a DrugBank XML file and return a DrugbankProcessor by extracting Statements from the given XML file.

# Code
```
import logging
from xml.etree import ElementTree

logger = logging.getLogger(__name__)
from .processor import DrugbankProcessor


def process_element_tree(et):
    logger.info('Extracting DrugBank statements...')
    dp = DrugbankProcessor(et)
    dp.extract_statements()

def process_xml(fname):
    """Return a processor by extracting Statements from DrugBank XML.

    Parameters
    ----------
    fname : str
        The path to a DrugBank XML file to process.

    Returns
    -------
    DrugbankProcessor
        A DrugbankProcessor instance which contains a list of INDRA
        Statements in its statements attribute that were extracted
        from the given XML file.
    """
    logger.info('Loading %s...' % fname)
    et = ElementTree.parse(fname)

```
