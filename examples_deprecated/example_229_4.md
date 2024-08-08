# Description
Run the INDRA machine with a given list of PMIDs from a file.

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
@click.option('--pmids', type=click.File(), default=sys.stdin,
              help="A file with a PMID on each line")
def run_with_pmids(model_path, pmids):
    """Run with given list of PMIDs."""
    from indra.tools.machine.machine import run_with_pmids_helper

```
