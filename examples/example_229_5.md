# Description
Convert the model to CX format and optionally write the output to a file.

# Code
```
import os
import sys
import click
from indra.tools.machine.config import copy_default_config

@click.group()
def main():

@main.command()
@click.argument('model_path')
@click.argument('name')
@click.option('--output', type=click.File('w'))
def to_cx(model_path, name, output):
    from indra.tools.machine.machine import load_model, assemble_cx
    model = load_model(model_path)
    stmts = model.get_statements()
    cx_str = assemble_cx(stmts, name)

```
