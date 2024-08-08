# Description
Summarize the DGI statements using the `DGIProcessor` and `tabulate` library to format the output.

# Code
```
collections import Counter
tabulate import tabulate

def main():
    """Summarize the DGI statements."""
    processor = DGIProcessor()
    statements = processor.extract_statements()

    print(f"Number skipped: {processor.skipped}\n")
    print(tabulate(
        Counter(
            statement.__class__.__name__ for statement in statements
        ).most_common(),
        headers=["Statement Type", "Count"],
    ))

    print()
    print(tabulate(
        Counter(
            evidence.annotations["source"]
            for statement in statements
            for evidence in statement.evidence
        ).most_common(),
        headers=["Source", "Count"],
    ))

    print()
    print(tabulate(
        Counter(
            interaction
            for statement in statements
            for evidence in statement.evidence
            for interaction in evidence.annotations["interactions"].split(",")
        ).most_common(),
        headers=["Interaction", "Count"],

```
