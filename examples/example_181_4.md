# Description
Using `process_owl` to process a BioPAX OWL file.

# Code
```

def process_owl(owl_filename, encoding=None):
    """Returns a BiopaxProcessor for a BioPAX OWL file.

    Parameters
    ----------
    owl_filename : str
        The name of the OWL file to process.
    encoding : Optional[str]
        The encoding type to be passed to :func:`pybiopax.model_from_owl_file`.

    Returns
    -------
    bp : BiopaxProcessor
        A BiopaxProcessor containing the obtained BioPAX model in bp.model.
    """
    model = model_from_owl_file(owl_filename, encoding=encoding)

```
