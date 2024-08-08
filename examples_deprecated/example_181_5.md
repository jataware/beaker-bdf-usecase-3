# Description
Using `process_owl_gz` to process a gzipped BioPAX OWL file.

# Code
```

def process_owl_gz(owl_gz_filename):
    """Returns a BiopaxProcessor for a gzipped BioPAX OWL file.

    Parameters
    ----------
    owl_gz_filename : str
        The name of the gzipped OWL file to process.

    Returns
    -------
    bp : BiopaxProcessor
        A BiopaxProcessor containing the obtained BioPAX model in bp.model.
    """
    model = model_from_owl_gz(owl_gz_filename)

```
