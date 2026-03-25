"""Simple event-thread storage for session history."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class MemoryEvent:
    """One event in a session history thread."""

    timestamp_utc: str
    label: str
    details: str


@dataclass(slots=True)
class QuantumMemoryThread:
    """Append-only event thread scaffold."""

    thread_id: str
    events: list[MemoryEvent] = field(default_factory=list)

    def append(self, event: MemoryEvent) -> None:
        """Add an event to the thread."""
        self.events.append(event)
