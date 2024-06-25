# Description
Updating HGNC entries by downloading and saving specific columns from the HGNC website.

# Code
```
os
logging

def update_hgnc_entries():
    logger.info('--Updating HGNC entries-----')

    # Select relevant columns and parameters
    cols = [
        'gd_hgnc_id', 'gd_app_sym', 'gd_app_name', 'gd_status',
        'gd_aliases', 'md_eg_id', 'md_prot_id',
        'md_mgd_id', 'md_rgd_id', 'gd_prev_sym', 'gd_pub_ensembl_id',
        'gd_locus_type',
        'gd_enz_ids',
    ]

    statuses = ['Approved', 'Entry%20Withdrawn']
    params = {
            'hgnc_dbtag': 'on',
            'order_by': 'gd_app_sym_sort',
            'format': 'text',
            'submit': 'submit'
            }

    # Construct a download URL from the above parameters
    url = 'https://www.genenames.org/cgi-bin/download/custom?'
    url += '&'.join(['col=%s' % c for c in cols]) + '&'
    url += '&'.join(['status=%s' % s for s in statuses]) + '&'
    url += '&'.join(['%s=%s' % (k, v) for k, v in params.items()])

    # Save the download into a file
    fname = os.path.join(path, 'hgnc_entries.tsv')

```
