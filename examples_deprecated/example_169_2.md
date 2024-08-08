# Description
Draw the influence map and save it to a file.

# Code
```

    def draw_im(self, fname):
        """Draw and save the influence map in a file.

        Parameters
        ----------
        fname : str
            The name of the file to save the influence map in.
            The extension of the file will determine the file format,
            typically png or pdf.
        """
        im = self.get_im()
        im_agraph = nx.nx_agraph.to_agraph(im)

```
