# Description
Filter to a given statement type.

# Code
```
import logging

@register_pipeline
def filter_by_type(stmts_in, stmt_type, invert=False, **kwargs):
    """Filter to a given statement type.

    Parameters
    ----------
    stmts_in : list[indra.statements.Statement]
        A list of statements to filter.
    stmt_type : str or indra.statements.Statement
        The class of the statement type to filter for. Alternatively,
        a string matching the name of the statement class, e.g.,
        "Activation" can be used.
        Example: indra.statements.Modification or "Modification"
    invert : Optional[bool]
        If True, the statements that are not of the given type
        are returned. Default: False
    save : Optional[str]
        The name of a pickle file to save the results (stmts_out) into.

    Returns
    -------
    stmts_out : list[indra.statements.Statement]
        A list of filtered statements.
    """
    if isinstance(stmt_type, str):
        stmt_type = get_statement_by_name(stmt_type)
    logger.info('Filtering %d statements for type %s%s...' %
                (len(stmts_in), 'not ' if invert else '',
                 stmt_type.__name__))
    if not invert:
        stmts_out = [st for st in stmts_in if isinstance(st, stmt_type)]
    else:
        stmts_out = [st for st in stmts_in if not isinstance(st, stmt_type)]

    logger.info('%d statements after filter...' % len(stmts_out))
    dump_pkl = kwargs.get('save')
    if dump_pkl:
        dump_statements(stmts_out, dump_pkl)

```
