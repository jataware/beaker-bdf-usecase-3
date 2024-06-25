
from beaker_bunsen.bunsen_context import BunsenContext

from .agent import BDFAgent


class BDFContext(BunsenContext):

    agent_cls = BDFAgent
    enabled_subkernels = ["python3"]

    @classmethod
    def default_payload(cls) -> str:
        return "{}"
