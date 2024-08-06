# Description
Read miRBase data into lookup dictionaries

# Code
```
import os

HERE = os.path.dirname(os.path.abspath(__file__))

def _read():
    """Read the miRBase data into some lookup dictionaries."""
    mirbase_id_to_name = {}
    mirbase_name_to_id = {}
    hgnc_id_to_mirbase_id = {}
    mirbase_id_to_hgnc_id = {}
    hgnc_symbol_to_mirbase_id = {}
    mirbase_id_to_hgnc_symbol = {}

    with open(MIRBASE_FILE) as file:
        next(file)
        for line in file:
            try:
                mirbase_id, mirbase_name, db, identifier, name = \
                                                line.strip().split('\t')
            except ValueError:  # fails on WORMBASE since no names
                continue

            mirbase_id_to_name[mirbase_id] = mirbase_name
            mirbase_name_to_id[mirbase_name] = mirbase_id

            if db == 'HGNC':
                hgnc_id_to_mirbase_id[identifier] = mirbase_id
                mirbase_id_to_hgnc_id[mirbase_id] = identifier
                hgnc_symbol_to_mirbase_id[name] = mirbase_id
                mirbase_id_to_hgnc_symbol[mirbase_id] = name

    return (
        mirbase_id_to_name,
        mirbase_name_to_id,
        hgnc_id_to_mirbase_id,
        mirbase_id_to_hgnc_id,
        hgnc_symbol_to_mirbase_id,
        mirbase_id_to_hgnc_symbol,
    )


(
    _mirbase_id_to_name,
    _mirbase_name_to_id,
    _hgnc_id_to_mirbase_id,
    _mirbase_id_to_hgnc_id,
    _hgnc_symbol_to_mirbase_id,
    _mirbase_id_to_hgnc_symbol,

```
