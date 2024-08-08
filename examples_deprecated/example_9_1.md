# Description
Example code to get mutations from the cBioPortal API for a given study, gene list, mutation type, and case ID.

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


def get_genetic_profiles(study_id, profile_filter=None):
    res = send_request('get', f'studies/{study_id}/molecular-profiles')
    if profile_filter:
        res = [prof for prof in res if (profile_filter.casefold() in prof['molecularAlterationType'].casefold())]
    profile_ids = [prof['molecularProfileId'] for prof in res]
    return profile_ids


def get_entrez_mappings(gene_list):
    if gene_list:
        hgnc_mappings = {g: hgnc_client.get_hgnc_id(g) for g in gene_list}
        entrez_mappings = {g: hgnc_client.get_entrez_id(hgnc_mappings[g]) for g in gene_list if hgnc_mappings[g] is not None}
        entrez_to_gene_symbol = {v: k for k, v in entrez_mappings.items() if v is not None and k is not None}
    else:
        entrez_to_gene_symbol = {}

def get_mutations(study_id, gene_list=None, mutation_type=None,
                  case_id=None):
    """Return mutations as a list of genes and list of amino acid changes.

    Parameters
    ----------
    study_id : str
        The ID of the cBio study.
        Example: 'cellline_ccle_broad' or 'paad_icgc'
    gene_list : list[str]
        A list of genes with their HGNC symbols.
        Example: ['BRAF', 'KRAS']
    mutation_type : Optional[str]
        The type of mutation to filter to.
        mutation_type can be one of: missense, nonsense, frame_shift_ins,
        frame_shift_del, splice_site
    case_id : Optional[str]
        The case ID within the study to filter to.

    Returns
    -------
    mutations : dict
        A dict with entries for each gene symbol and another list
        with entries for each corresponding amino acid change.
    """
    genetic_profile = get_genetic_profiles(study_id, 'mutation')[0]

    entrez_to_gene_symbol = get_entrez_mappings(gene_list)
    entrez_ids = list(entrez_to_gene_symbol)

    # Does this need to be parameterized?
    case_set_id = study_id + '_all'

    mutations = send_request('post',
                             f'molecular-profiles/{genetic_profile}/'
                             f'mutations/fetch',
                             {'sampleListId': case_set_id,
                              'entrezGeneIds': entrez_ids})

    if case_id:
        mutations = [m for m in mutations if m['sampleId'] == case_id]

    if mutation_type:
        mutations = [m for m in mutations if (mutation_type.casefold()
                                              in m['mutationType'].casefold())]

    mutations_dict = {
        'gene_symbol': [entrez_to_gene_symbol[str(m['entrezGeneId'])]
                        for m in mutations],
        'amino_acid_change': [m['proteinChange'] for m in mutations],
        'sample_id': [m['sampleId'] for m in mutations],
    }

```
