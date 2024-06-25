# Description
Add chemical cross-references (xrefs) between various databases including ChEBI, DrugBank, and PubChem.

# Code
```
chebi_client
drugbank_client

    def add_chemical_xrefs(self):
        from indra.databases import chebi_client, drugbank_client
        mappings = [
            (chebi_client.chebi_chembl, 'CHEBI', 'CHEMBL', True),
            (chebi_client.chebi_pubchem, 'CHEBI', 'PUBCHEM', False),
            (chebi_client.pubchem_chebi, 'PUBCHEM', 'CHEBI', False),
            (chebi_client.hmdb_chebi, 'HMDB', 'CHEBI', True),
            (chebi_client.cas_chebi, 'CAS', 'CHEBI', True),
            (drugbank_client.drugbank_to_db, 'DRUGBANK', None, False),
            (drugbank_client.db_to_drugbank, None, 'DRUGBANK', False),
        ]
        edges = []
        data = {'type': 'xref', 'source': 'chebi'}

        def label_fix(ns, id):
            if ns == 'CHEBI' and not id.startswith('CHEBI'):
                id = 'CHEBI:%s' % id
            return self.label(ns, id)

        for map_dict, from_ns, to_ns, symmetric in mappings:
            for from_id, to_id in map_dict.items():
                # Here we assume if no namespace is given, then
                # we're dealing with a (namespace, id) tuple
                if from_ns is None:
                    from_ns_, from_id = from_id
                    to_ns_ = to_ns
                elif to_ns is None:
                    from_id, to_ns_ = from_id
                    from_ns_ = from_ns
                else:
                    from_ns_, to_ns_ = from_ns, to_ns
                source = label_fix(from_ns_, from_id)
                target = label_fix(to_ns_, to_id)
                edges.append((source, target, data))
                if symmetric:
                    edges.append((target, source, data))

```
