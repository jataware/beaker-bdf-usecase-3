# Description
Add nodes for HMS-LINCS dataset.

# Code
```

    def add_hms_lincs_nodes(self):
        from indra.databases.lincs_client import LincsClient
        lc = LincsClient()

        nodes = []
        for hmsl_id, data in lc._sm_data.items():
            if '-' in hmsl_id:
                hmsl_base_id, suffix = hmsl_id.split('-')
            else:
                hmsl_base_id, suffix = hmsl_id, None
            if suffix == '999':
                continue
            nodes.append((self.label('HMS-LINCS', hmsl_base_id),
                          {'name': data['Name']}))

```
