# Description
This example demonstrates how to get a DrugbankProcessor using the process_xml function with the drugbank_downloader module.

# Code
```
import logging
from typing import Optional, Sequence, Union
import drugbank_downloader
from xml.etree import ElementTree

logger = logging.getLogger(__name__)
from .processor import DrugbankProcessor

def process_element_tree(et):
    logger.info('Extracting DrugBank statements...')
    dp = DrugbankProcessor(et)
    dp.extract_statements()

def process_from_web(
    username: Optional[str] = None,
    password: Optional[str] = None,
    version: Optional[str] = None,
    prefix: Union[None, str, Sequence[str]] = None,
) -> DrugbankProcessor:
    """Get a processor using :func:`process_xml` with :mod:`drugbank_downloader`.

    Parameters
    ----------
    username :
        The DrugBank username. If not passed, looks up in the environment
        ``DRUGBANK_USERNAME``. If not found, raises a ValueError.
    password :
        The DrugBank password. If not passed, looks up in the environment
        ``DRUGBANK_PASSWORD``. If not found, raises a ValueError.
    version :
        The DrugBank version. If not passed, uses :mod:`bioversions` to
        look up the most recent version.
    prefix :
        The prefix and subkeys passed to :func:`pystow.ensure` to specify
        a non-default location to download the data to.

    Returns
    -------
    DrugbankProcessor
        A DrugbankProcessor instance which contains a list of INDRA
        Statements in its statements attribute that were extracted
        from the given DrugBank version
    """
    import drugbank_downloader
    et = drugbank_downloader.parse_drugbank(
        username=username,
        password=password,
        version=version,
        prefix=prefix,
    )

```
