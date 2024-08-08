# Description
Control the build and clean up caches for the INDRA bio ontology using command line operations.

# Code
```

.. code-block:: bash

    python -m indra.ontology.bio <operation>

to build or clean up the INDRA bio ontology. The script takes
a single operation argument which can be as follows:

* `build`: build the ontology and cache it
* `clean`: delete the current version of the ontology from the cache
* `clean-old`: delete all versions of the ontology except the current one
* `clean-all`: delete all versions of the bio ontology from the cache

```
