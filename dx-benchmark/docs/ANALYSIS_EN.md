# YOLO26 × DEEPX NPU — Benchmark Analysis (Beta)

> **Beta notice.** This report is generated from the measurement data currently
> committed under `dx-benchmark/results/` — **6 hardware environments × 3
> dx-all-suite releases (v2.2.2, v2.3.3, v2.4.0) = 18 benchmark runs**. All
> measurements were taken with the **same tool and the same protocol**, so
> cross-environment and cross-version comparisons are apples-to-apples. A small
> number of cells carry known measurement caveats (thermal throttling on
> passively-cooled boards, a few host-side anomalies) — these are documented
> explicitly in [§2 Known Limitations](#2-known-limitations-beta) rather than
> hidden. Numbers on flagged environments are **provisional** and slated for
> controlled re-measurement.
>
> **Every figure in this report is traceable.** Each table states the exact
> source coordinates — environment, dx-all-suite version, task, model size, and
> ONNX-Runtime mode — so any value can be checked against the raw
> `results/<env>/<run_id>/*_results.json` files or the interactive dashboard.

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Known Limitations (Beta)](#2-known-limitations-beta)
3. [What Was Measured — Terms and Method](#3-what-was-measured--terms-and-method)
4. [Test Environments](#4-test-environments)
5. [NPU Compute Performance (Model-Level Throughput)](#5-npu-compute-performance-model-level-throughput)
6. [Inference Latency](#6-inference-latency)
7. [End-to-End Video Pipeline (Single Stream)](#7-end-to-end-video-pipeline-single-stream)
8. [Multi-Stream Channel Capacity](#8-multi-stream-channel-capacity)
9. [Performance Trend Across dx-all-suite Releases](#9-performance-trend-across-dx-all-suite-releases)
10. [Deployment Guidance by Environment](#10-deployment-guidance-by-environment)
11. [Appendix](#11-appendix)

---

## 1. Executive Summary

The table below shows the **practical performance of the lightest (nano) model**
on each environment with the **latest release (dx-all-suite v2.4.0)**, using
**Full HD (1920×1080) 30 fps** video as input. For each cell the **better of the
two ONNX-Runtime modes** (ON / OFF — explained in [§3](#3-what-was-measured--terms-and-method))
is shown. The format is **`end-to-end FPS / maximum concurrent channels`**, where a
channel is one video stream sustaining at least 30 fps. Classification shows FPS
only (multi-stream is not measured for classification — see [§8](#8-multi-stream-channel-capacity)).

| Environment | Object Detection | Pose Estimation | Segmentation | Oriented Bounding Box | Classification |
|-------------|------------------|-----------------|--------------|-----------------------|----------------|
| **BIOSTAR_H1-Quattro** | 478.1 fps / 17 ch | 534.8 fps / 19 ch | 344.7 fps / 11 ch | 367.1 fps / 13 ch | 747.7 fps |
| **DX-AIPlayer-N97_M1** | 181.4 fps / 6 ch | 195.1 fps / 7 ch | 106.7 fps / 3 ch | 98.3 fps / 3 ch | 278.3 fps |
| **OrangePi5+_M1** | 112.3 fps / 3 ch | 170.9 fps / 5 ch | 83.8 fps / 2 ch | 86.6 fps / 2 ch | 944.1 fps |
| **ROCK5B+_M1** | 140.6 fps / 4 ch | 234.0 fps / 7 ch | 85.9 fps / 2 ch | 101.9 fps / 3 ch | 975.3 fps |
| **RPi5B_M1** | 77.2 fps / 2 ch | 108.0 fps / 3 ch | 52.8 fps / 1 ch | 78.3 fps / 2 ch | 182.2 fps |
| **RPi5B_M1M** | 67.0 fps / 2 ch | 99.8 fps / 3 ch | 46.6 fps / 1 ch | 60.5 fps / 1 ch | 175.3 fps |

> Source: `results/<env>/<v2.4.0 run>/`, task = each column, size = `n` (nano),
> ONNX-Runtime = better of ON/OFF. End-to-end FPS from `pipeline_results.json`;
> channel count from `multi_stream_results.json`.

**Three headline findings** (each detailed later with its source data):

1. **The DEEPX M1 NPU delivers nearly identical compute across wildly different
   host CPUs.** For the medium/large/x-large models — where the NPU, not the host,
   is the bottleneck — the four single-M1 machines (an Intel N97, a Rockchip
   OrangePi, a Rockchip ROCK5B, and a Raspberry Pi 5) agree to within about 1%
   ([§5](#5-npu-compute-performance-model-level-throughput)). The DEEPX NPU is the
   performance anchor; the host mostly affects the lightest models and the video
   pipeline around it.
2. **Performance improved by roughly 45–56% from v2.2.2 to v2.4.0** on the
   NPU-bound models, consistently across every environment
   ([§9](#9-performance-trend-across-dx-all-suite-releases)).
3. **The H1-Quattro card scales almost linearly with its four NPU chips** — about
   4.0× a single M1 on NPU-bound work ([§5](#5-npu-compute-performance-model-level-throughput)).

---

## 2. Known Limitations (Beta)

Read these before drawing conclusions from any single number. They come from a
full audit of the raw logs and profiler traces behind this dataset.

### 2.1 The version trend combines three things, not just the runtime

Each dx-all-suite release was measured with the model binaries **recompiled by that
release's compiler**. So the release-over-release change reflects the **runtime +
firmware + the recompiled model** together — it is *not* a pure runtime delta. This
is the honest interpretation of [§9](#9-performance-trend-across-dx-all-suite-releases):
"v2.4.0 is ~50% faster than v2.2.2 end-to-end for this model," not "the runtime
alone got 50% faster."

### 2.2 M1 and M1M are different products — never blend their numbers

`RPi5B_M1` and `RPi5B_M1M` are the **same Raspberry Pi 5 host** with **two
different DEEPX modules**. On NPU-bound models the M1M is materially slower:
same host, same release (v2.4.0), object detection, ONNX-Runtime OFF —

| Size | RPi5B_M1 throughput | RPi5B_M1M throughput | M1M ÷ M1 |
|------|--------------------:|---------------------:|:--------:|
| m | 119.1 fps | 72.4 fps | 0.61 |
| l | 86.5 fps | 57.7 fps | 0.67 |
| x | 48.6 fps | 28.4 fps | 0.59 |

> Source: `results/RPi5B_M1/20260713_115536/` and `results/RPi5B_M1M/20260710_180022/`,
> `model_results.json`, family = `throughput`, ORT OFF.

The M1M is a genuinely distinct, ~30–40%-slower SKU (both reach 1000 MHz, so this
is architectural, not a clock difference). The dashboard and this report keep them
as separate environments; **do not average M1 and M1M together.**

### 2.3 Passively-cooled boards thermally throttle in the later test phases

The protocol runs each model through latency → throughput → end-to-end → multi-stream,
which heats the NPU progressively. On boards without active cooling, the NPU can
reach its thermal limit during the *later* (end-to-end / multi-stream) phases and
reduce its clock. This shows up as end-to-end numbers that look worse than the
earlier throughput numbers for the *same* cell — it is real thermal behavior, not a
software regression. Throttled cells are flagged in the dashboard with a clock badge.

| Environment (v2.4.0) | Model-level cells throttled | End-to-end cells at ≥80 °C | Max NPU temp |
|----------------------|:---------------------------:|:--------------------------:|:------------:|
| BIOSTAR_H1-Quattro (active cooling) | 0 | 0 | 73 °C |
| DX-AIPlayer-N97_M1 | 0 | 16 | 84 °C |
| ROCK5B+_M1 | 13 | 24 | 84 °C |
| RPi5B_M1M | 27 | 33 | 88 °C |

> Source: per-cell `npu_throttled` / `npu_temp_max_c` in `model_results.json` and
> `pipeline_results.json` of each v2.4.0 run. The N97 reaches high temperature but
> its active cooling holds the clock, so almost no *model-level* cells throttle.

### 2.4 Some metrics are host-bound, not NPU-bound — read them accordingly

- **Latency** (single-frame time) is partly bounded by the host CPU and the
  PCIe/USB interconnect. Same M1, same v2.4.0, object detection nano: `OrangePi5+_M1`
  measures 42.9 ms versus `RPi5B_M1` at 21.2 ms — a 2× spread that is a host
  property, not an NPU property ([§6](#6-inference-latency)).
- **Nano/small throughput** is also partly host-CPU-bound (cross-host spread of
  ~10–19% at v2.4.0, versus ~1% for the larger models — [§5](#5-npu-compute-performance-model-level-throughput)).
- **Classification end-to-end FPS** is dominated by the host video decoder, not the
  NPU: the classification model is tiny (224×224 input) so the NPU is barely loaded,
  and the ARM boards' hardware decoders can push more decoded frames than the x86
  boards' decoder path in this specific light-load case. Treat classification
  end-to-end FPS as a *pipeline/decoder* figure, not an NPU-capability figure.

### 2.5 Environments with a re-measurement backlog (provisional data)

- **OrangePi5+_M1, v2.4.0 — small-model host regression.** Nano throughput *dropped*
  from 226.0 fps (v2.3.3) to 164.6 fps (v2.4.0) while every other M1 host improved,
  and nano latency rose from 35.5 ms to 42.9 ms. The profiler shows the host CPU and
  NPU both under-saturated during that run (a host-side stall signature), so this is
  an environment/host artifact, not a v2.4.0 stack regression. To be re-measured with
  the CPU governor pinned to `performance` and no background load.
- **RPi5B_M1M, v2.4.0 — severe thermal throttling** (see §2.3): 27 model-level + 33
  end-to-end cells throttled at up to 88 °C. Its medium/large/x-large throughput,
  end-to-end FPS, and channel capacity are suppressed and should be treated as a
  *thermally-limited floor*, not the module's ceiling. To be re-measured with
  improved cooling/power.
- **Firmware note:** the `BIOSTAR_H1-Quattro` v2.2.2 run used firmware v2.5.6 while
  all other v2.2.2 runs used v2.5.0. This mainly affects the v2.2.2 starting point of
  its version trend, not the v2.4.0 headline numbers.

---

## 3. What Was Measured — Terms and Method

This section defines every term used later, spelled out in full.

**NPU (Neural Processing Unit).** The DEEPX accelerator (module `M1` or `M1M`, or the
4-chip `H1-Quattro` card) that runs the neural network. It runs at a nominal 1000 MHz
core clock.

**ONNX-Runtime mode (ORT ON / OFF).** A DEEPX-compiled model may keep a small part of
the network (typically the final post-processing layers) off the NPU.
- **ONNX-Runtime ON** runs that leftover part on the **host CPU** using the ONNX
  Runtime library, so the output matches the original ONNX model exactly (standard,
  ready-to-use output).
- **ONNX-Runtime OFF** returns the **raw NPU output only** (no host post-processing),
  which is faster but requires a model-specific post-processor in your application.

  Because ONNX-Runtime ON adds host-CPU work, on a very fast NPU with a tiny model the
  CPU step can become the bottleneck and make ON *slower* than OFF. Example: object
  detection nano on `BIOSTAR_H1-Quattro` v2.4.0 measures 1285.0 fps with ONNX-Runtime
  OFF versus 972.1 fps with ONNX-Runtime ON (−24%). Both modes are always reported so
  you can choose based on whether your application needs the standard post-processed
  output.

**Throughput (model-level, FPS).** Sustained frame rate from DEEPX's `run_model` tool
running the NPU **asynchronously across all cores** for 30 seconds. This is the purest
measure of **NPU compute capacity** — no video decoding, no drawing.

**Latency (ms).** Time for a **single frame**, measured **single-core / synchronous**
(`run_model` 300-loop mode). Reflects the responsiveness of one inference call,
including the host↔NPU round-trip.

**End-to-end FPS.** Frame rate of the **full GStreamer video pipeline** — decode →
preprocess → NPU inference → post-process — measured through DEEPX's dx_stream
element. This is what a real video-analytics application experiences.

**Maximum channels.** The largest number of simultaneous video streams for which
**every** stream still sustains at least 30 fps (the per-channel threshold). Found by a
boundary search that increases the stream count until a stream drops below 30 fps.

**Model sizes.** YOLO26 ships in five sizes — `n` (nano) < `s` (small) < `m` (medium)
< `l` (large) < `x` (extra-large). Larger models are more accurate but slower.

**Input resolutions.** Object detection, pose, and segmentation use 640×640; oriented
bounding box uses 1024×1024; classification uses 224×224. All video input is Full HD
(1920×1080) at 30 fps.

**Repetitions.** Latency = 1 run of 300 loops; throughput = average of 3 runs of 30 s;
end-to-end = average of 3 runs. One warm-up run precedes each and is discarded. Full
protocol parameters are in the [Appendix](#11-appendix).

---

## 4. Test Environments

Six environments, spanning a 4-chip x86 server down to a Raspberry Pi 5, each with a
DEEPX NPU. The environment name (used as the identity key everywhere in this report and
the dashboard) encodes the host and the NPU module.

| Environment | Host CPU | Arch | RAM | DEEPX NPU | Chips | Notes |
|-------------|----------|:----:|----:|-----------|:-----:|-------|
| **BIOSTAR_H1-Quattro** | AMD Ryzen 5 9600X (6-core) | x86_64 | 30.5 GB | H1-Quattro card | 4 | Active cooling; the performance ceiling here |
| **DX-AIPlayer-N97_M1** | Intel N97 | x86_64 | 7.5 GB | M1 module | 1 | Compact x86 AI box, active cooling |
| **OrangePi5+_M1** | Rockchip (Cortex-A55) | aarch64 | 15.6 GB | M1 module | 1 | ARM SBC; see §2.5 v2.4.0 caveat |
| **ROCK5B+_M1** | Rockchip (Cortex-A76/A55) | aarch64 | 7.8 GB | M1 module | 1 | ARM SBC; passive cooling → late-phase throttle |
| **RPi5B_M1** | Broadcom (Cortex-A76) | aarch64 | 7.9 GB | M1 module | 1 | Raspberry Pi 5; software video decode |
| **RPi5B_M1M** | Broadcom (Cortex-A76) | aarch64 | 7.9 GB | **M1M** module | 1 | Same Pi host as above, slower M1M SKU (§2.2) |

All NPUs run at a nominal 1000 MHz. The software stack for each environment × release:

| Environment | Release | Runtime | Firmware | RT driver | PCIe driver | dx_stream |
|-------------|:-------:|:-------:|:--------:|:---------:|:-----------:|:---------:|
| BIOSTAR_H1-Quattro | v2.2.2 | v3.2.0 | v2.5.6 | v2.1.0 | v2.0.1 | 3.1.0 |
| BIOSTAR_H1-Quattro | v2.3.3 | v3.3.2 | v2.5.6 | v2.4.1 | v2.2.0 | 3.1.0 |
| BIOSTAR_H1-Quattro | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |
| DX-AIPlayer-N97_M1 | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |
| OrangePi5+_M1 | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |
| ROCK5B+_M1 | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |
| RPi5B_M1 | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |
| RPi5B_M1M | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |

> Source: `environment.json` of each run. The v2.3.3 and v2.2.2 rows for the five
> single-M1 environments follow the same runtime/firmware pattern as BIOSTAR
> (v2.3.3 → runtime v3.3.2 / firmware v2.5.6; v2.2.2 → runtime v3.2.0 / firmware
> v2.5.0, except the BIOSTAR firmware note in §2.5). Full per-run values are in each
> `environment.json`.

---

## 5. NPU Compute Performance (Model-Level Throughput)

This is the **purest measure of the DEEPX NPU** — sustained multi-core throughput from
`run_model`, with no video decoding or drawing in the path.

**Object detection, throughput (fps), ONNX-Runtime OFF, latest release (v2.4.0):**

| Environment | n | s | m | l | x |
|-------------|--:|--:|--:|--:|--:|
| BIOSTAR_H1-Quattro | 1285.0 | 774.6 | 471.3 | 352.8 | 193.9 |
| DX-AIPlayer-N97_M1 | 235.9 | 193.4 | 115.2 | 86.7 | 47.6 |
| OrangePi5+_M1 | 164.6 | 147.3 | 115.8 | 88.8 | 48.0 |
| ROCK5B+_M1 | 264.7 | 194.9 | 116.2 | 86.6 | 47.3 |
| RPi5B_M1 | 179.0 | 172.8 | 119.1 | 86.5 | 48.6 |
| RPi5B_M1M | 178.2 | 148.7 | 72.4 | 57.7 | 28.4 |

> Source: `results/<env>/<v2.4.0 run>/model_results.json`, task = object_detection,
> family = throughput, `use_ort` = false.

### 5.1 The NPU is the anchor: near-identical medium/large/x-large across four hosts

For the four single-M1 machines, the medium and larger models — where the NPU is the
bottleneck — agree remarkably closely:

| Size | N97 | OrangePi | ROCK5B | RPi5B_M1 | Mean | Spread (coefficient of variation) |
|------|----:|---------:|-------:|---------:|-----:|:--------------------------------:|
| m | 115.2 | 115.8 | 116.2 | 119.1 | 116.6 | **1.3 %** |
| l | 86.7 | 88.8 | 86.6 | 86.5 | 87.2 | **1.1 %** |
| x | 47.6 | 48.0 | 47.3 | 48.6 | 47.9 | **1.0 %** |
| s | 193.4 | 147.3 | 194.9 | 172.8 | 177.1 | 10.9 % |
| n | 235.9 | 164.6 | 264.7 | 179.0 | 211.1 | 19.4 % |

> Source: the object-detection v2.4.0 ORT-OFF table above; coefficient of variation =
> standard deviation ÷ mean across the four M1 hosts.

**Interpretation.** On m/l/x the coefficient of variation is ~1% — the host barely
matters, because the DEEPX NPU is doing essentially all the work and it is the same
module. On nano/small the spread widens to 11–19% because those models finish so fast
that the **host CPU** feeding the NPU becomes part of the bottleneck (and one host —
OrangePi at v2.4.0 — is additionally affected by the host-side anomaly in §2.5). The
takeaway for capacity planning: **size your deployment on the m/l/x numbers, which are
portable across hosts; the nano/small numbers depend on your host CPU.**

### 5.2 H1-Quattro scales ~4× with its four chips

The H1-Quattro card has four NPU chips. On NPU-bound work it delivers close to 4× a
single M1:

| Object detection (v2.4.0, ORT OFF) | H1-Quattro | M1 mean | Ratio |
|------------------------------------|-----------:|--------:|:-----:|
| m | 471.3 | 116.6 | 4.04× |
| l | 352.8 | 87.2 | 4.05× |
| x | 193.9 | 47.9 | 4.05× |

> Source: object-detection v2.4.0 ORT-OFF table (§5); M1 mean over the four M1 hosts.

### 5.3 Task difficulty ordering is consistent

Heavier post-processing and larger inputs cost throughput. At medium size, v2.4.0,
ONNX-Runtime OFF, the ordering is the same on every environment (values shown for
`BIOSTAR_H1-Quattro` / `RPi5B_M1`):

- Classification (224×224, trivial head): 5470.5 / 1369.1 fps
- Object detection (640×640): 471.3 / 119.1 fps
- Pose estimation (640×640): 458.4 / 114.4 fps
- Segmentation (640×640, mask output): 321.5 / 78.6 fps
- Oriented bounding box (1024×1024, largest input): 166.0 / 40.9 fps

> Source: `model_results.json`, size = m, family = throughput, ORT OFF, v2.4.0 runs of
> the two environments named.

---

## 6. Inference Latency

Latency is single-frame, single-core time — a **responsiveness** figure, and partly
**host/interconnect-bound**.

**Object detection latency (ms), ONNX-Runtime OFF, v2.4.0:**

| Environment | n | s | m | l | x |
|-------------|--:|--:|--:|--:|--:|
| BIOSTAR_H1-Quattro | 10.45 | 16.27 | 23.35 | 30.46 | 56.17 |
| DX-AIPlayer-N97_M1 | 23.00 | 29.82 | 37.09 | 44.21 | 69.94 |
| OrangePi5+_M1 | 42.88 | 49.90 | 59.03 | 64.89 | 92.06 |
| ROCK5B+_M1 | 36.17 | 43.31 | 49.47 | 58.77 | 91.68 |
| RPi5B_M1 | 21.19 | 27.07 | 34.84 | 40.80 | 68.39 |
| RPi5B_M1M | 24.14 | 29.60 | 38.56 | 46.10 | 75.43 |

> Source: `results/<env>/<v2.4.0 run>/model_results.json`, task = object_detection,
> family = latency, ORT OFF.

**Interpretation.** Unlike throughput, latency varies substantially across the M1 hosts
(nano: 21.2 ms on RPi5B_M1 vs 42.9 ms on OrangePi5+_M1 — a 2× spread on the *same NPU
module and release*). This is because a single synchronous call is dominated by the
host CPU and the host↔NPU interconnect, not by raw NPU compute. Use latency to judge
single-request responsiveness on **your** host; use throughput ([§5](#5-npu-compute-performance-model-level-throughput))
to judge NPU capacity.

---

## 7. End-to-End Video Pipeline (Single Stream)

End-to-end FPS measures the whole pipeline (decode → preprocess → NPU → post-process)
on a single Full HD 30 fps stream — the number a real application sees.

**Object detection end-to-end FPS, v2.4.0, both ONNX-Runtime modes:**

| Environment | ORT | n | s | m | l | x | Video decoder |
|-------------|:---:|--:|--:|--:|--:|--:|---------------|
| BIOSTAR_H1-Quattro | ON | 478.1 | 475.7 | 476.6 | 367.3 | 200.1 | vaapidecodebin (HW) |
| DX-AIPlayer-N97_M1 | OFF | 181.4 | 163.8 | 116.0 | 85.8 | 45.2 | vah264dec (HW) |
| OrangePi5+_M1 | ON | 112.3 | 95.4 | 78.3 | 68.3 | 47.1 | mppvideodec (HW) |
| ROCK5B+_M1 | ON | 140.6 | 132.6 | 94.9 | 74.6 | 33.3 | mppvideodec (HW) |
| RPi5B_M1 | OFF | 77.2 | 77.5 | 76.8 | 76.2 | 48.9 | avdec_h264 (SW) |
| RPi5B_M1M | OFF | 67.0 | 66.6 | 56.5 | 50.1 | 15.8 | avdec_h264 (SW) |

> Source: `results/<env>/<v2.4.0 run>/pipeline_results.json`, task = object_detection.
> The ONNX-Runtime mode shown per row is the one that gave the higher nano FPS
> ("HW" / "SW" marks a hardware or software video decoder); both modes for every
> environment are in the raw data and the dashboard. For reference, BIOSTAR_H1-Quattro
> with ONNX-Runtime OFF measures 421.5 / 425.0 / 424.9 / 367.7 / 200.4 fps (n→x).

**Interpretation.**

- **The video decoder can cap light models.** On `RPi5B_M1`, nano through large all
  land at ~77 fps regardless of model size — the **software** H.264 decoder
  (`avdec_h264`), not the NPU, is the ceiling for light models. Boards with hardware
  decoders (`vaapidecodebin`, `vah264dec`, `mppvideodec`) do not hit this wall until
  much higher rates.
- **For heavy models the NPU becomes the ceiling again** and end-to-end FPS tracks the
  throughput ordering from [§5](#5-npu-compute-performance-model-level-throughput). On
  `RPi5B_M1` the x-large model runs at 48.9 fps end-to-end — below the ~77 fps decoder
  cap — because the NPU is now the slow part.
- **ONNX-Runtime ON vs OFF** for end-to-end is model- and host-dependent: on the ARM
  boards ON often wins for light models (the extra host post-processing overlaps with
  NPU idle time), while on the fast x86 boards the difference narrows or reverses.

---

## 8. Multi-Stream Channel Capacity

The maximum number of Full HD 30 fps streams each sustaining ≥30 fps.

**Object detection, maximum channels, v2.4.0 (better of ONNX-Runtime ON/OFF):**

| Environment | n | s | m | l | x |
|-------------|--:|--:|--:|--:|--:|
| BIOSTAR_H1-Quattro | 17 | 17 | 16 | 12 | 6 |
| DX-AIPlayer-N97_M1 | 6 | 5 | 3 | 2 | 1 |
| OrangePi5+_M1 | 3 | 3 | 3 | 2 | 1 |
| ROCK5B+_M1 | 4 | 4 | 2 | 2 | 1 |
| RPi5B_M1 | 2 | 2 | 2 | 2 | 1 |
| RPi5B_M1M | 2 | 2 | 1 | 1 | 0 |

> Source: `results/<env>/<v2.4.0 run>/multi_stream_results.json`, task =
> object_detection, `capacity_streams` at the 30 fps-per-channel threshold.

**Interpretation.** Channel capacity is the multi-stream generalization of end-to-end
FPS and inherits the same bottlenecks: the H1-Quattro's four chips give it a large
lead (up to 17 object-detection channels at nano), while single-M1 ARM boards land in
the 2–6 channel range depending on the host and cooling. `RPi5B_M1M` shows 0 channels
for x-large — the combination of the slower M1M SKU (§2.2) and thermal throttling
(§2.3) leaves it unable to sustain even one x-large stream at 30 fps. **Classification
is intentionally not measured for multi-stream**, because a 224×224 classifier is not
representative of real multi-stream video-analytics workloads and its end-to-end number
is decoder-bound (§2.4).

---

## 9. Performance Trend Across dx-all-suite Releases

The same environments were measured on three releases. Because each release also
recompiled the models (§2.1), this trend reflects the **combined** improvement of
runtime + firmware + recompiled model.

**Object detection throughput (fps), ONNX-Runtime OFF, across releases:**

| Environment | Size | v2.2.2 | v2.3.3 | v2.4.0 | Change (v2.2.2 → v2.4.0) |
|-------------|:----:|-------:|-------:|-------:|:------------------------:|
| BIOSTAR_H1-Quattro | m | 308.8 | 372.3 | 471.3 | **+52.6 %** |
| BIOSTAR_H1-Quattro | l | 230.6 | 273.1 | 352.8 | **+53.0 %** |
| BIOSTAR_H1-Quattro | x | 132.3 | 156.2 | 193.9 | **+46.6 %** |
| DX-AIPlayer-N97_M1 | m | 76.5 | 90.8 | 115.2 | +50.5 % |
| DX-AIPlayer-N97_M1 | l | 57.3 | 66.6 | 86.7 | +51.4 % |
| RPi5B_M1 | m | 76.3 | 90.3 | 119.1 | +56.1 % |
| RPi5B_M1 | l | 57.1 | 66.3 | 86.5 | +51.5 % |
| RPi5B_M1M | m | 52.5 | 62.4 | 72.4 | +37.8 % |
| RPi5B_M1M | x | 23.4 | 27.3 | 28.4 | +21.6 % |

> Source: `model_results.json` of each environment's v2.2.2 / v2.3.3 / v2.4.0 runs,
> task = object_detection, family = throughput, ORT OFF. Full 6-environment table is
> in the dashboard's **Version Trend** tab.

**Interpretation.** The NPU-bound models gained a consistent **~45–56%** from v2.2.2 to
v2.4.0 across every actively-cooled / M1 environment, and the gain is **monotonic**
(each release ≥ the previous). The `RPi5B_M1M` gains are smaller on the largest models
(+21.6% for x-large) precisely because its v2.4.0 run thermally throttled (§2.3) — the
module's *thermally-limited* result understates the true release-over-release
improvement. This is the clearest single argument for **upgrading to the latest
dx-all-suite release**: the same hardware runs materially faster.

---

## 10. Deployment Guidance by Environment

Practical guidance, grounded in the tables above (all v2.4.0).

- **BIOSTAR_H1-Quattro (4-chip x86 server).** The high-density choice: 16–17
  object-detection channels or 19 pose channels at nano. Actively cooled, so it holds
  its clock (0 throttled cells). Use it where channel density matters most.
- **DX-AIPlayer-N97_M1 (compact x86 AI box).** A balanced single-M1 appliance: 6
  object-detection / 7 pose channels at nano, with a hardware decoder and active
  cooling. Good general-purpose edge box.
- **ROCK5B+_M1 / OrangePi5+_M1 (ARM SBCs, single M1).** Capable single-NPU boards
  (3–4 object-detection, 5–7 pose channels at nano). Both are passively cooled, so for
  sustained heavy models add cooling to avoid the late-phase throttling in §2.3.
  OrangePi's v2.4.0 small-model numbers are provisional (§2.5).
- **RPi5B_M1 (Raspberry Pi 5, single M1).** Entry-level, viable for 1–2 channels of
  detection/segmentation. Note its **software** video decoder caps light-model
  end-to-end FPS around ~77 fps — a hardware-decode host removes that ceiling.
- **RPi5B_M1M (Raspberry Pi 5, M1M module).** The lowest tier here: the M1M SKU is
  ~30–40% slower than M1 on heavy models (§2.2) and this unit additionally throttled
  (§2.3). Size deployments conservatively and treat its heavy-model numbers as a floor.

**General rules of thumb:**
- Plan NPU capacity from the **m/l/x throughput** numbers — they are host-portable
  (§5.1). Reserve nano/small for cases where you have verified your host CPU keeps up.
- If you need standard, ready-to-use model output, use **ONNX-Runtime ON**; if you can
  post-process the raw NPU output yourself and want maximum speed, use **OFF** (§3).
- For sustained multi-stream on passively-cooled boards, budget for cooling or expect
  the throttled numbers, not the peak ones.

---

## 11. Appendix

### 11.1 Reproducing the Benchmark

From the `dx-benchmark/` directory (see the tool's `README.md` for setup):

```bash
# Check the environment and print a fingerprint
./run.sh preflight

# Preview the benchmark matrix without running
./run.sh dry-run

# Run the full suite (model-level + end-to-end + multi-stream)
./run.sh run

# Run only specific sizes / task
./run.sh run --sizes n,s --task object_detection

# Rerun only failed items from an existing result directory
./run.sh run --resume results/<env>/<run_id> --retry-failed

# Rebuild the dashboard from all results
./run.sh dashboard results
```

### 11.2 Measurement Protocol — Key Parameters

| Parameter | Value |
|-----------|-------|
| Throughput measurement duration | 30 seconds |
| Latency loop count | 300 loops (single-core synchronous) |
| Throughput repetitions | 3 |
| End-to-end repetitions | 3 |
| Warm-up runs | 1 (discarded) |
| Multi-stream per-channel threshold | 30 fps |
| Thermal hot-start block | 60 °C (run rejected above this) |
| Cooldown target before each model | min(idle + 10 °C, 55 °C) |
| Video input | Full HD (1920×1080), 30 fps |

### 11.3 Detailed Results by Environment (latest release)

Full machine-readable results for each environment's latest (v2.4.0) run:

| Environment | Report |
|-------------|--------|
| BIOSTAR_H1-Quattro | [`results/BIOSTAR_H1-Quattro/20260710_180653/REPORT.md`](../results/BIOSTAR_H1-Quattro/20260710_180653/REPORT.md) |
| DX-AIPlayer-N97_M1 | [`results/DX-AIPlayer-N97_M1/20260710_180416/REPORT.md`](../results/DX-AIPlayer-N97_M1/20260710_180416/REPORT.md) |
| OrangePi5+_M1 | [`results/OrangePi5+_M1/20260713_132657/REPORT.md`](../results/OrangePi5+_M1/20260713_132657/REPORT.md) |
| ROCK5B+_M1 | [`results/ROCK5B+_M1/20260710_090255/REPORT.md`](../results/ROCK5B+_M1/20260710_090255/REPORT.md) |
| RPi5B_M1 | [`results/RPi5B_M1/20260713_115536/REPORT.md`](../results/RPi5B_M1/20260713_115536/REPORT.md) |
| RPi5B_M1M | [`results/RPi5B_M1M/20260710_180022/REPORT.md`](../results/RPi5B_M1M/20260710_180022/REPORT.md) |

Each environment also has v2.2.2 and v2.3.3 runs under `results/<env>/`; the
interactive dashboard (`results/dashboard/index.html`) lets you compare any
environment / version / task / size / ONNX-Runtime combination.

### 11.4 Glossary

| Term | Meaning |
|------|---------|
| **NPU (Neural Processing Unit)** | The DEEPX accelerator that runs the neural network (M1 / M1M module, or H1-Quattro 4-chip card) |
| **Throughput** | Sustained multi-core asynchronous NPU frame rate from `run_model` (pure NPU compute) |
| **Latency** | Single-frame, single-core inference time (responsiveness) |
| **End-to-end FPS** | Full video-pipeline frame rate (decode → preprocess → NPU → post-process) |
| **Maximum channels** | Most simultaneous streams each sustaining ≥30 fps |
| **ONNX-Runtime ON/OFF (ORT)** | ON = leftover post-processing layers run on the host CPU via ONNX Runtime (standard output); OFF = raw NPU output only (faster, needs a custom post-processor) |
| **Thermal throttling** | NPU clock reduction under high temperature (roughly 85–90 °C) |
| **Coefficient of variation** | Standard deviation ÷ mean, expressed as a percent — used here to quantify cross-host spread |

---

*Generated from the `dx-benchmark` tool's committed measurement data
(`dx-benchmark/results/`). To regenerate the underlying numbers or explore them
interactively, see [§11.1](#111-reproducing-the-benchmark) and the dashboard.*
