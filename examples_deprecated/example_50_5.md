# Description
Print a summary of a list of statements by statement type.

# Code
```
from collections import Counter

def print_stmt_summary(statements: Collection[Statement]):
    """Print a summary of a list of statements by statement type

    Requires the tabulate package (https://pypi.org/project/tabulate).

    Parameters
    ----------
    statements : List[Statement]
        The list of INDRA Statements to be printed.
    """
    from tabulate import tabulate
    print(tabulate(
        Counter(
            statement.__class__.__name__
            for statement in statements
        ).most_common(),
        headers=["Statement Type", "Count"],
        tablefmt='github',

```
