"""
Dream Engine Module

Generates surreal dream narratives using opposition mapping algorithm.
Fragments are paired based on semantic opposition to create the
juxtaposition characteristic of dreams.
"""

from typing import List, Tuple, Dict
from dataclasses import dataclass
import random
import numpy as np

from .extractor import Fragment


@dataclass
class DreamPair:
    """A pair of opposing fragments for dream construction."""
    fragment_a: Fragment
    fragment_b: Fragment
    opposition_score: float  # Higher = more opposing


class DreamEngine:
    """Generates dream sequences using opposition mapping."""

    def __init__(self, randomness: float = 0.3):
        """
        Initialize dream engine.

        Args:
            randomness: How much randomness to introduce (0-1).
                       Higher = more surreal/unexpected connections.
        """
        self.randomness = randomness

    def generate_dream_sequence(self, fragments: List[Fragment],
                               num_pairs: int = 5) -> List[DreamPair]:
        """
        Generate a sequence of opposing fragment pairs.

        Args:
            fragments: List of conversation fragments
            num_pairs: Number of pairs to generate

        Returns:
            List of DreamPair objects sorted by dream flow
        """
        if len(fragments) < 2:
            return []

        # Calculate opposition scores between all fragment pairs
        pairs = self._find_oppositions(fragments)

        # Select top pairs with some randomness for surrealism
        selected_pairs = self._select_dream_pairs(pairs, num_pairs)

        # Arrange in dream-like flow (not chronological!)
        arranged_pairs = self._arrange_dream_flow(selected_pairs)

        return arranged_pairs

    def _find_oppositions(self, fragments: List[Fragment]) -> List[DreamPair]:
        """Find opposing pairs using multiple signals."""
        pairs = []

        for i, frag_a in enumerate(fragments):
            for frag_b in fragments[i+1:]:
                # Calculate opposition score
                score = self._calculate_opposition(frag_a, frag_b)

                pairs.append(DreamPair(
                    fragment_a=frag_a,
                    fragment_b=frag_b,
                    opposition_score=score
                ))

        return pairs

    def _calculate_opposition(self, a: Fragment, b: Fragment) -> float:
        """
        Calculate opposition score between two fragments.

        Opposition = combination of:
        - Sentiment opposition (opposite emotions)
        - Keyword distance (different topics)
        - Time distance (far apart in conversation)
        """
        # Sentiment opposition: higher if opposite sentiments
        sentiment_opp = abs(a.sentiment - b.sentiment)

        # Keyword opposition: lower overlap = more different topics
        keyword_overlap = len(set(a.keywords) & set(b.keywords))
        keyword_opp = 1 - (keyword_overlap / max(len(a.keywords), len(b.keywords), 1))

        # Time distance: fragments far apart are more "dream-like"
        time_dist = abs(a.timestamp - b.timestamp)
        time_opp = min(time_dist / 100, 1)  # Normalize to 0-1

        # Combined score (weighted)
        opposition = (
            0.4 * sentiment_opp +
            0.4 * keyword_opp +
            0.2 * time_opp
        )

        return opposition

    def _select_dream_pairs(self, pairs: List[DreamPair],
                           num_pairs: int) -> List[DreamPair]:
        """Select pairs for the dream with controlled randomness."""
        # Sort by opposition score
        pairs.sort(key=lambda p: p.opposition_score, reverse=True)

        selected = []

        # Always include the most opposing pair
        if pairs:
            selected.append(pairs[0])

        # For remaining slots, use weighted random selection
        # Higher opposition = higher probability, but not deterministic
        remaining_pairs = pairs[1:]
        if remaining_pairs:
            # Create probability distribution (higher score = higher prob)
            scores = [p.opposition_score for p in remaining_pairs]
            total = sum(scores)

            # Add some noise for surrealism
            noise = np.random.normal(0, self.randomness, len(scores))
            probs = [(s + n) / total for s, n in zip(scores, noise)]
            probs = [max(0, p) for p in probs]
            prob_sum = sum(probs)

            if prob_sum > 0:
                probs = [p / prob_sum for p in probs]

                # Select remaining pairs
                num_to_select = min(num_pairs - 1, len(remaining_pairs))
                indices = np.random.choice(
                    len(remaining_pairs),
                    size=num_to_select,
                    replace=False,
                    p=probs
                )

                for idx in indices:
                    selected.append(remaining_pairs[idx])

        return selected

    def _arrange_dream_flow(self, pairs: List[DreamPair]) -> List[DreamPair]:
        """
        Arrange pairs in dream-like flow.

        Dreams don't follow linear logic. We arrange to create
        transitions that feel surreal but have subconscious patterns.
        """
        if not pairs:
            return []

        # Start with highest opposition
        pairs.sort(key=lambda p: p.opposition_score, reverse=True)

        # For dream flow, we want:
        # 1. Strong opening (most opposing)
        # 2. Build intensity
        # 3. End with unresolved tension

        arranged = [pairs[0]]  # Strongest opener

        remaining = pairs[1:]

        # Alternate between high and medium opposition
        high_opp = [p for p in remaining if p.opposition_score > 0.5]
        med_opp = [p for p in remaining if p.opposition_score <= 0.5]

        while high_opp or med_opp:
            if high_opp and (not med_opp or random.random() > 0.3):
                arranged.append(high_opp.pop(0))
            elif med_opp:
                arranged.append(med_opp.pop(0))
            else:
                break

        return arranged

    def format_for_llm(self, pairs: List[DreamPair]) -> str:
        """
        Format dream pairs as JSON for LLM processing.

        This is what gets fed to the LLM for narrative generation.
        """
        import json

        formatted = []
        for pair in pairs:
            formatted.append({
                "fragment_a": {
                    "text": pair.fragment_a.text[:200],  # Truncate for token efficiency
                    "keywords": pair.fragment_a.keywords,
                    "sentiment": pair.fragment_a.sentiment
                },
                "fragment_b": {
                    "text": pair.fragment_b.text[:200],
                    "keywords": pair.fragment_b.keywords,
                    "sentiment": pair.fragment_b.sentiment
                },
                "opposition_score": pair.opposition_score
            })

        return json.dumps({
            "dream_pairs": formatted,
            "instructions": (
                "Create a first-person surreal dream narrative. "
                "Weave these opposing fragments together using dream logic - "
                "metaphor, juxtaposition, time distortion. "
                "End with a '梦醒时分' section extracting 2-3 key insights."
            )
        }, ensure_ascii=False, indent=2)
