"""Response-tier routing scaffold."""

from __future__ import annotations

from enum import Enum


class ResponseTier(str, Enum):
    """Named output tiers for the scaffold."""

    DEFAULT = "default"
    MIRROR = "mirror"
    ORACLE = "oracle"
    COMMAND = "command"


class StateDependentRouter:
    """Route sessions based on score and explicit command detection."""

    def route(self, *, score: float, command_detected: bool, locked_out: bool) -> ResponseTier:
        if locked_out:
            return ResponseTier.DEFAULT
        if command_detected:
            return ResponseTier.COMMAND
        if score >= 0.8:
            return ResponseTier.ORACLE
        if score >= 0.6:
            return ResponseTier.MIRROR
        return ResponseTier.DEFAULT
