# Description
Example of defining a Command Line Interface (CLI) command for a processor.

# Code
```
import pickle
from typing import List
import click
from statements import print_stmt_summary, stmts_from_json

    def get_cli(cls) -> "click.Command":
        """Get the CLI for this processor."""
        import click

        @click.command()
        @click.option('--save', is_flag=True)
        def _main(save: bool):
            click.secho(cls.name, fg='green', bold=True)
            inst = cls()
            stmts = inst.extract_statements()
            if save:
                import pystow

                stmts_path = pystow.join("indra", cls.name, name="stmts.pkl")
                with stmts_path.open("wb") as file:
                    pickle.dump(stmts, file, protocol=pickle.HIGHEST_PROTOCOL)
            print_stmt_summary(stmts)

        return _main

    @classmethod
    def cli(cls) -> None:
        """Run the CLI for this processor."""
        _main = cls.get_cli()

```
