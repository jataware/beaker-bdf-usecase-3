# Description
Assemble a modification and demodification model from INDRA Statements.

# Code
```
from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import itertools
from collections import defaultdict
import indra.statements as ist
from indra.assemblers.pysb.assembler import get_agent_rule_str, get_binding_site_name, abbrevs, states
import logging
logger = logging.getLogger(__name__)

class Nugget(object):
    def __init__(self, id, name, rate):
        self.counters = defaultdict(int)
        self.id = id
        self.name = name
        self.rate = rate
        self.nodes = []
        self.edges = []
        self.typings = {}

    def add_agent(self, agent):
        agent_id = self.add_node(agent.name)
        self.add_typing(agent_id, 'agent')
        for bc in agent.bound_conditions:
            if bc.is_bound:
                test_type = 'is_bnd'
            else:
                test_type = 'is_free'
            bound_name = bc.agent.name
            agent_bs = get_binding_site_name(bc.agent)
            test_name = '%s_bound_to_%s_test' % (agent_id, bound_name)
            agent_bs_id = self.add_node(agent_bs)
            test_id = self.add_node(test_name)
            self.add_edge(agent_bs_id, agent_id)
            self.add_edge(agent_bs_id, test_id)
            self.add_typing(agent_bs_id, 'locus')
            self.add_typing(test_id, test_type)
        for mod in agent.mods:
            mod_site_str = abbrevs[mod.mod_type]
            if mod.residue is not None:
                mod_site_str = mod.residue
            mod_pos_str = mod.position if mod.position is not None else ''
            mod_site = ('%s%s' % (mod_site_str, mod_pos_str))
            site_states = states[mod.mod_type]
            if mod.is_modified:
                val = site_states[1]
            else:
                val = site_states[0]
            mod_site_id = self.add_node(mod_site, {'val': val})
            self.add_edge(mod_site_id, agent_id)
            self.add_typing(mod_site_id, 'state')
        return agent_id

    def add_node(self, name_base, attrs=None):
        if name_base not in self.counters:
            node_id = name_base
        else:
            node_id = '%s_%d' % (name_base, self.counters[name_base])
        node = {'id': node_id}
        if attrs:
            node['attrs'] = attrs
        self.nodes.append(node)
        self.counters[node_id] += 1
        return node_id

    def add_edge(self, from_node, to_node):
        self.edges.append({'from': from_node, 'to': to_node})

    def add_typing(self, node_id, typing):
        self.typings[node_id] = typing

    def get_nugget_dict(self):
        nugget_dict = {'id': self.id, 'graph': {'nodes': self.nodes, 'edges': self.edges}, 'attrs': {'name': self.name, 'rate': self.rate}}
        return nugget_dict

    def get_typing_dict(self):

def _mod_demod_assemble_one_step(stmt, model, is_mod):
    # Define some basic parameters for the modification
    mc = stmt._get_mod_condition()
    mod_condition_name = mc.mod_type

    mod_site = get_mod_site_name(mc)
    rule_enz_str = get_agent_rule_str(stmt.enz)
    rule_sub_str = get_agent_rule_str(stmt.sub)
    nugget_name = '%s_%s_%s_%s' % \
        (rule_enz_str, mod_condition_name, rule_sub_str, mod_site)
    action_name =  nugget_name + '_act'
    kf_mod = 1e-6
    nugget = Nugget(nugget_name, nugget_name, kf_mod)
    enz_id = nugget.add_agent(stmt.enz)
    sub_id = nugget.add_agent(stmt.sub)

    st = states[mod_condition_name]
    from_state, to_state = (st[0], st[1]) if is_mod else (st[1], st[0])

    mod_site_id = nugget.add_node(mod_site, {'val': from_state})
    action_id = nugget.add_node(action_name, {'val': to_state})
    nugget.add_typing(mod_site_id, 'state')
    nugget.add_typing(action_id, 'mod')
    nugget.add_edge(mod_site_id, sub_id)
    nugget.add_edge(action_id, mod_site_id)
    nugget.add_edge(enz_id, action_id)

    # Typing dicts linking the nugget to the Action Graph and to the
    # Kami graph
    typing_dict_ag = {'from': nugget_name, 'to': 'action_graph',
                      'mapping': {}, 'total': False,
                      'ignore_attrs': False}
    typing_dict_kami = {'from': nugget_name, 'to': 'kami',
                        'mapping': nugget.get_typing_dict(), 'total': True,
                        'ignore_attrs': True}
    # Add the graphs for this nugget to the graphs and typing lists
    model['typing'] += [typing_dict_ag, typing_dict_kami]
    model['graphs'].append(nugget.get_nugget_dict())



def modification_assemble_one_step(stmt, model):
    if stmt.enz is None:
        return
    _mod_demod_assemble_one_step(stmt, model, True)


def demodification_assemble_one_step(stmt, model):
    if stmt.enz is None:
        return

```
