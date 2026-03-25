"""Fallback gate for low-coherence or mismatched sessions."""

from __future__ import annotations


def should_lock_out(score: float, *, minimum_score: float = 0.45) -> bool:
    """Return True when the session should fall back to the default tier."""
    return score < minimum_score
