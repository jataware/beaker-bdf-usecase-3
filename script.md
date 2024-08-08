Can you load Table 3G from mmc3.xlsx. It contains information about HRD tumor classes from the Geffen et al paper "Pan-cancer analysis of
post-translational modifications reveals shared patterns of protein regulation". Take a look at each column to make sure you understand what's in each of them.

Can you try to identify the statistically significant results in the dataset. Which phosphorylated proteins (phosphoproteome) are more abundant in the HRD tumor classes? Provide the protein names and amino acid sites that are phosphorylated, e.g., PARP1 at site S782.

Please construct a list of all phosphorylation sites that have significantly increased compared to control, and represent these as tuples compatible with Protmapper (gene_name, 'hgnc', residue, position). Limit it to just the first 50 or so.

Can you run code to use protmapper to map these sites to human reference and filter to valid sites?

Can you use the run_code tool to query the INDRA DB for phosphorylation statements whose substrate is one of the proteins whose phosphorylation appears in the site list and construct a dictionary of statements organized by specific sites making sure that phosphorylation of that specific site is described in the list of statements as values. Please print progress querying INDRA with tqdm.

Can you print some statistics of the number of sites and the number with any known annotations and explore specific examples of site annotations.
