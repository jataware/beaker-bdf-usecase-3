# Description
Example code to fetch mutation data based on a given gene and amino acid change from the CCLE study using the cBioPortal API.

# Code
```
import json
import logging
import requests
from functools import lru_cache
from indra.databases import hgnc_client

logger = logging.getLogger(__name__)

cbio_url = 'https://www.cbioportal.org/api'
ccle_study = 'cellline_ccle_broad'


def send_request(method, endpoint, json_data=None):
    json_data_str = json.dumps(json_data) if json_data else None
    res = _send_request_cached(method, endpoint, json_data_str)
    return res


@lru_cache(maxsize=1000)
def _send_request_cached(method, endpoint, json_data_str=None):
    if endpoint.startswith('/'): endpoint = endpoint[1:]
    json_data = json.loads(json_data_str) if json_data_str else {}
    request_fun = getattr(requests, method)
    full_url = cbio_url + '/' + endpoint
    res = request_fun(full_url, json=json_data)
    if res.status_code != 200: logger.error(f'Request returned with code {res.status_code}: {res.text}'); return
    return res.json()


def get_mutations(study_id, gene_list=None, mutation_type=None, case_id=None):
    genetic_profile = get_genetic_profiles(study_id, 'mutation')[0]
    entrez_to_gene_symbol = get_entrez_mappings(gene_list)
    entrez_ids = list(entrez_to_gene_symbol)
    case_set_id = study_id + '_all'
    mutations = send_request('post', f'molecular-profiles/{genetic_profile}/mutations/fetch', {'sampleListId': case_set_id, 'entrezGeneIds': entrez_ids})
    if case_id: mutations = [m for m in mutations if m['sampleId'] == case_id]
    if mutation_type: mutations = [m for m in mutations if (mutation_type.casefold() in m['mutationType'].casefold())]
    mutations_dict = {'gene_symbol': [entrez_to_gene_symbol[str(m['entrezGeneId'])] for m in mutations],'amino_acid_change': [m['proteinChange'] for m in mutations],'sample_id': [m['sampleId'] for m in mutations]}

def get_ccle_lines_for_mutation(gene, amino_acid_change):
    """Return cell lines with a given point mutation in a given gene.

    Checks which cell lines in CCLE have a particular point mutation
    in a given gene and return their names in a list.

    Parameters
    ----------
    gene : str
        The HGNC symbol of the mutated gene in whose product the amino
        acid change occurs. Example: "BRAF"
    amino_acid_change : str
        The amino acid change of interest. Example: "V600E"

    Returns
    -------
    cell_lines : list
        A list of CCLE cell lines in which the given mutation occurs.
    """
    mutations = get_mutations(ccle_study, [gene], 'missense')
    cell_lines = {cl for aac, cl
                  in zip(mutations['amino_acid_change'], mutations['sample_id'])
                  if aac == amino_acid_change}

```
