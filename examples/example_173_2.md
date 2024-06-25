# Description
Build the INDRA bio ontology graph by adding nodes, xrefs, hierarchies, and blacklist filtering.

# Code
```
import logging
from indra.util import read_unicode_csv
from indra.resources import get_resource_path

    def _build(self):
        # Add all nodes with annotations
        logger.info('Adding nodes...')
        self.add_hgnc_nodes()
        self.add_uniprot_nodes()
        self.add_famplex_nodes()
        self.add_obo_nodes()
        self.add_mesh_nodes()
        self.add_ncit_nodes()
        self.add_uppro_nodes()
        self.add_mirbase_nodes()
        self.add_chembl_nodes()
        self.add_hms_lincs_nodes()
        self.add_drugbank_nodes()
        # Add xrefs
        logger.info('Adding xrefs...')
        self.add_hgnc_uniprot_entrez_xrefs()
        self.add_hgnc_entrez_xrefs()
        self.add_famplex_xrefs()
        self.add_chemical_xrefs()
        self.add_ncit_xrefs()
        self.add_mesh_xrefs()
        self.add_mirbase_xrefs()
        self.add_hms_lincs_xrefs()
        self.add_pubchem_xrefs()
        self.add_biomappings()
        # Add hierarchies
        logger.info('Adding hierarchy...')
        self.add_famplex_hierarchy()
        self.add_obo_hierarchies()
        self.add_mesh_hierarchy()
        self.add_activity_hierarchy()
        self.add_modification_hierarchy()
        self.add_uppro_hierarchy()
        self.add_lspci()
        # Add replacements
        logger.info('Adding replacements...')
        self.add_uniprot_replacements()
        self.add_obo_replacements()
        # Remove blacklisted edges
        logger.info('Removing blacklisted edges...')
        self.remove_edges(EDGES_BLACKLIST)

        # The graph is now initialized
        self._initialized = True
        # Build name to ID lookup
        logger.info('Building name lookup...')
        self._build_name_lookup()

```
