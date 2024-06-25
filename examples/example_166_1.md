# Description
Export a PySB model into SBGN format. This includes generating the reaction network, creating SBGN glyphs for species and reactions, and connecting them with arcs.

# Code
```
import logging
import lxml.etree
import lxml.builder
from pysb.bng import generate_equations
from indra.assemblers.sbgn import SBGNAssembler

def export_sbgn(model):
    """Return an SBGN model string corresponding to the PySB model.

    This function first calls generate_equations on the PySB model to obtain
    a reaction network (i.e. individual species, reactions). It then iterates
    over each reaction and and instantiates its reactants, products, and the
    process itself as SBGN glyphs and arcs.

    Parameters
    ----------
    model : pysb.core.Model
        A PySB model to be exported into SBGN

    Returns
    -------
    sbgn_str : str
        An SBGN model as string
    """
    import lxml.etree
    import lxml.builder
    from pysb.bng import generate_equations
    from indra.assemblers.sbgn import SBGNAssembler

    logger.info('Generating reaction network with BNG for SBGN export. ' +
                'This could take a long time.')
    generate_equations(model)

    sa = SBGNAssembler()

    glyphs = {}
    for idx, species in enumerate(model.species):
        glyph = sa._glyph_for_complex_pattern(species)
        if glyph is None:
            continue
        sa._map.append(glyph)
        glyphs[idx] = glyph
    for reaction in model.reactions:
        # Get all the reactions / products / controllers of the reaction
        reactants = set(reaction['reactants']) - set(reaction['products'])
        products = set(reaction['products']) - set(reaction['reactants'])
        controllers = set(reaction['reactants']) & set(reaction['products'])
        # Add glyph for reaction
        process_glyph = sa._process_glyph('process')
        # Connect reactants with arcs
        if not reactants:
            glyph_id = sa._none_glyph()
            sa._arc('consumption', glyph_id, process_glyph)
        else:
            for r in reactants:
                glyph = glyphs.get(r)
                if glyph is None:
                    glyph_id = sa._none_glyph()
                else:
                    glyph_id = glyph.attrib['id']
                sa._arc('consumption', glyph_id, process_glyph)
        # Connect products with arcs
        if not products:
            glyph_id = sa._none_glyph()
            sa._arc('production', process_glyph, glyph_id)
        else:
            for p in products:
                glyph = glyphs.get(p)
                if glyph is None:
                    glyph_id = sa._none_glyph()
                else:
                    glyph_id = glyph.attrib['id']
                sa._arc('production', process_glyph, glyph_id)
        # Connect controllers with arcs
        for c in controllers:
            glyph = glyphs[c]
            sa._arc('catalysis', glyph.attrib['id'], process_glyph)

    sbgn_str = sa.print_model().decode('utf-8')

```