# Description
Extracting clean text from raw rxiv text content while parsing titles, headings, subheadings, and filtering irrelevant content.

# Code
```

def get_text_from_rxiv_text(rxiv_text):
    """Return clean text from the raw rxiv text content.

    This function parses out the title, headings and subheadings, and
    the content of sections under headings/subheadings.
    It filters out some irrelevant content e.g., references and
    footnotes.

    Parameters
    ----------
    rxiv_text : str
        The content of the rxiv full text as obtained from the web.

    Returns
    -------
    str
        The text content stripped out from the raw full text.
    """
    lines = [line.strip() for line in rxiv_text.split('\n') if line.strip()]
    current_section = 'title'
    text = lines[0] + '\n'
    line_idx = 1
    skip_section = {'References', 'Footnotes', 'Acknowledgements',
                    'Supplementary Figures', 'Declaration of Interests',
                    'Author Contributions', 'Code and data availability'}
    for line in lines[line_idx:]:
        line_idx += 1
        match = re.match('## (.+)', line)
        if match:
            current_section = match.groups()[0]
            break
    while line_idx < len(lines):
        for line in lines[line_idx:]:
            line_idx += 1
            match_heading = re.match('## (.+)', line)
            match_subheading = re.match('### (.+)', line)
            if match_heading:
                current_section = match_heading.groups()[0]
                break
            elif current_section in skip_section:
                continue
            elif match_subheading:
                text += (match_subheading.groups()[0] + '\n')
            else:
                text += (line + '\n')

```
