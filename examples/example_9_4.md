# Description
Example code to fetch mRNA expression data for a given list of genes and optionally specified cell lines from the CCLE study using the cBioPortal API.

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


def get_profile_data(study_id, gene_list, profile_filter, case_set_filter=None):
    genetic_profiles = get_genetic_profiles(study_id, profile_filter)
    if genetic_profiles: genetic_profile = genetic_profiles[0]
    else: return {}
    case_set_ids = get_case_lists(study_id)
    if case_set_filter: case_set_id = [x for x in case_set_ids if case_set_filter in x][0]
    else: case_set_id = study_id + '_all'
    entrez_to_gene_symbol = get_entrez_mappings(gene_list)
    entrez_ids = list(entrez_to_gene_symbol)
    res = send_request('post', f'molecular-profiles/{genetic_profile}/molecular-data/fetch', {'sampleListId': case_set_id, 'entrezGeneIds': entrez_ids})
    profile_data = {}
    for sample in res:
        sample_id = sample['sampleId']
        if sample_id not in profile_data: profile_data[sample_id] = {}
        gene_symbol = entrez_to_gene_symbol[str(sample['entrezGeneId'])]
        profile_data[sample_id][gene_symbol] = sample['value']
    return profile_data


def get_entrez_mappings(gene_list):
    if gene_list:
        hgnc_mappings = {g: hgnc_client.get_hgnc_id(g) for g in gene_list}
        entrez_mappings = {g: hgnc_client.get_entrez_id(hgnc_mappings[g]) for g in gene_list if hgnc_mappings[g] is not None}
        entrez_to_gene_symbol = {v: k for k, v in entrez_mappings.items() if v is not None and k is not None}
    else:
        entrez_to_gene_symbol = {}

def get_ccle_mrna(gene_list, cell_lines=None):
    """Return a dict of mRNA amounts in given genes and cell lines from CCLE.

    Parameters
    ----------
    gene_list : list[str]
        A list of HGNC gene symbols to get mRNA amounts for.
    cell_lines : Optional[list[str]]
        A list of CCLE cell line names to get mRNA amounts for.

    Returns
    -------
    mrna_amounts : dict[dict[float]]
        A dict keyed to cell lines containing a dict keyed to genes
        containing float
    """
    profile_data = get_profile_data(ccle_study, gene_list,
                                    'MRNA_EXPRESSION', 'all')
    mrna_amounts = {cell_line: value
                    for cell_line, value in profile_data.items()
                    if cell_lines is None or cell_line in cell_lines}
    # This is to make sure that if cell_lines were specified then
    # we return None if there is no data for a given cell line
    # This matches the old behavior of the function
    if cell_lines:
        for cell_line in cell_lines:
            if cell_line not in mrna_amounts:
                mrna_amounts[cell_line] = None
            else:
                for gene in gene_list:
                    if gene not in mrna_amounts[cell_line]:
                        mrna_amounts[cell_line][gene] = None

```
