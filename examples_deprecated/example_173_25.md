# Description
Add cross-references (xrefs) for HMS-LINCS.

# Code
```

    def add_hms_lincs_xrefs(self):
        from indra.databases.lincs_client import LincsClient
        lc = LincsClient()

        edges = []
        for hmsl_id, data in lc._sm_data.items():
            if '-' in hmsl_id:
                hmsl_base_id, suffix = hmsl_id.split('-')
            else:
                hmsl_base_id, suffix = hmsl_id, None
            if suffix == '999':
                continue
            refs = lc.get_small_molecule_refs(hmsl_id)
            for ref_ns, ref_id in refs.items():
                if ref_ns == 'HMS-LINCS':
                    continue
                edges.append((self.label('HMS-LINCS', hmsl_base_id),
                              self.label(ref_ns, ref_id),
                              {'type': 'xref', 'source': 'hms-lincs'}))
                edges.append((self.label(ref_ns, ref_id),
                              self.label('HMS-LINCS', hmsl_base_id),

```
