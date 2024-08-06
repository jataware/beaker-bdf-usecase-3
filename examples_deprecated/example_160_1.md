# Description
Creating an IndexCardAssembler

# Code
```
import json
import logging
from indra.statements import *
from indra.literature import id_lookup
from indra.databases import hgnc_client, uniprot_client, chebi_client, go_client

logger = logging.getLogger(__name__)

global_submitter = 'indra'

class IndexCard(object):
    def __init__(self):
        self.card  = {
            'pmc_id': None,
            'submitter': None,
            'interaction': {
                'negative_information': False,
                'hypothesis_information' : None,
                'interaction_type': None,
                'participant_a': {
                    'entity_type': None,
                    'entity_text': None,
                    'identifier': None
                    },
                'participant_b': {
                    'entity_type': None,
                    'entity_text': None,
                    'identifier': None
                    }
                }
            }
    def get_string(self):
        return json.dumps(self.card)

def get_participant(agent):
    # Handle missing Agent as generic protein
    if agent is None:
        return get_generic('protein')
    # The Agent is not missing
    text_name = agent.db_refs.get('TEXT')
    if text_name is None:
        text_name = agent.name
    participant = {}
    participant['entity_text'] = [text_name]
    hgnc_id = agent.db_refs.get('HGNC')
    uniprot_id = agent.db_refs.get('UP')
    chebi_id = agent.db_refs.get('CHEBI')
    pfam_def_ids = agent.db_refs.get('PFAM-DEF')
    # If HGNC grounding is available, that is the first choice
    if hgnc_id:
        uniprot_id = hgnc_client.get_uniprot_id(hgnc_id)
    if uniprot_id:
        uniprot_mnemonic = str(uniprot_client.get_mnemonic(uniprot_id))
        participant['identifier'] = 'UNIPROT:%s' % uniprot_mnemonic
        participant['entity_type'] = 'protein'
    elif chebi_id:
        pubchem_id = chebi_client.get_pubchem_id(chebi_id)
        participant['identifier'] = 'PUBCHEM:%s' % pubchem_id
        participant['entity_type'] = 'chemical'
    elif pfam_def_ids:
        participant['entity_type'] = 'protein_family'
        participant['entities'] = []
        pfam_def_list = []
        for p in pfam_def_ids.split('|'):
            dbname, dbid = p.split(':')
            pfam_def_list.append({dbname: dbid})
        for pdi in pfam_def_list:
            # TODO: handle non-uniprot protein IDs here
            uniprot_id = pdi.get('UP')
            if uniprot_id:
                entity_dict = {}
                uniprot_mnemonic = str(uniprot_client.get_mnemonic(uniprot_id))
                gene_name = uniprot_client.get_gene_name(uniprot_id)
                if gene_name is None:
                    gene_name = ""
                entity_dict['entity_text'] = [gene_name]
                entity_dict['identifier'] = 'UNIPROT:%s' % uniprot_mnemonic
                entity_dict['entity_type'] = 'protein'
                participant['entities'].append(entity_dict)
    else:
        participant['identifier'] = ''
        participant['entity_type'] = 'protein'

    features = []
    not_features = []
    # Binding features
    for bc in agent.bound_conditions:
        feature = {
            'feature_type': 'binding_feature',
            'bound_to': {
                # NOTE: get type and identifier for bound to protein
                'entity_type': 'protein',
                'entity_text': [bc.agent.name],
                'identifier': ''
                }
            }
        if bc.is_bound:
            features.append(feature)
        else:
            not_features.append(feature)
    # Modification features
    for mc in agent.mods:
        feature = {
            'feature_type': 'modification_feature',
            'modification_type': mc.mod_type.lower(),
            }
        if mc.position is not None:
            pos = int(mc.position)
            feature['location'] = pos
        if mc.residue is not None:
            feature['aa_code'] = mc.residue
        if mc.is_modified:
            features.append(feature)
        else:
            not_features.append(feature)
    # Mutation features
    for mc in agent.mutations:
        feature = {}
        feature['feature_type'] = 'mutation_feature'
        if mc.residue_from is not None:
            feature['from_aa'] = mc.residue_from
        if mc.residue_to is not None:
            feature['to_aa'] = mc.residue_to
        if mc.position is not None:
            pos = int(mc.position)
            feature['location'] = pos
        features.append(feature)
    if features:
        participant['features'] = features
    if not_features:
        participant['not_features'] = not_features
    return participant

def get_pmc_id(stmt):
    pmc_id = ''
    for ev in stmt.evidence:
        pmc_id = id_lookup(ev.pmid, 'pmid')['pmcid']
        if pmc_id is not None:
            if not pmc_id.startswith('PMC'):
                pmc_id = 'PMC' + pmc_id
        else:
            pmc_id = ''
    return str(pmc_id)

def get_evidence_info(stmt):
    ev_txts = []
    contexts = []
    hypotheses = []
    evs = (('', stmt.evidence),
           ('PARTIAL: ', ([] if not hasattr(stmt, 'partial_evidence')
                          else stmt.partial_evidence)))
    for prefix, ev_list in evs:
        for ev in ev_list:
            if ev.text is None:
                ev_txts.append(
                    '%sEvidence text not available for %s entry: %s' %
                    (prefix, ev.source_api, ev.source_id))
            else:
                ev_txts.append('%s%s' % (prefix, ev.text))

            if ev.context and ev.context.species:
                species = ev.context.species
                obj = {}
                obj['name'] = species.name
                obj['taxonomy'] = species.db_refs.get('TAXONOMY')
                    if species.db_refs is not None else None
            else:
                obj = None
            contexts.append(obj)

            hypothesis = ev.epistemics.get('hypothesis')
            hypotheses.append(hypothesis)
    return {'text': ev_txts,
            'context': contexts,
            'hypothesis': hypotheses}

class IndexCardAssembler(object):
    @staticmethod
    def assemble_one_card(stmt, pmc_override=None):
        if isinstance(stmt, Modification):
            card = assemble_modification(stmt)
        elif isinstance(stmt, SelfModification):
            card = assemble_selfmodification(stmt)
        elif isinstance(stmt, Complex):
            card = assemble_complex(stmt)
        elif isinstance(stmt, Translocation):
            card = assemble_translocation(stmt)
        elif isinstance(stmt, RegulateActivity):
            card = assemble_regulate_activity(stmt)
        elif isinstance(stmt, RegulateAmount):
            card = assemble_regulate_amount(stmt)
        else:
            return None
        if card is not None:
            card.card['meta'] = {'id': stmt.uuid, 'belief': stmt.belief}
            ev_info = get_evidence_info(stmt)
            card.card['interaction']['hypothesis_information'] = ev_info['hypothesis']
            card.card['interaction']['context'] = ev_info['context']
            card.card['evidence'] = ev_info['text']
            card.card['submitter'] = global_submitter
            if pmc_override is not None:
                card.card['pmc_id'] = pmc_override
            else:
                card.card['pmc_id'] = get_pmc_id(stmt)

class IndexCardAssembler(object):
    """Assembler creating index cards from a set of INDRA Statements.

    Parameters
    ----------
    statements : list
        A list of INDRA statements to be assembled.
    pmc_override : Optional[str]
        A PMC ID to assign to the index card.

    Attributes
    ----------
    statements : list
        A list of INDRA statements to be assembled.
    """

    def __init__(self, statements=None, pmc_override=None):
        if statements is None:
            self.statements = []
        else:
            self.statements = statements
        self.cards = []
        self.pmc_override = pmc_override

    def add_statements(self, statements):
        """Add statements to the assembler.

        Parameters
        ----------
        statements : list[indra.statement.Statements]
            The list of Statements to add to the assembler.
        """
        self.statements.extend(statements)

    def make_model(self):
        """Assemble statements into index cards."""
        for stmt in self.statements:
            card = self.assemble_one_card(stmt, self.pmc_override)
            if card is not None:
                self.cards.append(card)
        return self.cards

    @staticmethod
    def assemble_one_card(stmt, pmc_override=None):
        if isinstance(stmt, Modification):
            card = assemble_modification(stmt)
        elif isinstance(stmt, SelfModification):
            card = assemble_selfmodification(stmt)
        elif isinstance(stmt, Complex):
            card = assemble_complex(stmt)
        elif isinstance(stmt, Translocation):
            card = assemble_translocation(stmt)
        elif isinstance(stmt, RegulateActivity):
            card = assemble_regulate_activity(stmt)
        elif isinstance(stmt, RegulateAmount):
            card = assemble_regulate_amount(stmt)
        else:
            return None
        if card is not None:
            card.card['meta'] = {'id': stmt.uuid, 'belief': stmt.belief}
            ev_info = get_evidence_info(stmt)
            card.card['interaction']['hypothesis_information'] = \
                ev_info['hypothesis']
            card.card['interaction']['context'] = ev_info['context']
            card.card['evidence'] = ev_info['text']
            card.card['submitter'] = global_submitter
            if pmc_override is not None:
                card.card['pmc_id'] = pmc_override
            else:
                card.card['pmc_id'] = get_pmc_id(stmt)
        return card

    def print_model(self):
        """Return the assembled cards as a JSON string.

        Returns
        -------
        cards_json : str
            The JSON string representing the assembled cards.
        """
        cards = [c.card for c in self.cards]
        # If there is only one card, print it as a single
        # card not as a list
        if len(cards) == 1:
            cards = cards[0]
        cards_json = json.dumps(cards, indent=1)
        return cards_json

    def save_model(self, file_name='index_cards.json'):
        """Save the assembled cards into a file.

        Parameters
        ----------
        file_name : Optional[str]
            The name of the file to save the cards into. Default:
            index_cards.json
        """
        with open(file_name, 'wt') as fh:
            fh.write(self.print_model())


class IndexCard(object):
    def __init__(self):

```
