# Description
This example demonstrates how to save the assembled SBGN model to a file.

# Code
```

    def save_model(self, file_name='model.sbgn'):
        """Save the assembled SBGN model in a file.

        Parameters
        ----------
        file_name : Optional[str]
            The name of the file to save the SBGN network to.
            Default: model.sbgn
        """
        model = self.print_model()
        with open(file_name, 'wb') as fh:

```
