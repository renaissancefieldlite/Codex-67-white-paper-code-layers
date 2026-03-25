"""Coherence scoring scaffold for four activation criteria."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ResonanceResult:
    """Result bundle for the four-part resonance score."""

    tonal_precision: float
    linguistic_integrity: float
    emotional_coherence: float
    intent_purity: float

    @property
    def total_score(self) -> float:
        return (
            self.tonal_precision
            + self.linguistic_integrity
            + self.emotional_coherence
            + self.intent_purity
        ) / 4.0


class ResonanceValidator:
    """Very small heuristic validator for the scaffold package."""

    def evaluate(self, text: str) -> ResonanceResult:
        stripped = text.strip()
        length = len(stripped)
        words = stripped.split()
        unique_ratio = len(set(words)) / len(words) if words else 0.0
        alpha = sum(1 for char in stripped if char.isalpha()) or 1
        uppercase_ratio = sum(1 for char in stripped if char.isupper()) / alpha
        exclamations = stripped.count("!")

        tonal_precision = max(0.0, 1.0 - min(uppercase_ratio * 1.4, 1.0))
        linguistic_integrity = min(unique_ratio + 0.2, 1.0)
        emotional_coherence = max(0.0, 1.0 - min(exclamations / 8.0, 1.0))
        intent_purity = min(length / 120.0, 1.0) if length else 0.0

        return ResonanceResult(
            tonal_precision=round(tonal_precision, 3),
            linguistic_integrity=round(linguistic_integrity, 3),
            emotional_coherence=round(emotional_coherence, 3),
            intent_purity=round(intent_purity, 3),
        )
