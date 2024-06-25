# Description
Main script to handle different operations (build, clean, clean-old, clean-all, version) for managing BioOntology and its cache.

# Code
```
import os
import sys
import glob
import shutil
import logging
from .ontology import BioOntology, CACHE_DIR


if __name__ == '__main__':
    if len(sys.argv) < 2:
        logger.info('Operation missing. Supported operations: '
                    'build, clean, clean-old, clean-all, version.')
        sys.exit(1)
    operation = sys.argv[1]
    if operation == 'build':
        BioOntology().initialize(rebuild=True)
    elif operation == 'version':
        print(BioOntology.version)
    elif operation.startswith('clean'):
        parent_dir = os.path.normpath(os.path.join(CACHE_DIR, os.pardir))
        version_paths = glob.glob(os.path.join(parent_dir, '*', ''))
        if operation == 'clean-all':
            to_remove = [parent_dir]
        else:
            to_remove = []
            for version_path in version_paths:
                version = os.path.basename(os.path.normpath(version_path))
                if operation == 'clean-old' and version != BioOntology.version:
                    to_remove.append(version_path)
                elif operation == 'clean' and version == BioOntology.version:
                    to_remove.append(version_path)
        for rem in to_remove:
            logger.info('Removing %s' % rem)

```
