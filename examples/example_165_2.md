# Description
This example demonstrates the usage of the `modification_assemble_one_step` function to add phosphorylation rules to a PySB model using a one-step process.

# Code
```
import logging
from pysb import Model, Monomer, Parameter, Rule, Annotation, Observable, Expression
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

def modification_assemble_one_step(stmt, model, agent_set, parameters,
                                   rate_law=None):
    if stmt.enz is None:
        return

    mc = stmt._get_mod_condition()
    mod_site = get_mod_site_name(mc)

    rule_enz_str = get_agent_rule_str(stmt.enz)
    rule_sub_str = get_agent_rule_str(stmt.sub)
    stmt_type_str = stmt.__class__.__name__.lower()
    rule_name = '%s_%s_%s_%s' % \
        (rule_enz_str, stmt_type_str, rule_sub_str, mod_site)

    # Remove pre-set activity flag
    enz_pattern = get_monomer_pattern(model, stmt.enz)
    # This is where we decide which state to have on the left hand side
    # or the right hand side based on whether it's adding or removing
    # a modification.
    if isinstance(stmt, ist.RemoveModification):
        mod_site_state, unmod_site_state = states[mc.mod_type]
    else:
        unmod_site_state, mod_site_state = states[mc.mod_type]
    sub_unmod = get_monomer_pattern(model, stmt.sub,
                                    extra_fields={mod_site: unmod_site_state})
    sub_mod = get_monomer_pattern(model, stmt.sub,
                                  extra_fields={mod_site: mod_site_state})

    if not rate_law:
        param_name = 'kf_%s%s_%s' % (stmt.enz.name[0].lower(),
                                     stmt.sub.name[0].lower(), mc.mod_type)
        kfp = parameters.get('kf', Param(param_name, 1e-6, True))
        mod_rate = get_create_parameter(model, kfp)
    elif rate_law == 'michaelis_menten':
        # Parameters
        param_name = ('Km_' + stmt.enz.name[0].lower() +
                      stmt.sub.name[0].lower() + '_' + mc.mod_type)
        Kmp = parameters.get('Km', Param(param_name, 1e8, True))
        Km = get_create_parameter(model, Kmp)
        param_name = ('kc_' + stmt.enz.name[0].lower() +
                      stmt.sub.name[0].lower() + '_' + mc.mod_type)
        kcp = parameters.get('kc', Param(param_name, 100, True))
        kcat = get_create_parameter(model, kcp)

        # We need an observable for the substrate to use in the rate law
        sub_obs = Observable(rule_name + '_sub_obs', sub_unmod)
        model.add_component(sub_obs)
        # Note that [E0]*[S] is automatically multiplied into this rate
        # as the product of the reactants therefore they don't appear
        # in this expression
        # v = Vmax*[S]/(Km+[S]) = kcat*[E0]*[S]/(Km + [S])
        mod_rate = Expression(rule_name + '_rate', kcat / (Km + sub_obs))
        model.add_component(mod_rate)

    r = Rule(rule_name,
             enz_pattern + sub_unmod >>
             enz_pattern + sub_mod,
             mod_rate)
    anns = [Annotation(rule_name, enz_pattern.monomer.name,
                       'rule_has_subject'),
            Annotation(rule_name, sub_unmod.monomer.name, 'rule_has_object')]
    anns += [Annotation(rule_name, stmt.uuid, 'from_indra_statement')]

```
