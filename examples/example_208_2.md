# Description
Print all regulations extracted from REACH output.

# Code
```
import os
import re
import logging
import objectpath
from collections import defaultdict
from indra.statements import *
from indra.util import read_unicode_csv
from indra.databases import go_client, uniprot_client
from indra.ontology.standardize import standardize_db_refs, standardize_agent_name, standardize_name_db_refs
from indra.statements.validate import validate_text_refs
from collections import namedtuple

logger = logging.getLogger(__name__)

Site = namedtuple('Site', ['residue', 'position'])

class ReachProcessor(object):
    def __init__(self, json_dict, pmid=None, organism_priority=None):
        self.tree = objectpath.Tree(json_dict)
        self.organism_priority = organism_priority
        self.statements = []
        self.citation = pmid
        if pmid is None:
            if self.tree is not None:
                self.citation = self.tree.execute('$.events.object_meta.doc_id')
                if not validate_text_refs({'PMID': self.citation}):
                    logger.debug('The citation added is not a valid PMID, removing.')
                    self.citation = None
        self.get_all_events()
    def get_all_events(self):
        self.all_events = {}
        events = self.tree.execute('$.events.frames')
        if events is None:
            return
        for e in events:
            event_type = e.get('type')
            frame_id = e.get('frame_id')
            try:
                self.all_events[event_type].append(frame_id)
            except KeyError:

def print_regulations(self):
    qstr = "$.events.frames[(@.type is 'regulation')]"
    res = self.tree.execute(qstr)
    if res is None:
        return
    for r in res:
        print(r['subtype'])
        for a in r['arguments']:

```
