# Description
Curating text from a website to create INDRA Statements using the hypothes.is browser plug-in.

# Code
```

Curating Statements
~~~~~~~~~~~~~~~~~~~
To curate text from a website with the intention of creating one or more INDRA
Statements, select some text and create a new annotation using the
hypothes.is browser plug-in. The content of the annotation consists of
one or more lines. The first line should contain one or more English sentences
describing the mechanism(s) that will be represented as an INDRA Statement
(e.g., AMPK activates STAT3) based on the selected text. Each subsequent
line of the annotation is assumed to be a context annotation. These lines
are of the form "<context type>: <context text>" where <context type> can be one
of: Cell type, Cell line, Disease, Organ, Location, Species, and <context text>
is the text describing the context, e.g., lysosome, liver, prostate cancer, etc.

The annotation should also be tagged with `indra` (though by default, if no
tags are given, the processor assumes that the given annotation is an

```
