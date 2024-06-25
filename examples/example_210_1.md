# Description
Extract statements from RLIMS-P JSON and ensure their validity.

# Code
```
import tqdm
from indra.statements.validate import assert_valid_statements
from indra.statements import Agent, Phosphorylation, Autophosphorylation, Evidence

class RlimspProcessor(object):
    def __init__(self, rlimsp_json, doc_id_type=None):
        self._json = rlimsp_json
        self.statements = []
        self.doc_id_type = doc_id_type
        self.processed_texts = []
        return

class RlimspParagraph(object):
    def __init__(self, p_info, doc_id_type):
        self._text = p_info['text']
        self._sentences = []
        self._sentence_starts = []
        for s in p_info['sentence']:
            start = s['charStart']
            stop = s['charEnd']
            self._sentences.append(self._text[start:stop])
            self._sentence_starts.append(start)
        if 'pmid' in p_info and 'pmcid' in p_info:
            self._text_refs = {n.upper(): p_info[n] for n in ['pmid', 'pmcid'] if p_info[n]}
        elif doc_id_type:
            self._text_refs = {doc_id_type.upper(): p_info['docId']}
        else:
            logger.info('Could not establish text refs for paragraph.')
            self._text_refs = {}
        self._relations = p_info['relation']
        self._entity_dict = p_info['entity']
        return

    def get_statements(self):
        stmts = []
        for rel_key, rel_info in self._relations.items():
            args = {e['role']: e['entity_duid'] for e in rel_info['argument']}
            entity_args = args.copy()
            trigger_id = entity_args.pop('TRIGGER')
            trigger_info = self._entity_dict[trigger_id]
            site_id = entity_args.pop('SITE', None)
            entities = {role: self._get_agent(eid) for role, eid in entity_args.items()}
            rel_type = rel_info['relationType']
            enz, enz_coords = entities.get('KINASE', (None, None))
            sub, sub_coords = entities.get('SUBSTRATE', (None, None))
            if sub is None: continue
            trigger_text = trigger_info.get('entityText')
            is_autophos = enz is not None and enz.name == sub.name and 'auto' in trigger_text
            residue, position, site_coords = self._get_site(site_id)
            ev = self._get_evidence(trigger_info, args, [enz_coords, sub_coords], site_coords)
            tax = enz.db_refs.pop('TAX') if enz and 'TAX' in enz.db_refs else sub.db_refs.pop('TAX') if sub and 'TAX' in sub.db_refs else None
            if tax is not None: context = BioContext(species=RefContext(tax, {'TAXONOMY': tax})); ev.context = context
            stmt = Autophosphorylation(sub, residue=residue, position=position, evidence=[ev]) if is_autophos else Phosphorylation(enz, sub, residue=residue, position=position, evidence=[ev])
            stmts.append(stmt)

def extract_statements(self):
    """Extract the statements from the json."""
    for p_info in tqdm.tqdm(self._json, desc='Processing RLIMS-P JSON'):
        para = RlimspParagraph(p_info, self.doc_id_type)
        if para._text not in self.processed_texts:
            self.processed_texts.append(para._text)
            stmts = para.get_statements()
            assert_valid_statements(stmts)
            self.statements.extend(stmts)

```
