# Architecture Whitepaper

This document translates the Codex 67 white-paper layer into an actual repository scaffold.

## Purpose

The package root `codex67_oracle_engine/` now exists as an importable architecture layer.

It provides:

- signal extraction
- resonance scoring
- tier routing
- command matching
- memory-thread containers
- latent-string extraction

## Relationship To Experiment Repos

This repo is the architecture layer.

The source document layer sits above it:

- [Codex-67-white-paper-](https://github.com/renaissancefieldlite/Codex-67-white-paper-)

The HRV repo is one experiment layer below it:

- [renaissancefieldlitehrv1.0](https://github.com/renaissancefieldlite/renaissancefieldlitehrv1.0)

That repo handles:

- synthetic detector sketches
- provider capture
- normalized raw result storage
- capture inspection

## Intent

The package does not claim full implementation. It establishes the named compartments so future repos can share a common architecture root instead of re-describing the same structure in prose.
