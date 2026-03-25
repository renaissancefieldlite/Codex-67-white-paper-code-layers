"""Typed symbolic imprint objects for session logging."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class FieldDataImprint:
    """Simple container for session-state metadata."""

    session_id: str
    state_label: str
    coherence_score: float
    tags: list[str] = field(default_factory=list)
    notes: str = ""
