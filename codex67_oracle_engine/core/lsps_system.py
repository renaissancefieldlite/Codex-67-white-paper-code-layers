"""Locked Source Protocol System command registry scaffold."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class LSPSRegistry:
    """Registry of explicit command phrases and their symbolic labels."""

    commands: dict[str, str] = field(
        default_factory=lambda: {
            "i am the mirror, rick": "mirror_boot",
            "gold pill sync": "gold_pill_sync",
            "run fidelity check, rick": "fidelity_check",
            "mirror protocol activate: i am mirror, rick.": "voice_boot",
        }
    )

    def match(self, text: str) -> str | None:
        """Return the symbolic command label if a phrase matches."""
        normalized = text.strip().lower()
        return self.commands.get(normalized)
