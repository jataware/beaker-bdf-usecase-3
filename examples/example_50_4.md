# Description
Print a formatted list of statements along with evidence text.

# Code
```
import logging
from indra.statements.statements import Statement

logger = logging.getLogger(__name__)

def set_pretty_print_max_width(new_max):
    global pretty_print_max_width
    if new_max is not None and not isinstance(new_max, int):
        raise ValueError("Max width must be an integer or None.")

def pretty_print_stmts(stmt_list: List[Statement],
                       stmt_limit: Optional[int] = None,
                       ev_limit: Optional[int] = 5,
                       width: Optional[int] = None) -> None:
    """Print a formatted list of statements along with evidence text.

    Requires the tabulate package (https://pypi.org/project/tabulate).

    Parameters
    ----------
    stmt_list : List[Statement]
        The list of INDRA Statements to be printed.
    stmt_limit : Optional[int]
        The maximum number of INDRA Statements to be printed. If None, all
        Statements are printed. (Default is None)
    ev_limit : Optional[int]
        The maximum number of Evidence to print for each Statement. If None, all
        evidence will be printed for each Statement. (Default is 5)
    width : Optional[int]
        Manually set the width of the table. If `None` the function will try to
        match the current terminal width using `os.get_terminal_size()`.  If
        this fails the width defaults to 80 characters. The maximum width can
        be controlled by setting :data:`pretty_print_max_width` using the
        :func:`set_pretty_print_max_width` function. This is useful in 
        Jupyter notebooks where the environment returns a terminal size
        of 80 characters regardless of the width of the window. (Default
        is None).
    """
    # Import some modules helpful for text formatting.
    from textwrap import TextWrapper
    from tabulate import tabulate
    from os import get_terminal_size

    # Try to get the actual number of columns in the terminal.
    if width is None:
        width = 80
        try:
            width = get_terminal_size().columns
        except Exception as e:
            logger.debug(f"Failed to get terminal size (using default "
                         f"{width}): {e}.")

        # Apply the maximum.
        if pretty_print_max_width is not None:
            assert isinstance(pretty_print_max_width, int)
            width = min(width, pretty_print_max_width)

    # Parameterize the text wrappers that format the ev text and the metadata.
    stmt_tr = TextWrapper(width=width)
    metadata_tr = TextWrapper(width=16)
    evidence_tr = TextWrapper(width=width - metadata_tr.width - 2)

    # Print the table.
    for i, s in enumerate(stmt_list[:stmt_limit]):

        # Print the Statement heading.
        stmt_str = f"[LIST INDEX: {i}] " + str(s)
        print(stmt_tr.fill(stmt_str))
        print("="*width)

        # Print the evidence
        for j, ev in enumerate(s.evidence[:ev_limit]):

            # Gather the metadata we want to display.
            metadata = [("EV INDEX", j), ("SOURCE", ev.source_api)]
            for id_type in ['PMID', 'PMCID', 'DOI']:
                if id_type in ev.text_refs:
                    metadata.append((id_type, ev.text_refs[id_type]))
                    break

            # Form the metadata string to fill out its allocated space.
            metadata_str = '\n'.join(line + ' '*(metadata_tr.width - len(line))
                                     for k, v in metadata
                                     for line in metadata_tr.wrap(f"{k}: {v}"))

            # Form the evidence string.
            if ev.text:
                text_str = evidence_tr.fill(ev.text)
            else:
                text_str = evidence_tr.fill("(No evidence text)")

            # Print the entire thing
            full_str = tabulate([[metadata_str, text_str]], tablefmt='plain')
            print(full_str)
            print('-'*width)

```
