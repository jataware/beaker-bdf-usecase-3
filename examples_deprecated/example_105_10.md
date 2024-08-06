# Description
Examples of multiple MESH term lookups using `mesh_client.get_mesh_id_name`.

# Code
```

def test_mesh_term_lookups():
    queries = {'Breast Cancer': ('D001943', 'Breast Neoplasms'),
               'Neoplasms': ('D009369', 'Neoplasms'),
               'Intestinal Neoplasms': ('D007414', 'Intestinal Neoplasms'),
               'Carcinoma, Non-Small-Cell Lung':
                                ('D002289', 'Carcinoma, Non-Small-Cell Lung'),
               'Prostate Cancer': ('D011471', 'Prostatic Neoplasms')}
    for query_term, (correct_id, correct_name) in queries.items():
        mesh_id, mesh_name = mesh_client.get_mesh_id_name(query_term)
        assert mesh_id == correct_id, (query_term, mesh_id, correct_id)

```
