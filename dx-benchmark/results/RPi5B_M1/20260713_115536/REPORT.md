# YOLO26 Benchmark Report

**Generated:** 2026-07-14 08:13:19 (Local)

## Test Timing

| # | Type | Start | End | Duration |
|---|------|-------|-----|----------|
| 1 | run | 2026-07-13 11:55:36 | 2026-07-14 08:13:19 | 20h 17m 43s |

## Executive Summary

### Object Detection

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26-n_640x640.dxnn | ON | 22.62 | 100.2 | 64.6 | 2 |
| yolo26-n_640x640.dxnn | OFF | 21.19 | 179.0 | 77.2 | 2 |
| yolo26-s_640x640.dxnn | ON | 30.03 | 101.1 | 64.7 | 2 |
| yolo26-s_640x640.dxnn | OFF | 27.07 | 172.8 | 77.5 | 2 |
| yolo26-m_640x640.dxnn | ON | 36.22 | 99.3 | 63.9 | 2 |
| yolo26-m_640x640.dxnn | OFF | 34.84 | 119.1 | 76.8 | 2 |
| yolo26-l_640x640.dxnn | ON | 44.03 | 89.8 | 63.6 | 2 |
| yolo26-l_640x640.dxnn | OFF | 40.80 | 86.5 | 76.2 | 2 |
| yolo26-x_640x640.dxnn | ON | 69.49 | 48.8 | 48.7 | 1 |
| yolo26-x_640x640.dxnn | OFF | 68.39 | 48.6 | 48.9 | 1 |

### Pose Estimation

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26-n-pose_640x640.dxnn | ON | 19.34 | 143.0 | 78.6 | 2 |
| yolo26-n-pose_640x640.dxnn | OFF | 17.80 | 248.1 | 108.0 | 3 |
| yolo26-s-pose_640x640.dxnn | ON | 25.02 | 142.7 | 78.2 | 2 |
| yolo26-s-pose_640x640.dxnn | OFF | 24.05 | 181.9 | 107.9 | 3 |
| yolo26-m-pose_640x640.dxnn | ON | 32.50 | 115.6 | 78.3 | 2 |
| yolo26-m-pose_640x640.dxnn | OFF | 30.88 | 114.4 | 105.1 | 3 |
| yolo26-l-pose_640x640.dxnn | ON | 40.74 | 84.8 | 77.7 | 2 |
| yolo26-l-pose_640x640.dxnn | OFF | 38.15 | 85.3 | 84.9 | 2 |
| yolo26-x-pose_640x640.dxnn | ON | 67.35 | 47.2 | 47.9 | 1 |
| yolo26-x-pose_640x640.dxnn | OFF | 64.76 | 46.1 | 47.6 | 1 |

### Segmentation

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26-n-seg_640x640.dxnn | ON | 37.68 | 64.5 | 42.9 | 1 |
| yolo26-n-seg_640x640.dxnn | OFF | 39.12 | 95.4 | 52.8 | 1 |
| yolo26-s-seg_640x640.dxnn | ON | 47.35 | 64.2 | 42.8 | 1 |
| yolo26-s-seg_640x640.dxnn | OFF | 43.97 | 95.6 | 52.2 | 1 |
| yolo26-m-seg_640x640.dxnn | ON | 59.91 | 64.4 | 42.1 | 1 |
| yolo26-m-seg_640x640.dxnn | OFF | 56.86 | 78.6 | 51.6 | 1 |
| yolo26-l-seg_640x640.dxnn | ON | 67.61 | 62.4 | 41.8 | 1 |
| yolo26-l-seg_640x640.dxnn | OFF | 65.25 | 64.7 | 50.6 | 1 |
| yolo26-x-seg_640x640.dxnn | ON | 105.84 | 34.4 | 32.5 | 1 |
| yolo26-x-seg_640x640.dxnn | OFF | 102.31 | 34.3 | 34.5 | 1 |

### Oriented BBox (OBB)

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26-n-obb_1024x1024.dxnn | ON | 35.46 | 103.9 | 66.5 | 2 |
| yolo26-n-obb_1024x1024.dxnn | OFF | 33.99 | 97.6 | 78.3 | 2 |
| yolo26-s-obb_1024x1024.dxnn | ON | 50.18 | 60.1 | 62.1 | 2 |
| yolo26-s-obb_1024x1024.dxnn | OFF | 49.62 | 60.3 | 61.6 | 2 |
| yolo26-m-obb_1024x1024.dxnn | ON | 68.20 | 40.1 | 41.2 | 1 |
| yolo26-m-obb_1024x1024.dxnn | OFF | 67.32 | 40.9 | 41.9 | 1 |
| yolo26-l-obb_1024x1024.dxnn | ON | 87.87 | 29.6 | 30.6 | 1 |
| yolo26-l-obb_1024x1024.dxnn | OFF | 85.41 | 29.6 | 31.0 | 1 |
| yolo26-x-obb_1024x1024.dxnn | ON | 155.43 | 16.5 | 16.7 | — |
| yolo26-x-obb_1024x1024.dxnn | OFF | 154.06 | 16.5 | 16.7 | — |

### Classification

| Model | ORT | Latency (ms) | Throughput (FPS) | E2E FPS | Max Channels |
|-------|-----|:------------:|:----------------:|:-------:|:------------:|
| yolo26-n_224x224.dxnn | ON | 1.41 | 3486.2 | 182.2 | — |
| yolo26-n_224x224.dxnn | OFF | 1.41 | 3490.0 | 182.2 | — |
| yolo26-s_224x224.dxnn | ON | 2.05 | 2004.1 | 181.6 | — |
| yolo26-s_224x224.dxnn | OFF | 2.08 | 2004.0 | 182.6 | — |
| yolo26-m_224x224.dxnn | ON | 2.54 | 1370.2 | 182.6 | — |
| yolo26-m_224x224.dxnn | OFF | 2.66 | 1369.1 | 182.0 | — |
| yolo26-l_224x224.dxnn | ON | 3.89 | 873.1 | 181.9 | — |
| yolo26-l_224x224.dxnn | OFF | 3.88 | 872.2 | 182.2 | — |
| yolo26-x_224x224.dxnn | ON | 6.43 | 482.3 | 181.2 | — |
| yolo26-x_224x224.dxnn | OFF | 6.33 | 483.9 | 181.0 | — |

## Environment

| Item | Value |
|------|-------|
| Product | RPi5B |
| Hostname | raspberrypi |
| OS | Debian GNU/Linux 12 (bookworm) |
| Kernel | 6.12.93+rpt-rpi-2712 |
| CPU | Cortex-A76 |
| CPU Cores | 4 |
| RAM | 7.9 GB |
| NPU SKU | M1 |
| NPU RT | v3.4.0 |
| NPU Driver (RT) | v2.5.1 |
| NPU Driver (PCIe) | v2.4.1 |
| NPU Firmware | v2.7.1 |
| NPU Memory | LPDDR5 5600 Mbps, 3.92GiB |
| NPU Board | M.2, Rev 1.0 |
| NPU PCIe | Gen3 X1 [01:00:00] |

### Tools

| Tool | Available | Version |
|------|-----------|---------|
| run_model | Yes | DXRT v3.4.0 run_model |
| gst-launch-1.0 | Yes | gst-launch-1.0 version 1.22.0 |
| gst-inspect-1.0 | Yes | gst-inspect-1.0 version 1.22.0 |
| dxtop | Yes | DX-TOP 1.1.0 |
| ffprobe | Yes | ffprobe version 5.1.9-0+deb12u1+rpt1 Copyright (c) 2007-2026... |

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
| yolo26-n_640x640.dxnn | 100.2 ±0.0 | 188 | 22.3 | 68.6 | 37~38 | 1000 | ok |
| yolo26-s_640x640.dxnn | 101.1 ±1.0 | 186 | 42.2 | 74.6 | 43~44 | 1000 | ok |
| yolo26-m_640x640.dxnn | 99.3 ±1.0 | 188 | 72.2 | 85.0 | 51~54 | 1000 | ok |
| yolo26-l_640x640.dxnn | 89.8 ±0.0 | 141 | 90.8 | 100.0 | 52~57 | 1000 | ok |
| yolo26-x_640x640.dxnn | 48.8 ±0.0 | 72 | 88.3 | 100.0 | 53~58 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n_640x640.dxnn | 179.0 ±0.1 | 107 | 43.8 | 74.5 | 42~43 | 1000 | ok |
| yolo26-s_640x640.dxnn | 172.8 ±0.8 | 108 | 80.9 | 92.2 | 48~50 | 1000 | ok |
| yolo26-m_640x640.dxnn | 119.1 ±1.2 | 73 | 91.2 | 100.0 | 52~57 | 1000 | ok |
| yolo26-l_640x640.dxnn | 86.5 ±1.1 | 59 | 91.8 | 100.0 | 52~56 | 1000 | ok |
| yolo26-x_640x640.dxnn | 48.6 ±1.2 | 34 | 90.2 | 100.0 | 54~59 | 1000 | ok |

#### Pose Estimation

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-pose_640x640.dxnn | 143.0 ±1.8 | 181 | 37.1 | 70.4 | 46 | 1000 | ok |
| yolo26-s-pose_640x640.dxnn | 142.7 ±1.6 | 180 | 68.9 | 84.0 | 47~49 | 1000 | ok |
| yolo26-m-pose_640x640.dxnn | 115.6 ±0.2 | 117 | 91.4 | 100.0 | 53~58 | 1000 | ok |
| yolo26-l-pose_640x640.dxnn | 84.8 ±1.2 | 79 | 90.3 | 100.0 | 52~57 | 1000 | ok |
| yolo26-x-pose_640x640.dxnn | 47.2 ±0.6 | 45 | 88.7 | 100.0 | 54~59 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-pose_640x640.dxnn | 248.1 ±4.6 | 107 | 71.9 | 86.1 | 45~47 | 1000 | ok |
| yolo26-s-pose_640x640.dxnn | 181.9 ±0.9 | 74 | 92.3 | 100.0 | 50~53 | 1000 | ok |
| yolo26-m-pose_640x640.dxnn | 114.4 ±1.3 | 49 | 91.8 | 100.0 | 53~58 | 1000 | ok |
| yolo26-l-pose_640x640.dxnn | 85.3 ±0.2 | 37 | 90.5 | 100.0 | 53~57 | 1000 | ok |
| yolo26-x-pose_640x640.dxnn | 46.1 ±0.2 | 22 | 88.6 | 100.0 | 54~59 | 1000 | ok |

#### Segmentation

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-seg_640x640.dxnn | 64.5 ±0.2 | 222 | 18.6 | 59.7 | 45 | 1000 | ok |
| yolo26-s-seg_640x640.dxnn | 64.2 ±0.3 | 233 | 35.0 | 76.2 | 45~46 | 1000 | ok |
| yolo26-m-seg_640x640.dxnn | 64.4 ±0.4 | 209 | 69.8 | 84.1 | 52~57 | 1000 | ok |
| yolo26-l-seg_640x640.dxnn | 62.4 ±0.0 | 180 | 85.5 | 99.3 | 54~59 | 1000 | ok |
| yolo26-x-seg_640x640.dxnn | 34.4 ±0.2 | 81 | 88.5 | 100.0 | 56~61 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-seg_640x640.dxnn | 95.4 ±0.2 | 145 | 27.6 | 86.8 | 43~44 | 1000 | ok |
| yolo26-s-seg_640x640.dxnn | 95.6 ±0.1 | 124 | 53.6 | 88.0 | 48~50 | 1000 | ok |
| yolo26-m-seg_640x640.dxnn | 78.6 ±0.6 | 104 | 88.9 | 100.0 | 55~61 | 1000 | ok |
| yolo26-l-seg_640x640.dxnn | 64.7 ±0.0 | 83 | 90.7 | 100.0 | 54~60 | 1000 | ok |
| yolo26-x-seg_640x640.dxnn | 34.3 ±0.2 | 48 | 88.8 | 100.0 | 56~62 | 1000 | ok |

#### Oriented BBox (OBB)

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | 103.9 ±0.1 | 114 | 90.8 | 100.0 | 49~51 | 1000 | ok |
| yolo26-s-obb_1024x1024.dxnn | 60.1 ±0.3 | 69 | 91.1 | 100.0 | 50~52 | 1000 | ok |
| yolo26-m-obb_1024x1024.dxnn | 40.1 ±0.5 | 44 | 91.2 | 100.0 | 53~58 | 1000 | ok |
| yolo26-l-obb_1024x1024.dxnn | 29.6 ±0.0 | 33 | 87.9 | 100.0 | 53~57 | 1000 | ok |
| yolo26-x-obb_1024x1024.dxnn | 16.5 ±0.0 | 19 | 86.6 | 100.0 | 55~59 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | 97.6 ±0.4 | 56 | 91.7 | 100.0 | 48~51 | 1000 | ok |
| yolo26-s-obb_1024x1024.dxnn | 60.3 ±0.4 | 36 | 90.6 | 100.0 | 49~52 | 1000 | ok |
| yolo26-m-obb_1024x1024.dxnn | 40.9 ±1.1 | 24 | 90.9 | 100.0 | 53~57 | 1000 | ok |
| yolo26-l-obb_1024x1024.dxnn | 29.6 ±0.1 | 19 | 90.9 | 100.0 | 53~57 | 1000 | ok |
| yolo26-x-obb_1024x1024.dxnn | 16.5 ±0.0 | 10 | 86.6 | 100.0 | 55~59 | 1000 | ok |

#### Classification

**ORT = ON**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n_224x224.dxnn | 3486.2 ±7.2 | 58 | 86.3 | 94.6 | 47~48 | 1000 | ok |
| yolo26-s_224x224.dxnn | 2004.1 ±3.4 | 39 | 88.3 | 97.5 | 48~50 | 1000 | ok |
| yolo26-m_224x224.dxnn | 1370.2 ±1.2 | 28 | 89.8 | 97.6 | 50~54 | 1000 | ok |
| yolo26-l_224x224.dxnn | 873.1 ±1.8 | 18 | 90.0 | 98.3 | 50~52 | 1000 | ok |
| yolo26-x_224x224.dxnn | 482.3 ±0.7 | 10 | 89.6 | 99.3 | 51~54 | 1000 | ok |

**ORT = OFF**

| Model | FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | Status |
|-------|-----|------|----------|----------|-------------|---------|--------|
| yolo26-n_224x224.dxnn | 3490.0 ±4.4 | 58 | 85.6 | 94.7 | 47 | 1000 | ok |
| yolo26-s_224x224.dxnn | 2004.0 ±4.5 | 38 | 89.2 | 97.1 | 43~46 | 1000 | ok |
| yolo26-m_224x224.dxnn | 1369.1 ±4.0 | 28 | 90.3 | 97.4 | 51~54 | 1000 | ok |
| yolo26-l_224x224.dxnn | 872.2 ±2.0 | 18 | 89.7 | 98.3 | 49~52 | 1000 | ok |
| yolo26-x_224x224.dxnn | 483.9 ±0.9 | 11 | 89.6 | 99.2 | 51~55 | 1000 | ok |

### Latency (Single-Core, Sync)

#### Object Detection

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n_640x640.dxnn | 44.2 | 22.62 | 20.14 | 2.48 | 35 | ok |
| yolo26-s_640x640.dxnn | 33.3 | 30.03 | 27.58 | 2.45 | 41 | ok |
| yolo26-m_640x640.dxnn | 27.6 | 36.22 | 33.68 | 2.55 | 45 | ok |
| yolo26-l_640x640.dxnn | 22.7 | 44.03 | 41.43 | 2.59 | 45 | ok |
| yolo26-x_640x640.dxnn | 14.4 | 69.49 | 66.93 | 2.55 | 45 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n_640x640.dxnn | 47.2 | 21.19 | 21.19 | N/A | 40 | ok |
| yolo26-s_640x640.dxnn | 36.9 | 27.07 | 27.07 | N/A | 44 | ok |
| yolo26-m_640x640.dxnn | 28.7 | 34.84 | 34.84 | N/A | 45 | ok |
| yolo26-l_640x640.dxnn | 24.5 | 40.80 | 40.80 | N/A | 45 | ok |
| yolo26-x_640x640.dxnn | 14.6 | 68.39 | 68.39 | N/A | 46 | ok |

#### Pose Estimation

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-pose_640x640.dxnn | 51.7 | 19.34 | 17.86 | 1.49 | 44 | ok |
| yolo26-s-pose_640x640.dxnn | 40.0 | 25.02 | 23.53 | 1.49 | 44 | ok |
| yolo26-m-pose_640x640.dxnn | 30.8 | 32.50 | 30.97 | 1.53 | 45 | ok |
| yolo26-l-pose_640x640.dxnn | 24.5 | 40.74 | 39.21 | 1.53 | 45 | ok |
| yolo26-x-pose_640x640.dxnn | 14.8 | 67.35 | 65.75 | 1.59 | 46 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-pose_640x640.dxnn | 56.2 | 17.80 | 17.80 | N/A | 42 | ok |
| yolo26-s-pose_640x640.dxnn | 41.6 | 24.05 | 24.05 | N/A | 45 | ok |
| yolo26-m-pose_640x640.dxnn | 32.4 | 30.88 | 30.88 | N/A | 45 | ok |
| yolo26-l-pose_640x640.dxnn | 26.2 | 38.15 | 38.15 | N/A | 45 | ok |
| yolo26-x-pose_640x640.dxnn | 15.4 | 64.76 | 64.76 | N/A | 46 | ok |

#### Segmentation

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-seg_640x640.dxnn | 26.5 | 37.68 | 34.66 | 3.01 | 44 | ok |
| yolo26-s-seg_640x640.dxnn | 21.1 | 47.35 | 44.20 | 3.14 | 42 | ok |
| yolo26-m-seg_640x640.dxnn | 16.7 | 59.91 | 56.87 | 3.05 | 45 | ok |
| yolo26-l-seg_640x640.dxnn | 14.8 | 67.61 | 64.51 | 3.10 | 45 | ok |
| yolo26-x-seg_640x640.dxnn | 9.4 | 105.84 | 102.71 | 3.13 | 46 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-seg_640x640.dxnn | 25.6 | 39.12 | 39.12 | N/A | 42 | ok |
| yolo26-s-seg_640x640.dxnn | 22.7 | 43.97 | 43.97 | N/A | 45 | ok |
| yolo26-m-seg_640x640.dxnn | 17.6 | 56.86 | 56.86 | N/A | 45 | ok |
| yolo26-l-seg_640x640.dxnn | 15.3 | 65.25 | 65.25 | N/A | 45 | ok |
| yolo26-x-seg_640x640.dxnn | 9.8 | 102.31 | 102.31 | N/A | 46 | ok |

#### Oriented BBox (OBB)

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-obb_1024x1024.dxnn | 28.2 | 35.46 | 33.67 | 1.80 | 45 | ok |
| yolo26-s-obb_1024x1024.dxnn | 19.9 | 50.18 | 48.46 | 1.72 | 45 | ok |
| yolo26-m-obb_1024x1024.dxnn | 14.7 | 68.20 | 66.45 | 1.75 | 46 | ok |
| yolo26-l-obb_1024x1024.dxnn | 11.4 | 87.87 | 86.12 | 1.75 | 46 | ok |
| yolo26-x-obb_1024x1024.dxnn | 6.4 | 155.43 | 153.60 | 1.83 | 47 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n-obb_1024x1024.dxnn | 29.4 | 33.99 | 33.99 | N/A | 45 | ok |
| yolo26-s-obb_1024x1024.dxnn | 20.2 | 49.62 | 49.62 | N/A | 45 | ok |
| yolo26-m-obb_1024x1024.dxnn | 14.9 | 67.32 | 67.32 | N/A | 46 | ok |
| yolo26-l-obb_1024x1024.dxnn | 11.7 | 85.41 | 85.41 | N/A | 46 | ok |
| yolo26-x-obb_1024x1024.dxnn | 6.5 | 154.06 | 154.06 | N/A | 48 | ok |

#### Classification

**ORT = ON**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n_224x224.dxnn | 709.9 | 1.41 | 1.41 | N/A | 44 | ok |
| yolo26-s_224x224.dxnn | 486.7 | 2.05 | 2.05 | N/A | 44 | ok |
| yolo26-m_224x224.dxnn | 393.1 | 2.54 | 2.54 | N/A | 44 | ok |
| yolo26-l_224x224.dxnn | 257.3 | 3.89 | 3.89 | N/A | 45 | ok |
| yolo26-x_224x224.dxnn | 155.6 | 6.43 | 6.43 | N/A | 45 | ok |

**ORT = OFF**

| Model | FPS | Total ms | NPU ms | CPU ms | NPU Temp °C | Status |
|-------|-----|----------|--------|--------|-------------|--------|
| yolo26-n_224x224.dxnn | 708.1 | 1.41 | 1.41 | N/A | 44 | ok |
| yolo26-s_224x224.dxnn | 480.8 | 2.08 | 2.08 | N/A | 39 | ok |
| yolo26-m_224x224.dxnn | 375.7 | 2.66 | 2.66 | N/A | 45 | ok |
| yolo26-l_224x224.dxnn | 257.5 | 3.88 | 3.88 | N/A | 45 | ok |
| yolo26-x_224x224.dxnn | 158.0 | 6.33 | 6.33 | N/A | 45 | ok |

## E2E Pipeline (Single-Stream)

### Object Detection

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_640x640.dxnn | avdec_h264 | 3455 | 3 | 64.6 ±0.1 | 53.45 | 317 | 16.1 | 38.1 | 38~39 | 1000 | 319 | ok |
| yolo26-s_640x640.dxnn | avdec_h264 | 3455 | 3 | 64.7 ±0.1 | 53.43 | 312 | 28.3 | 58.3 | 44 | 1000 | 343 | ok |
| yolo26-m_640x640.dxnn | avdec_h264 | 3455 | 3 | 63.9 ±0.2 | 54.04 | 302 | 45.5 | 74.3 | 55~56 | 1000 | 373 | ok |
| yolo26-l_640x640.dxnn | avdec_h264 | 3455 | 3 | 63.6 ±0.4 | 54.30 | 287 | 62.3 | 83.6 | 45~51 | 1000 | 387 | ok |
| yolo26-x_640x640.dxnn | avdec_h264 | 3455 | 3 | 48.7 ±0.1 | 71.01 | 152 | 93.5 | 100.0 | 65~71 | 1000 | 481 | ok |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_640x640.dxnn | avdec_h264 | 3455 | 3 | 77.2 ±0.2 | 44.76 | 309 | 17.7 | 55.0 | 42 | 1000 | 350 | ok |
| yolo26-s_640x640.dxnn | avdec_h264 | 3455 | 3 | 77.5 ±0.3 | 44.58 | 304 | 32.1 | 70.3 | 39~40 | 1000 | 371 | ok |
| yolo26-m_640x640.dxnn | avdec_h264 | 3455 | 3 | 76.8 ±0.5 | 44.98 | 303 | 53.1 | 86.8 | 58 | 1000 | 401 | ok |
| yolo26-l_640x640.dxnn | avdec_h264 | 3455 | 3 | 76.2 ±0.0 | 45.33 | 305 | 74.5 | 89.0 | 59~62 | 1000 | 417 | ok |
| yolo26-x_640x640.dxnn | avdec_h264 | 3455 | 3 | 48.9 ±0.1 | 70.62 | 163 | 94.0 | 100.0 | 67~72 | 1000 | 489 | ok |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26-n_640x640.dxnn | 64.6 | 77.2 | -12.6 | -16.3% |
| yolo26-s_640x640.dxnn | 64.7 | 77.5 | -12.8 | -16.6% |
| yolo26-m_640x640.dxnn | 63.9 | 76.8 | -12.9 | -16.8% |
| yolo26-l_640x640.dxnn | 63.6 | 76.2 | -12.6 | -16.5% |
| yolo26-x_640x640.dxnn | 48.7 | 48.9 | -0.3 | -0.5% |

### Pose Estimation

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-pose_640x640.dxnn | avdec_h264 | 3455 | 3 | 78.6 ±0.2 | 43.97 | 322 | 20.6 | 46.7 | 44 | 1000 | 310 | ok |
| yolo26-s-pose_640x640.dxnn | avdec_h264 | 3455 | 3 | 78.2 ±0.3 | 44.18 | 320 | 36.3 | 65.3 | 40~42 | 1000 | 333 | ok |
| yolo26-m-pose_640x640.dxnn | avdec_h264 | 3455 | 3 | 78.3 ±0.5 | 44.13 | 306 | 60.9 | 82.6 | 59~60 | 1000 | 364 | ok |
| yolo26-l-pose_640x640.dxnn | avdec_h264 | 3455 | 3 | 77.7 ±0.5 | 44.45 | 277 | 82.5 | 95.1 | 61~64 | 1000 | 382 | ok |
| yolo26-x-pose_640x640.dxnn | avdec_h264 | 3455 | 3 | 47.9 ±0.1 | 72.11 | 114 | 94.6 | 100.0 | 69~73 | 1000 | 474 | ok |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-pose_640x640.dxnn | avdec_h264 | 3455 | 3 | 108.0 ±0.6 | 31.98 | 302 | 27.8 | 58.8 | 46~47 | 1000 | 294 | ok |
| yolo26-s-pose_640x640.dxnn | avdec_h264 | 3455 | 3 | 107.9 ±0.9 | 32.01 | 300 | 50.9 | 73.7 | 41~52 | 1000 | 315 | ok |
| yolo26-m-pose_640x640.dxnn | avdec_h264 | 3455 | 3 | 105.1 ±1.0 | 32.87 | 277 | 82.7 | 95.7 | 61~64 | 1000 | 355 | ok |
| yolo26-l-pose_640x640.dxnn | avdec_h264 | 3455 | 3 | 84.9 ±0.4 | 40.69 | 189 | 92.2 | 100.0 | 62~65 | 1000 | 370 | ok |
| yolo26-x-pose_640x640.dxnn | avdec_h264 | 3455 | 3 | 47.6 ±0.3 | 72.64 | 96 | 94.7 | 100.0 | 69~74 | 1000 | 465 | ok |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26-n-pose_640x640.dxnn | 78.6 | 108.0 | -29.5 | -27.3% |
| yolo26-s-pose_640x640.dxnn | 78.2 | 107.9 | -29.7 | -27.5% |
| yolo26-m-pose_640x640.dxnn | 78.3 | 105.1 | -26.8 | -25.5% |
| yolo26-l-pose_640x640.dxnn | 77.7 | 84.9 | -7.2 | -8.5% |
| yolo26-x-pose_640x640.dxnn | 47.9 | 47.6 | +0.3 | +0.7% |

### Segmentation

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-seg_640x640.dxnn | avdec_h264 | 3455 | 3 | 42.9 ±0.2 | 80.58 | 311 | 13.7 | 32.8 | 43 | 1000 | 419 | ok |
| yolo26-s-seg_640x640.dxnn | avdec_h264 | 3455 | 3 | 42.8 ±0.3 | 80.78 | 305 | 25.1 | 56.8 | 46~47 | 1000 | 442 | ok |
| yolo26-m-seg_640x640.dxnn | avdec_h264 | 3455 | 3 | 42.1 ±0.4 | 82.05 | 291 | 46.3 | 72.9 | 59~60 | 1000 | 475 | ok |
| yolo26-l-seg_640x640.dxnn | avdec_h264 | 3455 | 3 | 41.8 ±0.5 | 82.72 | 278 | 57.3 | 82.4 | 62~64 | 1000 | 490 | ok |
| yolo26-x-seg_640x640.dxnn | avdec_h264 | 3455 | 3 | 32.5 ±2.0 | 106.41 | 158 | 92.4 | 100.0 | 74~78 | 800~1000 | 598 | ok |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-seg_640x640.dxnn | avdec_h264 | 3455 | 3 | 52.8 ±0.5 | 65.50 | 337 | 16.0 | 47.2 | 43 | 1000 | 459 | ok |
| yolo26-s-seg_640x640.dxnn | avdec_h264 | 3455 | 3 | 52.2 ±0.2 | 66.13 | 338 | 29.5 | 66.1 | 49 | 1000 | 482 | ok |
| yolo26-m-seg_640x640.dxnn | avdec_h264 | 3455 | 3 | 51.6 ±0.3 | 66.97 | 324 | 56.7 | 83.7 | 64~65 | 1000 | 531 | ok |
| yolo26-l-seg_640x640.dxnn | avdec_h264 | 3455 | 3 | 50.6 ±0.6 | 68.26 | 304 | 70.7 | 87.6 | 65~67 | 1000 | 533 | ok |
| yolo26-x-seg_640x640.dxnn | avdec_h264 | 3455 | 3 | 34.5 ±0.1 | 100.17 | 164 | 94.5 | 100.0 | 60~75 | 1000 | 612 | ok |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26-n-seg_640x640.dxnn | 42.9 | 52.8 | -9.9 | -18.7% |
| yolo26-s-seg_640x640.dxnn | 42.8 | 52.2 | -9.5 | -18.1% |
| yolo26-m-seg_640x640.dxnn | 42.1 | 51.6 | -9.5 | -18.4% |
| yolo26-l-seg_640x640.dxnn | 41.8 | 50.6 | -8.8 | -17.5% |
| yolo26-x-seg_640x640.dxnn | 32.5 | 34.5 | -2.0 | -5.9% |

### Oriented BBox (OBB)

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | avdec_h264 | 2640 | 3 | 66.5 ±0.2 | 39.68 | 316 | 50.9 | 76.0 | 50 | 1000 | 346 | ok |
| yolo26-s-obb_1024x1024.dxnn | avdec_h264 | 2640 | 3 | 62.1 ±0.2 | 42.52 | 245 | 89.8 | 100.0 | 43~56 | 1000 | 370 | ok |
| yolo26-m-obb_1024x1024.dxnn | avdec_h264 | 2640 | 3 | 41.2 ±0.2 | 64.12 | 136 | 94.4 | 100.0 | 65~69 | 1000 | 409 | ok |
| yolo26-l-obb_1024x1024.dxnn | avdec_h264 | 2640 | 3 | 30.6 ±0.2 | 86.14 | 99 | 93.3 | 100.0 | 53~64 | 1000 | 422 | ok |
| yolo26-x-obb_1024x1024.dxnn | avdec_h264 | 2640 | 3 | 16.7 ±0.4 | 158.51 | 56 | 94.0 | 100.0 | 74~79 | 1000 | 527 | ok |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | avdec_h264 | 2640 | 3 | 78.3 ±0.3 | 33.70 | 309 | 59.8 | 84.7 | 51~52 | 1000 | 336 | ok |
| yolo26-s-obb_1024x1024.dxnn | avdec_h264 | 2640 | 3 | 61.6 ±0.5 | 42.87 | 211 | 90.1 | 100.0 | 45~50 | 1000 | 370 | ok |
| yolo26-m-obb_1024x1024.dxnn | avdec_h264 | 2640 | 3 | 41.9 ±0.3 | 63.04 | 134 | 93.5 | 100.0 | 65~70 | 1000 | 398 | ok |
| yolo26-l-obb_1024x1024.dxnn | avdec_h264 | 2640 | 3 | 31.0 ±0.2 | 85.26 | 98 | 94.1 | 100.0 | 54~69 | 1000 | 415 | ok |
| yolo26-x-obb_1024x1024.dxnn | avdec_h264 | 2640 | 3 | 16.7 ±0.5 | 158.37 | 56 | 94.1 | 100.0 | 75~79 | 1000 | 520 | ok |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26-n-obb_1024x1024.dxnn | 66.5 | 78.3 | -11.8 | -15.1% |
| yolo26-s-obb_1024x1024.dxnn | 62.1 | 61.6 | +0.5 | +0.8% |
| yolo26-m-obb_1024x1024.dxnn | 41.2 | 41.9 | -0.7 | -1.7% |
| yolo26-l-obb_1024x1024.dxnn | 30.6 | 31.0 | -0.3 | -1.0% |
| yolo26-x-obb_1024x1024.dxnn | 16.7 | 16.7 | -0.0 | -0.1% |

### Classification

**ORT = ON**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_224x224.dxnn | avdec_h264 | 3455 | 3 | 182.2 ±0.2 | 18.97 | 270 | 4.1 | 12.9 | 45~46 | 1000 | 217 | ok |
| yolo26-s_224x224.dxnn | avdec_h264 | 3455 | 3 | 181.6 ±0.3 | 19.02 | 270 | 7.4 | 21.8 | 39~47 | 1000 | 220 | ok |
| yolo26-m_224x224.dxnn | avdec_h264 | 3455 | 3 | 182.6 ±0.3 | 18.92 | 271 | 10.6 | 30.4 | 49~51 | 1000 | 239 | ok |
| yolo26-l_224x224.dxnn | avdec_h264 | 3455 | 3 | 181.9 ±0.4 | 18.99 | 269 | 17.1 | 42.9 | 49~50 | 1000 | 250 | ok |
| yolo26-x_224x224.dxnn | avdec_h264 | 3455 | 3 | 181.2 ±0.2 | 19.07 | 268 | 29.7 | 59.3 | 52~53 | 1000 | 294 | ok |

**ORT = OFF**

| Model | Decoder | Frames | Runs | Avg FPS | Avg Duration (s) | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|--------|------|---------|------------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_224x224.dxnn | avdec_h264 | 3455 | 3 | 182.2 ±0.3 | 18.96 | 271 | 4.0 | 12.6 | 45~46 | 1000 | 216 | ok |
| yolo26-s_224x224.dxnn | avdec_h264 | 3455 | 3 | 182.6 ±0.4 | 18.92 | 271 | 7.4 | 22.1 | 44 | 1000 | 215 | ok |
| yolo26-m_224x224.dxnn | avdec_h264 | 3455 | 3 | 182.0 ±0.1 | 18.99 | 270 | 10.3 | 30.0 | 50~51 | 1000 | 227 | ok |
| yolo26-l_224x224.dxnn | avdec_h264 | 3455 | 3 | 182.2 ±0.2 | 18.97 | 270 | 16.8 | 41.7 | 49~50 | 1000 | 250 | ok |
| yolo26-x_224x224.dxnn | avdec_h264 | 3455 | 3 | 181.0 ±0.6 | 19.09 | 268 | 29.8 | 59.1 | 52~53 | 1000 | 292 | ok |

**ORT Comparison – E2E FPS**

| Model | ORT ON | ORT OFF | Delta | Delta % |
|-------|--------|---------|-------|---------|
| yolo26-n_224x224.dxnn | 182.2 | 182.2 | -0.1 | -0.0% |
| yolo26-s_224x224.dxnn | 181.6 | 182.6 | -1.0 | -0.5% |
| yolo26-m_224x224.dxnn | 182.6 | 182.0 | +0.6 | +0.3% |
| yolo26-l_224x224.dxnn | 181.9 | 182.2 | -0.2 | -0.1% |
| yolo26-x_224x224.dxnn | 181.2 | 181.0 | +0.2 | +0.1% |

## E2E Pipeline (Multi-Stream)

### Object Detection

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_640x640.dxnn | 2 | 3 | 64.4 ±0.0 | 32.2 | 316 | 16.2 | 38.3 | 39~40 | 1000 | 456 | ok |
| yolo26-n_640x640.dxnn | 3 | 3 | 64.5 ±0.2 | 21.5 | 314 | 16.3 | 38.3 | 40 | 1000 | 555 | ok |
| yolo26-s_640x640.dxnn | 2 | 3 | 64.3 ±0.1 | 32.1 | 313 | 29.0 | 59.2 | 39~44 | 1000 | 476 | ok |
| yolo26-s_640x640.dxnn | 3 | 3 | 64.3 ±0.1 | 21.4 | 312 | 29.2 | 62.8 | 43~44 | 1000 | 578 | ok |
| yolo26-m_640x640.dxnn | 2 | 3 | 61.6 ±0.3 | 30.8 | 307 | 44.6 | 73.3 | 56~57 | 1000 | 504 | ok |
| yolo26-m_640x640.dxnn | 3 | 3 | 62.6 ±0.9 | 20.9 | 305 | 45.8 | 73.2 | 56~57 | 1000 | 607 | ok |
| yolo26-l_640x640.dxnn | 2 | 3 | 62.9 ±0.8 | 31.5 | 289 | 64.1 | 85.6 | 58~61 | 1000 | 520 | ok |
| yolo26-l_640x640.dxnn | 3 | 3 | 62.2 ±0.9 | 20.7 | 289 | 63.6 | 87.4 | 52~62 | 1000 | 621 | ok |
| yolo26-x_640x640.dxnn | 1 | 3 | 48.7 ±0.1 | 48.7 | 152 | 93.5 | 100.0 | 65~71 | 1000 | 481 | ok |
| yolo26-x_640x640.dxnn | 2 | 3 | 47.9 ±0.4 | 24.0 | 154 | 96.0 | 100.0 | 76~78 | 1000 | 613 | ok |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n_640x640.dxnn | 2 | 3 | 77.7 ±0.5 | 38.9 | 306 | 18.2 | 55.9 | 41~42 | 1000 | 484 | ok |
| yolo26-n_640x640.dxnn | 3 | 3 | 77.5 ±0.3 | 25.8 | 309 | 18.4 | 56.5 | 41 | 1000 | 582 | ok |
| yolo26-s_640x640.dxnn | 2 | 3 | 77.5 ±0.3 | 38.7 | 309 | 33.4 | 72.0 | 43~44 | 1000 | 502 | ok |
| yolo26-s_640x640.dxnn | 3 | 3 | 77.4 ±0.5 | 25.8 | 308 | 33.9 | 72.8 | 45~46 | 1000 | 603 | ok |
| yolo26-m_640x640.dxnn | 2 | 3 | 77.1 ±0.5 | 38.5 | 304 | 54.8 | 84.7 | 59 | 1000 | 534 | ok |
| yolo26-m_640x640.dxnn | 3 | 3 | 76.9 ±0.4 | 25.6 | 306 | 54.8 | 83.0 | 59~60 | 1000 | 635 | ok |
| yolo26-l_640x640.dxnn | 2 | 3 | 76.5 ±0.3 | 38.2 | 302 | 77.1 | 90.5 | 64~65 | 1000 | 548 | ok |
| yolo26-l_640x640.dxnn | 3 | 3 | 75.5 ±0.7 | 25.1 | 307 | 77.4 | 91.7 | 67 | 1000 | 651 | ok |
| yolo26-x_640x640.dxnn | 1 | 3 | 48.9 ±0.1 | 48.9 | 163 | 94.0 | 100.0 | 67~72 | 1000 | 489 | ok |
| yolo26-x_640x640.dxnn | 2 | 3 | 48.3 ±0.6 | 24.1 | 163 | 96.5 | 100.0 | 77~78 | 1000 | 620 | ok |

**Channel Capacity Summary** (max streams where per-channel FPS ≥ 30)

| Model | ORT ON Capacity | Per-Ch FPS | ORT OFF Capacity | Per-Ch FPS |
|-------|-----------------|------------|------------------|------------|
| yolo26-n_640x640.dxnn | 2 | 32.2 | 2 | 38.9 |
| yolo26-s_640x640.dxnn | 2 | 32.1 | 2 | 38.7 |
| yolo26-m_640x640.dxnn | 2 | 30.8 | 2 | 38.5 |
| yolo26-l_640x640.dxnn | 2 | 31.5 | 2 | 38.2 |
| yolo26-x_640x640.dxnn | 1 | 48.7 | 1 | 48.9 |

### Pose Estimation

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-pose_640x640.dxnn | 2 | 3 | 78.1 ±0.1 | 39.1 | 323 | 21.6 | 46.2 | 43~44 | 1000 | 451 | ok |
| yolo26-n-pose_640x640.dxnn | 3 | 3 | 77.1 ±0.6 | 25.7 | 323 | 21.3 | 48.0 | 42~43 | 1000 | 551 | ok |
| yolo26-s-pose_640x640.dxnn | 2 | 3 | 78.2 ±0.4 | 39.1 | 318 | 38.0 | 67.4 | 45~46 | 1000 | 471 | ok |
| yolo26-s-pose_640x640.dxnn | 3 | 3 | 76.6 ±0.9 | 25.5 | 319 | 37.6 | 68.0 | 47~48 | 1000 | 577 | ok |
| yolo26-m-pose_640x640.dxnn | 2 | 3 | 75.1 ±0.3 | 37.6 | 310 | 59.1 | 81.7 | 62~63 | 1000 | 498 | ok |
| yolo26-m-pose_640x640.dxnn | 3 | 3 | 76.7 ±0.9 | 25.6 | 309 | 61.3 | 84.0 | 52~63 | 1000 | 604 | ok |
| yolo26-l-pose_640x640.dxnn | 2 | 3 | 74.4 ±0.1 | 37.2 | 285 | 80.4 | 93.2 | 67~68 | 1000 | 516 | ok |
| yolo26-l-pose_640x640.dxnn | 3 | 3 | 75.2 ±0.6 | 25.1 | 286 | 82.5 | 97.3 | 70~71 | 1000 | 619 | ok |
| yolo26-x-pose_640x640.dxnn | 1 | 3 | 47.9 ±0.1 | 47.9 | 114 | 94.6 | 100.0 | 69~73 | 1000 | 474 | ok |
| yolo26-x-pose_640x640.dxnn | 2 | 3 | 45.7 ±0.6 | 22.9 | 115 | 95.9 | 100.0 | 78~79 | 800~1000 | 609 | ok |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-pose_640x640.dxnn | 3 | 3 | 108.1 ±1.4 | 36.0 | 330 | 30.8 | 52.9 | 45 | 1000 | 543 | ok |
| yolo26-n-pose_640x640.dxnn | 4 | 3 | 106.2 ±1.1 | 26.5 | 333 | 30.7 | 52.1 | 44~45 | 1000 | 646 | ok |
| yolo26-s-pose_640x640.dxnn | 3 | 3 | 108.0 ±1.3 | 36.0 | 326 | 54.4 | 76.4 | 48~50 | 1000 | 568 | ok |
| yolo26-s-pose_640x640.dxnn | 4 | 3 | 107.0 ±1.0 | 26.7 | 327 | 54.3 | 77.6 | 52~53 | 1000 | 666 | ok |
| yolo26-m-pose_640x640.dxnn | 3 | 3 | 101.3 ±0.8 | 33.8 | 296 | 84.3 | 95.4 | 69~71 | 1000 | 591 | ok |
| yolo26-m-pose_640x640.dxnn | 4 | 3 | 102.0 ±0.8 | 25.5 | 296 | 84.5 | 96.1 | 73 | 1000 | 694 | ok |
| yolo26-l-pose_640x640.dxnn | 2 | 3 | 84.5 ±0.4 | 42.3 | 196 | 94.9 | 100.0 | 70~72 | 1000 | 504 | ok |
| yolo26-l-pose_640x640.dxnn | 3 | 3 | 84.5 ±0.2 | 28.2 | 197 | 95.7 | 100.0 | 75~76 | 1000 | 609 | ok |
| yolo26-x-pose_640x640.dxnn | 1 | 3 | 47.6 ±0.3 | 47.6 | 96 | 94.7 | 100.0 | 69~74 | 1000 | 465 | ok |
| yolo26-x-pose_640x640.dxnn | 2 | 3 | 45.2 ±1.1 | 22.6 | 99 | 96.0 | 100.0 | 78~79 | 800~1000 | 599 | ok |

**Channel Capacity Summary** (max streams where per-channel FPS ≥ 30)

| Model | ORT ON Capacity | Per-Ch FPS | ORT OFF Capacity | Per-Ch FPS |
|-------|-----------------|------------|------------------|------------|
| yolo26-n-pose_640x640.dxnn | 2 | 39.1 | 3 | 36.0 |
| yolo26-s-pose_640x640.dxnn | 2 | 39.1 | 3 | 36.0 |
| yolo26-m-pose_640x640.dxnn | 2 | 37.6 | 3 | 33.8 |
| yolo26-l-pose_640x640.dxnn | 2 | 37.2 | 2 | 42.3 |
| yolo26-x-pose_640x640.dxnn | 1 | 47.9 | 1 | 47.6 |

### Segmentation

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-seg_640x640.dxnn | 1 | 3 | 42.9 ±0.2 | 42.9 | 311 | 13.7 | 32.8 | 43 | 1000 | 419 | ok |
| yolo26-n-seg_640x640.dxnn | 2 | 3 | 42.2 ±0.5 | 21.1 | 313 | 13.5 | 32.5 | 42 | 1000 | 557 | ok |
| yolo26-s-seg_640x640.dxnn | 1 | 3 | 42.8 ±0.3 | 42.8 | 305 | 25.1 | 56.8 | 46~47 | 1000 | 442 | ok |
| yolo26-s-seg_640x640.dxnn | 2 | 3 | 41.3 ±0.1 | 20.6 | 308 | 24.5 | 56.5 | 47 | 1000 | 580 | ok |
| yolo26-m-seg_640x640.dxnn | 1 | 3 | 42.1 ±0.4 | 42.1 | 291 | 46.3 | 72.9 | 59~60 | 1000 | 475 | ok |
| yolo26-m-seg_640x640.dxnn | 2 | 3 | 41.3 ±0.2 | 20.6 | 296 | 46.0 | 74.2 | 62 | 1000 | 617 | ok |
| yolo26-l-seg_640x640.dxnn | 1 | 3 | 41.8 ±0.5 | 41.8 | 278 | 57.3 | 82.4 | 62~64 | 1000 | 490 | ok |
| yolo26-l-seg_640x640.dxnn | 2 | 3 | 41.6 ±0.4 | 20.8 | 281 | 57.7 | 84.1 | 66~67 | 1000 | 633 | ok |
| yolo26-x-seg_640x640.dxnn | 1 | 3 | 32.5 ±2.0 | 32.5 | 158 | 92.4 | 100.0 | 74~78 | 800~1000 | 598 | ok |
| yolo26-x-seg_640x640.dxnn | 2 | 3 | 29.3 ±0.3 | 14.6 | 145 | 91.5 | 100.0 | 80 | 800~1000 | 735 | ok |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-seg_640x640.dxnn | 1 | 3 | 52.8 ±0.5 | 52.8 | 337 | 16.0 | 47.2 | 43 | 1000 | 459 | ok |
| yolo26-n-seg_640x640.dxnn | 2 | 3 | 52.0 ±0.1 | 26.0 | 341 | 15.9 | 47.9 | 43 | 1000 | 603 | ok |
| yolo26-s-seg_640x640.dxnn | 1 | 3 | 52.2 ±0.2 | 52.2 | 338 | 29.5 | 66.1 | 49 | 1000 | 482 | ok |
| yolo26-s-seg_640x640.dxnn | 2 | 3 | 52.2 ±0.5 | 26.1 | 335 | 30.0 | 71.0 | 48~49 | 1000 | 629 | ok |
| yolo26-m-seg_640x640.dxnn | 1 | 3 | 51.6 ±0.3 | 51.6 | 324 | 56.7 | 83.7 | 64~65 | 1000 | 531 | ok |
| yolo26-m-seg_640x640.dxnn | 2 | 3 | 51.2 ±0.1 | 25.6 | 329 | 57.3 | 84.1 | 67 | 1000 | 666 | ok |
| yolo26-l-seg_640x640.dxnn | 1 | 3 | 50.6 ±0.6 | 50.6 | 304 | 70.7 | 87.6 | 65~67 | 1000 | 533 | ok |
| yolo26-l-seg_640x640.dxnn | 2 | 3 | 51.0 ±0.6 | 25.5 | 311 | 72.7 | 91.6 | 70~72 | 1000 | 675 | ok |
| yolo26-x-seg_640x640.dxnn | 1 | 3 | 34.5 ±0.1 | 34.5 | 164 | 94.5 | 100.0 | 60~75 | 1000 | 612 | ok |
| yolo26-x-seg_640x640.dxnn | 2 | 3 | 29.8 ±0.5 | 14.9 | 148 | 92.2 | 100.0 | 80 | 800~1000 | 771 | ok |

**Channel Capacity Summary** (max streams where per-channel FPS ≥ 30)

| Model | ORT ON Capacity | Per-Ch FPS | ORT OFF Capacity | Per-Ch FPS |
|-------|-----------------|------------|------------------|------------|
| yolo26-n-seg_640x640.dxnn | 1 | 42.9 | 1 | 52.8 |
| yolo26-s-seg_640x640.dxnn | 1 | 42.8 | 1 | 52.2 |
| yolo26-m-seg_640x640.dxnn | 1 | 42.1 | 1 | 51.6 |
| yolo26-l-seg_640x640.dxnn | 1 | 41.8 | 1 | 50.6 |
| yolo26-x-seg_640x640.dxnn | 1 | 32.5 | 1 | 34.5 |

### Oriented BBox (OBB)

**ORT = ON**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | 2 | 3 | 66.1 ±0.4 | 33.1 | 322 | 52.3 | 74.9 | 51 | 1000 | 481 | ok |
| yolo26-n-obb_1024x1024.dxnn | 3 | 3 | 65.7 ±0.6 | 21.9 | 322 | 52.9 | 78.0 | 52 | 1000 | 583 | ok |
| yolo26-s-obb_1024x1024.dxnn | 2 | 3 | 62.1 ±0.1 | 31.0 | 252 | 93.5 | 100.0 | 48~54 | 1000 | 505 | ok |
| yolo26-s-obb_1024x1024.dxnn | 3 | 3 | 61.7 ±0.1 | 20.6 | 253 | 93.9 | 100.0 | 60~63 | 1000 | 606 | ok |
| yolo26-m-obb_1024x1024.dxnn | 1 | 3 | 41.2 ±0.2 | 41.2 | 136 | 94.4 | 100.0 | 65~69 | 1000 | 409 | ok |
| yolo26-m-obb_1024x1024.dxnn | 2 | 3 | 41.1 ±0.2 | 20.6 | 143 | 96.1 | 100.0 | 75~76 | 1000 | 534 | ok |
| yolo26-l-obb_1024x1024.dxnn | 1 | 3 | 30.6 ±0.2 | 30.6 | 99 | 93.3 | 100.0 | 53~64 | 1000 | 422 | ok |
| yolo26-l-obb_1024x1024.dxnn | 2 | 3 | 30.7 ±0.1 | 15.3 | 102 | 95.5 | 100.0 | 73~75 | 1000 | 552 | ok |
| yolo26-x-obb_1024x1024.dxnn | 1 | 3 | 16.7 ±0.4 | 16.7 | 56 | 94.0 | 100.0 | 74~79 | 1000 | 527 | ok |

**ORT = OFF**

| Model | Streams | Runs | E2E FPS | Per-Ch FPS | CPU% | NPU Avg% | NPU Max% | NPU Temp °C | NPU MHz | RSS MiB | Status |
|-------|---------|------|---------|------------|------|----------|----------|-------------|---------|---------|--------|
| yolo26-n-obb_1024x1024.dxnn | 2 | 3 | 78.9 ±0.4 | 39.5 | 330 | 66.3 | 84.1 | 53~54 | 1000 | 503 | ok |
| yolo26-n-obb_1024x1024.dxnn | 3 | 3 | 79.0 ±0.1 | 26.4 | 332 | 67.2 | 85.3 | 54~55 | 1000 | 599 | ok |
| yolo26-s-obb_1024x1024.dxnn | 2 | 3 | 61.7 ±0.3 | 30.9 | 219 | 94.2 | 100.0 | 56~59 | 1000 | 503 | ok |
| yolo26-s-obb_1024x1024.dxnn | 3 | 3 | 61.6 ±0.2 | 20.5 | 220 | 95.1 | 100.0 | 62~64 | 1000 | 601 | ok |
| yolo26-m-obb_1024x1024.dxnn | 1 | 3 | 41.9 ±0.3 | 41.9 | 134 | 93.5 | 100.0 | 65~70 | 1000 | 398 | ok |
| yolo26-m-obb_1024x1024.dxnn | 2 | 3 | 41.5 ±0.2 | 20.7 | 138 | 96.0 | 100.0 | 75~76 | 1000 | 533 | ok |
| yolo26-l-obb_1024x1024.dxnn | 1 | 3 | 31.0 ±0.2 | 31.0 | 98 | 94.1 | 100.0 | 54~69 | 1000 | 415 | ok |
| yolo26-l-obb_1024x1024.dxnn | 2 | 3 | 30.8 ±0.1 | 15.4 | 101 | 95.5 | 100.0 | 70~75 | 1000 | 548 | ok |
| yolo26-x-obb_1024x1024.dxnn | 1 | 3 | 16.7 ±0.5 | 16.7 | 56 | 94.1 | 100.0 | 75~79 | 1000 | 520 | ok |

**Channel Capacity Summary** (max streams where per-channel FPS ≥ 30)

| Model | ORT ON Capacity | Per-Ch FPS | ORT OFF Capacity | Per-Ch FPS |
|-------|-----------------|------------|------------------|------------|
| yolo26-n-obb_1024x1024.dxnn | 2 | 33.1 | 2 | 39.5 |
| yolo26-s-obb_1024x1024.dxnn | 2 | 31.0 | 2 | 30.9 |
| yolo26-m-obb_1024x1024.dxnn | 1 | 41.2 | 1 | 41.9 |
| yolo26-l-obb_1024x1024.dxnn | 1 | 30.6 | 1 | 31.0 |

---
*Report generated by dx-benchmark tool*
