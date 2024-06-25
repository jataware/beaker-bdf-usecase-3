# Description
This example demonstrates the usage of the `complex_assemble_one_step` function to add rules for complex assembly in a PySB model.

# Code
```
import logging
import itertools
from pysb import Model, Monomer, Parameter, Rule, Annotation, ComponentDuplicateNameError, ComplexPattern
from pysb.core import SelfExporter
from indra import statements as ist
from .base_agents import BaseAgentSet
from .preassembler import PysbPreassembler


logger = logging.getLogger(__name__)

SelfExporter.do_export = False

def get_agent_rule_str(agent):
    ...   # Function to construct a string from an Agent as part of a PySB rule name


def get_monomer_pattern(model, agent):
    ...   # Function to construct a PySB MonomerPattern from an Agent


def add_rule_to_model(model, rule, annotations=None):
    ...   # Function to add a Rule to a PySB model and handle duplicate component errors


def get_create_parameter(model, param):
    ...   # Function to return a parameter with given name, creating it if needed


def get_uncond_agent(agent):

def complex_assemble_one_step(stmt, model, agent_set, parameters):
    pairs = itertools.combinations(stmt.members, 2)
    for pair in pairs:
        agent1 = pair[0]
        agent2 = pair[1]
        param_name = agent1.name[0].lower() + \
            agent2.name[0].lower() + '_bind'
        kfp = parameters.get('kf', Param('kf_' + param_name, 1e-6, True))
        kf_bind = get_create_parameter(model, kfp)
        krp = parameters.get('kr', Param('kr_' + param_name, 1e-1, True))
        kr_bind = get_create_parameter(model, krp)

        # Make a rule name
        rule_name = '_'.join([get_agent_rule_str(m) for m in pair])
        rule_name += '_bind'

        # Construct full patterns of each agent with conditions
        agent1_pattern = get_monomer_pattern(model, agent1)
        agent2_pattern = get_monomer_pattern(model, agent2)
        agent1_bs = get_binding_site_name(agent2)
        agent2_bs = get_binding_site_name(agent1)
        r = Rule(rule_name, agent1_pattern(**{agent1_bs: None}) +
                 agent2_pattern(**{agent2_bs: None}) >>
                 agent1_pattern(**{agent1_bs: 1}) %
                 agent2_pattern(**{agent2_bs: 1}),
                 kf_bind)
        anns = [Annotation(rule_name, agent1_pattern.monomer.name,
                           'rule_has_subject'),
                Annotation(rule_name, agent1_pattern.monomer.name,
                           'rule_has_object'),
                Annotation(rule_name, agent2_pattern.monomer.name,
                           'rule_has_subject'),
                Annotation(rule_name, agent2_pattern.monomer.name,
                           'rule_has_object'),
                Annotation(rule_name, stmt.uuid, 'from_indra_statement')]
        add_rule_to_model(model, r, anns)

        # In reverse reaction, assume that dissocition is unconditional

        agent1_uncond = get_uncond_agent(agent1)
        agent1_rule_str = get_agent_rule_str(agent1_uncond)
        monomer1_uncond = get_monomer_pattern(model, agent1_uncond)
        agent2_uncond = get_uncond_agent(agent2)
        agent2_rule_str = get_agent_rule_str(agent2_uncond)
        monomer2_uncond = get_monomer_pattern(model, agent2_uncond)
        rule_name = '%s_%s_dissociate' % (agent1_rule_str, agent2_rule_str)
        r = Rule(rule_name, monomer1_uncond(**{agent1_bs: 1}) %
                 monomer2_uncond(**{agent2_bs: 1}) >>
                 monomer1_uncond(**{agent1_bs: None}) +
                 monomer2_uncond(**{agent2_bs: None}),
                 kr_bind)
        anns = [Annotation(rule_name, monomer1_uncond.monomer.name,
                           'rule_has_subject'),
                Annotation(rule_name, monomer1_uncond.monomer.name,
                           'rule_has_object'),
                Annotation(rule_name, monomer2_uncond.monomer.name,
                           'rule_has_subject'),
                Annotation(rule_name, monomer2_uncond.monomer.name,
                           'rule_has_object'),
                Annotation(rule_name, stmt.uuid, 'from_indra_statement')]

```
