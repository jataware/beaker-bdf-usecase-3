# Description
Prepare a Kappa STD object with a given PySB model loaded. This includes exporting the PySB model as a Kappa string and parsing it within the Kappa STD.

# Code
```
import kappy

def _prepare_kappa(model):
    """Return a Kappa STD with the model loaded."""
    import kappy
    kappa = kappy.KappaStd()
    model_str = export(model, 'kappa')
    kappa.add_model_string(model_str)
    kappa.project_parse()

```
