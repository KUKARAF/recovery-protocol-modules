# Recovery Protocol - Modules

Learning modules for the Recovery Protocol system recovery game.

## Structure

```
modules/
└── back_to_basics_module/
    ├── tasks/           (Edit these to solve challenges)
    ├── tests/           (These verify your solutions)
    └── metadata.json    (Module definition)
```

## Usage

Clone this alongside recovery-protocol-framework:

```bash
git clone <framework-repo> recovery-framework
git clone <modules-repo> recovery-modules
cd recovery-framework
uv sync
```

Then from your game folder:

```bash
../recovery-framework/.venv/bin/python -m pytest recovery-modules/modules/back_to_basics_module/tests/
```

Or use the validation script in your game folder.

## Modules

- **back_to_basics_module** - Data manipulation fundamentals (sorting, filtering, parsing)
  - sort_signals
  - extract_callsign
  - decode_status
  - filter_logs
  - merge_signals

Future modules will cover:
- file_io_module
- data_structures_module
- algorithms_module
- concurrency_module
