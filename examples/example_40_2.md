# Description
Updating the kinase list by downloading data from UniProt, appending specific kinase entries, and saving the result.

# Code
```
os
logging
requests

def update_kinases():
    logger.info('--Updating kinase list------')
    url = 'http://www.uniprot.org/uniprot/?' + \
        'sort=entry_name&desc=no&compress=no&query=database:(type:' + \
        'interpro%20ipr011009)%20AND%20reviewed:yes%20AND%20organism:' + \
        '%22Homo%20sapiens%20(Human)%20[9606]%22&fil=&force=no' + \
        '&format=tab&columns=id,genes(PREFERRED),organism-id,entry%20name'
    fname = os.path.join(path, 'kinases.tsv')
    save_from_http(url, fname)

    from indra.databases import hgnc_client, uniprot_client
    add_kinases = ['PGK1', 'PKM', 'TAF1', 'NME1', 'BCKDK', 'PDK1', 'PDK2',
                   'PDK3', 'PDK4', 'BCR', 'FAM20C', 'BAZ1B', 'PIKFYVE']
    df = pandas.read_csv(fname, sep='\t')
    for kinase in add_kinases:
        hgnc_id = hgnc_client.get_hgnc_id(kinase)
        up_id = hgnc_client.get_uniprot_id(hgnc_id)
        up_mnemonic = uniprot_client.get_mnemonic(up_id)
        df = df.append({'Entry': up_id, 'Gene names  (primary )': kinase,
                        'Organism ID': '9606', 'Entry name': up_mnemonic},
                       ignore_index=True)

```
