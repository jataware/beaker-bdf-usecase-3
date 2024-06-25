# Description
Map grounding using the GroundingMapper.

# Code
```
import logging
from indra.pipeline import register_pipeline

@register_pipeline
def map_grounding(stmts_in, do_rename=True, grounding_map=None,
                  misgrounding_map=None, agent_map=None, ignores=None, use_adeft=True,
                  gilda_mode=None, grounding_map_policy='replace', **kwargs):
    """Map grounding using the GroundingMapper.

    Parameters
    ----------
    stmts_in : list[indra.statements.Statement]
        A list of statements to map.
    do_rename : Optional[bool]
        If True, Agents are renamed based on their mapped grounding.
    grounding_map : Optional[dict]
        A user supplied grounding map which maps a string to a
        dictionary of database IDs (in the format used by Agents'
        db_refs).
    misgrounding_map : Optional[dict]
        A user supplied misgrounding map which maps a string to a known
        misgrounding which can be eliminated by the grounding mapper.
    ignores : Optional[list]
        A user supplied list of ignorable strings which, if present as an
        Agent text in a Statement, the Statement is filtered out.
    use_adeft : Optional[bool]
        If True, Adeft will be attempted to be used for acronym disambiguation.
        Default: True
    gilda_mode : Optional[str]
        If None, Gilda will not be for disambiguation. If 'web', the address
        set in the GILDA_URL configuration or environmental variable is
        used as a Gilda web service. If 'local', the gilda package is
        imported and used locally.
    save : Optional[str]
        The name of a pickle file to save the results (stmts_out) into.
    grounding_map_policy : Optional[str]
        If a grounding map is provided, use the policy to extend or replace
        a default grounding map. Default: 'replace'.

    Returns
    -------
    stmts_out : list[indra.statements.Statement]
        A list of mapped statements.
    """
    from indra.preassembler.grounding_mapper import GroundingMapper,\
        default_agent_map, default_grounding_map, default_ignores, \
        default_misgrounding_map
    logger.info('Mapping grounding on %d statements...' % len(stmts_in))
    ignores = ignores if ignores else default_ignores
    gm = grounding_map
    if not gm:
        gm = default_grounding_map
    elif grounding_map_policy == 'extend':
        default_gm = {k: v for (k, v) in default_grounding_map.items()}
        default_gm.update(gm)
        gm = default_gm
    misgm = misgrounding_map if misgrounding_map else default_misgrounding_map
    agent_map = agent_map if agent_map else default_agent_map
    gm = GroundingMapper(gm, agent_map=agent_map,
                         misgrounding_map=misgm, ignores=ignores,
                         use_adeft=use_adeft, gilda_mode=gilda_mode)
    stmts_out = gm.map_stmts(stmts_in, do_rename=do_rename)
    # Patch wrong locations in Translocation statements
    for stmt in stmts_out:
        if isinstance(stmt, Translocation):
            if not stmt.from_location:
                stmt.from_location = None
            if not stmt.to_location:
                stmt.to_location = None
    dump_pkl = kwargs.get('save')
    if dump_pkl:
        dump_statements(stmts_out, dump_pkl)

```
