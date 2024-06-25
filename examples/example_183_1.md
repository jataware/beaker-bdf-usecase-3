# Description
Process statements from CREEDS by automatically downloading them using the specified entity type (gene, disease, or chemical).

# Code
```
import json
import requests
from pathlib import Path
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

def process_from_web(entity_type: str) -> CREEDSProcessor:
    """Process statements from CREEDS by automatially downloading them.

    Parameters
    ----------
    entity_type :
        Either 'gene', 'disease', or 'chemical' to specify
        which dataset to get.

    Returns
    -------
    :
        A processor with pre-extracted statements.
    """
    url = urls[entity_type]
    res = requests.get(url)
    res.raise_for_status()
    records = res.json()

```
