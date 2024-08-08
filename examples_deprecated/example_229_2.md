# Description
Run the INDRA machine with a PubMed search for new papers using the specified model and configuration.

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
@click.option('--config', help='Specify configuration file path, otherwise '
                               'looks for config.yaml in model path')
@click.option('-d', '--num-days', type=int)
def run_with_search(model_path, config, num_days):
    """Run with PubMed search for new papers."""
    from indra.tools.machine.machine import run_with_search_helper

```
