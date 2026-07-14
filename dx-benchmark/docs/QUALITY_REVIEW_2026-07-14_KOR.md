# dx-benchmark 결과 품질 검토 & 진상 규명 (내부용)

> **INTERNAL — 배포 금지.** 이 문서는 `results/` 데이터를 전세계 개발자·DEEPX NPU
> 고객에게 공개하기 전, 품질 이슈·이상점·재측정 대상·근본원인을 정리한 **내부 검토
> 노트**다. 공개용 성능 보고서는 `ANALYSIS_EN.md` / `ANALYSIS_KOR.md`를 참조.

- **작성일**: 2026-07-14
- **대상**: `dx-benchmark/results/` — 6개 HW × 3개 dx-all-suite 버전(v2.2.2 / v2.3.3 / v2.4.0) = 18 run
- **방법**: 전 run CSV/JSON + raw 로그 + profiler 전수 분석. 판정은 실제 데이터 근거(물리 기반 교차검증). 추측 배제.

---

## 1. 핵심 결론 (TL;DR)

> **"v2.4.0에서 throughput/E2E 하락이 많다"는 소프트웨어 회귀가 아니다.** 대부분
> **① thermal throttling(지배적)** 과 **② OrangePi 유닛 환경 이슈**로 설명되며,
> **NPU peak throughput(model-level m/l/x)은 전 보드에서 일관 개선**됐다. 단,
> **버전마다 모델이 재컴파일**되어 트렌드는 "순수 runtime"이 아니라 "스택 전체"의 변화다.

공개 가능 여부: **NPU peak 지표는 즉시 공개 가능 수준**. sustained(E2E/multi) 지표는
**냉각 표준화 + 통제된 재측정 + thermal 명시**가 선행돼야 함.

---

## 2. 측정 매트릭스

각 HW가 아래 3개 버전으로 정확히 커버됨(version-trend 설계 자체는 양호).

| dx-all-suite | RT | driver | firmware | PCIe drv | 컴파일 모델 세트 |
|---|---|---|---|---|---|
| v2.2.2 | v3.2.0 | v2.1.0 | v2.5.0 | v2.0.1 | `models_dx_com220rc2/` (DX-COM 2.2.0rc2) |
| v2.3.3 | v3.3.2 | v2.4.1 | v2.5.6 | v2.2.0 | `models_dxnn_v2.3.0/` (DX-COM 2.3.0) |
| v2.4.0 | v3.4.0 | v2.5.1 | v2.7.1 | v2.4.1 | `assets/models/` (신규, `_640x640` 네이밍) |

HW: 단일칩 M1 4종(DX-AIPlayer-N97 / OrangePi5+ / ROCK5B+ / RPi5B), M1M 1종(RPi5B), H1-Quattro(4×M1=12코어) 1종.

---

## 3. 진상 규명 — 왜 v2.4.0에서 하락이 많아졌나 (3대 원인)

### 원인 A — Thermal throttling (지배적; E2E/multi 하락의 주범)

- **증거**: ROCK5B v2.4.0 E2E 회귀 6셀 **전부 `throttled=True`**. phase별 온도/클록:
  - model **throughput** phase(시퀀스상 먼저, 시원): 74~80°C, clock 800~1000 → fps **개선(+7~24%)**
  - **E2E** phase(뒤, 지속부하): **82~83°C**, clock **400MHz 급락** → e2e fps **하락(−12~−28%)**
- **메커니즘**: 측정 시퀀스 `latency→throughput→E2E→multi`가 NPU를 점진 가열. v2.4.0의
  더 빠른 NPU + 새 firmware DVFS가 **더 뜨겁게** 동작 → 냉각 여유 적은 보드(**ROCK5B,
  RPi5B_M1M**)가 후반 지속부하에서 throttle. 능동/충분 냉각(N97·BIOSTAR)·RPi5B(M1)는 **E2E 회귀 0**.
- **성격**: 측정 버그 아님, **실제 열 특성**. throttle flag가 정확히 포착함.

### 원인 B — OrangePi5+ 유닛의 host per-inference 지연 (소형모델)

- **증거**: OrangePi n(OD) single-inference latency **35.5ms(v2.3.3) → 42.9ms(v2.4.0), +21% 악화**.
  그러나 **동일 모델·RT의 ROCK5B(같은 RK3588 SoC)는 37→36ms 평평**. NPU clock 1000 정상(**throttle 아님**).
  throughput phase에서 **CPU 126% AND NPU util 40% 둘 다 미포화 = stall 신호**.
- **해석**: NPU 연산도·모델도·RT 자체도 아님 → **OrangePi 유닛/환경 특정** round-trip 지연.
  후보: CPU governor / background load / PCIe link state. (단, CPU가 미포화이므로 governor
  단독 원인일 가능성은 낮음.)
- **한계**: 그 run에 환경 정보가 기록되지 않아 **소급 규명 불가 → 통제된 재측정만이 유일한 규명 경로.**

### 원인 C — 구조적 confound: 버전마다 모델 재컴파일

- **증거**: `modelFile` 경로가 버전별로 다름(2장 표). v2.2.2 `models_dx_com220rc2/`,
  v2.3.3 `models_dxnn_v2.3.0/`, v2.4.0 `assets/models/`(신규 컴파일러).
- **함의**: 버전 트렌드 = runtime + firmware + **재컴파일 모델**의 통합 변화. "runtime이
  빨라졌다"가 아니라 **"스택 전체가 빨라졌다"**. 공개 시 이 프레이밍 필수(그리고 이게 고객에겐 올바른 관점).

---

## 4. 전체 경향성 (공개 가능한 좋은 스토리 + 단서)

| 지표 | 경향 | 대표 수치 | 공개 적합도 |
|---|---|---|---|
| **model throughput m/l/x** | 전 보드 일관 개선, cross-host **CV < 1.5%** | OD: m 76→91→116, l 57→66→87, x 33→38→48 fps (누적 **+45~52%**) | ✅ 최상급 |
| H1-Quattro 스케일 | M1 대비 정확히 **4×** | m 471 vs 116 (4.06×), l 353 vs 87 (4.07×) | ✅ |
| model throughput n/s | host-CPU-bound, 편차 큼 | cross-host CV n 4.5→9.8→**19.4%**, s 0.8→0.6→**10.9%** | ⚠ caveat |
| latency (전 사이즈) | host/interconnect-bound | CV **10~29%**, 동일 M1인데 OrangePi가 RPi5의 ~2× 느림 | ⚠ "NPU latency" 라벨 오해 |
| E2E / multi-stream | host-decode + **thermal** 종속 | RPi5 경량모델 E2E는 디코더 상한 ~65fps 고정 | ⚠ 조건 명시 |

> 단서: ROCK5B는 throughput phase에도 경미한 throttle(clock 800~1000)이 있었음 →
> **냉각을 개선하면 NPU 이득은 현재 수치보다 더 클 수** 있음(현 수치는 다소 과소평가).

**내부 정합성**(신뢰 근거): throughput ≥ latency 위반 0건, 스케일링 단조성 위반 1건(노이즈),
E2E > throughput 위반 2건(모두 손상된 OrangePi v2.2.2 run에 국한).

---

## 5. 이상점 & 재측정 필요 케이스 (우선순위)

회귀 스캔(v2.3.3→v2.4.0, >10% 하락): **model-throughput 회귀는 OrangePi(4, 소형, host)와
M1M(3, 대형, throttle)에만.** N97/ROCK5B/RPi5B/BIOSTAR = 회귀 0 + 광범위 개선.
E2E 회귀는 M1M(16, throttle) / OrangePi(8, host) / ROCK5B(6, thermal)에 집중.

| # | 케이스 | 원인 | 조치 | 우선 |
|---|---|---|---|---|
| 1 | **RPi5B_M1M v2.4.0** — throughput/E2E/max-ch 붕괴(l=0채널) | 심각 thermal throttle(88°C, clock 200MHz, throttle flag 100건) | 냉각/전력 개선 후 **재측정** | 🔴 |
| 2 | **OrangePi5+ v2.4.0** — 소형모델 host 지연(OD-n −27%, seg-n −44%, seg-s −14%, cls-n −16%) | 유닛/환경(미기록) | governor 고정 + 환경 통제 **재측정** | 🔴 |
| 3 | **OrangePi5+ v2.2.2** — 손상 run(error 16건, throughput CV 37.6%) | 측정 실패 | **전체 재측정** | 🔴 |
| 4 | **ROCK5B v2.4.0** — E2E 6셀 하락(−12~−28%) | E2E phase thermal throttle | 냉각 개선 재측정 **또는** thermal 명시 공개 | 🟠 |
| 5 | **RPi5B(M1·M1M)** — incident 15~21건/run | NPU IPC/GStreamer hang (온도 정상 42°C, thermal 아님) | 안정성(PCIe/전원) 점검 후 재측정; 그전엔 provisional 표기 | 🟠 |
| 6 | **M1M ≠ M1** — model-level ~25~40% 느린 **별개 SKU** (m: M1 90 vs M1M 62). 구버전 metadata에 `sku=M1` 오라벨 | 구 RT SKU 자동탐지 한계 | 대시보드/데이터에서 **M1/M1M 분리 표기**; 구 run sku backfill | 🟠 |
| 7 | **BIOSTAR v2.2.2 firmware 불일치** — fw v2.5.6(나머지 v2.2.2는 v2.5.0) | 환경 비일관 | 메타 명시 or 재측정 | 🟡 |
| 8 | **모델 재컴파일 confound**(원인 C) | 구조적 | 버전별 **컴파일러 버전 명시** | 🟡 |
| 9 | `results/_ab`, `results/_ab_lean` — 개발자 A/B scratch(`atd-yjsong_M1`) | 비공개 데이터 | 공개 트리에서 **제외**(미추적 유지) | 🟡 |

---

## 6. 도구 현황 & Roadmap

**완료(2026-07-14, 브랜치 `feat/dx-benchmark-suite-relocation`, push됨)**
- `40e981d4` **G2**: `npu_throttled` 정의를 `clock_min < nominal(1000)`으로 교정
  (기존 `min < 0.95×관측max`는 낮은 클록에 고정된 경우를 놓침). report-only, 측정값 무영향.
  기존 18 run 4035행 **0 flip**(마이그레이션 불필요). +`tests/test_npu_monitor.py`(5). 전체 78 passed.
- `d2b26806` 대시보드 suite-version 비교 + aggregator per-run SDK/throttle 메타데이터
  (host-bound/NPU-bound 자동 태깅, throttle·decoder 뱃지, per-point rt 버전 tooltip).
- `1eb171d2` v2.4.0 6개 환경 데이터 + HW 폴더 rename.

**남은 작업(제안)**
- **G1** (P0, 측정 위생): preflight에서 CPU governor **기록 + performance 아니면 `[WARN]`**,
  실제 강제는 `--cpu-governor performance` **opt-in 플래그**만(기본은 환경 변경 0). 재측정 시
  환경을 known-good로 고정·기록 → 재발 시 governor 배제/확정 가능. (OrangePi 진단 도구는 아님 — 위생용.)
- **G3** (P1): 결과 QA 게이트 — aggregate 시 자동으로 동일 SKU cross-host throughput CV,
  회귀↔throttle 상관, throughput 셀 NPU-util floor, incident-count 임계를 검사해 셀별
  `quality: ok|suspect|remeasure`를 `dataset.json`에 태깅 → 대시보드 필터 + "공개 가능 셀만".
- **G4** (P1): aggregator consistency guard에 **firmware 불일치**(동일 버전 cross-HW) 경고 추가.
- (의도적 폐기: derive-at-read 헬퍼 / schema_version 스탬프 / mixed-version compat 테스트 — 과잉설계.)

**측정 표준화(재측정 전 필수)**
- 냉각 조건 표준화(또는 run별 명시) — thermal이 최대 변수.
- 재측정 대상: #1·#2·#3(필수), #4·#5(권장).

---

## 7. 공개/배포 정책 권고

1. **NPU peak(model-level m/l/x throughput)을 clean 지표로 전면 공개.** sustained(E2E/multi)는
   **thermal 종속임을 명시**하고 냉각 조건을 병기.
2. **버전 트렌드에 컴파일러(DX-COM) 버전 표기** — "스택 전체" 개선임을 분명히(원인 C).
3. **M1 vs M1M 분리 표기.** latency는 "end-to-end single-inference latency"로 재라벨하거나 호스트별 제시.
4. **QA 게이트(G3) 통과 셀만 공개**, 미달 셀은 "재측정 예정" 표기.
5. `_ab`/`_ab_lean` scratch는 공개 트리에서 제외.

---

## 부록 — 핵심 근거 수치

- **OrangePi n(OD) throughput**: v2.3.3 226fps / util 90% / cpu 177% / 6774 loops(30s) →
  v2.4.0 164fps / util 40% / cpu 126% / 4944 loops. 모델: `yolo26n.dxnn`(v2.3.0) → `yolo26-n_640x640.dxnn`(신규).
- **OrangePi n latency**: 35.5ms → 42.9ms(+21%). ROCK5B 동일 조건 37.0 → 36.2ms(평평).
- **ROCK5B v2.4.0 thermal**: throughput phase seg-m 74.9fps@76-80°C(clk 800-1000) vs
  E2E phase seg-m 48.1fps@82-83°C(clk→400) throttled=True. (throughput은 v2.3.3 대비 +15%, E2E는 −24%.)
- **M1M vs M1**(동일 RPi5B 호스트, OD throughput ort_off): m 90/62, l 66/46, x 38/27 — M1M ~30% 낮음.
- **throttle flag 수**(model+e2e+multi): RPi5B_M1M v2.4.0 100건, ROCK5B v2.4.0 86건, N97 v2.4.0 56건 등
  v2.4.0에서 급증(더 뜨거운 동작 반영) — 단 clean한 m/l/x throughput phase는 대체로 미포착.
