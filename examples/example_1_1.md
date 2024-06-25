# Description
This example demonstrates how to use the SimpleScorer class to calculate belief probabilities for a list of INDRA Statements.

# Code
```
import copy
import numpy
import json
import logging
from os import path, pardir
from typing import List, Optional, Dict, Sequence
from indra.mechlinker import LinkedStatement
from indra.statements import Evidence, Statement
logger = logging.getLogger(__name__)
THIS_DIR = path.dirname(path.abspath(__file__))
def load_default_probs() -> Dict[str, Dict[str, float]]:
    json_path = path.join(THIS_DIR, pardir, 'resources', 'default_belief_probs.json')
    with open(json_path, 'r') as f:
        prior_probs = json.load(f)
    return prior_probs
class BeliefScorer(object):
    def score_statements(self, statements: Sequence[Statement], extra_evidence: Optional[List[List[Evidence]]] = None) -> Sequence[float]:
        raise NotImplementedError('Need to subclass BeliefScorer and implement methods.')
    def score_statement(self, statement: Statement, extra_evidence: Optional[List[Evidence]] = None) -> float:
        extra_evidence_wrap = None if extra_evidence is None else [extra_evidence]
        return self.score_statements([statement], extra_evidence_wrap)[0]
    def check_prior_probs(self, statements: Sequence[Statement]) -> None:

class SimpleScorer(BeliefScorer):
    """Computes the prior probability of a statement given its type and
    evidence.

    Parameters
    ----------
    prior_probs :
        A dictionary of prior probabilities used to override/extend the default
        ones. There are two types of prior probabilities: rand and syst,
        corresponding to random error and systematic error rate for each
        knowledge source. The prior_probs dictionary has the general structure
        {'rand': {'s1': pr1, ..., 'sn': prn}, 'syst': {'s1': ps1, ..., 'sn':
        psn}} where 's1' ... 'sn' are names of input sources and pr1 ... prn
        and ps1 ... psn are error probabilities.  Examples: {'rand':
        {'some_source': 0.1}} sets the random error rate for some_source to
        0.1; {'rand': {''}}
    subtype_probs :
        A dictionary of random error probabilities for knowledge sources.
        When a subtype random error probability is not specified, will just
        use the overall type prior in prior_probs. If None, will
        only use the priors for each rule.
    """
    def __init__(
        self,
        prior_probs: Optional[Dict[str, Dict[str, float]]] = None,
        subtype_probs: Optional[Dict[str, Dict[str, float]]] = None,
    ):
        self.prior_probs = load_default_probs()
        self.subtype_probs: Optional[Dict[str, Dict[str, float]]] = {}
        self.update_probs(prior_probs, subtype_probs)

    def update_probs(
        self,
        prior_probs: Optional[Dict[str, Dict[str, float]]] = None,
        subtype_probs: Optional[Dict[str, Dict[str, float]]] = None,
    ) -> None:
        """Update Scorer's prior probabilities with the given dictionaries."""
        if prior_probs:
            for key in ('rand', 'syst'):
                self.prior_probs[key].update(prior_probs.get(key, {}))
        for err_type, source_dict in self.prior_probs.items():
            logger.debug("Prior probabilities for %s errors: %s"
                         % (err_type, source_dict))
        self.subtype_probs = subtype_probs

    def score_evidence_list(
        self,
        evidences: List[Evidence],
    ) -> float:
        """Return belief score given a list of supporting evidences.

        Parameters
        ----------
        evidences :
            List of evidences to use for calculating a statement's belief.

        Returns
        -------
        :
            Belief value based on the evidences.
        """
        def _score(evidences):
            if not evidences:
                return 0
            # Collect all unique sources
            sources = [ev.source_api for ev in evidences]
            uniq_sources = numpy.unique(sources)
            # Calculate the systematic error factors given unique sources
            syst_factors = {s: self.prior_probs['syst'][s]
                            for s in uniq_sources}
            # Calculate the random error factors for each source
            rand_factors = {k: [] for k in uniq_sources}
            for ev in evidences:
                rand_factors[ev.source_api].append(
                    evidence_random_noise_prior(
                        ev,
                        self.prior_probs['rand'],
                        self.subtype_probs))
            # The probability of incorrectness is the product of the
            # source-specific probabilities
            neg_prob_prior = 1
            for s in uniq_sources:
                neg_prob_prior *= (syst_factors[s] +
                                   numpy.prod(rand_factors[s]))
            # Finally, the probability of correctness is one minus incorrect
            prob_prior = 1 - neg_prob_prior
            return prob_prior
        # Split evidence into positive and negative and score
        pos_evidence = [ev for ev in evidences if
                        not ev.epistemics.get('negated')]
        neg_evidence = [ev for ev in evidences if
                        ev.epistemics.get('negated')]
        pp = _score(pos_evidence)
        np = _score(neg_evidence)
        # The basic assumption is that the positive and negative evidence
        # can't simultaneously be correct.
        # There are two cases to consider. (1) If the positive evidence is
        # incorrect then there is no Statement and the belief should be 0,
        # irrespective of the negative evidence.
        # (2) If the positive evidence is correct and the negative evidence
        # is incorrect.
        # This amounts to the following formula:
        # 0 * (1-pp) + 1 * (pp * (1-np)) which we simplify below
        score = pp * (1 - np)
        return score

    def score_statements(
        self,
        statements: Sequence[Statement],
        extra_evidence: Optional[List[List[Evidence]]] = None,
    ) -> List[float]:
        """Computes belief probabilities for a list of INDRA Statements.

        The Statements are assumed to be de-duplicated. In other words, each
        Statement is assumed to have a list of Evidence objects that supports
        it. The probability of correctness of the Statement is generally
        calculated based on the number of Evidences it has, their sources, and
        other features depending on the subclass implementation.

        Parameters
        ----------
        statements :
            INDRA Statements whose belief scores are to be calculated.
        extra_evidence :
            A list corresponding to the given list of statements, where
            each entry is a list of Evidence objects providing additional
            support for the corresponding statement (i.e., Evidences that
            aren't already included in the Statement's own evidence list).

        Returns
        -------
        :
            The computed prior probabilities for each statement.
        """
        # Check our list of extra evidences
        check_extra_evidence(extra_evidence, len(statements))
        # Get beliefs for each statement
        beliefs = []
        for ix, stmt in enumerate(statements):
            all_evidence = get_stmt_evidence(stmt, ix, extra_evidence)
            beliefs.append(self.score_evidence_list(all_evidence))

```
