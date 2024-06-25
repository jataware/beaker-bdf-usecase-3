# Description
This example demonstrates how to return the assembled SBGN model as an XML string with optional formatting.

# Code
```

    def print_model(self, pretty=True, encoding='utf8'):
        """Return the assembled SBGN model as an XML string.

        Parameters
        ----------
        pretty : Optional[bool]
            If True, the SBGN string is formatted with indentation (for human
            viewing) otherwise no indentation is used. Default: True

        Returns
        -------
        sbgn_str : bytes (str in Python 2)
            An XML string representation of the SBGN model.
        """
        return lxml.etree.tostring(self.sbgn, pretty_print=pretty,

```
