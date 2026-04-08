"""
Fragment Extraction Module

Extracts meaningful fragments from conversation history using TF-IDF
for keyword extraction and sentiment analysis.
"""

from typing import List, Dict
from dataclasses import dataclass
import re


@dataclass
class Fragment:
    """A conversation fragment with metadata."""
    text: str
    keywords: List[str]
    sentiment: float  # -1 (negative) to 1 (positive)
    timestamp: int  # position in conversation


class FragmentExtractor:
    """Extracts fragments from conversation text."""

    def __init__(self, min_fragment_length: int = 50):
        self.min_fragment_length = min_fragment_length

    def extract(self, conversation: str) -> List[Fragment]:
        """
        Extract fragments from conversation text.

        Args:
            conversation: Raw conversation text

        Returns:
            List of Fragment objects with metadata
        """
        # Split into logical segments
        segments = self._split_into_segments(conversation)

        fragments = []
        for i, segment in enumerate(segments):
            if len(segment.strip()) < self.min_fragment_length:
                continue

            keywords = self._extract_keywords(segment)
            sentiment = self._analyze_sentiment(segment)

            fragments.append(Fragment(
                text=segment.strip(),
                keywords=keywords,
                sentiment=sentiment,
                timestamp=i
            ))

        return fragments

    def _split_into_segments(self, text: str) -> List[str]:
        """Split conversation into logical segments."""
        # Split by message boundaries (simplified)
        # In production, would parse actual conversation format
        segments = re.split(r'\n(?=[A-Z])|\n\n+', text)
        return [s for s in segments if s.strip()]

    def _extract_keywords(self, text: str, top_k: int = 5) -> List[str]:
        """
        Extract keywords using simple frequency analysis.

        Note: In production, use scikit-learn TfidfVectorizer
        """
        # Simple word frequency for now
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())

        # Filter common words
        stopwords = {'this', 'that', 'with', 'from', 'have', 'been',
                    'were', 'they', 'what', 'when', 'where', 'will'}
        words = [w for w in words if w not in stopwords and len(w) > 3]

        # Count frequency
        from collections import Counter
        freq = Counter(words)

        return [word for word, _ in freq.most_common(top_k)]

    def _analyze_sentiment(self, text: str) -> float:
        """
        Simple sentiment analysis.

        Note: In production, use TextBlob or VADER
        Returns value between -1 (negative) and 1 (positive)
        """
        # Simple keyword-based sentiment
        positive_words = {'good', 'great', 'excellent', 'fixed', 'works',
                         'solved', 'success', 'happy', 'love', 'perfect'}
        negative_words = {'bad', 'error', 'bug', 'broken', 'fail', 'issue',
                         'problem', 'wrong', 'hate', 'terrible', 'slow'}

        words = set(re.findall(r'\b[a-zA-Z]+\b', text.lower()))

        score = 0
        for word in words:
            if word in positive_words:
                score += 0.1
            elif word in negative_words:
                score -= 0.1

        return max(-1, min(1, score))
