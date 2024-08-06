# Description
Save a stylesheet defining color and background-color for the given sources.

# Code
```
os
logging

def generate_source_css(fname: str,
                        source_colors: SourceColors = None):
    """Save a stylesheet defining color, background-color for the given sources

    Parameters
    ----------
    fname :
        Where to save the stylesheet
    source_colors :
        Colors defining the styles. Default: DEFAULT_SOURCE_COLORS.
    """
    if source_colors is None:
        source_colors = DEFAULT_SOURCE_COLORS

    rule_string = '.source-{src} {{\n    background-color: {src_bg};\n    ' \
                  'color: {src_txt};\n}}\n\n'

    stylesheet_str = ''
    for _, info in source_colors:
        text_color = info['color']
        for source_name, bg_color in info['sources'].items():
            stylesheet_str += rule_string.format(src=source_name,
                                                 src_bg=bg_color,
                                                 src_txt=text_color)

    with open(fname, 'w') as fh:

```
