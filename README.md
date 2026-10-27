# Recovery Protocol - Modules

Learning modules for the Recovery Protocol system recovery game.

## Structure

```
modules/
└── core/
    ├── tasks/           (Edit these to solve challenges)
    ├── tests/           (These verify your solutions)
    └── metadata.json    (Module definition)
```

## Usage

Clone this alongside recovery-protocol-framework, as your game folder's
`modules/` directory:

```bash
git clone <framework-repo> recovery-framework
git clone <modules-repo> game/modules
cd recovery-framework && uv sync
cd ../game
../recovery-framework/.venv/bin/recovery
```

`recovery` with no flags finds the first task that isn't passing yet and
checks it - nothing to remember or type. It also works from inside any
subdirectory of `game/`, not just its root.

## Modules

- **core** - Data manipulation fundamentals (sorting, filtering, parsing)
  - sort_signals
  - extract_callsign
  - decode_status
  - filter_logs
  - merge_signals

Future modules will cover:
- file_io
- data_structures
- algorithms
- concurrency

## CI

`.github/workflows/stub-integrity.yml` is a reversed check: every task
ships as an unsolved stub, so its tests are *expected* to fail. The job
goes red only if a task's tests pass against the shipped file - meaning a
solution leaked in instead of a stub.
