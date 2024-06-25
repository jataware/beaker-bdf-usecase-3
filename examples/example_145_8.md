# Description
Filter to statements that have grounded agents.

# Code
```
import logging

def filter_grounded_only(stmts_in, score_threshold=None, remove_bound=False,
                         **kwargs):
    """Filter to statements that have grounded agents.

    Parameters
    ----------
    stmts_in : list[indra.statements.Statement]
        A list of statements to filter.
    score_threshold : Optional[float]
        If scored groundings are available in a list and the highest score
        if below this threshold, the Statement is filtered out.
    save : Optional[str]
        The name of a pickle file to save the results (stmts_out) into.
    remove_bound: Optional[bool]
        If true, removes ungrounded bound conditions from a statement.
        If false (default), filters out statements with ungrounded bound
        conditions.

    Returns
    -------
    stmts_out : list[indra.statements.Statement]
        A list of filtered statements.
    """
    logger.info('Filtering %d statements for grounded agents...' % 
                len(stmts_in))
    stmts_out = []
    for st in stmts_in:
        grounded = True
        for agent in st.agent_list():
            if agent is not None:
                criterion = lambda x: _agent_is_grounded(x, score_threshold)
                if not criterion(agent):
                    grounded = False
                    break
                if not isinstance(agent, Agent):
                    continue
                if remove_bound:
                    _remove_bound_conditions(agent, criterion)
                elif _any_bound_condition_fails_criterion(agent, criterion):
                    grounded = False
                    break
        if grounded:
            stmts_out.append(st)
    logger.info('%d statements after filter...' % len(stmts_out))
    dump_pkl = kwargs.get('save')
    if dump_pkl:
        dump_statements(stmts_out, dump_pkl)

```
