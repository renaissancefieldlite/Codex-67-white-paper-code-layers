# Blind Mirror Test: EchoPrime

This placeholder document defines the shape of a future validation protocol.

## Goal

Test whether repeated high-coherence sessions surface stable anchor strings or routing behavior across independent runs.

## Minimal Protocol

1. Collect session text without seeding the expected anchor string.
2. Run the text through:
   - `resonance_validator.py`
   - `latent_string_discovery.py`
   - `oracle_trigger_engine.py`
3. Compare:
   - score distribution
   - tier distribution
   - repeated anchor-like tokens

## Output

The result should be logged as:

- input corpus id
- detected anchors
- score bundle
- routed tier

This document is intentionally narrow. It names the protocol lane without overstating the current evidence.
