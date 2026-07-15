# YOLO26 × DEEPX NPU — 벤치마크 분석 (Beta)

> **Beta 안내.** 이 보고서는 현재 `dx-benchmark/results/`에 커밋된 측정 데이터
> —**6개 hardware 환경 × 3개 dx-all-suite 릴리스(v2.2.2, v2.3.3, v2.4.0) = 18개
> 벤치마크 run**—로부터 생성되었습니다. 모든 측정은 **동일한 tool과 동일한
> protocol**로 수행되었으므로, 환경 간 비교와 버전 간 비교 모두 동일 조건 비교입니다.
> 일부 cell에는 알려진 측정 caveat(passive cooling board의 thermal throttling,
> 몇몇 host 측 이상치)이 있으며, 이는 숨기지 않고 [§2 알려진 한계](#2-알려진-한계-beta)에
> 명시했습니다. flag가 붙은 환경의 수치는 **잠정치(provisional)**이며 통제된 조건에서
> 재측정 예정입니다.
>
> **이 보고서의 모든 수치는 추적 가능합니다.** 각 표는 정확한 출처 좌표—환경,
> dx-all-suite 버전, task, model size, ONNX-Runtime mode—를 명시하므로, 어떤 값이든
> raw `results/<env>/<run_id>/*_results.json` 파일이나 interactive dashboard로 직접
> fact-check 할 수 있습니다.

---

## 목차

1. [요약](#1-요약)
2. [알려진 한계 (Beta)](#2-알려진-한계-beta)
3. [무엇을 측정했는가 — 용어와 방법](#3-무엇을-측정했는가--용어와-방법)
4. [실험 환경](#4-실험-환경)
5. [NPU 연산 성능 (Model-Level Throughput)](#5-npu-연산-성능-model-level-throughput)
6. [Inference Latency](#6-inference-latency)
7. [End-to-End 영상 파이프라인 (Single Stream)](#7-end-to-end-영상-파이프라인-single-stream)
8. [Multi-Stream 채널 수용량](#8-multi-stream-채널-수용량)
9. [dx-all-suite 릴리스별 성능 추이](#9-dx-all-suite-릴리스별-성능-추이)
10. [환경별 배포 가이드](#10-환경별-배포-가이드)
11. [부록](#11-부록)

---

## 1. 요약

아래 표는 각 환경에서 **가장 가벼운(nano) model**을 **최신 릴리스(dx-all-suite
v2.4.0)**로 실행했을 때의 **실사용 성능**을, **Full HD(1920×1080) 30 fps** 영상을
입력으로 하여 보여줍니다. 각 cell은 두 ONNX-Runtime mode(ON / OFF —
[§3](#3-무엇을-측정했는가--용어와-방법)에서 설명) 중 **더 좋은 쪽**을 표시합니다. 형식은
**`end-to-end FPS / 최대 동시 채널 수`**이며, 채널은 30 fps 이상을 유지하는 하나의
영상 stream입니다. Classification은 FPS만 표시합니다(multi-stream 미측정 —
[§8](#8-multi-stream-채널-수용량) 참조).

| 환경 | Object Detection | Pose Estimation | Segmentation | Oriented Bounding Box | Classification |
|------|------------------|-----------------|--------------|-----------------------|----------------|
| **BIOSTAR_H1-Quattro** | 478.1 fps / 17 ch | 534.8 fps / 19 ch | 344.7 fps / 11 ch | 367.1 fps / 13 ch | 747.7 fps |
| **DX-AIPlayer-N97_M1** | 181.4 fps / 6 ch | 195.1 fps / 7 ch | 106.7 fps / 3 ch | 98.3 fps / 3 ch | 278.3 fps |
| **OrangePi5+_M1** | 112.3 fps / 3 ch | 170.9 fps / 5 ch | 83.8 fps / 2 ch | 86.6 fps / 2 ch | 944.1 fps |
| **ROCK5B+_M1** | 140.6 fps / 4 ch | 234.0 fps / 7 ch | 85.9 fps / 2 ch | 101.9 fps / 3 ch | 975.3 fps |
| **RPi5B_M1** | 77.2 fps / 2 ch | 108.0 fps / 3 ch | 52.8 fps / 1 ch | 78.3 fps / 2 ch | 182.2 fps |
| **RPi5B_M1M** | 67.0 fps / 2 ch | 99.8 fps / 3 ch | 46.6 fps / 1 ch | 60.5 fps / 1 ch | 175.3 fps |

> 출처: `results/<env>/<v2.4.0 run>/`, task = 각 열, size = `n`(nano),
> ONNX-Runtime = ON/OFF 중 우수값. End-to-end FPS는 `pipeline_results.json`,
> 채널 수는 `multi_stream_results.json`.

**세 가지 핵심 결과** (각각 뒤에서 출처 데이터와 함께 상세히 설명):

1. **DEEPX M1 NPU는 매우 다른 host CPU에서도 거의 동일한 연산 성능을 낸다.**
   NPU가 병목인 medium/large/x-large model에서는, 네 대의 single-M1 머신(Intel N97,
   Rockchip OrangePi, Rockchip ROCK5B, Raspberry Pi 5)이 약 1% 이내로 일치합니다
   ([§5](#5-npu-연산-성능-model-level-throughput)). DEEPX NPU가 성능의 기준점이며,
   host는 주로 가장 가벼운 model과 그 주변 영상 pipeline에만 영향을 줍니다.
2. **v2.2.2 → v2.4.0에서 성능이 약 45–56% 향상**되었으며, NPU-bound model에서
   모든 환경에 걸쳐 일관되게 나타납니다
   ([§9](#9-dx-all-suite-릴리스별-성능-추이)).
3. **H1-Quattro card는 4개의 NPU chip 수에 거의 선형적으로 확장**됩니다 — NPU-bound
   작업에서 single M1의 약 4.0배 ([§5](#5-npu-연산-성능-model-level-throughput)).

---

## 2. 알려진 한계 (Beta)

특정 수치 하나로 결론을 내리기 전에 반드시 읽어 주세요. 아래 내용은 이 데이터셋
뒤에 있는 raw log와 profiler trace를 전수 분석한 결과입니다.

### 2.1 버전 추이는 runtime만이 아니라 세 가지가 합쳐진 결과다

각 dx-all-suite 릴리스는 **그 릴리스의 compiler로 재컴파일한 model binary**로
측정되었습니다. 따라서 릴리스 간 변화는 **runtime + firmware + 재컴파일된 model**이
함께 반영된 결과이며, 순수 runtime만의 변화가 아닙니다. 이것이
[§9](#9-dx-all-suite-릴리스별-성능-추이)의 정직한 해석입니다: "이 model에 대해
v2.4.0이 end-to-end로 v2.2.2보다 ~50% 빠르다"이지 "runtime만 50% 빨라졌다"가
아닙니다.

### 2.2 M1과 M1M은 서로 다른 제품 — 절대 수치를 섞지 말 것

`RPi5B_M1`과 `RPi5B_M1M`은 **동일한 Raspberry Pi 5 host**에 **서로 다른 두 DEEPX
module**을 장착한 것입니다. NPU-bound model에서 M1M은 확연히 느립니다. 동일 host,
동일 릴리스(v2.4.0), object detection, ONNX-Runtime OFF 기준 —

| Size | RPi5B_M1 throughput | RPi5B_M1M throughput | M1M ÷ M1 |
|------|--------------------:|---------------------:|:--------:|
| m | 119.1 fps | 72.4 fps | 0.61 |
| l | 86.5 fps | 57.7 fps | 0.67 |
| x | 48.6 fps | 28.4 fps | 0.59 |

> 출처: `results/RPi5B_M1/20260713_115536/`, `results/RPi5B_M1M/20260710_180022/`,
> `model_results.json`, family = `throughput`, ORT OFF.

M1M은 실제로 구별되는, ~30–40% 더 느린 SKU입니다(둘 다 1000 MHz에 도달하므로 clock
차이가 아니라 architecture 차이). Dashboard와 이 보고서는 둘을 별개 환경으로
유지합니다. **M1과 M1M을 평균 내지 마세요.**

### 2.3 Passive cooling board는 후반 test 단계에서 thermal throttling이 발생한다

Protocol은 각 model을 latency → throughput → end-to-end → multi-stream 순서로
실행하며, 이 과정에서 NPU가 점진적으로 가열됩니다. active cooling이 없는 board에서는
*후반*(end-to-end / multi-stream) 단계에서 NPU가 thermal 한계에 도달해 clock을
낮출 수 있습니다. 이는 *같은* cell의 앞선 throughput 수치보다 end-to-end 수치가 더
나빠 보이는 형태로 나타나며, software regression이 아니라 실제 thermal 동작입니다.
Throttling된 cell은 dashboard에서 clock badge로 표시됩니다.

| 환경 (v2.4.0) | Model-level throttled cell | End-to-end ≥80 °C cell | 최고 NPU 온도 |
|---------------|:--------------------------:|:----------------------:|:-------------:|
| BIOSTAR_H1-Quattro (active cooling) | 0 | 0 | 73 °C |
| DX-AIPlayer-N97_M1 | 0 | 16 | 84 °C |
| ROCK5B+_M1 | 13 | 24 | 84 °C |
| RPi5B_M1M | 27 | 33 | 88 °C |

> 출처: 각 v2.4.0 run의 `model_results.json`, `pipeline_results.json` 내 cell별
> `npu_throttled` / `npu_temp_max_c`. N97은 높은 온도에 도달하지만 active cooling이
> clock을 유지하므로 *model-level* cell은 거의 throttling되지 않습니다.

### 2.4 일부 지표는 NPU-bound가 아니라 host-bound다 — 그에 맞게 해석할 것

- **Latency**(단일 frame 시간)는 부분적으로 host CPU와 PCIe/USB interconnect에 의해
  좌우됩니다. 동일 M1, 동일 v2.4.0, object detection nano에서 `OrangePi5+_M1`은
  42.9 ms, `RPi5B_M1`은 21.2 ms로 2배 차이가 나는데, 이는 NPU 특성이 아니라 host
  특성입니다 ([§6](#6-inference-latency)).
- **nano/small throughput**도 부분적으로 host-CPU-bound입니다(v2.4.0 기준 환경 간
  편차 ~10–19%, 반면 큰 model은 ~1% — [§5](#5-npu-연산-성능-model-level-throughput)).
- **Classification end-to-end FPS**는 NPU가 아니라 host 영상 decoder가 지배합니다.
  classification model은 매우 작아서(224×224 입력) NPU 부하가 거의 없고, 이 가벼운
  부하 상황에서는 ARM board의 hardware decoder가 x86 board의 decoder 경로보다 더 많은
  decode frame을 밀어낼 수 있습니다. Classification end-to-end FPS는 NPU 성능 지표가
  아니라 *pipeline/decoder* 지표로 해석하세요.

### 2.5 재측정 backlog가 있는 환경 (잠정 데이터)

- **OrangePi5+_M1, v2.4.0 — small-model host regression.** nano throughput이
  226.0 fps(v2.3.3)에서 164.6 fps(v2.4.0)로 *하락*했는데, 다른 모든 M1 host는
  향상되었습니다. nano latency도 35.5 ms → 42.9 ms로 상승했습니다. 해당 run의
  profiler에서 host CPU와 NPU가 모두 미포화 상태(host-side stall 서명)로 나타나므로,
  이는 v2.4.0 stack의 regression이 아니라 환경/host artifact입니다. CPU governor를
  `performance`로 고정하고 background load 없이 재측정 예정.
- **RPi5B_M1M, v2.4.0 — 심각한 thermal throttling** (§2.3 참조): model-level 27개
  + end-to-end 33개 cell이 최대 88 °C에서 throttling. medium/large/x-large
  throughput, end-to-end FPS, 채널 수용량이 억제되어 있으므로 module의 상한이 아니라
  *thermal 제한 하한*으로 간주해야 합니다. cooling/power 개선 후 재측정 예정.
- **Firmware 참고:** `BIOSTAR_H1-Quattro` v2.2.2 run은 firmware v2.5.6을 사용했고,
  다른 모든 v2.2.2 run은 v2.5.0을 사용했습니다. 이는 주로 해당 환경 버전 추이의
  v2.2.2 시작점에 영향을 줄 뿐 v2.4.0 headline 수치에는 영향이 없습니다.

---

## 3. 무엇을 측정했는가 — 용어와 방법

이 절은 이후에 쓰이는 모든 용어를 풀어서 정의합니다.

**NPU (Neural Processing Unit).** 신경망을 실행하는 DEEPX accelerator(module `M1`
또는 `M1M`, 혹은 4-chip `H1-Quattro` card). nominal core clock은 1000 MHz입니다.

**ONNX-Runtime mode (ORT ON / OFF).** DEEPX가 컴파일한 model은 신경망의 일부(주로
마지막 post-processing layer)를 NPU 밖에 남길 수 있습니다.
- **ONNX-Runtime ON**은 그 남은 부분을 ONNX Runtime library로 **host CPU**에서
  실행하여, 출력이 원본 ONNX model과 정확히 일치합니다(표준, 바로 사용 가능한 출력).
- **ONNX-Runtime OFF**는 **raw NPU 출력만** 반환합니다(host post-processing 없음).
  더 빠르지만 application에 model별 post-processor가 필요합니다.

  ONNX-Runtime ON은 host CPU 작업을 추가하므로, 매우 빠른 NPU에서 작은 model을 돌릴
  때는 CPU 단계가 병목이 되어 ON이 OFF보다 *느려질* 수 있습니다. 예: object detection
  nano, `BIOSTAR_H1-Quattro` v2.4.0에서 ONNX-Runtime OFF는 1285.0 fps, ON은
  972.1 fps(−24%). 두 mode를 항상 함께 보고하므로, application이 표준 post-processing
  출력을 필요로 하는지에 따라 선택할 수 있습니다.

**Throughput (model-level, FPS).** DEEPX `run_model` tool이 NPU를 **모든 core에서
비동기(asynchronous)**로 30초간 실행해 얻는 지속 frame rate. 영상 decode나 그리기가
전혀 없는, **NPU 연산 능력**의 가장 순수한 척도입니다.

**Latency (ms).** **단일 frame** 시간으로, **single-core / synchronous**
(`run_model` 300-loop mode)로 측정합니다. host↔NPU 왕복을 포함한 한 번의 inference
호출 반응성을 반영합니다.

**End-to-end FPS.** decode → preprocess → NPU inference → post-process로 이어지는
**전체 GStreamer 영상 pipeline**의 frame rate로, DEEPX dx_stream element를 통해
측정합니다. 실제 영상 분석 application이 체감하는 값입니다.

**최대 채널 수 (Maximum channels).** **모든** stream이 여전히 최소 30 fps를 유지하는
가장 큰 동시 영상 stream 수(채널당 threshold). stream 수를 늘려 가며 한 stream이 30
fps 아래로 떨어지는 지점을 찾는 boundary search로 구합니다.

**Model size.** YOLO26는 다섯 가지 size로 제공됩니다 — `n`(nano) < `s`(small) <
`m`(medium) < `l`(large) < `x`(extra-large). 큰 model일수록 정확하지만 느립니다.

**입력 해상도.** object detection·pose·segmentation은 640×640, oriented bounding
box는 1024×1024, classification은 224×224를 사용합니다. 모든 영상 입력은 Full
HD(1920×1080) 30 fps입니다.

**반복 횟수.** latency = 300-loop 1회, throughput = 30초 × 3회 평균, end-to-end =
3회 평균. 각각에 앞서 warm-up 1회를 실행하고 버립니다. 전체 protocol parameter는
[부록](#11-부록) 참조.

---

## 4. 실험 환경

4-chip x86 server부터 Raspberry Pi 5까지, 각각 DEEPX NPU를 장착한 6개 환경입니다.
환경 이름(이 보고서와 dashboard 전반에서 식별 key로 사용)은 host와 NPU module을
인코딩합니다.

| 환경 | Host CPU | Arch | RAM | DEEPX NPU | Chip | 비고 |
|------|----------|:----:|----:|-----------|:----:|------|
| **BIOSTAR_H1-Quattro** | AMD Ryzen 5 9600X (6-core) | x86_64 | 30.5 GB | H1-Quattro card | 4 | Active cooling; 여기서 성능 상한 |
| **DX-AIPlayer-N97_M1** | Intel N97 | x86_64 | 7.5 GB | M1 module | 1 | 소형 x86 AI box, active cooling |
| **OrangePi5+_M1** | Rockchip (Cortex-A55) | aarch64 | 15.6 GB | M1 module | 1 | ARM SBC; §2.5 v2.4.0 caveat 참조 |
| **ROCK5B+_M1** | Rockchip (Cortex-A76/A55) | aarch64 | 7.8 GB | M1 module | 1 | ARM SBC; passive cooling → 후반 throttle |
| **RPi5B_M1** | Broadcom (Cortex-A76) | aarch64 | 7.9 GB | M1 module | 1 | Raspberry Pi 5; software 영상 decode |
| **RPi5B_M1M** | Broadcom (Cortex-A76) | aarch64 | 7.9 GB | **M1M** module | 1 | 위와 동일 Pi host, 더 느린 M1M SKU (§2.2) |

모든 NPU는 nominal 1000 MHz로 동작합니다. 환경 × 릴리스별 software stack:

| 환경 | 릴리스 | Runtime | Firmware | RT driver | PCIe driver | dx_stream |
|------|:------:|:-------:|:--------:|:---------:|:-----------:|:---------:|
| BIOSTAR_H1-Quattro | v2.2.2 | v3.2.0 | v2.5.6 | v2.1.0 | v2.0.1 | 3.1.0 |
| BIOSTAR_H1-Quattro | v2.3.3 | v3.3.2 | v2.5.6 | v2.4.1 | v2.2.0 | 3.1.0 |
| BIOSTAR_H1-Quattro | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |
| DX-AIPlayer-N97_M1 | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |
| OrangePi5+_M1 | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |
| ROCK5B+_M1 | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |
| RPi5B_M1 | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |
| RPi5B_M1M | v2.4.0 | v3.4.0 | v2.7.1 | v2.5.1 | v2.4.1 | 3.1.0 |

> 출처: 각 run의 `environment.json`. 5개 single-M1 환경의 v2.3.3·v2.2.2 행은
> BIOSTAR와 동일한 runtime/firmware 패턴을 따릅니다(v2.3.3 → runtime v3.3.2 /
> firmware v2.5.6; v2.2.2 → runtime v3.2.0 / firmware v2.5.0, 단 §2.5의 BIOSTAR
> firmware 예외). 전체 run별 값은 각 `environment.json`에 있습니다.

---

## 5. NPU 연산 성능 (Model-Level Throughput)

**DEEPX NPU의 가장 순수한 척도**입니다 — `run_model`의 지속 multi-core throughput,
경로에 영상 decode나 그리기가 없습니다.

**Object detection throughput (fps), ONNX-Runtime OFF, 최신 릴리스(v2.4.0):**

| 환경 | n | s | m | l | x |
|------|--:|--:|--:|--:|--:|
| BIOSTAR_H1-Quattro | 1285.0 | 774.6 | 471.3 | 352.8 | 193.9 |
| DX-AIPlayer-N97_M1 | 235.9 | 193.4 | 115.2 | 86.7 | 47.6 |
| OrangePi5+_M1 | 164.6 | 147.3 | 115.8 | 88.8 | 48.0 |
| ROCK5B+_M1 | 264.7 | 194.9 | 116.2 | 86.6 | 47.3 |
| RPi5B_M1 | 179.0 | 172.8 | 119.1 | 86.5 | 48.6 |
| RPi5B_M1M | 178.2 | 148.7 | 72.4 | 57.7 | 28.4 |

> 출처: `results/<env>/<v2.4.0 run>/model_results.json`, task = object_detection,
> family = throughput, `use_ort` = false.

### 5.1 NPU가 기준점이다: 네 host에서 medium/large/x-large가 거의 동일

네 대의 single-M1 머신에서, NPU가 병목인 medium 이상 model은 놀랄 만큼 근접합니다:

| Size | N97 | OrangePi | ROCK5B | RPi5B_M1 | 평균 | 편차 (coefficient of variation) |
|------|----:|---------:|-------:|---------:|-----:|:-------------------------------:|
| m | 115.2 | 115.8 | 116.2 | 119.1 | 116.6 | **1.3 %** |
| l | 86.7 | 88.8 | 86.6 | 86.5 | 87.2 | **1.1 %** |
| x | 47.6 | 48.0 | 47.3 | 48.6 | 47.9 | **1.0 %** |
| s | 193.4 | 147.3 | 194.9 | 172.8 | 177.1 | 10.9 % |
| n | 235.9 | 164.6 | 264.7 | 179.0 | 211.1 | 19.4 % |

> 출처: 위 object-detection v2.4.0 ORT-OFF 표. coefficient of variation = 네 M1
> host에 걸친 표준편차 ÷ 평균.

**해석.** m/l/x에서 coefficient of variation은 ~1%로, host의 영향이 거의 없습니다.
DEEPX NPU가 사실상 모든 작업을 수행하고 그 module이 동일하기 때문입니다. nano/small
에서는 편차가 11–19%로 커지는데, 이 model들이 너무 빨리 끝나서 NPU에 데이터를
공급하는 **host CPU**가 병목의 일부가 되기 때문입니다(그리고 한 host — v2.4.0의
OrangePi — 는 §2.5의 host-side 이상까지 겹칩니다). 용량 산정 시 요점: **배포 규모는
host 간 이식성이 좋은 m/l/x 수치로 잡고, nano/small 수치는 host CPU에 의존한다는 점을
감안하세요.**

### 5.2 H1-Quattro는 4개 chip으로 ~4× 확장

H1-Quattro card는 4개의 NPU chip을 가집니다. NPU-bound 작업에서 single M1의 4배에
근접합니다:

| Object detection (v2.4.0, ORT OFF) | H1-Quattro | M1 평균 | 배율 |
|------------------------------------|-----------:|--------:|:----:|
| m | 471.3 | 116.6 | 4.04× |
| l | 352.8 | 87.2 | 4.05× |
| x | 193.9 | 47.9 | 4.05× |

> 출처: object-detection v2.4.0 ORT-OFF 표(§5); M1 평균은 네 M1 host 평균.

### 5.3 Task 난이도 순서는 일관적

무거운 post-processing과 큰 입력은 throughput을 깎습니다. medium size, v2.4.0,
ONNX-Runtime OFF에서 순서는 모든 환경에서 동일합니다(`BIOSTAR_H1-Quattro` /
`RPi5B_M1` 값):

- Classification (224×224, 단순 head): 5470.5 / 1369.1 fps
- Object detection (640×640): 471.3 / 119.1 fps
- Pose estimation (640×640): 458.4 / 114.4 fps
- Segmentation (640×640, mask 출력): 321.5 / 78.6 fps
- Oriented bounding box (1024×1024, 최대 입력): 166.0 / 40.9 fps

> 출처: `model_results.json`, size = m, family = throughput, ORT OFF, 명시된 두
> 환경의 v2.4.0 run.

---

## 6. Inference Latency

Latency는 단일 frame·single-core 시간으로 **반응성** 지표이며 부분적으로
**host/interconnect-bound**입니다.

**Object detection latency (ms), ONNX-Runtime OFF, v2.4.0:**

| 환경 | n | s | m | l | x |
|------|--:|--:|--:|--:|--:|
| BIOSTAR_H1-Quattro | 10.45 | 16.27 | 23.35 | 30.46 | 56.17 |
| DX-AIPlayer-N97_M1 | 23.00 | 29.82 | 37.09 | 44.21 | 69.94 |
| OrangePi5+_M1 | 42.88 | 49.90 | 59.03 | 64.89 | 92.06 |
| ROCK5B+_M1 | 36.17 | 43.31 | 49.47 | 58.77 | 91.68 |
| RPi5B_M1 | 21.19 | 27.07 | 34.84 | 40.80 | 68.39 |
| RPi5B_M1M | 24.14 | 29.60 | 38.56 | 46.10 | 75.43 |

> 출처: `results/<env>/<v2.4.0 run>/model_results.json`, task = object_detection,
> family = latency, ORT OFF.

**해석.** throughput과 달리 latency는 M1 host 간에 크게 달라집니다(nano:
RPi5B_M1 21.2 ms vs OrangePi5+_M1 42.9 ms — *동일 NPU module·릴리스*에서 2배 차이).
단일 synchronous 호출은 raw NPU 연산이 아니라 host CPU와 host↔NPU interconnect가
지배하기 때문입니다. 단일 요청 반응성은 **당신의** host에서 latency로 판단하고, NPU
용량은 throughput([§5](#5-npu-연산-성능-model-level-throughput))으로 판단하세요.

---

## 7. End-to-End 영상 파이프라인 (Single Stream)

End-to-end FPS는 단일 Full HD 30 fps stream에서 전체 pipeline(decode →
preprocess → NPU → post-process)을 측정합니다 — 실제 application이 보는 값입니다.

**Object detection end-to-end FPS, v2.4.0, ONNX-Runtime mode별:**

| 환경 | ORT | n | s | m | l | x | 영상 decoder |
|------|:---:|--:|--:|--:|--:|--:|--------------|
| BIOSTAR_H1-Quattro | ON | 478.1 | 475.7 | 476.6 | 367.3 | 200.1 | vaapidecodebin (HW) |
| DX-AIPlayer-N97_M1 | OFF | 181.4 | 163.8 | 116.0 | 85.8 | 45.2 | vah264dec (HW) |
| OrangePi5+_M1 | ON | 112.3 | 95.4 | 78.3 | 68.3 | 47.1 | mppvideodec (HW) |
| ROCK5B+_M1 | ON | 140.6 | 132.6 | 94.9 | 74.6 | 33.3 | mppvideodec (HW) |
| RPi5B_M1 | OFF | 77.2 | 77.5 | 76.8 | 76.2 | 48.9 | avdec_h264 (SW) |
| RPi5B_M1M | OFF | 67.0 | 66.6 | 56.5 | 50.1 | 15.8 | avdec_h264 (SW) |

> 출처: `results/<env>/<v2.4.0 run>/pipeline_results.json`, task = object_detection.
> 행별 ONNX-Runtime mode는 nano FPS가 더 높았던 쪽입니다("HW"/"SW"는 hardware/
> software 영상 decoder). 모든 환경의 두 mode 모두 raw 데이터와 dashboard에 있습니다.
> 참고로 BIOSTAR_H1-Quattro의 ONNX-Runtime OFF는 421.5 / 425.0 / 424.9 / 367.7 /
> 200.4 fps(n→x)입니다.

**해석.**

- **영상 decoder가 가벼운 model을 제한할 수 있다.** `RPi5B_M1`에서는 nano부터
  large까지 model size와 무관하게 모두 ~77 fps에 수렴합니다 — 가벼운 model에서는
  NPU가 아니라 **software** H.264 decoder(`avdec_h264`)가 상한입니다. hardware
  decoder(`vaapidecodebin`, `vah264dec`, `mppvideodec`)를 쓰는 board는 훨씬 높은
  rate까지 이 벽에 부딪히지 않습니다.
- **무거운 model에서는 다시 NPU가 상한**이 되어 end-to-end FPS가
  [§5](#5-npu-연산-성능-model-level-throughput)의 throughput 순서를 따릅니다.
  `RPi5B_M1`에서 x-large는 end-to-end 48.9 fps로 ~77 fps decoder 상한 아래인데,
  이제 NPU가 느린 부분이기 때문입니다.
- **ONNX-Runtime ON vs OFF**는 end-to-end에서 model·host 의존적입니다. ARM board
  에서는 가벼운 model에서 ON이 종종 유리하고(추가 host post-processing이 NPU idle
  시간과 겹침), 빠른 x86 board에서는 차이가 좁아지거나 역전됩니다.

---

## 8. Multi-Stream 채널 수용량

각 stream이 30 fps 이상을 유지하는 Full HD 30 fps stream의 최대 개수입니다.

**Object detection 최대 채널 수, v2.4.0 (ONNX-Runtime ON/OFF 중 우수):**

| 환경 | n | s | m | l | x |
|------|--:|--:|--:|--:|--:|
| BIOSTAR_H1-Quattro | 17 | 17 | 16 | 12 | 6 |
| DX-AIPlayer-N97_M1 | 6 | 5 | 3 | 2 | 1 |
| OrangePi5+_M1 | 3 | 3 | 3 | 2 | 1 |
| ROCK5B+_M1 | 4 | 4 | 2 | 2 | 1 |
| RPi5B_M1 | 2 | 2 | 2 | 2 | 1 |
| RPi5B_M1M | 2 | 2 | 1 | 1 | 0 |

> 출처: `results/<env>/<v2.4.0 run>/multi_stream_results.json`, task =
> object_detection, 30 fps/채널 threshold에서 `capacity_streams`.

**해석.** 채널 수용량은 end-to-end FPS의 multi-stream 일반화이며 같은 병목을
물려받습니다: H1-Quattro의 4개 chip이 큰 우위를 줍니다(nano object detection 최대 17
채널). single-M1 ARM board는 host와 cooling에 따라 2–6 채널 범위입니다.
`RPi5B_M1M`은 x-large에서 0 채널인데, 더 느린 M1M SKU(§2.2)와 thermal
throttling(§2.3)이 겹쳐 x-large 1 stream도 30 fps로 유지하지 못하기 때문입니다.
**Classification은 multi-stream에서 의도적으로 측정하지 않습니다.** 224×224
classifier는 실제 multi-stream 영상 분석 workload를 대표하지 않고, 그 end-to-end
수치는 decoder-bound이기 때문입니다(§2.4).

---

## 9. dx-all-suite 릴리스별 성능 추이

동일한 환경들을 세 릴리스에서 측정했습니다. 각 릴리스가 model도 재컴파일했으므로
(§2.1), 이 추이는 runtime + firmware + 재컴파일된 model의 **결합** 개선을 반영합니다.

**Object detection throughput (fps), ONNX-Runtime OFF, 릴리스별:**

| 환경 | Size | v2.2.2 | v2.3.3 | v2.4.0 | 변화 (v2.2.2 → v2.4.0) |
|------|:----:|-------:|-------:|-------:|:----------------------:|
| BIOSTAR_H1-Quattro | m | 308.8 | 372.3 | 471.3 | **+52.6 %** |
| BIOSTAR_H1-Quattro | l | 230.6 | 273.1 | 352.8 | **+53.0 %** |
| BIOSTAR_H1-Quattro | x | 132.3 | 156.2 | 193.9 | **+46.6 %** |
| DX-AIPlayer-N97_M1 | m | 76.5 | 90.8 | 115.2 | +50.5 % |
| DX-AIPlayer-N97_M1 | l | 57.3 | 66.6 | 86.7 | +51.4 % |
| RPi5B_M1 | m | 76.3 | 90.3 | 119.1 | +56.1 % |
| RPi5B_M1 | l | 57.1 | 66.3 | 86.5 | +51.5 % |
| RPi5B_M1M | m | 52.5 | 62.4 | 72.4 | +37.8 % |
| RPi5B_M1M | x | 23.4 | 27.3 | 28.4 | +21.6 % |

> 출처: 각 환경의 v2.2.2 / v2.3.3 / v2.4.0 run `model_results.json`, task =
> object_detection, family = throughput, ORT OFF. 전체 6개 환경 표는 dashboard의
> **Version Trend** 탭에 있습니다.

**해석.** NPU-bound model은 v2.2.2 → v2.4.0에서 모든 active-cooling / M1 환경에 걸쳐
일관되게 **~45–56%** 향상되었고, 그 향상은 **단조(monotonic)**입니다(각 릴리스 ≥ 이전
릴리스). `RPi5B_M1M`의 가장 큰 model 향상 폭이 작은 것(x-large +21.6%)은 v2.4.0 run이
thermal throttling되었기 때문(§2.3)으로, module의 *thermal 제한* 결과가 실제 릴리스
간 향상을 과소평가한 것입니다. 이것이 **최신 dx-all-suite 릴리스로 업그레이드**해야
하는 가장 분명한 근거입니다: 같은 hardware가 확연히 빨라집니다.

---

## 10. 환경별 배포 가이드

위 표들에 근거한 실무 가이드입니다(모두 v2.4.0).

- **BIOSTAR_H1-Quattro (4-chip x86 server).** 고밀도 선택지: nano에서 object
  detection 16–17 채널 또는 pose 19 채널. active cooling이라 clock을
  유지합니다(throttled cell 0). 채널 밀도가 가장 중요한 곳에 사용하세요.
- **DX-AIPlayer-N97_M1 (소형 x86 AI box).** 균형 잡힌 single-M1 appliance: nano에서
  object detection 6 / pose 7 채널, hardware decoder와 active cooling 보유. 범용
  edge box로 적합.
- **ROCK5B+_M1 / OrangePi5+_M1 (ARM SBC, single M1).** 유능한 single-NPU
  board(nano에서 object detection 3–4, pose 5–7 채널). 둘 다 passive cooling이므로,
  무거운 model을 지속 실행하려면 §2.3의 후반 throttling을 피하기 위해 cooling을
  추가하세요. OrangePi의 v2.4.0 small-model 수치는 잠정치입니다(§2.5).
- **RPi5B_M1 (Raspberry Pi 5, single M1).** 입문용으로, detection/segmentation 1–2
  채널에 적합. **software** 영상 decoder가 가벼운 model의 end-to-end FPS를 ~77 fps
  부근으로 제한한다는 점에 유의하세요 — hardware decode host는 이 상한을 없앱니다.
- **RPi5B_M1M (Raspberry Pi 5, M1M module).** 여기서 최하위 tier: M1M SKU는 무거운
  model에서 M1보다 ~30–40% 느리고(§2.2) 이 unit은 추가로 throttling되었습니다(§2.3).
  배포는 보수적으로 산정하고 무거운 model 수치는 하한으로 간주하세요.

**일반 원칙:**
- NPU 용량은 host 이식성이 좋은 **m/l/x throughput** 수치로 계획하세요(§5.1). nano/
  small은 host CPU가 따라오는지 검증한 경우에만 사용하세요.
- 표준·즉시 사용 가능한 model 출력이 필요하면 **ONNX-Runtime ON**을, raw NPU 출력을
  직접 post-processing 할 수 있고 최대 속도를 원하면 **OFF**를 사용하세요(§3).
- passive cooling board에서 지속 multi-stream을 하려면 cooling을 확보하거나, peak가
  아니라 throttled 수치를 기준으로 잡으세요.

---

## 11. 부록

### 11.1 벤치마크 재현

`dx-benchmark/` 디렉터리에서(설정은 tool의 `README.md` 참조):

```bash
# 환경 점검 + fingerprint 출력
./run.sh preflight

# 실행 없이 벤치마크 matrix 미리보기
./run.sh dry-run

# 전체 suite 실행 (model-level + end-to-end + multi-stream)
./run.sh run

# 특정 size / task만 실행
./run.sh run --sizes n,s --task object_detection

# 기존 결과 디렉터리에서 실패한 항목만 재실행
./run.sh run --resume results/<env>/<run_id> --retry-failed

# 전체 결과로부터 dashboard 재빌드
./run.sh dashboard results
```

### 11.2 측정 Protocol — 핵심 Parameter

| Parameter | 값 |
|-----------|-----|
| Throughput 측정 시간 | 30초 |
| Latency loop 수 | 300 loop (single-core synchronous) |
| Throughput 반복 | 3회 |
| End-to-end 반복 | 3회 |
| Warm-up run | 1회 (버림) |
| Multi-stream 채널당 threshold | 30 fps |
| Thermal hot-start 차단 | 60 °C (이상이면 run 거부) |
| model별 cooldown 목표 | min(idle + 10 °C, 55 °C) |
| 영상 입력 | Full HD (1920×1080), 30 fps |

### 11.3 환경별 상세 결과 (최신 릴리스)

각 환경의 최신(v2.4.0) run에 대한 machine-readable 상세 결과:

| 환경 | Report |
|------|--------|
| BIOSTAR_H1-Quattro | [`results/BIOSTAR_H1-Quattro/20260710_180653/REPORT.md`](../results/BIOSTAR_H1-Quattro/20260710_180653/REPORT.md) |
| DX-AIPlayer-N97_M1 | [`results/DX-AIPlayer-N97_M1/20260710_180416/REPORT.md`](../results/DX-AIPlayer-N97_M1/20260710_180416/REPORT.md) |
| OrangePi5+_M1 | [`results/OrangePi5+_M1/20260713_132657/REPORT.md`](../results/OrangePi5+_M1/20260713_132657/REPORT.md) |
| ROCK5B+_M1 | [`results/ROCK5B+_M1/20260710_090255/REPORT.md`](../results/ROCK5B+_M1/20260710_090255/REPORT.md) |
| RPi5B_M1 | [`results/RPi5B_M1/20260713_115536/REPORT.md`](../results/RPi5B_M1/20260713_115536/REPORT.md) |
| RPi5B_M1M | [`results/RPi5B_M1M/20260710_180022/REPORT.md`](../results/RPi5B_M1M/20260710_180022/REPORT.md) |

각 환경에는 `results/<env>/` 아래에 v2.2.2·v2.3.3 run도 있습니다. interactive
dashboard(`results/dashboard/index.html`)에서 임의의 환경 / 버전 / task / size /
ONNX-Runtime 조합을 비교할 수 있습니다.

### 11.4 용어집

| 용어 | 의미 |
|------|------|
| **NPU (Neural Processing Unit)** | 신경망을 실행하는 DEEPX accelerator(M1 / M1M module, 또는 H1-Quattro 4-chip card) |
| **Throughput** | `run_model`의 지속 multi-core asynchronous NPU frame rate (순수 NPU 연산) |
| **Latency** | 단일 frame·single-core inference 시간 (반응성) |
| **End-to-end FPS** | 전체 영상 pipeline frame rate (decode → preprocess → NPU → post-process) |
| **최대 채널 수** | 각 stream이 30 fps 이상을 유지하는 최대 동시 stream 수 |
| **ONNX-Runtime ON/OFF (ORT)** | ON = 남은 post-processing layer를 ONNX Runtime으로 host CPU에서 실행(표준 출력); OFF = raw NPU 출력만(더 빠름, 별도 post-processor 필요) |
| **Thermal throttling** | 고온(대략 85–90 °C)에서의 NPU clock 감소 |
| **Coefficient of variation** | 표준편차 ÷ 평균의 백분율 — 여기서는 host 간 편차 정량화에 사용 |

---

*`dx-benchmark` tool에 커밋된 측정 데이터(`dx-benchmark/results/`)로부터 생성됨.
기반 수치를 재생성하거나 interactive하게 탐색하려면 [§11.1](#111-벤치마크-재현)과
dashboard를 참조하세요.*
