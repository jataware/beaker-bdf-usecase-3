# Description
Filter to statements with belief above a given cutoff.

# Code
```
import logging

def filter_belief(stmts_in, belief_cutoff, **kwargs):
    """Filter to statements with belief above a given cutoff.

    Parameters
    ----------
    stmts_in : list[indra.statements.Statement]
        A list of statements to filter.
    belief_cutoff : float
        Only statements with belief above the belief_cutoff will be returned.
        Here 0 < belief_cutoff < 1.
    save : Optional[str]
        The name of a pickle file to save the results (stmts_out) into.

    Returns
    -------
    stmts_out : list[indra.statements.Statement]
        A list of filtered statements.
    """
    dump_pkl = kwargs.get('save')
    logger.info('Filtering %d statements to above %f belief' %
                (len(stmts_in), belief_cutoff))
    # The first round of filtering is in the top-level list
    stmts_out = []
    # Now we eliminate supports/supported-by
    for stmt in stmts_in:
        if stmt.belief < belief_cutoff:
            continue
        stmts_out.append(stmt)
        supp_by = []
        supp = []
        for st in stmt.supports:
            if st.belief >= belief_cutoff:
                supp.append(st)
        for st in stmt.supported_by:
            if st.belief >= belief_cutoff:
                supp_by.append(st)
        stmt.supports = supp
        stmt.supported_by = supp_by
    logger.info('%d statements after filter...' % len(stmts_out))
    if dump_pkl:
        dump_statements(stmts_out, dump_pkl)

```
