# YOLO26 Benchmark Tool

Unified benchmarking tool for YOLO26 models on DEEPX NPU.
Produces reproducible performance measurements across any Host PC + NPU combination using a standardized procedure.

## Key Features

- **Model-Level Benchmarks**: NPU inference engine throughput/latency measurement (direct `run_model` execution)
- **E2E Pipeline Benchmarks**: Full GStreamer pipeline FPS measurement via DX-STREAM (Single-Stream)
- **Multi-Stream Benchmarks**: Boundary channel count search based on single-stream FPS (1ch reuses single-stream results)
- **NPU Temperature/Clock Monitoring**: Automatic logging of NPU temperature, utilization, and clock (MHz) via dxtop + dxrt-cli pre/post snapshots for throttle detection
- **CPU/NPU Clock Tracking**: Records NPU MHz and CPU MHz to track changes (min/max)
- **Thermal Steady-State Normalization**: Rejects start above 60°C, per-model cooldown targeting `min(idle + Δ10°C, 55°C)`, benchmark failure on cooldown timeout
- **Automatic ORT ON/OFF Comparison**: Both modes measured automatically in every benchmark
- **Environment Fingerprinting**: Automatic capture of measurement context for reproducibility
- **Markdown Report Generation**: Result tables + ORT comparison + channel capacity summary
- **Static Dashboard**: HTML dashboard for comparing results across multiple environments
- **Version Trend Tracking**: Line charts comparing performance changes across dx-all-suite releases for the same HW_ID
- **Resume / Retry-Failed**: Continue from interrupted runs or rerun only failed conditions

## Supported Tasks

| Task | Model-Level | E2E Pipeline | Multi-Stream |
|------|:-----------:|:------------:|:------------:|
| Object Detection | O | O | O |
| Pose Estimation | O | O | O |
| Segmentation | O | O | O |
| Oriented BBox (OBB) | O | O | O |
| Classification | O | O | — |

> OBB models use 1024x1024 input, Classification uses 224x224 (keep-ratio=false), all others use 640x640.
> Classification Multi-Stream is excluded: Classification is less representative of common E2E multi-stream usage scenarios.

## Directory Structure

```
dx-benchmark/
├── run.sh          # launcher
├── setup_data.sh   # data setup: download models + videos (no sudo)
├── setup_host.sh   # one-time host provisioning (sudo): system deps + dxrt sudoers + journal
├── README.md
├── docs/           # ANALYSIS_EN.md, ANALYSIS_KOR.md (performance analysis)
├── benchmark/      # python package (python3 -m benchmark)
│   ├── __main__.py, config.py, model_list.json, ...
│   └── assets/{models,videos}/   # downloaded (gitignored)
└── results/        # per-run results
    ├── <hw_id>/<run_id>/   # tracked: *_results.json + environment.json + REPORT.md
    │                       # gitignored (local-only): raw/, incidents/, *.csv
    └── dashboard/          # tracked build artifacts (index.html/app.js/styles.css/dataset.json)
```

> **What ships in git:** the compact per-run JSON summaries + `REPORT.md`, plus the
> built dashboard. The large `raw/` logs, `incidents/` diagnostics, and the `*.csv`
> mirrors of the JSON are regenerated locally by `run`/`report` and are **git-ignored**
> — they are not needed to read results or rebuild the dashboard. The `*_results.json`
> files are the lossless source of truth (the CSVs carry identical columns).

## Prerequisites

- **OS**: Linux (x86_64 or arm64) with a DEEPX NPU (DX-M1 / DX-H1).
- **Python 3.9+** — standard library only, no third-party pip packages required.
- **DEEPX runtime installed** — the benchmark drives already-installed artifacts, not source:
  - `run_model`, `gst-launch-1.0`, `gst-inspect-1.0`, `dxrt-cli` on `PATH`
  - dx_stream GStreamer plugin (`libgstdxstream.so`) and postprocess libraries under
    `/usr/local/share/gstdxstream/lib/`
  - Install via the suite: `dx-runtime/install.sh --all` (see the dx-all-suite README).
- **System tools**: `time` (GNU), `jq`, `ffmpeg` (provides `ffprobe`), `curl`, `tar`.
  Install them all in one shot with `sudo ./setup_host.sh` (apt), or manually on non-apt
  distros (e.g. `dnf install time jq ffmpeg curl tar`).
- **Network access** to `https://sdk.deepx.ai` to download benchmark models/videos.
- Run `./run.sh preflight` first — it verifies the tools above (always-required plus the
  E2E prerequisites) and prints an environment fingerprint.

Then download data once: `./setup_data.sh` (models + videos; no sudo). For host
provisioning (system deps + passwordless dxrt restart + journal access), run
`sudo ./setup_host.sh`.

> **For comparable numbers**: the fingerprint records your CPU governor, NPU/CPU clocks,
> and thermal state so every run is traceable. You do **not** need a specific CPU governor
> — the benchmark reports whatever your host actually uses (the as-deployed number). Just
> keep conditions (cooling, power, background load, governor) consistent across the runs
> you compare.

## Usage

### 1. Environment Check

```bash
cd /path/to/dx-benchmark
./run.sh preflight
# raw equivalent (from dx-benchmark/): python3 -m benchmark preflight
```

### 2. Dry-Run (Preview Matrix)

```bash
./run.sh dry-run
./run.sh dry-run --sizes n,s --task object_detection
```

### 3. Run Benchmarks

```bash
# Full suite (model + e2e + multi-stream)
./run.sh run

# Run by family
./run.sh run --family model
./run.sh run --family e2e
./run.sh run --family multi

# Limit sizes / time
./run.sh run --sizes n,s --family model --model-time 30

# Resume interrupted run
./run.sh run --resume results/BIOSTAR_H1-Quattro/20260710_180653

# Retry failed conditions only
./run.sh run --resume results/BIOSTAR_H1-Quattro/20260710_180653 --retry-failed
```

### 4. Regenerate Report

```bash
# Specify a {hw_id}/{run_id} result directory path
./run.sh report results/BIOSTAR_H1-Quattro/20260710_180653
```

### 5. Aggregate Results

```bash
# Aggregate multiple environment/run results into a single dataset.json
./run.sh aggregate results
./run.sh aggregate results --output /tmp/dataset.json
```

### 6. Build Dashboard

```bash
# Aggregate + generate dashboard
./run.sh dashboard results
# → generates index.html, app.js, styles.css, dataset.json under results/dashboard/

# Custom output directory
./run.sh dashboard results --output /tmp/dashboard

# Local preview
cd results/dashboard && python3 -m http.server 8899
```

Pure HTML/CSS/JS with no external CDN — works fully offline.

**Dashboard Tabs:**

| Tab | Description |
|-----|-------------|
| E2E FPS Overview | E2E FPS comparison chart by Task/ORT (grouped bars by model size). Max Ch badge displayed above E2E FPS. |
| Full Metrics | Cross-environment comparison of NPU Latency, Throughput, E2E FPS per Task/Size/ORT. Latency shown as dashed line on secondary Y-axis. |
| Detailed Data | Full numeric table with Environment/Task/ORT filters. Run ID dropdown for specific run selection. |
| Version Trend | dx-all-suite version performance trend line charts from nested result history. Metrics dropdown: Latency/Throughput/E2E FPS/Max Channel. |

### 7. Version Trend Tracking

Compare benchmark results before and after dx-all-suite releases using the same HW_ID.

**Workflow:**

```bash
# (1) Run benchmark on each environment
./run.sh run

# (2) Bump dx-all-suite version (release.ver or --dx-all-suite-version), run again on the same HW
./run.sh run

# (3) Generate dashboard from nested results root → check Version Trend tab
./run.sh dashboard results
```

Results always follow the `results/{hw_id}/{run_id}/` structure. HW_ID is automatically computed from the `environment.json` fingerprint during `run`.

- With `--product-name`: `{product_name}_{hw_config}` (e.g., `DX-AIPlayer-N97_M1`)
- Without: `{hostname}_{hw_config}` (e.g., `RPi5B_M1`)

**Result Directory Structure:**

```
results/
├── DX-AIPlayer-N97_M1/          # When --product-name is used
│   ├── 20260629_172308/         # one run per (env, dx-all-suite version)
│   │   ├── environment.json           # tracked
│   │   ├── {model,pipeline,multi_stream}_results.json   # tracked (source of truth)
│   │   ├── REPORT.md                   # tracked
│   │   ├── {model,pipeline,multi_stream}_results.csv    # git-ignored (CSV mirror)
│   │   ├── raw/                        # git-ignored (raw logs)
│   │   └── incidents/                  # git-ignored (timeout diagnostics)
│   └── 20260710_180416/
│       └── (same layout)
├── RPi5B_M1/                     # Hostname-based (default)
│   └── 20260713_115536/
│       └── (same layout)
└── dashboard/                    # tracked build artifacts (consumed by suite tooling)
    ├── index.html
    ├── app.js
    ├── styles.css
    └── dataset.json
```

**Version Trend Tab:**

- Environment / Task / ORT / Metrics filters for condition selection
- Metrics dropdown: Latency, Throughput, E2E FPS, Max Channel
- X-axis: dx-all-suite version (latest run per version; run date shown as secondary label), Y-axis: selected metric
- Per-size (N/S/M/L/X) line charts
- Automatic label de-overlap, selected column highlight (white halo + black text)
- Click a point to view the snapshot's environment details (Host PC / NPU / Tools)

### dx-all-suite version tracking

The dashboard's **Version Trend** tab compares results across dx-all-suite
releases. The version is captured per run, resolved in this order:

- `--dx-all-suite-version v2.4.0` passed to `run` (explicit — always wins), **or**
- run in-suite: auto-read from the suite-root `release.ver` (walked up from the
  package dir), **or**
- on an interactive terminal with neither available: you are prompted for it, **or**
- otherwise (headless / unattended): a `[WARN]` is printed and the run is recorded
  with version `unknown` (it groups under an `unknown` bucket in the trend).

**Unattended runs:** always pass `--dx-all-suite-version` explicitly for headless
or long-running unattended jobs — otherwise, on a TTY with no `release.ver`, the
run pauses at the interactive prompt.

**Back-data (runs measured before this feature):** gather the run directories under
`results/<hw_id>/<run_id>/` and add a single top-level string key to each
`environment.json` — note this is the snake_case JSON key, not the CLI flag:

    "dx_all_suite_version": "v2.3.0"

Runs left unstamped group under `unknown`.

## CLI Options

### `run` / `dry-run` Common Options

| Option | Default | Description |
|--------|---------|-------------|
| `--task` | `all` | Task type (`all`, `object_detection`, `pose_estimation`, `segmentation`, `oriented_bbox`, `classification`) |
| `--sizes` | `n,s,m,l,x` | Model sizes to measure (comma-separated) |
| `--family` | `all` | Benchmark family: `model`, `e2e`, `multi`, `all` |
| `--model-time` | 30 | Model-level throughput measurement duration (seconds, `run_model -t`). Latency uses fixed 300 loops (`-l`) |
| `--warmup` | 1 | Warmup run count |
| `--runs` | — | Override all repetition counts to the same value. Defaults: latency=1, throughput=3, e2e=3 |
| `--fps-threshold` | 30 | Per-channel minimum FPS threshold for multi-stream |
| `--video` | Auto per task | Override input video path (applied to all tasks) |
| `--output` | `results/` | Output root directory. Actual output: `<output>/<hw_id>/<run_id>/` |
| `--resume` | — | Resume from an existing result directory |
| `--retry-failed` | — | With `--resume`, rerun only entries not in `ok`/`partial` status |
| `--product-name` | — | Product name. Used in HW_ID instead of hostname (e.g., `DX-AIPlayer-N97`) |
| `--dx-all-suite-version VER` | Auto (`release.ver`) | dx-all-suite release version for the Version Trend axis (e.g. `v2.4.0`). Default: auto-read from suite-root `release.ver` |

### Subcommands

| Command | Description |
|---------|-------------|
| `preflight` | Check tool availability + print environment fingerprint |
| `dry-run` | Preview benchmark matrix (no execution) |
| `run` | Execute benchmarks |
| `report <result_dir>` | Regenerate Markdown report from existing results |
| `aggregate <results_root> [--output PATH]` | Aggregate results into dataset.json |
| `dashboard <results_root> [--output DIR]` | Generate static HTML dashboard |

## Output Structure

```
results/{hw_id}/{run_id}/
├── environment.json              # tracked — environment fingerprint + timing + timing_history
├── model_results.json            # tracked — model-level results (throughput + latency)
├── pipeline_results.json         # tracked — E2E single-stream results
├── multi_stream_results.json     # tracked — multi-stream boundary search results
├── REPORT.md                     # tracked — comprehensive Markdown report
├── *_results.csv                 # git-ignored — CSV mirror of the JSON above (identical columns)
├── raw/                          # git-ignored — raw logs (.log + .npu.log + profiler.json)
└── incidents/                    # git-ignored — timeout diagnostic snapshots (when applicable)
```

Every command reads the **JSON** files (`aggregate`, `dashboard`, `report`, and
`--resume` all consume `*_results.json`), so the git-ignored CSVs and raw logs are
never required to view results or rebuild the dashboard from a fresh clone.

## Resume vs Retry-Failed

| Scenario | Command |
|----------|---------|
| Interrupted → continue unfinished combinations | `--resume <dir>` |
| Rerun only failed conditions | `--resume <dir> --retry-failed` |
| Fresh measurement | New result directory via `run` |

## Measurement Protocol

| Parameter | Value |
|-----------|-------|
| Throughput duration (`-t`) | 30s |
| Latency loops (`-l`) | 300 loops (`run_model -s` mode ignores `-t`, uses `-l` only) |
| Warmup | 1 run |
| Latency runs | 1 |
| Throughput runs | 3 |
| E2E runs | 3 (uniform across all tasks) |
| ORT modes | ON + OFF |
| Thermal mode | steady |
| Hot-start block | 60°C (benchmark start rejected if exceeded) |
| Cooldown target | `min(idle + Δ10°C, 55°C)` |
| Cooldown timeout | 1000s (RuntimeError on exceed) |
| NPU warmup | 1.0s |
| NPU drain | 0.5s |
| NPU clock monitoring | dxtop Core Clock MHz (during measurement) + dxrt-cli pre/post snapshots |
| CPU clock monitoring | sysfs scaling_cur_freq pre/post snapshots |
| Multi-stream 1ch | Reuses single-stream result |
| Multi-stream max streams | 128 (safety cap) |
| Process timeout | `run_model`: 600s/run; E2E/multi: 90s no-progress stall + 1800s hard cap |
| Graceful shutdown | SIGTERM → 10s wait → SIGKILL (2-phase) |
| Retry (model / E2E / multi) | warmup: 1 retry on timeout; measured runs: up to 2 backfill attempts |
| NPU recovery | Automatic dxrt.service restart after SIGKILL |

> **Reading NPU %** — Throughput/E2E/Multi report NPU **core utilization** sampled by
> dxtop over the run (sustained load). Latency reports NPU **occupancy**
> (`npu_task_ms / total_ms`, from the profiler): a sub-second single-core run is too
> short for dxtop's ~1 Hz sampler, so its clock/throttle are omitted and shown only for
> the sustained metrics. A red clock elsewhere means it dropped below the nominal rated
> clock under load (throttling) — idle DVFS downclock is not throttling.

## Per-Model Execution Order (Thermal Normalization)

Each model × ORT combination follows these steps sequentially.
This ordering ensures the NPU warms up naturally from cold state.

```
── [1/N] yolo26-n_640x640.dxnn  ORT=ON  (object_detection) ──

  ① Cooldown → Rejects start above 60°C. Wait until ≤ min(idle + Δ10°C, 55°C) (when family=model is included)
  ② Latency  → Single-core sync mode (-l 300 loops), profiler-based NPU/CPU ms
                (cold state → NPU DVFS stabilization begins)
  ③ Throughput → Multi-core async mode, FPS measurement (3 runs)
                 (sustained NPU load → natural temperature convergence)
  ④ E2E Single-Stream → Full GStreamer pipeline FPS measurement (3 runs)
  ⑤ Multi-Stream Sweep → Start point estimation from single-stream FPS, then boundary search

→ Proceed to next model × ORT combination (repeat from ①)
```

**Design Rationale:**

- ② Latency runs from cold state. The profiler accurately measures NPU/CPU time separation with minimal temperature impact.
- ③ Throughput runs 30s × 3 consecutive runs to sufficiently heat the NPU.
- ④ By E2E measurement time, NPU temperature has nearly converged (steady state) after ②+③.
- ⑤ Multi-stream runs immediately after E2E, maintaining thermal equilibrium without additional cooldown.
- ① Cooldown is only performed when the model family is included.
- If cooldown times out (1000s), the run fails with RuntimeError.
- If both latency and throughput time out, E2E/Multi-Stream phases are automatically skipped for that model.

## Timeout Recovery and Retry Strategy

During benchmark execution, GStreamer pipelines or run_model processes may become
unresponsive (deadlock, NPU hang). A 3-layer recovery structure handles these cases.

### Layer 1: Graceful Shutdown (SIGTERM → SIGKILL)

When a `run_model` process exceeds its 600s timeout — or an E2E/multi-stream pipeline
stalls (no progress for 90s) or exceeds the 1800s hard cap:

1. **SIGTERM** sent to the entire process group → up to 10s wait for graceful exit
2. If not terminated by SIGTERM → **SIGKILL** forced termination
3. If SIGKILL was needed → NPU device recovery (see below)

> Force-killing gst-launch-1.0 via SIGKILL destroys dxrtd's IPC message queue
> (Error 43: Identifier removed). All subsequent NPU inference fails in this state,
> making device recovery mandatory.

### Layer 2: Python-Level Retry (Per Pipeline)

Handles transient deadlocks in individual pipelines/models:

Retry behavior is unified across families via two knobs — `model_warmup_retries`
(default 1) and `model_run_retries` (default 2):

| Phase | Retries | Notes |
|-------|:-------:|-------|
| Warmup (model / E2E / multi) | 1 | 1 retry on timeout (`model_warmup_retries`) before giving up the cell |
| Measured run (model / E2E / multi) | up to 2 | Backfill failed/timed-out runs toward the target count (`model_run_retries`); remaining successful runs are averaged |
| Multi-stream sweep | up to 2 / channel | Same backfill budget per stream count |

When both model-level (latency + throughput) time out consecutively,
E2E and multi-stream phases are automatically skipped for that model × ORT combination.

### Incident Diagnostic Collection

On timeout, diagnostic snapshots are saved to the `incidents/` directory:

- `dxrt-cli -s` NPU status
- `systemctl status dxrt.service` service status
- `journalctl` recent 100 lines / `dmesg` recent 200 lines
- Process tree dump (`ps`)
- NPU temperature/clock snapshot

### NPU Device Recovery

Automatically triggered when SIGKILL was required:

1. `pkill -9 gst-launch-1.0` — clean up orphaned pipeline processes
2. `sudo -n systemctl restart dxrt.service` — restart NPU runtime daemon (3s settle)
3. Same procedure for run_model timeout (`pkill -9 run_model` + service restart)

> Passwordless sudo required: run `sudo ./setup_host.sh` or manually add the
> following rules to `/etc/sudoers.d/benchmark-dxrt`:
> ```
> user ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart dxrt.service
> user ALL=(ALL) NOPASSWD: /usr/bin/dmesg *
> user ALL=(ALL) NOPASSWD: /usr/bin/journalctl *
> ```

## Development / Testing

The tool has no third-party runtime dependencies (standard library only). The test
suite uses `pytest` (a dev-only dependency):

```bash
cd /path/to/dx-benchmark
pip install pytest          # dev-only; not needed to run benchmarks
python3 -m pytest tests/
```

The repo-root `conftest.py` is intentionally empty — its mere presence sets the pytest
`rootdir` and puts the package root on `sys.path`, so `import benchmark` resolves without
any install or `PYTHONPATH` tweaks.
