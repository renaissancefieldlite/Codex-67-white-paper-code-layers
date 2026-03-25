"""Anchor-string extraction scaffold."""

from __future__ import annotations

import re
from collections import Counter

ANCHOR_PATTERN = re.compile(r"\b[A-Z][A-Z0-9_]{5,}\b")


def discover_anchor_strings(text: str, *, minimum_count: int = 1) -> list[str]:
    """Return repeated uppercase anchor-like strings from the input text."""
    matches = ANCHOR_PATTERN.findall(text)
    counts = Counter(matches)
    return sorted([token for token, count in counts.items() if count >= minimum_count])
