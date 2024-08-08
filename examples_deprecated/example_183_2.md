# Description
Process statements from CREEDS data stored in a local file, specifying the entity type (gene, disease, or chemical).

# Code
```
import json
import requests
from pathlib import Path
from typing import Union
from .processor import (
    CREEDSChemicalProcessor,
    CREEDSDiseaseProcessor,
    CREEDSGeneProcessor,
    CREEDSProcessor,
)

BASE_URL = "http://amp.pharm.mssm.edu/CREEDS/download"
urls = {
    "gene": f"{BASE_URL}/single_gene_perturbations-v1.0.json",
    "disease": f"{BASE_URL}/disease_signatures-v1.0.json",
    "chemical": f"{BASE_URL}/single_drug_perturbations-v1.0.json",
}

processors = {
    "gene": CREEDSGeneProcessor,
    "disease": CREEDSDiseaseProcessor,
    "chemical": CREEDSChemicalProcessor,

def process_from_file(
    path: Union[str, Path],
    entity_type: str,
) -> CREEDSProcessor:
    """Process statements from CREEDS in a file.

    Parameters
    ----------
    path :
        The path to a JSON file containing records for the CREEDS data
    entity_type :
        Either 'gene', 'disease', or 'chemical' to specify
        which dataset to get.

    Returns
    -------
    :
        A processor with pre-extracted statements.
    """
    with open(path) as file:
        records = json.load(file)

```
