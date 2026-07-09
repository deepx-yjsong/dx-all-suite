# YOLO26 Benchmark Report

**Generated:** 2026-07-01 15:49:17 (Local)

## Test Timing

| # | Type | Start | End | Duration |
|---|------|-------|-----|----------|
| 1 | run | 2026-07-01 11:37:56 | 2026-07-01 15:49:17 | 4h 11m 20s |

## Executive Summary

### Object Detection

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26n.dxnn | ON | 59.55 | 136.1 | — | — |
| yolo26n.dxnn | OFF | 34.89 | 138.3 | — | — |
| yolo26s.dxnn | ON | 71.95 | 97.2 | — | — |
| yolo26s.dxnn | OFF | 46.95 | 102.9 | — | — |
| yolo26m.dxnn | ON | 79.53 | 75.5 | — | — |
| yolo26m.dxnn | OFF | 53.60 | 76.4 | — | — |
| yolo26l.dxnn | ON | 90.08 | 57.1 | — | — |
| yolo26l.dxnn | OFF | 63.62 | 57.1 | — | — |
| yolo26x.dxnn | ON | 113.49 | 26.9 | — | — |
| yolo26x.dxnn | OFF | 95.79 | 32.7 | — | — |

### Pose Estimation

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26n-pose.dxnn | ON | 46.13 | 157.6 | — | — |
| yolo26n-pose.dxnn | OFF | 30.44 | 163.1 | — | — |
| yolo26s-pose.dxnn | ON | 54.52 | 102.0 | — | — |
| yolo26s-pose.dxnn | OFF | 38.76 | 102.3 | — | — |
| yolo26m-pose.dxnn | ON | 61.57 | 74.6 | — | — |
| yolo26m-pose.dxnn | OFF | 47.54 | 74.6 | — | — |
| yolo26l-pose.dxnn | ON | 76.00 | 56.0 | — | — |
| yolo26l-pose.dxnn | OFF | 56.50 | 56.0 | — | — |
| yolo26x-pose.dxnn | ON | 103.13 | 32.2 | — | — |
| yolo26x-pose.dxnn | OFF | 87.99 | 26.5 | — | — |

### Segmentation

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26n-seg.dxnn | ON | 74.22 | 110.3 | — | — |
| yolo26n-seg.dxnn | OFF | 50.40 | 104.7 | — | — |
| yolo26s-seg.dxnn | ON | 90.24 | 73.9 | — | — |
| yolo26s-seg.dxnn | OFF | 60.49 | 77.9 | — | — |
| yolo26m-seg.dxnn | ON | 108.17 | 55.8 | — | — |
| yolo26m-seg.dxnn | OFF | 76.74 | 56.0 | — | — |
| yolo26l-seg.dxnn | ON | 112.37 | 45.3 | — | — |
| yolo26l-seg.dxnn | OFF | 88.50 | 45.5 | — | — |
| yolo26x-seg.dxnn | ON | 155.64 | 25.6 | — | — |
| yolo26x-seg.dxnn | OFF | 137.35 | 25.6 | — | — |

### Oriented BBox (OBB)

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26n-obb.dxnn | ON | 69.95 | 59.2 | — | — |
| yolo26n-obb.dxnn | OFF | 50.18 | 59.3 | — | — |
| yolo26s-obb.dxnn | ON | 89.16 | 36.4 | — | — |
| yolo26s-obb.dxnn | OFF | 71.91 | 36.4 | — | — |
| yolo26m-obb.dxnn | ON | 110.97 | 27.3 | — | — |
| yolo26m-obb.dxnn | OFF | 90.88 | 27.3 | — | — |
| yolo26l-obb.dxnn | ON | 133.98 | 20.4 | — | — |
| yolo26l-obb.dxnn | OFF | 112.91 | 20.4 | — | — |
| yolo26x-obb.dxnn | ON | 209.25 | 11.9 | — | — |
| yolo26x-obb.dxnn | OFF | 191.54 | 11.9 | — | — |

### Classification

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26n-cls.dxnn | ON | 2.51 | 2672.8 | — | — |
| yolo26n-cls.dxnn | OFF | 2.47 | 2671.9 | — | — |
| yolo26s-cls.dxnn | ON | 3.51 | 1618.4 | — | — |
| yolo26s-cls.dxnn | OFF | 3.21 | 1616.3 | — | — |
| yolo26m-cls.dxnn | ON | 3.96 | 1274.9 | — | — |
| yolo26m-cls.dxnn | OFF | 3.86 | 1274.2 | — | — |
| yolo26l-cls.dxnn | ON | 5.55 | 797.4 | — | — |
| yolo26l-cls.dxnn | OFF | 5.47 | 796.7 | — | — |
| yolo26x-cls.dxnn | ON | 8.43 | 401.6 | — | — |
| yolo26x-cls.dxnn | OFF | 8.61 | 401.5 | — | — |

## Environment

| Item | Value |
|------|-------|
| Product | OrangePi5+ |
| Hostname | orangepi5plus |
| OS | Debian GNU/Linux 12 (bookworm) |
| Kernel | 6.1.43-rockchip-rk3588 |
| CPU | Cortex-A55 |
| CPU Cores | 8 |
| RAM | 15.6 GB |
| NPU SKU | M1 |
| NPU RT | v3.2.0 |
| NPU Driver (RT) | v2.1.0 |
| NPU Driver (PCIe) | v2.0.1 |
| NPU Firmware | v2.5.0 |
| NPU Memory | LPDDR5 5600 Mbps, 3.92GiB |
| NPU Board | M.2, Rev 1.0 |
| NPU PCIe | Gen3 X4 [01:00:00] |

### Tools

| Tool | Available | Version |
|------|-----------|---------|
| run_model | Yes | DXRT v3.2.0 run_model |
| gst-launch-1.0 | Yes | gst-launch-1.0 version 1.22.0 |
| gst-inspect-1.0 | Yes | gst-inspect-1.0 version 1.22.0 |
| dxtop | Yes | DX-TOP 1.0.1 |
| ffprobe | Yes | ffprobe version 5.1.3-4 Copyright (c) 2007-2022 the FFmpeg d... |

## Benchmark Parameters

| Parameter | Value |
|-----------|-------|
| Throughput duration (-t) | 30 sec |
| Latency loops (-l) | 300 |
| Model warmup runs | 1 |
| Model latency runs | 1 |
| Model throughput runs | 3 |
| E2E pipeline runs | 3 |
| Multi-stream FPS threshold | 30.0 fps |
| ORT modes | ON, OFF |
| Benchmark families | all |

## Measurement Protocol

| Item | Value |
|------|-------|
| Version | v2 |
| Thermal Mode | steady |
| Throughput Time | 30 s |
| Latency Loops | 300 |
| Model Warmup | 1 |
| Model Latency Runs | 1 |
| Model Throughput Runs | 3 |
| E2E Runs | 3 |
| FPS Threshold | 30.0 |
| Multi-Stream Search | single-stream-estimate-linear-boundary |
| Stable Capacity Rule | status_ok_and_all_runs_success_and_avg_per_channel_fps_ge_threshold |
| Cooldown Target ΔT | 10.0 °C |
| Cooldown Absolute Cap | 55.0 °C |
| Hot-Start Block | 60.0 °C |
| Cooldown Max Time | 1800.0 s |
| NPU Warmup | 1.0 s |
| NPU Drain | 0.5 s |

## Benchmarked Models

| Model | Task | Input Size | NPU Memory (MB) | ORT CPU Offload | Multi-Stream Sweep |
|-------|------|------------|:----------------:|:---------------:|:------------------:|
| yolo26n.dxnn | Object Detection | 640×640 | 140.1 | Yes | ✅ |
| yolo26s.dxnn | Object Detection | 640×640 | 147.2 | Yes | ✅ |
| yolo26m.dxnn | Object Detection | 640×640 | 148.4 | Yes | ✅ |
| yolo26l.dxnn | Object Detection | 640×640 | 162.6 | Yes | ✅ |
| yolo26x.dxnn | Object Detection | 640×640 | 271.1 | Yes | ✅ |
| yolo26n-pose.dxnn | Pose Estimation | 640×640 | 151.5 | Yes | ✅ |
| yolo26s-pose.dxnn | Pose Estimation | 640×640 | 159.0 | Yes | ✅ |
| yolo26m-pose.dxnn | Pose Estimation | 640×640 | 152.3 | Yes | ✅ |
| yolo26l-pose.dxnn | Pose Estimation | 640×640 | 158.2 | Yes | ✅ |
| yolo26x-pose.dxnn | Pose Estimation | 640×640 | 253.3 | Yes | ✅ |
| yolo26n-seg.dxnn | Segmentation | 640×640 | 160.7 | Yes | ✅ |
| yolo26s-seg.dxnn | Segmentation | 640×640 | 168.4 | Yes | ✅ |
| yolo26m-seg.dxnn | Segmentation | 640×640 | 187.2 | Yes | ✅ |
| yolo26l-seg.dxnn | Segmentation | 640×640 | 192.0 | Yes | ✅ |
| yolo26x-seg.dxnn | Segmentation | 640×640 | 308.1 | Yes | ✅ |
| yolo26n-obb.dxnn | Oriented BBox (OBB) | 1024×1024 | 357.9 | Yes | ✅ |
| yolo26s-obb.dxnn | Oriented BBox (OBB) | 1024×1024 | 365.7 | Yes | ✅ |
| yolo26m-obb.dxnn | Oriented BBox (OBB) | 1024×1024 | 369.6 | Yes | ✅ |
| yolo26l-obb.dxnn | Oriented BBox (OBB) | 1024×1024 | 369.8 | Yes | ✅ |
| yolo26x-obb.dxnn | Oriented BBox (OBB) | 1024×1024 | 567.7 | Yes | ✅ |
| yolo26n-cls.dxnn | Classification | 224×224 | 10.8 | No | — |
| yolo26s-cls.dxnn | Classification | 224×224 | 14.6 | No | — |
| yolo26m-cls.dxnn | Classification | 224×224 | 17.7 | No | — |
| yolo26l-cls.dxnn | Classification | 224×224 | 20.4 | No | — |
| yolo26x-cls.dxnn | Classification | 224×224 | 44.7 | No | — |

## Input Videos

### Object Detection / Pose / Segmentation

| Item | Value |
|------|-------|
| File | od_benchmark_video.mp4 |
| Resolution | 1920 x 1080 |
| Codec | h264 |
| FPS | 30.0 |
| Frames | 3455 |
| Duration | 115.3 sec |
| Bitrate | 4.47 Mbps |
| Format | QuickTime / MOV |
| Pixel Format | yuv420p |

### Oriented BBox (OBB)

| Item | Value |
|------|-------|
| File | obb_benchmark_video.mp4 |
| Resolution | 1920 x 1080 |
| Codec | h264 |
| FPS | 30.0 |
| Frames | 2640 |
| Duration | 88.0 sec |
| Bitrate | 4.87 Mbps |
| Format | QuickTime / MOV |
| Pixel Format | yuv420p |

### Classification

| Item | Value |
|------|-------|
| File | od_benchmark_video.mp4 |
| Resolution | 1920 x 1080 |
| Codec | h264 |
| FPS | 30.0 |
| Frames | 3455 |
| Duration | 115.3 sec |
| Bitrate | 4.47 Mbps |
| Format | QuickTime / MOV |
| Pixel Format | yuv420p |

## Model-Level Benchmarks

### Throughput (Multi-Core, Async)

#### Object Detection

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26n.dxnn | 136.1 ±1.3 | 215 | 61.9 | 82.4 | 48~51 | 1000 | ok |
| yolo26s.dxnn | 97.2 ±0.9 | 184 | 80.3 | 96.1 | 54~56 | 1000 | ok |
| yolo26m.dxnn | 75.5 ±0.1 | 166 | 87.7 | 100.0 | 58~62 | 1000 | ok |
| yolo26l.dxnn | 57.1 ±0.0 | 152 | 92.0 | 100.0 | 59~61 | 1000 | ok |
| yolo26x.dxnn | 26.9 ±10.0 | 97 | 69.1 | 100.0 | 56~58 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26n.dxnn | 138.3 ±3.1 | 175 | 66.8 | 87.1 | 52~53 | 1000 | ok |
| yolo26s.dxnn | 102.9 ±0.5 | 139 | 88.3 | 100.0 | 56~58 | 1000 | ok |
| yolo26m.dxnn | 76.4 ±0.1 | 123 | 88.5 | 100.0 | 60~63 | 1000 | ok |
| yolo26l.dxnn | 57.1 ±0.0 | 105 | 92.8 | 100.0 | 50~54 | 1000 | ok |
| yolo26x.dxnn | 32.7 ±0.0 | 70 | 89.9 | 100.0 | 58~61 | 1000 | ok |

#### Pose Estimation

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26n-pose.dxnn | 157.6 ±0.3 | 196 | 83.9 | 97.1 | 56~58 | 1000 | ok |
| yolo26s-pose.dxnn | 102.0 ±0.1 | 168 | 90.5 | 100.0 | 56~58 | 1000 | ok |
| yolo26m-pose.dxnn | 74.6 ±0.0 | 135 | 90.6 | 100.0 | 59~62 | 1000 | ok |
| yolo26l-pose.dxnn | 56.0 ±0.0 | 114 | 89.2 | 100.0 | 60~62 | 1000 | ok |
| yolo26x-pose.dxnn | 32.2 ±0.0 | 84 | 88.4 | 100.0 | 61~63 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26n-pose.dxnn | 163.1 ±0.2 | 148 | 90.1 | 100.0 | 56~58 | 1000 | ok |
| yolo26s-pose.dxnn | 102.3 ±0.0 | 119 | 89.5 | 100.0 | 57~59 | 1000 | ok |
| yolo26m-pose.dxnn | 74.6 ±0.0 | 110 | 89.2 | 100.0 | 60~63 | 1000 | ok |
| yolo26l-pose.dxnn | 56.0 ±0.0 | 82 | 89.0 | 100.0 | 60~63 | 1000 | ok |
| yolo26x-pose.dxnn | 26.5 ±9.9 | 41 | 69.8 | 100.0 | 59~62 | 1000 | ok |

#### Segmentation

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26n-seg.dxnn | 110.3 ±0.9 | 283 | 56.0 | 83.5 | 56~58 | 1000 | ok |
| yolo26s-seg.dxnn | 73.9 ±0.7 | 212 | 71.5 | 91.0 | 56~59 | 1000 | ok |
| yolo26m-seg.dxnn | 55.8 ±0.0 | 168 | 89.0 | 100.0 | 61~65 | 1000 | ok |
| yolo26l-seg.dxnn | 45.3 ±0.0 | 147 | 89.9 | 100.0 | 61~65 | 1000 | ok |
| yolo26x-seg.dxnn | 25.6 ±0.0 | 103 | 87.5 | 100.0 | 62~66 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26n-seg.dxnn | 104.7 ±0.1 | 200 | 56.6 | 78.5 | 56~58 | 1000 | ok |
| yolo26s-seg.dxnn | 77.9 ±0.3 | 173 | 77.8 | 94.2 | 58~60 | 1000 | ok |
| yolo26m-seg.dxnn | 56.0 ±0.0 | 137 | 89.3 | 100.0 | 63~66 | 1000 | ok |
| yolo26l-seg.dxnn | 45.5 ±0.0 | 116 | 89.3 | 100.0 | 62~65 | 1000 | ok |
| yolo26x-seg.dxnn | 25.6 ±0.0 | 79 | 88.4 | 100.0 | 63~66 | 1000 | ok |

#### Oriented BBox (OBB)

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26n-obb.dxnn | 59.2 ±0.1 | 131 | 90.9 | 100.0 | 57~58 | 1000 | ok |
| yolo26s-obb.dxnn | 36.4 ±0.0 | 101 | 89.0 | 100.0 | 56~58 | 1000 | ok |
| yolo26m-obb.dxnn | 27.3 ±0.0 | 85 | 88.8 | 100.0 | 58~61 | 1000 | ok |
| yolo26l-obb.dxnn | 20.4 ±0.0 | 73 | 88.3 | 100.0 | 60~62 | 1000 | ok |
| yolo26x-obb.dxnn | 11.9 ±0.0 | 48 | 90.9 | 100.0 | 61~62 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26n-obb.dxnn | 59.3 ±0.0 | 91 | 91.6 | 100.0 | 56~57 | 1000 | ok |
| yolo26s-obb.dxnn | 36.4 ±0.0 | 65 | 92.4 | 100.0 | 56~58 | 1000 | ok |
| yolo26m-obb.dxnn | 27.3 ±0.0 | 51 | 91.0 | 100.0 | 59~62 | 1000 | ok |
| yolo26l-obb.dxnn | 20.4 ±0.0 | 42 | 90.8 | 100.0 | 60~62 | 1000 | ok |
| yolo26x-obb.dxnn | 11.9 ±0.0 | 26 | 89.5 | 100.0 | 54~58 | 1000 | ok |

#### Classification

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26n-cls.dxnn | 2672.8 ±2.0 | 120 | 90.8 | 97.6 | 53~54 | 1000 | ok |
| yolo26s-cls.dxnn | 1618.4 ±2.3 | 85 | 90.5 | 99.0 | 54~56 | 1000 | ok |
| yolo26m-cls.dxnn | 1274.9 ±1.9 | 75 | 88.9 | 99.2 | 58~61 | 1000 | ok |
| yolo26l-cls.dxnn | 797.4 ±0.3 | 65 | 91.3 | 99.5 | 59~60 | 1000 | ok |
| yolo26x-cls.dxnn | 401.6 ±0.1 | 38 | 89.2 | 100.0 | 60~62 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26n-cls.dxnn | 2671.9 ±1.7 | 120 | 88.8 | 97.7 | 54 | 1000 | ok |
| yolo26s-cls.dxnn | 1616.3 ±0.5 | 86 | 89.9 | 99.1 | 55~56 | 1000 | ok |
| yolo26m-cls.dxnn | 1274.2 ±4.8 | 75 | 89.0 | 98.8 | 60~62 | 1000 | ok |
| yolo26l-cls.dxnn | 796.7 ±0.5 | 64 | 91.6 | 99.5 | 59~60 | 1000 | ok |
| yolo26x-cls.dxnn | 401.5 ±0.2 | 37 | 92.0 | 100.0 | 60~62 | 1000 | ok |

### Latency (Single-Core, Sync)

#### Object Detection

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26n.dxnn | 16.8 | 59.55 | 40.90 | 18.65 | 44 | ok |
| yolo26s.dxnn | 13.9 | 71.95 | 54.24 | 17.70 | 49 | ok |
| yolo26m.dxnn | 12.6 | 79.53 | 53.58 | 25.95 | 52 | ok |
| yolo26l.dxnn | 11.1 | 90.08 | 64.81 | 25.27 | 54 | ok |
| yolo26x.dxnn | 8.8 | 113.49 | 97.60 | 15.89 | 50 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|-------------|--------|
| yolo26n.dxnn | 28.7 | 34.89 | 34.89 | 48 | ok |
| yolo26s.dxnn | 21.3 | 46.95 | 46.95 | 51 | ok |
| yolo26m.dxnn | 18.7 | 53.60 | 53.60 | 55 | ok |
| yolo26l.dxnn | 15.7 | 63.62 | 63.62 | 43 | ok |
| yolo26x.dxnn | 10.4 | 95.79 | 95.79 | 52 | ok |

#### Pose Estimation

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26n-pose.dxnn | 21.7 | 46.13 | 32.29 | 13.84 | 53 | ok |
| yolo26s-pose.dxnn | 18.3 | 54.52 | 44.86 | 9.66 | 52 | ok |
| yolo26m-pose.dxnn | 16.2 | 61.57 | 52.55 | 9.02 | 53 | ok |
| yolo26l-pose.dxnn | 13.2 | 76.00 | 65.03 | 10.97 | 55 | ok |
| yolo26x-pose.dxnn | 9.7 | 103.13 | 90.46 | 12.67 | 55 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|-------------|--------|
| yolo26n-pose.dxnn | 32.9 | 30.44 | 30.44 | 52 | ok |
| yolo26s-pose.dxnn | 25.8 | 38.76 | 38.76 | 53 | ok |
| yolo26m-pose.dxnn | 21.0 | 47.54 | 47.54 | 55 | ok |
| yolo26l-pose.dxnn | 17.7 | 56.50 | 56.50 | 55 | ok |
| yolo26x-pose.dxnn | 11.4 | 87.99 | 87.99 | 56 | ok |

#### Segmentation

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26n-seg.dxnn | 13.5 | 74.22 | 53.90 | 20.32 | 53 | ok |
| yolo26s-seg.dxnn | 11.1 | 90.24 | 72.86 | 17.38 | 52 | ok |
| yolo26m-seg.dxnn | 9.2 | 108.17 | 88.61 | 19.55 | 54 | ok |
| yolo26l-seg.dxnn | 8.9 | 112.37 | 93.00 | 19.37 | 54 | ok |
| yolo26x-seg.dxnn | 6.4 | 155.64 | 136.33 | 19.30 | 55 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|-------------|--------|
| yolo26n-seg.dxnn | 19.8 | 50.40 | 50.40 | 53 | ok |
| yolo26s-seg.dxnn | 16.5 | 60.49 | 60.49 | 53 | ok |
| yolo26m-seg.dxnn | 13.0 | 76.74 | 76.74 | 55 | ok |
| yolo26l-seg.dxnn | 11.3 | 88.50 | 88.50 | 55 | ok |
| yolo26x-seg.dxnn | 7.3 | 137.35 | 137.35 | 55 | ok |

#### Oriented BBox (OBB)

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26n-obb.dxnn | 14.3 | 69.95 | 55.91 | 14.05 | 54 | ok |
| yolo26s-obb.dxnn | 11.2 | 89.16 | 77.24 | 11.92 | 52 | ok |
| yolo26m-obb.dxnn | 9.0 | 110.97 | 96.88 | 14.09 | 53 | ok |
| yolo26l-obb.dxnn | 7.5 | 133.98 | 120.70 | 13.29 | 55 | ok |
| yolo26x-obb.dxnn | 4.8 | 209.25 | 191.24 | 18.02 | 56 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|-------------|--------|
| yolo26n-obb.dxnn | 19.9 | 50.18 | 50.18 | 53 | ok |
| yolo26s-obb.dxnn | 13.9 | 71.91 | 71.91 | 53 | ok |
| yolo26m-obb.dxnn | 11.0 | 90.88 | 90.88 | 55 | ok |
| yolo26l-obb.dxnn | 8.9 | 112.91 | 112.91 | 55 | ok |
| yolo26x-obb.dxnn | 5.2 | 191.54 | 191.54 | 48 | ok |

#### Classification

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26n-cls.dxnn | 398.5 | 2.51 | 2.51 | N/A | 51 | ok |
| yolo26s-cls.dxnn | 284.9 | 3.51 | 3.51 | N/A | 51 | ok |
| yolo26m-cls.dxnn | 252.6 | 3.96 | 3.96 | N/A | 53 | ok |
| yolo26l-cls.dxnn | 180.1 | 5.55 | 5.55 | N/A | 55 | ok |
| yolo26x-cls.dxnn | 118.6 | 8.43 | 8.43 | N/A | 55 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|-------------|--------|
| yolo26n-cls.dxnn | 404.1 | 2.47 | 2.47 | 51 | ok |
| yolo26s-cls.dxnn | 311.6 | 3.21 | 3.21 | 52 | ok |
| yolo26m-cls.dxnn | 259.1 | 3.86 | 3.86 | 55 | ok |
| yolo26l-cls.dxnn | 182.7 | 5.47 | 5.47 | 55 | ok |
| yolo26x-cls.dxnn | 116.2 | 8.61 | 8.61 | 55 | ok |

## E2E Pipeline (Single-Stream)

### Object Detection

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|--------|
| yolo26n.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|--------|
| yolo26n.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26n.dxnn | N/A | N/A | N/A | N/A |
| yolo26s.dxnn | N/A | N/A | N/A | N/A |
| yolo26m.dxnn | N/A | N/A | N/A | N/A |
| yolo26l.dxnn | N/A | N/A | N/A | N/A |
| yolo26x.dxnn | N/A | N/A | N/A | N/A |

### Pose Estimation

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|--------|
| yolo26n-pose.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-pose.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-pose.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-pose.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-pose.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|--------|
| yolo26n-pose.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-pose.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-pose.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-pose.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-pose.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26n-pose.dxnn | N/A | N/A | N/A | N/A |
| yolo26s-pose.dxnn | N/A | N/A | N/A | N/A |
| yolo26m-pose.dxnn | N/A | N/A | N/A | N/A |
| yolo26l-pose.dxnn | N/A | N/A | N/A | N/A |
| yolo26x-pose.dxnn | N/A | N/A | N/A | N/A |

### Segmentation

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|--------|
| yolo26n-seg.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-seg.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-seg.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-seg.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-seg.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|--------|
| yolo26n-seg.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-seg.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-seg.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-seg.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-seg.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26n-seg.dxnn | N/A | N/A | N/A | N/A |
| yolo26s-seg.dxnn | N/A | N/A | N/A | N/A |
| yolo26m-seg.dxnn | N/A | N/A | N/A | N/A |
| yolo26l-seg.dxnn | N/A | N/A | N/A | N/A |
| yolo26x-seg.dxnn | N/A | N/A | N/A | N/A |

### Oriented BBox (OBB)

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|--------|
| yolo26n-obb.dxnn | unknown | 2640 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-obb.dxnn | unknown | 2640 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-obb.dxnn | unknown | 2640 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-obb.dxnn | unknown | 2640 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-obb.dxnn | unknown | 2640 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|--------|
| yolo26n-obb.dxnn | unknown | 2640 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-obb.dxnn | unknown | 2640 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-obb.dxnn | unknown | 2640 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-obb.dxnn | unknown | 2640 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-obb.dxnn | unknown | 2640 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26n-obb.dxnn | N/A | N/A | N/A | N/A |
| yolo26s-obb.dxnn | N/A | N/A | N/A | N/A |
| yolo26m-obb.dxnn | N/A | N/A | N/A | N/A |
| yolo26l-obb.dxnn | N/A | N/A | N/A | N/A |
| yolo26x-obb.dxnn | N/A | N/A | N/A | N/A |

### Classification

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|--------|
| yolo26n-cls.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-cls.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-cls.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-cls.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-cls.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|--------|
| yolo26n-cls.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-cls.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-cls.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-cls.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-cls.dxnn | unknown | 3455 | 0/3 | 0.0 | N/A | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26n-cls.dxnn | N/A | N/A | N/A | N/A |
| yolo26s-cls.dxnn | N/A | N/A | N/A | N/A |
| yolo26m-cls.dxnn | N/A | N/A | N/A | N/A |
| yolo26l-cls.dxnn | N/A | N/A | N/A | N/A |
| yolo26x-cls.dxnn | N/A | N/A | N/A | N/A |

## E2E Pipeline (Multi-Stream)

### Object Detection

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|--------|
| yolo26n.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|--------|
| yolo26n.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |

### Pose Estimation

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|--------|
| yolo26n-pose.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-pose.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-pose.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-pose.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-pose.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|--------|
| yolo26n-pose.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-pose.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-pose.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-pose.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-pose.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |

### Segmentation

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|--------|
| yolo26n-seg.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-seg.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-seg.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-seg.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-seg.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|--------|
| yolo26n-seg.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-seg.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-seg.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-seg.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-seg.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |

### Oriented BBox (OBB)

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|--------|
| yolo26n-obb.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-obb.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-obb.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-obb.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-obb.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|--------|
| yolo26n-obb.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26s-obb.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26m-obb.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26l-obb.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |
| yolo26x-obb.dxnn | 1 | 0/3 | 0.0 | 0.0 | 0 | 0.0 | 0.0 | N/A | 0 | error |

---
*Report generated by dx_stream benchmark tool*
