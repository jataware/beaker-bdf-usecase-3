# Description
Create and assemble a Nice CX network from a set of INDRA Statements.

# Code
```
import re
import json
import logging
import itertools
from ndex2.nice_cx_network import NiceCXNetwork
from collections import OrderedDict
from indra.statements import *
from indra.databases import context_client, ndex_client
from indra.databases.identifiers import get_identifiers_url, url_prefixes

db_ns_type_mappings = {'HGNC': 'gene', 'UP': 'protein', 'FPLX': 'proteinfamily', 'CHEBI': 'chemical', 'GO': 'biological_process'}


import re
import json
import time
import logging
import itertools
from ndex2.nice_cx_network import NiceCXNetwork
from collections import OrderedDict
from indra.statements import *
from indra.databases import context_client, ndex_client
from indra.databases.identifiers import get_identifiers_url, url_prefixes


logger = logging.getLogger(__name__)


class NiceCxAssembler(object):
    """Assembles a Nice CX network from a set of INDRA Statements.

    Parameters
    ----------
    stmts : Optional[list[indra.statements.Statement]]
        A list of INDRA Statements to be assembled.
    network_name : Optional[str]
        The name of the network to be assembled. Default: indra_assembled

    Attributes
    ----------
    network : ndex2.nice_cx_network.NiceCXNetwork
        A Nice CX network object that is assembled from Statements.
    """
    def __init__(self, stmts=None, network_name=None):
        self.statements = stmts if stmts else []
        self.network = NiceCXNetwork()
        self.network.set_network_attribute('name',
                                           (network_name if network_name
                                            else 'indra_assembled'))

```
