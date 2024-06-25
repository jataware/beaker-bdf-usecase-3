# Description
Create a new RAS Machine directory with the specified structure.

# Code
```
import os
import sys
import click
from indra.tools.machine.config import copy_default_config

@click.group()
def main():

@main.command()
@click.argument('directory')
def make(directory):
    """Makes a RAS Machine directory"""

    if os.path.exists(directory):
        if os.path.isdir(directory):
            click.echo('Directory already exists')
        else:
            click.echo('Path exists and is not a directory')
        sys.exit()

    os.makedirs(directory)
    os.mkdir(os.path.join(directory, 'jsons'))

```
