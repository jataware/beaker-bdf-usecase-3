# Description
Creating grounding annotations for entity or concept using the hypothes.is browser plug-in.

# Code
```

Curating grounding
~~~~~~~~~~~~~~~~~~
Generally, grounding annotations are only needed if INDRA's current resources
(reading systems, grounding mapping, Gilda, etc.) don't contain a given
synonym for an entity of interest.

With the hypothes.is browser plug-in, select some text on a website that
contains lexical information about an entity or concept of interest.
The conctent of the new annotation can contain one or more lines with identical
syntax as follows:
[text to ground] -> <db_name1>:<db_id1>|<db_name2>:<db_id2>|...
In each case, db_name is a grounding database name space such as HGNC or CHEBI,
and db_id is a value within that namespace such as 1097 or CHEBI:63637.
Example: [AMPK] -> FPLX:AMPK.

The annotation needs to be tagged with `gilda` for the processor to know that

```
