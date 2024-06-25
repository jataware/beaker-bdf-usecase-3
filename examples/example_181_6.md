# Description
Using `process_owl_str` to process the string content of a BioPAX OWL file.

# Code
```

def process_owl_str(owl_str):
    """Returns a BiopaxProcessor for a BioPAX OWL file.

    Parameters
    ----------
    owl_str : str
        The string content of an OWL file to process.

    Returns
    -------
    bp : BiopaxProcessor
        A BiopaxProcessor containing the obtained BioPAX model in bp.model.
    """
    model = model_from_owl_str(owl_str)

```
