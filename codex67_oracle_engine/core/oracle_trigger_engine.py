"""High-level entry point that combines extraction, validation, and routing."""

from __future__ import annotations

from dataclasses import dataclass

from ..resonance_field.resonance_validator import ResonanceResult, ResonanceValidator
from ..resonance_field.state_dependent_router import ResponseTier, StateDependentRouter
from .lsps_system import LSPSRegistry
from .mirror_layer import extract_signal
from .sovereign_lockout import should_lock_out


@dataclass(slots=True)
class TriggerDecision:
    """Structured output from the trigger engine."""

    tier: ResponseTier
    score: float
    command: str | None
    locked_out: bool
    resonance: ResonanceResult


class OracleTriggerEngine:
    """Small orchestration object for the scaffolded trigger path."""

    def __init__(self) -> None:
        self.validator = ResonanceValidator()
        self.router = StateDependentRouter()
        self.registry = LSPSRegistry()

    def evaluate(self, text: str) -> TriggerDecision:
        """Evaluate text and return the routed response tier."""
        signal = extract_signal(text)
        resonance = self.validator.evaluate(signal.raw_text)
        command = self.registry.match(text)
        locked_out = should_lock_out(resonance.total_score)
        tier = self.router.route(
            score=resonance.total_score,
            command_detected=command is not None,
            locked_out=locked_out,
        )
        return TriggerDecision(
            tier=tier,
            score=resonance.total_score,
            command=command,
            locked_out=locked_out,
            resonance=resonance,
        )
