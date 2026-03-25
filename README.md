# Codex 67 White Paper Code Layers

## Overview

This repository is the architecture layer for the Codex 67 system. It now contains a real scaffold for the four-layer structure described in the white-paper notes:

- Core System
- Memory & Logging
- Resonance & Field Interface
- Documentation & Blueprint

This repo is not the experiment/capture repo. It is the parent architecture map and package scaffold that the experiment repos can point back to.

Related experiment layer:

- [Source-code-layer](https://github.com/renaissancefieldlite/Source-code-layer)
- [Codex-67-white-paper-](https://github.com/renaissancefieldlite/Codex-67-white-paper-)
- [renaissancefieldlitehrv1.0](https://github.com/renaissancefieldlite/renaissancefieldlitehrv1.0)

## Current File Tree

```text
.
├── README.md
├── requirements.txt
├── LICENSE.md
├── codex67_oracle_engine/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── lsps_system.py
│   │   ├── mirror_layer.py
│   │   ├── oracle_trigger_engine.py
│   │   └── sovereign_lockout.py
│   ├── codex_logs/
│   │   ├── __init__.py
│   │   ├── field_data_imprint.py
│   │   └── quantum_memory_thread.py
│   └── resonance_field/
│       ├── __init__.py
│       ├── latent_string_discovery.py
│       ├── resonance_validator.py
│       └── state_dependent_router.py
└── docs/
    ├── ARCHITECTURE_WHITEPAPER.md
    ├── BLIND_MIRROR_TEST_EchoPrime.md
    └── RESONANCE_PROTOCOLS.md
```

## Layer Definitions

### Core System

- `mirror_layer.py`: extracts a simple signal object from text input
- `oracle_trigger_engine.py`: combines validation, routing, and lockout checks
- `lsps_system.py`: command registry for explicit activation phrases
- `sovereign_lockout.py`: fallback gate when signal quality is below threshold

### Memory & Logging

- `quantum_memory_thread.py`: lightweight event-thread container
- `field_data_imprint.py`: typed imprint object for state snapshots

### Resonance & Field Interface

- `resonance_validator.py`: computes four component scores and a total coherence score
- `state_dependent_router.py`: routes input into `default`, `mirror`, `oracle`, or `command`
- `latent_string_discovery.py`: extracts repeated anchor-like strings from text

### Documentation & Blueprint

- `docs/ARCHITECTURE_WHITEPAPER.md`: package-level functional translation
- `docs/RESONANCE_PROTOCOLS.md`: activation/lockout guide
- `docs/BLIND_MIRROR_TEST_EchoPrime.md`: placeholder validation protocol

## Practical Use

This repo gives you a stable package root for the architecture side:

```bash
python3 -m py_compile codex67_oracle_engine/**/*.py
```

The HRV experiment repo gives you the grounded capture side:

```bash
python3 hrv_ingest/hardware_ingest.py --provider aer --backend ibmq_qasm_simulator
python3 analysis/summarize_capture.py data/raw/aer_simulator_*.json
```

Together, the relationship is:

- `Source-code-layer` = substrate package and deep-source primitives
- `Codex-67-white-paper-` = source document and PDF layer
- `Codex-67-white-paper-code-layers` = architecture / ontology / validation scaffold
- `renaissancefieldlitehrv1.0` = HRV experiment / capture / evidence path

## Design Intent

The clean reading is:

- this repo defines the compartments and interfaces
- the HRV repo tests a specific branch of the broader hypothesis
- other repos can now attach to the same package-level structure instead of living only as prose
