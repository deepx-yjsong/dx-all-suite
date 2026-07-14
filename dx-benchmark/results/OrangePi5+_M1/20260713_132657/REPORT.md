# YOLO26 Benchmark Report

**Generated:** 2026-07-14 08:34:10 (Local)

## Test Timing

| # | Type | Start | End | Duration |
|---|------|-------|-----|----------|
| 1 | run | 2026-07-13 13:26:57 | 2026-07-14 08:34:10 | 19h 7m 13s |

## Executive Summary

### Object Detection

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26-n_640x640.dxnn | ON | 40.59 | 160.7 | 112.3 | 3 |
| yolo26-n_640x640.dxnn | OFF | 42.88 | 164.6 | 98.4 | 3 |
| yolo26-s_640x640.dxnn | ON | 66.34 | 138.7 | 95.4 | 3 |
| yolo26-s_640x640.dxnn | OFF | 49.90 | 147.3 | 99.2 | 3 |
| yolo26-m_640x640.dxnn | ON | 62.65 | 107.5 | 78.3 | 2 |
| yolo26-m_640x640.dxnn | OFF | 59.03 | 115.8 | 96.9 | 3 |
| yolo26-l_640x640.dxnn | ON | 70.46 | 87.1 | 68.3 | 2 |
| yolo26-l_640x640.dxnn | OFF | 64.89 | 88.8 | 82.7 | 2 |
| yolo26-x_640x640.dxnn | ON | 111.19 | 48.9 | 47.1 | 1 |
| yolo26-x_640x640.dxnn | OFF | 92.06 | 48.0 | 47.3 | 1 |

### Pose Estimation

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26-n-pose_640x640.dxnn | ON | 35.13 | 202.5 | 143.6 | 4 |
| yolo26-n-pose_640x640.dxnn | OFF | 30.84 | 206.6 | 170.9 | 5 |
| yolo26-s-pose_640x640.dxnn | ON | 43.34 | 157.6 | 115.5 | 3 |
| yolo26-s-pose_640x640.dxnn | OFF | 39.84 | 165.2 | 132.4 | 4 |
| yolo26-m-pose_640x640.dxnn | ON | 60.60 | 113.6 | 92.2 | 3 |
| yolo26-m-pose_640x640.dxnn | OFF | 54.07 | 112.5 | 103.6 | 3 |
| yolo26-l-pose_640x640.dxnn | ON | 62.58 | 86.6 | 79.2 | 2 |
| yolo26-l-pose_640x640.dxnn | OFF | 57.24 | 84.7 | 83.8 | 2 |
| yolo26-x-pose_640x640.dxnn | ON | 94.60 | 46.6 | 44.6 | 1 |
| yolo26-x-pose_640x640.dxnn | OFF | 84.52 | 46.8 | 45.2 | 1 |

### Segmentation

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26-n-seg_640x640.dxnn | ON | 65.84 | 87.9 | 72.1 | 2 |
| yolo26-n-seg_640x640.dxnn | OFF | 55.97 | 88.8 | 83.8 | 2 |
| yolo26-s-seg_640x640.dxnn | ON | 79.13 | 84.7 | 64.4 | 2 |
| yolo26-s-seg_640x640.dxnn | OFF | 66.81 | 87.6 | 75.5 | 2 |
| yolo26-m-seg_640x640.dxnn | ON | 91.55 | 69.3 | 52.3 | 1 |
| yolo26-m-seg_640x640.dxnn | OFF | 84.23 | 68.2 | 61.0 | 1 |
| yolo26-l-seg_640x640.dxnn | ON | 98.30 | 61.1 | 47.6 | 1 |
| yolo26-l-seg_640x640.dxnn | OFF | 94.90 | 62.4 | 55.0 | 1 |
| yolo26-x-seg_640x640.dxnn | ON | 141.47 | 34.7 | 26.0 | — |
| yolo26-x-seg_640x640.dxnn | OFF | 127.05 | 34.1 | 25.6 | — |

### Oriented BBox (OBB)

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26-n-obb_1024x1024.dxnn | ON | 55.29 | 96.4 | 73.8 | 2 |
| yolo26-n-obb_1024x1024.dxnn | OFF | 56.11 | 97.8 | 86.6 | 2 |
| yolo26-s-obb_1024x1024.dxnn | ON | 83.33 | 62.5 | 56.0 | 1 |
| yolo26-s-obb_1024x1024.dxnn | OFF | 79.35 | 60.6 | 61.2 | 2 |
| yolo26-m-obb_1024x1024.dxnn | ON | 107.23 | 41.7 | 40.5 | 1 |
| yolo26-m-obb_1024x1024.dxnn | OFF | 89.44 | 40.6 | 40.7 | 1 |
| yolo26-l-obb_1024x1024.dxnn | ON | 125.16 | 29.9 | 30.0 | — |
| yolo26-l-obb_1024x1024.dxnn | OFF | 107.17 | 29.4 | 30.2 | 1 |
| yolo26-x-obb_1024x1024.dxnn | ON | 184.09 | 16.5 | 14.4 | — |
| yolo26-x-obb_1024x1024.dxnn | OFF | 179.23 | 16.5 | 14.9 | — |

### Classification

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26-n_224x224.dxnn | ON | 2.68 | 2833.8 | 944.1 | — |
| yolo26-n_224x224.dxnn | OFF | 2.87 | 2820.8 | 942.2 | — |
| yolo26-s_224x224.dxnn | ON | 5.05 | 1934.8 | 929.9 | — |
| yolo26-s_224x224.dxnn | OFF | 4.82 | 1934.0 | 942.4 | — |
| yolo26-m_224x224.dxnn | ON | 5.71 | 1364.8 | 935.9 | — |
| yolo26-m_224x224.dxnn | OFF | 5.70 | 1364.5 | 929.8 | — |
| yolo26-l_224x224.dxnn | ON | 6.98 | 872.6 | 851.1 | — |
| yolo26-l_224x224.dxnn | OFF | 6.83 | 873.8 | 853.8 | — |
| yolo26-x_224x224.dxnn | ON | 9.85 | 483.9 | 477.9 | — |
| yolo26-x_224x224.dxnn | OFF | 9.61 | 483.0 | 480.0 | — |

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
| NPU RT | v3.4.0 |
| NPU Driver (RT) | v2.5.1 |
| NPU Driver (PCIe) | v2.4.1 |
| NPU Firmware | v2.7.1 |
| NPU Memory | LPDDR5 5600 Mbps, 3.92GiB |
| NPU Board | M.2, Rev 1.0 |
| NPU PCIe | Gen1 X4 [01:00:00] |

### Tools

| Tool | Available | Version |
|------|-----------|---------|
| run_model | Yes | DXRT v3.4.0 run_model |
| gst-launch-1.0 | Yes | gst-launch-1.0 version 1.22.0 |
| gst-inspect-1.0 | Yes | gst-inspect-1.0 version 1.22.0 |
| dxtop | Yes | DX-TOP 1.1.0 |
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
| Cooldown Max Time | 1000.0 s |
| NPU Warmup | 1.0 s |
| NPU Drain | 0.5 s |

## Benchmarked Models

| Model | Task | Input Size | NPU Memory (MB) | ORT CPU Offload | Multi-Stream Sweep |
|-------|------|------------|:----------------:|:---------------:|:------------------:|
| yolo26-n_640x640.dxnn | Object Detection | 640×640 | 117.8 | Yes | ✅ |
| yolo26-s_640x640.dxnn | Object Detection | 640×640 | 151.9 | Yes | ✅ |
| yolo26-m_640x640.dxnn | Object Detection | 640×640 | 244.6 | Yes | ✅ |
| yolo26-l_640x640.dxnn | Object Detection | 640×640 | 297.6 | Yes | ✅ |
| yolo26-x_640x640.dxnn | Object Detection | 640×640 | 528.8 | Yes | ✅ |
| yolo26-n-pose_640x640.dxnn | Pose Estimation | 640×640 | 119.8 | Yes | ✅ |
| yolo26-s-pose_640x640.dxnn | Pose Estimation | 640×640 | 157.9 | Yes | ✅ |
| yolo26-m-pose_640x640.dxnn | Pose Estimation | 640×640 | 256.7 | Yes | ✅ |
| yolo26-l-pose_640x640.dxnn | Pose Estimation | 640×640 | 309.6 | Yes | ✅ |
| yolo26-x-pose_640x640.dxnn | Pose Estimation | 640×640 | 522.6 | Yes | ✅ |
| yolo26-n-seg_640x640.dxnn | Segmentation | 640×640 | 140.2 | Yes | ✅ |
| yolo26-s-seg_640x640.dxnn | Segmentation | 640×640 | 177.9 | Yes | ✅ |
| yolo26-m-seg_640x640.dxnn | Segmentation | 640×640 | 272.8 | Yes | ✅ |
| yolo26-l-seg_640x640.dxnn | Segmentation | 640×640 | 325.8 | Yes | ✅ |
| yolo26-x-seg_640x640.dxnn | Segmentation | 640×640 | 561.1 | Yes | ✅ |
| yolo26-n-obb_1024x1024.dxnn | Oriented BBox (OBB) | 1024×1024 | 243.5 | Yes | ✅ |
| yolo26-s-obb_1024x1024.dxnn | Oriented BBox (OBB) | 1024×1024 | 379.6 | Yes | ✅ |
| yolo26-m-obb_1024x1024.dxnn | Oriented BBox (OBB) | 1024×1024 | 651.2 | Yes | ✅ |
| yolo26-l-obb_1024x1024.dxnn | Oriented BBox (OBB) | 1024×1024 | 799.0 | Yes | ✅ |
| yolo26-x-obb_1024x1024.dxnn | Oriented BBox (OBB) | 1024×1024 | 1330.5 | Yes | ✅ |
| yolo26-n_224x224.dxnn | Classification | 224×224 | 5.1 | No | — |
| yolo26-s_224x224.dxnn | Classification | 224×224 | 10.0 | No | — |
| yolo26-m_224x224.dxnn | Classification | 224×224 | 14.8 | No | — |
| yolo26-l_224x224.dxnn | Classification | 224×224 | 19.9 | No | — |
| yolo26-x_224x224.dxnn | Classification | 224×224 | 49.2 | No | — |

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
| yolo26-n_640x640.dxnn | 160.7 ±0.4 | 198 | 38.5 | 69.1 | 45~48 | 1000 | ok |
| yolo26-s_640x640.dxnn | 138.7 ±1.2 | 188 | 63.6 | 81.6 | 55~57 | 1000 | ok |
| yolo26-m_640x640.dxnn | 107.5 ±0.1 | 168 | 77.6 | 97.4 | 59~63 | 1000 | ok |
| yolo26-l_640x640.dxnn | 87.1 ±0.3 | 152 | 84.6 | 100.0 | 60~64 | 1000 | ok |
| yolo26-x_640x640.dxnn | 48.9 ±0.4 | 119 | 88.9 | 100.0 | 61~65 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n_640x640.dxnn | 164.6 ±0.6 | 132 | 40.4 | 69.1 | 53~54 | 1000 | ok |
| yolo26-s_640x640.dxnn | 147.3 ±0.6 | 125 | 67.1 | 84.6 | 55~57 | 1000 | ok |
| yolo26-m_640x640.dxnn | 115.8 ±1.8 | 110 | 86.5 | 100.0 | 60~65 | 1000 | ok |
| yolo26-l_640x640.dxnn | 88.8 ±0.2 | 102 | 89.6 | 100.0 | 60~64 | 1000 | ok |
| yolo26-x_640x640.dxnn | 48.0 ±0.6 | 80 | 88.5 | 100.0 | 61~65 | 1000 | ok |

#### Pose Estimation

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-pose_640x640.dxnn | 202.5 ±1.2 | 190 | 57.8 | 79.2 | 55~56 | 1000 | ok |
| yolo26-s-pose_640x640.dxnn | 157.6 ±0.9 | 176 | 77.1 | 92.0 | 57~60 | 1000 | ok |
| yolo26-m-pose_640x640.dxnn | 113.6 ±0.2 | 145 | 89.0 | 100.0 | 61~66 | 1000 | ok |
| yolo26-l-pose_640x640.dxnn | 86.6 ±0.1 | 132 | 89.3 | 100.0 | 61~66 | 1000 | ok |
| yolo26-x-pose_640x640.dxnn | 46.6 ±0.3 | 100 | 89.3 | 100.0 | 62~67 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-pose_640x640.dxnn | 206.6 ±1.5 | 127 | 58.8 | 81.4 | 55~57 | 1000 | ok |
| yolo26-s-pose_640x640.dxnn | 165.2 ±1.7 | 120 | 82.7 | 97.2 | 57~60 | 1000 | ok |
| yolo26-m-pose_640x640.dxnn | 112.5 ±0.2 | 102 | 91.0 | 100.0 | 61~66 | 1000 | ok |
| yolo26-l-pose_640x640.dxnn | 84.7 ±1.6 | 101 | 90.0 | 100.0 | 60~65 | 1000 | ok |
| yolo26-x-pose_640x640.dxnn | 46.8 ±0.7 | 65 | 89.3 | 100.0 | 62~67 | 1000 | ok |

#### Segmentation

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-seg_640x640.dxnn | 87.9 ±0.5 | 190 | 25.9 | 62.2 | 53~54 | 1000 | ok |
| yolo26-s-seg_640x640.dxnn | 84.7 ±0.5 | 190 | 49.2 | 78.3 | 56~58 | 1000 | ok |
| yolo26-m-seg_640x640.dxnn | 69.3 ±0.5 | 162 | 76.1 | 94.2 | 62~67 | 1000 | ok |
| yolo26-l-seg_640x640.dxnn | 61.1 ±0.1 | 153 | 81.9 | 99.6 | 62~67 | 1000 | ok |
| yolo26-x-seg_640x640.dxnn | 34.7 ±0.0 | 115 | 88.7 | 100.0 | 64~70 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-seg_640x640.dxnn | 88.8 ±0.5 | 144 | 26.4 | 65.4 | 54 | 1000 | ok |
| yolo26-s-seg_640x640.dxnn | 87.6 ±0.3 | 139 | 50.4 | 80.7 | 56~58 | 1000 | ok |
| yolo26-m-seg_640x640.dxnn | 68.2 ±0.1 | 129 | 75.9 | 93.4 | 61~66 | 1000 | ok |
| yolo26-l-seg_640x640.dxnn | 62.4 ±0.2 | 115 | 85.2 | 100.0 | 62~68 | 1000 | ok |
| yolo26-x-seg_640x640.dxnn | 34.1 ±0.4 | 81 | 88.7 | 100.0 | 64~70 | 1000 | ok |

#### Oriented BBox (OBB)

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | 96.4 ±0.1 | 157 | 83.5 | 97.7 | 56~58 | 1000 | ok |
| yolo26-s-obb_1024x1024.dxnn | 62.5 ±0.5 | 119 | 90.5 | 100.0 | 58~61 | 1000 | ok |
| yolo26-m-obb_1024x1024.dxnn | 41.7 ±0.2 | 97 | 89.8 | 100.0 | 61~66 | 1000 | ok |
| yolo26-l-obb_1024x1024.dxnn | 29.9 ±0.9 | 96 | 88.5 | 100.0 | 61~65 | 1000 | ok |
| yolo26-x-obb_1024x1024.dxnn | 16.5 ±0.0 | 57 | 85.7 | 100.0 | 62~67 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | 97.8 ±0.5 | 102 | 88.6 | 100.0 | 56~59 | 1000 | ok |
| yolo26-s-obb_1024x1024.dxnn | 60.6 ±0.3 | 89 | 88.9 | 100.0 | 58~60 | 1000 | ok |
| yolo26-m-obb_1024x1024.dxnn | 40.6 ±1.2 | 63 | 90.6 | 100.0 | 61~66 | 1000 | ok |
| yolo26-l-obb_1024x1024.dxnn | 29.4 ±0.0 | 52 | 88.4 | 100.0 | 60~64 | 1000 | ok |
| yolo26-x-obb_1024x1024.dxnn | 16.5 ±0.0 | 29 | 86.4 | 100.0 | 63~67 | 1000 | ok |

#### Classification

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n_224x224.dxnn | 2833.8 ±8.9 | 86 | 69.2 | 80.2 | 54 | 1000 | ok |
| yolo26-s_224x224.dxnn | 1934.8 ±1.7 | 67 | 85.7 | 95.3 | 55~57 | 1000 | ok |
| yolo26-m_224x224.dxnn | 1364.8 ±1.2 | 62 | 87.1 | 96.6 | 59~62 | 1000 | ok |
| yolo26-l_224x224.dxnn | 872.6 ±1.0 | 52 | 88.4 | 98.3 | 57~59 | 1000 | ok |
| yolo26-x_224x224.dxnn | 483.9 ±1.2 | 35 | 87.7 | 99.4 | 59~61 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n_224x224.dxnn | 2820.8 ±13.2 | 86 | 68.8 | 79.3 | 54~55 | 1000 | ok |
| yolo26-s_224x224.dxnn | 1934.0 ±3.3 | 66 | 87.5 | 95.8 | 55~57 | 1000 | ok |
| yolo26-m_224x224.dxnn | 1364.5 ±0.6 | 62 | 88.4 | 97.0 | 59~62 | 1000 | ok |
| yolo26-l_224x224.dxnn | 873.8 ±0.5 | 52 | 89.2 | 98.0 | 57~59 | 1000 | ok |
| yolo26-x_224x224.dxnn | 483.0 ±0.7 | 37 | 91.3 | 99.2 | 58~61 | 1000 | ok |

### Latency (Single-Core, Sync)

#### Object Detection

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n_640x640.dxnn | 24.6 | 40.59 | 35.07 | 5.52 | 42 | ok |
| yolo26-s_640x640.dxnn | 15.1 | 66.34 | 60.68 | 5.66 | 51 | ok |
| yolo26-m_640x640.dxnn | 16.0 | 62.65 | 55.79 | 6.86 | 52 | ok |
| yolo26-l_640x640.dxnn | 14.2 | 70.46 | 61.83 | 8.64 | 52 | ok |
| yolo26-x_640x640.dxnn | 9.0 | 111.19 | 103.63 | 7.56 | 52 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n_640x640.dxnn | 23.3 | 42.88 | 42.88 | N/A | 51 | ok |
| yolo26-s_640x640.dxnn | 20.0 | 49.90 | 49.90 | N/A | 52 | ok |
| yolo26-m_640x640.dxnn | 16.9 | 59.03 | 59.03 | N/A | 52 | ok |
| yolo26-l_640x640.dxnn | 15.4 | 64.89 | 64.89 | N/A | 52 | ok |
| yolo26-x_640x640.dxnn | 10.9 | 92.06 | 92.06 | N/A | 53 | ok |

#### Pose Estimation

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-pose_640x640.dxnn | 28.5 | 35.13 | 29.93 | 5.20 | 52 | ok |
| yolo26-s-pose_640x640.dxnn | 23.1 | 43.34 | 38.90 | 4.44 | 52 | ok |
| yolo26-m-pose_640x640.dxnn | 16.5 | 60.60 | 57.21 | 3.38 | 53 | ok |
| yolo26-l-pose_640x640.dxnn | 16.0 | 62.58 | 58.50 | 4.07 | 53 | ok |
| yolo26-x-pose_640x640.dxnn | 10.6 | 94.60 | 90.93 | 3.68 | 53 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-pose_640x640.dxnn | 32.4 | 30.84 | 30.84 | N/A | 52 | ok |
| yolo26-s-pose_640x640.dxnn | 25.1 | 39.84 | 39.84 | N/A | 52 | ok |
| yolo26-m-pose_640x640.dxnn | 18.5 | 54.07 | 54.07 | N/A | 53 | ok |
| yolo26-l-pose_640x640.dxnn | 17.5 | 57.24 | 57.24 | N/A | 53 | ok |
| yolo26-x-pose_640x640.dxnn | 11.8 | 84.52 | 84.52 | N/A | 53 | ok |

#### Segmentation

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-seg_640x640.dxnn | 15.2 | 65.84 | 58.00 | 7.85 | 51 | ok |
| yolo26-s-seg_640x640.dxnn | 12.6 | 79.13 | 69.45 | 9.68 | 52 | ok |
| yolo26-m-seg_640x640.dxnn | 10.9 | 91.55 | 85.22 | 6.33 | 53 | ok |
| yolo26-l-seg_640x640.dxnn | 10.2 | 98.30 | 86.96 | 11.34 | 53 | ok |
| yolo26-x-seg_640x640.dxnn | 7.1 | 141.47 | 130.61 | 10.86 | 53 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-seg_640x640.dxnn | 17.9 | 55.97 | 55.97 | N/A | 52 | ok |
| yolo26-s-seg_640x640.dxnn | 15.0 | 66.81 | 66.81 | N/A | 52 | ok |
| yolo26-m-seg_640x640.dxnn | 11.9 | 84.23 | 84.23 | N/A | 52 | ok |
| yolo26-l-seg_640x640.dxnn | 10.5 | 94.90 | 94.90 | N/A | 53 | ok |
| yolo26-x-seg_640x640.dxnn | 7.9 | 127.05 | 127.05 | N/A | 54 | ok |

#### Oriented BBox (OBB)

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-obb_1024x1024.dxnn | 18.1 | 55.29 | 48.89 | 6.40 | 52 | ok |
| yolo26-s-obb_1024x1024.dxnn | 12.0 | 83.33 | 78.09 | 5.24 | 52 | ok |
| yolo26-m-obb_1024x1024.dxnn | 9.3 | 107.23 | 102.60 | 4.63 | 53 | ok |
| yolo26-l-obb_1024x1024.dxnn | 8.0 | 125.16 | 120.39 | 4.77 | 53 | ok |
| yolo26-x-obb_1024x1024.dxnn | 5.4 | 184.09 | 177.21 | 6.88 | 55 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-obb_1024x1024.dxnn | 17.8 | 56.11 | 56.11 | N/A | 52 | ok |
| yolo26-s-obb_1024x1024.dxnn | 12.6 | 79.35 | 79.35 | N/A | 52 | ok |
| yolo26-m-obb_1024x1024.dxnn | 11.2 | 89.44 | 89.44 | N/A | 54 | ok |
| yolo26-l-obb_1024x1024.dxnn | 9.3 | 107.17 | 107.17 | N/A | 53 | ok |
| yolo26-x-obb_1024x1024.dxnn | 5.6 | 179.23 | 179.23 | N/A | 55 | ok |

#### Classification

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n_224x224.dxnn | 372.6 | 2.68 | 2.68 | N/A | 52 | ok |
| yolo26-s_224x224.dxnn | 197.9 | 5.05 | 5.05 | N/A | 52 | ok |
| yolo26-m_224x224.dxnn | 175.0 | 5.71 | 5.71 | N/A | 52 | ok |
| yolo26-l_224x224.dxnn | 143.3 | 6.98 | 6.98 | N/A | 52 | ok |
| yolo26-x_224x224.dxnn | 101.5 | 9.85 | 9.85 | N/A | 52 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n_224x224.dxnn | 348.6 | 2.87 | 2.87 | N/A | 52 | ok |
| yolo26-s_224x224.dxnn | 207.6 | 4.82 | 4.82 | N/A | 52 | ok |
| yolo26-m_224x224.dxnn | 175.4 | 5.70 | 5.70 | N/A | 52 | ok |
| yolo26-l_224x224.dxnn | 146.4 | 6.83 | 6.83 | N/A | 52 | ok |
| yolo26-x_224x224.dxnn | 104.1 | 9.61 | 9.61 | N/A | 52 | ok |

## E2E Pipeline (Single-Stream)

### Object Detection

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_640x640.dxnn | mppvideodec | 3455 | 3 | 112.3 ±0.6 | 30.76 | 204 | 29.2 | 53.6 | 48~50 | 1000 | 187 | ok |
| yolo26-s_640x640.dxnn | mppvideodec | 3455 | 3 | 95.4 ±0.4 | 36.22 | 186 | 44.4 | 66.6 | 58 | 1000 | 208 | ok |
| yolo26-m_640x640.dxnn | mppvideodec | 3455 | 3 | 78.3 ±0.1 | 44.10 | 169 | 59.8 | 79.5 | 65~67 | 1000 | 240 | ok |
| yolo26-l_640x640.dxnn | mppvideodec | 3455 | 3 | 68.3 ±0.2 | 50.59 | 161 | 71.0 | 92.4 | 67~69 | 1000 | 254 | ok |
| yolo26-x_640x640.dxnn | mppvideodec | 3455 | 3 | 47.1 ±0.4 | 73.37 | 136 | 91.5 | 100.0 | 73~78 | 800~1000 | 354 | ok |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_640x640.dxnn | mppvideodec | 3455 | 3 | 98.4 ±2.4 | 35.10 | 205 | 22.0 | 76.5 | 53 | 1000 | 199 | ok |
| yolo26-s_640x640.dxnn | mppvideodec | 3455 | 3 | 99.2 ±1.2 | 34.84 | 205 | 41.4 | 72.5 | 57~58 | 1000 | 220 | ok |
| yolo26-m_640x640.dxnn | mppvideodec | 3455 | 3 | 96.9 ±0.8 | 35.67 | 209 | 71.6 | 88.5 | 67~69 | 1000 | 251 | ok |
| yolo26-l_640x640.dxnn | mppvideodec | 3455 | 3 | 82.7 ±0.2 | 41.79 | 210 | 86.0 | 100.0 | 68~71 | 1000 | 266 | ok |
| yolo26-x_640x640.dxnn | mppvideodec | 3455 | 3 | 47.3 ±0.9 | 73.05 | 155 | 93.2 | 100.0 | 74~78 | 800~1000 | 358 | ok |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26-n_640x640.dxnn | 112.3 | 98.4 | +13.9 | +14.1% |
| yolo26-s_640x640.dxnn | 95.4 | 99.2 | -3.8 | -3.8% |
| yolo26-m_640x640.dxnn | 78.3 | 96.9 | -18.5 | -19.1% |
| yolo26-l_640x640.dxnn | 68.3 | 82.7 | -14.4 | -17.4% |
| yolo26-x_640x640.dxnn | 47.1 | 47.3 | -0.2 | -0.4% |

### Pose Estimation

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-pose_640x640.dxnn | mppvideodec | 3455 | 3 | 143.6 ±1.4 | 24.05 | 204 | 39.9 | 63.2 | 57 | 1000 | 178 | ok |
| yolo26-s-pose_640x640.dxnn | mppvideodec | 3455 | 3 | 115.5 ±0.6 | 29.90 | 182 | 57.7 | 76.7 | 61~62 | 1000 | 201 | ok |
| yolo26-m-pose_640x640.dxnn | mppvideodec | 3455 | 3 | 92.2 ±1.1 | 37.46 | 158 | 74.6 | 93.8 | 69~72 | 1000 | 233 | ok |
| yolo26-l-pose_640x640.dxnn | mppvideodec | 3455 | 3 | 79.2 ±1.1 | 43.63 | 144 | 85.6 | 100.0 | 70~74 | 1000 | 248 | ok |
| yolo26-x-pose_640x640.dxnn | mppvideodec | 3455 | 3 | 44.6 ±2.3 | 77.47 | 106 | 92.6 | 100.0 | 76~80 | 800~1000 | 369 | ok |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-pose_640x640.dxnn | mppvideodec | 3455 | 3 | 170.9 ±2.1 | 20.21 | 182 | 46.8 | 70.6 | 57~58 | 1000 | 168 | ok |
| yolo26-s-pose_640x640.dxnn | mppvideodec | 3455 | 3 | 132.4 ±1.8 | 26.09 | 165 | 65.2 | 86.5 | 61~62 | 1000 | 190 | ok |
| yolo26-m-pose_640x640.dxnn | mppvideodec | 3455 | 3 | 103.6 ±0.4 | 33.35 | 146 | 83.3 | 98.7 | 70~73 | 1000 | 221 | ok |
| yolo26-l-pose_640x640.dxnn | mppvideodec | 3455 | 3 | 83.8 ±0.4 | 41.25 | 125 | 89.6 | 100.0 | 69~73 | 1000 | 235 | ok |
| yolo26-x-pose_640x640.dxnn | mppvideodec | 3455 | 3 | 45.2 ±1.8 | 76.39 | 89 | 93.2 | 100.0 | 76~80 | 800~1000 | 352 | ok |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26-n-pose_640x640.dxnn | 143.6 | 170.9 | -27.3 | -16.0% |
| yolo26-s-pose_640x640.dxnn | 115.5 | 132.4 | -16.9 | -12.7% |
| yolo26-m-pose_640x640.dxnn | 92.2 | 103.6 | -11.3 | -10.9% |
| yolo26-l-pose_640x640.dxnn | 79.2 | 83.8 | -4.6 | -5.5% |
| yolo26-x-pose_640x640.dxnn | 44.6 | 45.2 | -0.6 | -1.4% |

### Segmentation

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-seg_640x640.dxnn | mppvideodec | 3455 | 3 | 72.1 ±0.5 | 47.94 | 250 | 24.5 | 49.9 | 55~56 | 1000 | 290 | ok |
| yolo26-s-seg_640x640.dxnn | mppvideodec | 3455 | 3 | 64.4 ±0.7 | 53.64 | 227 | 40.2 | 68.7 | 60~62 | 1000 | 310 | ok |
| yolo26-m-seg_640x640.dxnn | mppvideodec | 3455 | 3 | 52.3 ±1.0 | 66.06 | 198 | 61.9 | 82.5 | 73~76 | 1000 | 346 | ok |
| yolo26-l-seg_640x640.dxnn | mppvideodec | 3455 | 3 | 47.6 ±0.4 | 72.56 | 194 | 68.6 | 89.7 | 74~78 | 1000 | 360 | ok |
| yolo26-x-seg_640x640.dxnn | mppvideodec | 3455 | 3 | 26.0 ±2.7 | 132.68 | 126 | 88.7 | 100.0 | 81~82 | 600~1000 | 466 | ok |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-seg_640x640.dxnn | mppvideodec | 3455 | 3 | 83.8 ±0.4 | 41.23 | 272 | 25.0 | 78.4 | 56~57 | 1000 | 306 | ok |
| yolo26-s-seg_640x640.dxnn | mppvideodec | 3455 | 3 | 75.5 ±0.3 | 45.77 | 259 | 46.9 | 73.1 | 61~62 | 1000 | 329 | ok |
| yolo26-m-seg_640x640.dxnn | mppvideodec | 3455 | 3 | 61.0 ±0.5 | 56.65 | 228 | 71.4 | 90.7 | 72~77 | 1000 | 368 | ok |
| yolo26-l-seg_640x640.dxnn | mppvideodec | 3455 | 3 | 55.0 ±1.4 | 62.85 | 207 | 79.8 | 100.0 | 75~80 | 1000 | 379 | ok |
| yolo26-x-seg_640x640.dxnn | mppvideodec | 3455 | 3 | 25.6 ±2.6 | 135.23 | 127 | 89.9 | 100.0 | 81~82 | 600~1000 | 479 | ok |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26-n-seg_640x640.dxnn | 72.1 | 83.8 | -11.7 | -14.0% |
| yolo26-s-seg_640x640.dxnn | 64.4 | 75.5 | -11.1 | -14.7% |
| yolo26-m-seg_640x640.dxnn | 52.3 | 61.0 | -8.7 | -14.2% |
| yolo26-l-seg_640x640.dxnn | 47.6 | 55.0 | -7.4 | -13.4% |
| yolo26-x-seg_640x640.dxnn | 26.0 | 25.6 | +0.5 | +1.9% |

### Oriented BBox (OBB)

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | mppvideodec | 2640 | 3 | 73.8 ±0.2 | 35.76 | 161 | 64.1 | 82.8 | 58~59 | 1000 | 218 | ok |
| yolo26-s-obb_1024x1024.dxnn | mppvideodec | 2640 | 3 | 56.0 ±0.6 | 47.18 | 141 | 83.8 | 100.0 | 64~66 | 1000 | 239 | ok |
| yolo26-m-obb_1024x1024.dxnn | mppvideodec | 2640 | 3 | 40.5 ±0.1 | 65.12 | 111 | 92.3 | 100.0 | 73~78 | 1000 | 272 | ok |
| yolo26-l-obb_1024x1024.dxnn | mppvideodec | 2640 | 3 | 30.0 ±0.0 | 88.07 | 97 | 93.1 | 100.0 | 73~78 | 1000 | 288 | ok |
| yolo26-x-obb_1024x1024.dxnn | mppvideodec | 2640 | 3 | 14.4 ±0.9 | 182.86 | 58 | 91.7 | 100.0 | 81~82 | 600~1000 | 391 | ok |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | mppvideodec | 2640 | 3 | 86.6 ±0.7 | 30.47 | 184 | 75.5 | 94.1 | 60~61 | 1000 | 218 | ok |
| yolo26-s-obb_1024x1024.dxnn | mppvideodec | 2640 | 3 | 61.2 ±0.2 | 43.15 | 152 | 91.6 | 100.0 | 64~66 | 1000 | 243 | ok |
| yolo26-m-obb_1024x1024.dxnn | mppvideodec | 2640 | 3 | 40.7 ±0.1 | 64.86 | 119 | 93.1 | 100.0 | 74~78 | 1000 | 271 | ok |
| yolo26-l-obb_1024x1024.dxnn | mppvideodec | 2640 | 3 | 30.2 ±0.1 | 87.38 | 106 | 93.7 | 100.0 | 73~79 | 1000 | 285 | ok |
| yolo26-x-obb_1024x1024.dxnn | mppvideodec | 2640 | 3 | 14.9 ±0.9 | 177.05 | 61 | 91.8 | 100.0 | 80~81 | 600~1000 | 389 | ok |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26-n-obb_1024x1024.dxnn | 73.8 | 86.6 | -12.8 | -14.8% |
| yolo26-s-obb_1024x1024.dxnn | 56.0 | 61.2 | -5.2 | -8.5% |
| yolo26-m-obb_1024x1024.dxnn | 40.5 | 40.7 | -0.2 | -0.4% |
| yolo26-l-obb_1024x1024.dxnn | 30.0 | 30.2 | -0.2 | -0.8% |
| yolo26-x-obb_1024x1024.dxnn | 14.4 | 14.9 | -0.5 | -3.2% |

### Classification

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_224x224.dxnn | mppvideodec | 3455 | 3 | 944.1 ±11.0 | 3.66 | 164 | 12.2 | 47.4 | 53~54 | 1000 | 91 | ok |
| yolo26-s_224x224.dxnn | mppvideodec | 3455 | 3 | 929.9 ±8.2 | 3.71 | 164 | 21.9 | 66.5 | 56 | 1000 | 100 | ok |
| yolo26-m_224x224.dxnn | mppvideodec | 3455 | 3 | 935.9 ±7.9 | 3.69 | 160 | 32.8 | 75.8 | 60~61 | 1000 | 115 | ok |
| yolo26-l_224x224.dxnn | mppvideodec | 3455 | 3 | 851.1 ±4.3 | 4.06 | 153 | 55.6 | 97.8 | 59 | 1000 | 128 | ok |
| yolo26-x_224x224.dxnn | mppvideodec | 3455 | 3 | 477.9 ±3.8 | 7.23 | 119 | 65.4 | 98.6 | 62 | 1000 | 204 | ok |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_224x224.dxnn | mppvideodec | 3455 | 3 | 942.2 ±14.6 | 3.67 | 163 | 13.2 | 47.6 | 54 | 1000 | 91 | ok |
| yolo26-s_224x224.dxnn | mppvideodec | 3455 | 3 | 942.4 ±4.5 | 3.67 | 163 | 21.5 | 66.4 | 56 | 1000 | 100 | ok |
| yolo26-m_224x224.dxnn | mppvideodec | 3455 | 3 | 929.8 ±14.1 | 3.72 | 161 | 31.6 | 76.0 | 61 | 1000 | 115 | ok |
| yolo26-l_224x224.dxnn | mppvideodec | 3455 | 3 | 853.8 ±4.0 | 4.05 | 152 | 56.2 | 97.6 | 59 | 1000 | 128 | ok |
| yolo26-x_224x224.dxnn | mppvideodec | 3455 | 3 | 480.0 ±0.8 | 7.20 | 118 | 67.9 | 98.9 | 61~62 | 1000 | 204 | ok |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26-n_224x224.dxnn | 944.1 | 942.2 | +1.9 | +0.2% |
| yolo26-s_224x224.dxnn | 929.9 | 942.4 | -12.5 | -1.3% |
| yolo26-m_224x224.dxnn | 935.9 | 929.8 | +6.1 | +0.7% |
| yolo26-l_224x224.dxnn | 851.1 | 853.8 | -2.7 | -0.3% |
| yolo26-x_224x224.dxnn | 477.9 | 480.0 | -2.1 | -0.4% |

## E2E Pipeline (Multi-Stream)

### Object Detection

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_640x640.dxnn | 3 | 3 | 112.3 ±0.6 | 37.4 | 210 | 30.7 | 56.8 | 53~55 | 1000 | 205 | ok |
| yolo26-n_640x640.dxnn | 4 | 3 | 114.1 ±1.2 | 28.5 | 210 | 31.4 | 53.6 | 56~57 | 1000 | 211 | ok |
| yolo26-s_640x640.dxnn | 3 | 3 | 95.6 ±0.5 | 31.9 | 190 | 46.9 | 67.7 | 60~61 | 1000 | 226 | ok |
| yolo26-s_640x640.dxnn | 4 | 3 | 95.2 ±0.4 | 23.8 | 190 | 47.2 | 68.6 | 62 | 1000 | 232 | ok |
| yolo26-m_640x640.dxnn | 2 | 3 | 78.6 ±0.7 | 39.3 | 172 | 62.6 | 80.7 | 70~72 | 1000 | 251 | ok |
| yolo26-m_640x640.dxnn | 3 | 3 | 78.5 ±0.6 | 26.1 | 172 | 63.2 | 79.8 | 73~74 | 1000 | 257 | ok |
| yolo26-l_640x640.dxnn | 2 | 3 | 68.2 ±0.4 | 34.1 | 164 | 73.8 | 91.3 | 73~74 | 1000 | 265 | ok |
| yolo26-l_640x640.dxnn | 3 | 3 | 68.4 ±0.3 | 22.8 | 164 | 74.3 | 94.3 | 76 | 1000 | 271 | ok |
| yolo26-x_640x640.dxnn | 1 | 3 | 47.1 ±0.4 | 47.1 | 136 | 91.5 | 100.0 | 73~78 | 800~1000 | 354 | ok |
| yolo26-x_640x640.dxnn | 2 | 3 | 40.7 ±0.2 | 20.4 | 125 | 90.2 | 100.0 | 81 | 800~1000 | 359 | ok |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_640x640.dxnn | 3 | 3 | 99.3 ±0.0 | 33.1 | 216 | 23.5 | 73.5 | 54~55 | 1000 | 220 | ok |
| yolo26-n_640x640.dxnn | 4 | 3 | 99.4 ±0.1 | 24.8 | 219 | 23.7 | 73.5 | 55~56 | 1000 | 233 | ok |
| yolo26-s_640x640.dxnn | 3 | 3 | 98.6 ±0.4 | 32.9 | 214 | 43.4 | 69.1 | 60~61 | 1000 | 242 | ok |
| yolo26-s_640x640.dxnn | 4 | 3 | 98.8 ±0.1 | 24.7 | 213 | 43.9 | 69.1 | 62 | 1000 | 250 | ok |
| yolo26-m_640x640.dxnn | 3 | 3 | 97.2 ±0.6 | 32.4 | 214 | 76.7 | 91.5 | 76~79 | 1000 | 273 | ok |
| yolo26-m_640x640.dxnn | 4 | 3 | 94.6 ±0.4 | 23.6 | 222 | 80.5 | 94.3 | 81 | 800~1000 | 284 | ok |
| yolo26-l_640x640.dxnn | 2 | 3 | 82.8 ±0.5 | 41.4 | 214 | 88.9 | 100.0 | 76~79 | 1000 | 278 | ok |
| yolo26-l_640x640.dxnn | 3 | 3 | 77.2 ±0.7 | 25.7 | 209 | 90.2 | 100.0 | 80~81 | 800~1000 | 286 | ok |
| yolo26-x_640x640.dxnn | 1 | 3 | 47.3 ±0.9 | 47.3 | 155 | 93.2 | 100.0 | 74~78 | 800~1000 | 358 | ok |
| yolo26-x_640x640.dxnn | 2 | 3 | 40.6 ±0.3 | 20.3 | 143 | 94.2 | 100.0 | 82 | 600~1000 | 367 | ok |

**Channel Capacity Summary** (max streams where per-channel FPS ≥ 30)

| Model | ORT ON Capacity | Per-Ch FPS | ORT OFF Capacity | Per-Ch FPS |
|-------|-----------------|------------|------------------|------------|
| yolo26-n_640x640.dxnn | 3 | 37.4 | 3 | 33.1 |
| yolo26-s_640x640.dxnn | 3 | 31.9 | 3 | 32.9 |
| yolo26-m_640x640.dxnn | 2 | 39.3 | 3 | 32.4 |
| yolo26-l_640x640.dxnn | 2 | 34.1 | 2 | 41.4 |
| yolo26-x_640x640.dxnn | 1 | 47.1 | 1 | 47.3 |

### Pose Estimation

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-pose_640x640.dxnn | 4 | 3 | 143.7 ±0.6 | 35.9 | 210 | 43.6 | 65.5 | 59~61 | 1000 | 207 | ok |
| yolo26-n-pose_640x640.dxnn | 5 | 3 | 144.1 ±1.4 | 28.8 | 210 | 44.1 | 64.8 | 63 | 1000 | 212 | ok |
| yolo26-s-pose_640x640.dxnn | 3 | 3 | 115.2 ±1.1 | 38.4 | 187 | 61.3 | 76.9 | 65~66 | 1000 | 222 | ok |
| yolo26-s-pose_640x640.dxnn | 4 | 3 | 115.2 ±1.0 | 28.8 | 187 | 61.9 | 78.0 | 68 | 1000 | 230 | ok |
| yolo26-m-pose_640x640.dxnn | 3 | 3 | 91.7 ±1.2 | 30.6 | 161 | 79.8 | 98.3 | 78~81 | 800~1000 | 254 | ok |
| yolo26-m-pose_640x640.dxnn | 4 | 3 | 86.3 ±0.7 | 21.6 | 158 | 82.0 | 99.8 | 82 | 600~1000 | 262 | ok |
| yolo26-l-pose_640x640.dxnn | 2 | 3 | 76.1 ±2.4 | 38.0 | 149 | 86.9 | 100.0 | 79~81 | 800~1000 | 261 | ok |
| yolo26-l-pose_640x640.dxnn | 3 | 3 | 70.0 ±0.2 | 23.3 | 145 | 87.5 | 100.0 | 82 | 600~1000 | 268 | ok |
| yolo26-x-pose_640x640.dxnn | 1 | 3 | 44.6 ±2.3 | 44.6 | 106 | 92.6 | 100.0 | 76~80 | 800~1000 | 369 | ok |
| yolo26-x-pose_640x640.dxnn | 2 | 3 | 36.5 ±0.4 | 18.3 | 97 | 93.2 | 100.0 | 82 | 600~1000 | 369 | ok |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-pose_640x640.dxnn | 5 | 3 | 171.6 ±0.2 | 34.3 | 190 | 52.6 | 71.4 | 61~63 | 1000 | 209 | ok |
| yolo26-n-pose_640x640.dxnn | 6 | 3 | 171.6 ±0.5 | 28.6 | 190 | 52.6 | 70.9 | 64 | 1000 | 214 | ok |
| yolo26-s-pose_640x640.dxnn | 4 | 3 | 133.4 ±0.4 | 33.4 | 170 | 71.2 | 87.4 | 66~68 | 1000 | 223 | ok |
| yolo26-s-pose_640x640.dxnn | 5 | 3 | 133.1 ±0.5 | 26.6 | 171 | 71.1 | 86.7 | 70 | 1000 | 230 | ok |
| yolo26-m-pose_640x640.dxnn | 3 | 3 | 98.2 ±3.9 | 32.7 | 145 | 88.3 | 100.0 | 80~82 | 600~1000 | 242 | ok |
| yolo26-m-pose_640x640.dxnn | 4 | 3 | 93.0 ±0.1 | 23.3 | 139 | 91.4 | 100.0 | 82~83 | 600~1000 | 254 | ok |
| yolo26-l-pose_640x640.dxnn | 2 | 3 | 82.0 ±2.1 | 41.0 | 125 | 92.3 | 100.0 | 78~80 | 800~1000 | 250 | ok |
| yolo26-l-pose_640x640.dxnn | 3 | 3 | 74.6 ±0.2 | 24.9 | 119 | 92.4 | 100.0 | 81 | 800~1000 | 259 | ok |
| yolo26-x-pose_640x640.dxnn | 1 | 3 | 45.2 ±1.8 | 45.2 | 89 | 93.2 | 100.0 | 76~80 | 800~1000 | 352 | ok |
| yolo26-x-pose_640x640.dxnn | 2 | 3 | 38.5 ±1.1 | 19.3 | 80 | 94.7 | 100.0 | 82~83 | 600~1000 | 352 | ok |

**Channel Capacity Summary** (max streams where per-channel FPS ≥ 30)

| Model | ORT ON Capacity | Per-Ch FPS | ORT OFF Capacity | Per-Ch FPS |
|-------|-----------------|------------|------------------|------------|
| yolo26-n-pose_640x640.dxnn | 4 | 35.9 | 5 | 34.3 |
| yolo26-s-pose_640x640.dxnn | 3 | 38.4 | 4 | 33.4 |
| yolo26-m-pose_640x640.dxnn | 3 | 30.6 | 3 | 32.7 |
| yolo26-l-pose_640x640.dxnn | 2 | 38.0 | 2 | 41.0 |
| yolo26-x-pose_640x640.dxnn | 1 | 44.6 | 1 | 45.2 |

### Segmentation

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-seg_640x640.dxnn | 2 | 3 | 73.3 ±1.8 | 36.7 | 251 | 25.7 | 50.2 | 58~60 | 1000 | 306 | ok |
| yolo26-n-seg_640x640.dxnn | 3 | 3 | 72.4 ±0.2 | 24.1 | 254 | 25.6 | 48.1 | 61 | 1000 | 317 | ok |
| yolo26-s-seg_640x640.dxnn | 2 | 3 | 64.9 ±1.3 | 32.4 | 228 | 41.9 | 64.7 | 65~67 | 1000 | 329 | ok |
| yolo26-s-seg_640x640.dxnn | 3 | 3 | 64.8 ±0.5 | 21.6 | 229 | 42.0 | 65.1 | 68~69 | 1000 | 342 | ok |
| yolo26-m-seg_640x640.dxnn | 1 | 3 | 52.3 ±1.0 | 52.3 | 198 | 61.9 | 82.5 | 73~76 | 1000 | 346 | ok |
| yolo26-m-seg_640x640.dxnn | 2 | 3 | 50.2 ±1.0 | 25.1 | 201 | 65.1 | 90.1 | 81~82 | 600~1000 | 365 | ok |
| yolo26-l-seg_640x640.dxnn | 1 | 3 | 47.6 ±0.4 | 47.6 | 194 | 68.6 | 89.7 | 74~78 | 1000 | 360 | ok |
| yolo26-l-seg_640x640.dxnn | 2 | 3 | 44.3 ±0.2 | 22.1 | 187 | 74.5 | 95.9 | 82~83 | 600~1000 | 379 | ok |
| yolo26-x-seg_640x640.dxnn | 1 | 3 | 26.0 ±2.7 | 26.0 | 126 | 88.7 | 100.0 | 81~82 | 600~1000 | 466 | ok |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-seg_640x640.dxnn | 2 | 3 | 83.9 ±0.1 | 42.0 | 268 | 25.1 | 81.4 | 60~62 | 1000 | 329 | ok |
| yolo26-n-seg_640x640.dxnn | 3 | 3 | 83.9 ±0.1 | 28.0 | 277 | 25.8 | 80.5 | 63~64 | 1000 | 342 | ok |
| yolo26-s-seg_640x640.dxnn | 2 | 3 | 75.6 ±0.1 | 37.8 | 263 | 48.5 | 75.7 | 66~68 | 1000 | 352 | ok |
| yolo26-s-seg_640x640.dxnn | 3 | 3 | 75.8 ±0.5 | 25.3 | 264 | 48.8 | 74.3 | 71~72 | 1000 | 366 | ok |
| yolo26-m-seg_640x640.dxnn | 2 | 3 | 53.5 ±2.1 | 26.8 | 212 | 80.2 | 100.0 | 82~83 | 400~1000 | 388 | ok |
| yolo26-m-seg_640x640.dxnn | 1 | 3 | 61.0 ±0.5 | 61.0 | 228 | 71.4 | 90.7 | 72~77 | 1000 | 368 | ok |
| yolo26-l-seg_640x640.dxnn | 1 | 3 | 55.0 ±1.4 | 55.0 | 207 | 79.8 | 100.0 | 75~80 | 1000 | 379 | ok |
| yolo26-l-seg_640x640.dxnn | 2 | 3 | 45.5 ±0.4 | 22.7 | 185 | 89.3 | 100.0 | 82~83 | 400~1000 | 396 | ok |
| yolo26-x-seg_640x640.dxnn | 1 | 3 | 25.6 ±2.6 | 25.6 | 127 | 89.9 | 100.0 | 81~82 | 600~1000 | 479 | ok |

**Channel Capacity Summary** (max streams where per-channel FPS ≥ 30)

| Model | ORT ON Capacity | Per-Ch FPS | ORT OFF Capacity | Per-Ch FPS |
|-------|-----------------|------------|------------------|------------|
| yolo26-n-seg_640x640.dxnn | 2 | 36.7 | 2 | 42.0 |
| yolo26-s-seg_640x640.dxnn | 2 | 32.4 | 2 | 37.8 |
| yolo26-m-seg_640x640.dxnn | 1 | 52.3 | 1 | 61.0 |
| yolo26-l-seg_640x640.dxnn | 1 | 47.6 | 1 | 55.0 |

### Oriented BBox (OBB)

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | 2 | 3 | 74.2 ±0.6 | 37.1 | 167 | 66.5 | 87.3 | 62~63 | 1000 | 231 | ok |
| yolo26-n-obb_1024x1024.dxnn | 3 | 3 | 73.7 ±0.2 | 24.6 | 167 | 66.8 | 85.3 | 65~66 | 1000 | 243 | ok |
| yolo26-s-obb_1024x1024.dxnn | 1 | 3 | 56.0 ±0.6 | 56.0 | 141 | 83.8 | 100.0 | 64~66 | 1000 | 239 | ok |
| yolo26-s-obb_1024x1024.dxnn | 2 | 3 | 56.2 ±0.2 | 28.1 | 144 | 86.6 | 100.0 | 70~72 | 1000 | 254 | ok |
| yolo26-m-obb_1024x1024.dxnn | 1 | 3 | 40.5 ±0.1 | 40.5 | 111 | 92.3 | 100.0 | 73~78 | 1000 | 272 | ok |
| yolo26-m-obb_1024x1024.dxnn | 2 | 3 | 34.8 ±0.4 | 17.4 | 109 | 91.7 | 100.0 | 81~82 | 800~1000 | 287 | ok |
| yolo26-l-obb_1024x1024.dxnn | 1 | 3 | 30.0 ±0.0 | 30.0 | 97 | 93.1 | 100.0 | 73~78 | 1000 | 288 | ok |
| yolo26-x-obb_1024x1024.dxnn | 1 | 3 | 14.4 ±0.9 | 14.4 | 58 | 91.7 | 100.0 | 81~82 | 600~1000 | 391 | ok |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | 2 | 3 | 86.2 ±0.3 | 43.1 | 190 | 77.9 | 97.9 | 64~65 | 1000 | 231 | ok |
| yolo26-n-obb_1024x1024.dxnn | 3 | 3 | 85.9 ±0.2 | 28.6 | 192 | 79.1 | 93.9 | 66~68 | 1000 | 244 | ok |
| yolo26-s-obb_1024x1024.dxnn | 2 | 3 | 61.0 ±0.2 | 30.5 | 158 | 93.5 | 100.0 | 70~72 | 1000 | 257 | ok |
| yolo26-s-obb_1024x1024.dxnn | 3 | 3 | 61.0 ±0.1 | 20.3 | 156 | 94.2 | 100.0 | 74~76 | 1000 | 267 | ok |
| yolo26-m-obb_1024x1024.dxnn | 1 | 3 | 40.7 ±0.1 | 40.7 | 119 | 93.1 | 100.0 | 74~78 | 1000 | 271 | ok |
| yolo26-m-obb_1024x1024.dxnn | 2 | 3 | 34.2 ±0.8 | 17.1 | 116 | 92.5 | 100.0 | 82 | 600~1000 | 287 | ok |
| yolo26-l-obb_1024x1024.dxnn | 1 | 3 | 30.2 ±0.1 | 30.2 | 106 | 93.7 | 100.0 | 73~79 | 1000 | 285 | ok |
| yolo26-l-obb_1024x1024.dxnn | 2 | 3 | 25.8 ±0.1 | 12.9 | 99 | 92.3 | 100.0 | 81~82 | 600~1000 | 303 | ok |
| yolo26-x-obb_1024x1024.dxnn | 1 | 3 | 14.9 ±0.9 | 14.9 | 61 | 91.8 | 100.0 | 80~81 | 600~1000 | 389 | ok |

**Channel Capacity Summary** (max streams where per-channel FPS ≥ 30)

| Model | ORT ON Capacity | Per-Ch FPS | ORT OFF Capacity | Per-Ch FPS |
|-------|-----------------|------------|------------------|------------|
| yolo26-n-obb_1024x1024.dxnn | 2 | 37.1 | 2 | 43.1 |
| yolo26-s-obb_1024x1024.dxnn | 1 | 56.0 | 2 | 30.5 |
| yolo26-m-obb_1024x1024.dxnn | 1 | 40.5 | 1 | 40.7 |
| yolo26-l-obb_1024x1024.dxnn | < 1 | — | 1 | 30.2 |

---
*Report generated by dx-benchmark tool*
