# Description
The `eliminate_exact_duplicates` method to remove duplicate INDRA statements.

# Code
```

    def eliminate_exact_duplicates(self):
        """Eliminate Statements that were extracted multiple times.

        Due to the way the patterns are implemented, they can sometimes yield
        the same Statement information multiple times, in which case,
        we end up with redundant Statements that aren't from independent
        underlying entries. To avoid this, here, we filter out such
        duplicates.
        """
        # Here we use the deep hash of each Statement, and by making a dict,
        # we effectively keep only one Statement with a given deep hash
        self.statements = list({stmt.get_hash(shallow=False, refresh=True): stmt

```
