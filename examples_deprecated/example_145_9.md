# Description
Filter to statements containing genes only.

# Code
```
import logging

def filter_genes_only(stmts_in, specific_only=False, remove_bound=False,
                      **kwargs):
    """Filter to statements containing genes only.

    Parameters
    ----------
    stmts_in : list[indra.statements.Statement]
        A list of statements to filter.
    specific_only : Optional[bool]
        If True, only elementary genes/proteins will be kept and families
        will be filtered out. If False, families are also included in the
        output. Default: False
    save : Optional[str]
        The name of a pickle file to save the results (stmts_out) into.
    remove_bound: Optional[bool]
        If true, removes bound conditions that are not genes
        If false (default), filters out statements with non-gene bound
        conditions

    Returns
    -------
    stmts_out : list[indra.statements.Statement]
        A list of filtered statements.
    """
    logger.info('Filtering %d statements for ones containing genes only...' % 
                len(stmts_in))
    stmts_out = []
    for st in stmts_in:
        genes_only = True
        for agent in st.agent_list():
            if agent is not None:
                criterion = lambda a: _agent_is_gene(a, specific_only)
                if not criterion(agent):
                    genes_only = False
                    break
                if remove_bound:
                    _remove_bound_conditions(agent, criterion)
                else:
                    if _any_bound_condition_fails_criterion(agent, criterion):
                        genes_only = False
                        break

        if genes_only:
            stmts_out.append(st)
    logger.info('%d statements after filter...' % len(stmts_out))
    dump_pkl = kwargs.get('save')
    if dump_pkl:
        dump_statements(stmts_out, dump_pkl)

```
