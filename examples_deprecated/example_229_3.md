# Description
Print a summary of the model specified by the path.

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
def summarize(model_path):
    """Print model summary."""
    from indra.tools.machine.machine import summarize_helper

```
