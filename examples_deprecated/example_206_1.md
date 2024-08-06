# Description
Process Post-Translational Modifications (PTM) from OmniPath JSON. Generates INDRA Statements based on PTM data.

# Code
```
from __future__ import unicode_literals

import copy
import logging
from indra.statements.validate import validate_text_refs
from indra.ontology.standardize import standardize_agent_name
from indra.statements import modtype_to_modclass, Agent, Evidence, Complex, get_statement_by_name as stmt_by_name, BoundCondition

logger = logging.getLogger(__name__)

ignore_srcs = [db.lower() for db in ['NetPath', 'SIGNOR', 'ProtMapper', 'BioGRID', 'HPRD-phos', 'phosphoELM']]

class OmniPathProcessor(object):
    def __init__(self, ptm_json=None, ligrec_json=None):
        self.statements = []
        self.ptm_json = ptm_json
        self.ligrec_json = ligrec_json

    @staticmethod
    def _agent_from_up_id(up_id):
        db_refs = {'UP': up_id}
        ag = Agent(up_id, db_refs=db_refs)
        standardize_agent_name(ag)

    def process_ptm_mods(self):
        """Process ptm json if present"""
        if self.ptm_json:
            self.statements += self._stmts_from_op_mods(self.ptm_json)

    def process_ligrec_interactions(self):
        """Process ligand-receptor json if present"""
        if self.ligrec_json:
            self.statements += self._stmt_from_op_lr(self.ligrec_json)

    def _stmts_from_op_mods(self, ptm_json):
        """Build Modification Statements from a list of Omnipath PTM entries
        """
        ptm_stmts = []
        unhandled_mod_types = []
        annot_ignore = {'enzyme', 'substrate', 'residue_type',
                        'residue_offset', 'references', 'modification'}
        if ptm_json is None:
            return []
        for mod_entry in ptm_json:
            # Skip entries without references
            if not mod_entry['references']:
                continue
            enz = self._agent_from_up_id(mod_entry['enzyme'])
            sub = self._agent_from_up_id(mod_entry['substrate'])
            res = mod_entry['residue_type']
            pos = mod_entry['residue_offset']
            evidence = []
            for source_pmid in mod_entry['references']:
                source_db, pmid_ref = source_pmid.split(':', 1)
                # Skip evidence from already known sources
                if source_db.lower() in ignore_srcs:
                    continue
                if 'pmc' in pmid_ref.lower():
                    text_refs = {'PMCID': pmid_ref.split('/')[-1]}
                    pmid = None
                elif not validate_text_refs({'PMID': pmid_ref}):
                    pmid = None
                    text_refs = None
                else:
                    pmid = pmid_ref
                    text_refs = {'PMID': pmid}

                evidence.append(Evidence(
                    source_api='omnipath',
                    source_id=source_db,
                    pmid=pmid,
                    text_refs=text_refs,
                    annotations={k: v for k, v in mod_entry.items() if k not
                                 in annot_ignore}
                ))
            mod_type = mod_entry['modification']
            modclass = modtype_to_modclass.get(mod_type)
            if modclass is None:
                unhandled_mod_types.append(mod_type)
                continue
            else:
                # All evidences filtered out
                if not evidence:
                    continue
                stmt = modclass(enz, sub, res, pos, evidence)
            ptm_stmts.append(stmt)

```
