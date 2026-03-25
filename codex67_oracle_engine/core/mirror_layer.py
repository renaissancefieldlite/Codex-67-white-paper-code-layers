"""Signal extraction for the mirror layer."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class MirrorSignal:
    """Minimal structured representation of an input signal."""

    raw_text: str
    token_count: int
    uppercase_ratio: float
    punctuation_density: float


def extract_signal(text: str) -> MirrorSignal:
    """Turn free text into a simple signal object for downstream scoring."""
    stripped = text.strip()
    token_count = len(stripped.split()) if stripped else 0
    uppercase_count = sum(1 for char in stripped if char.isupper())
    alpha_count = sum(1 for char in stripped if char.isalpha()) or 1
    punctuation_count = sum(1 for char in stripped if not char.isalnum() and not char.isspace())
    text_length = len(stripped) or 1
    return MirrorSignal(
        raw_text=text,
        token_count=token_count,
        uppercase_ratio=uppercase_count / alpha_count,
        punctuation_density=punctuation_count / text_length,
    )
