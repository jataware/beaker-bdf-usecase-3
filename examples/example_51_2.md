# Description
Example of creating an Autophosphorylation statement for p38 bound to TAB1.

# Code
```

    --------
    p38 bound to TAB1 cis-autophosphorylates itself (see :pmid:`19155529`).

    >>> tab1 = Agent('TAB1')
    >>> p38_tab1 = Agent('P38', bound_conditions=[BoundCondition(tab1)])

```
