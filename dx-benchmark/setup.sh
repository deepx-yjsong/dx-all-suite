#!/usr/bin/env bash
# dx-benchmark environment setup.
# Usage: ./setup.sh [all|env|models|videos]   (default: all)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"
MODEL_DIR="$SCRIPT_DIR/benchmark/assets/models"
VIDEO_DIR="$SCRIPT_DIR/benchmark/assets/videos"

phase_env() {
    # One-time environment setup for benchmark automation (from setup_benchmark_env.sh).
    #   1. Passwordless sudo for dxrt.service restart (crash recovery)
    #   2. Passwordless sudo for dmesg (kernel log collection on incidents)
    #   3. Passwordless sudo for journalctl (dxrt service log collection on incidents)
    #   4. systemd-journal group membership (journal access without sudo)
    local SUDOERS_FILE="/etc/sudoers.d/benchmark-dxrt"

    # ── Determine target user ─────────────────────────────────────────────────
    local TARGET_USER="${1:-${SUDO_USER:-}}"

    if [[ -z "${TARGET_USER}" ]]; then
        echo "ERROR: Cannot determine target user."
        echo "Usage: sudo $0 [username]"
        exit 1
    fi

    # Verify user exists
    if ! id "${TARGET_USER}" &>/dev/null; then
        echo "ERROR: User '${TARGET_USER}' does not exist on this system."
        exit 1
    fi

    # ── Must run as root ──────────────────────────────────────────────────────
    if [[ "$(id -u)" -ne 0 ]]; then
        echo "ERROR: This script must be run with sudo (or as root)."
        echo "Usage: sudo $0 [username]"
        exit 1
    fi

    echo "[setup] Target user: ${TARGET_USER}"

    # ── Resolve command paths ─────────────────────────────────────────────────
    local SYSTEMCTL_BIN DMESG_BIN JOURNALCTL_BIN
    SYSTEMCTL_BIN="$(command -v systemctl 2>/dev/null || echo /usr/bin/systemctl)"
    DMESG_BIN="$(command -v dmesg 2>/dev/null || echo /usr/bin/dmesg)"
    JOURNALCTL_BIN="$(command -v journalctl 2>/dev/null || echo /usr/bin/journalctl)"

    # ── Install sudoers rules ─────────────────────────────────────────────────
    # Build multi-line sudoers content
    local SUDOERS_CONTENT="# Benchmark automation: passwordless sudo for dxrt crash recovery and incident log collection
${TARGET_USER} ALL=(ALL) NOPASSWD: ${SYSTEMCTL_BIN} restart dxrt.service
${TARGET_USER} ALL=(ALL) NOPASSWD: ${DMESG_BIN} --time-format=iso -T
${TARGET_USER} ALL=(ALL) NOPASSWD: ${JOURNALCTL_BIN} -u dxrt.service *"

    # Check if already fully configured
    if [[ -f "${SUDOERS_FILE}" ]] && \
       grep -qF "restart dxrt.service" "${SUDOERS_FILE}" && \
       grep -qF "${DMESG_BIN}" "${SUDOERS_FILE}" && \
       grep -qF "${JOURNALCTL_BIN}" "${SUDOERS_FILE}"; then
        echo "[setup] Sudoers rules already configured. Skipping."
    else
        echo "${SUDOERS_CONTENT}" > "${SUDOERS_FILE}"
        chmod 0440 "${SUDOERS_FILE}"

        # Validate with visudo — rollback on failure
        if visudo -cf "${SUDOERS_FILE}" &>/dev/null; then
            echo "[setup] Sudoers rules installed: ${SUDOERS_FILE}"
            echo "        - systemctl restart dxrt.service"
            echo "        - dmesg (kernel log for incident collection)"
            echo "        - journalctl (service log for incident collection)"
        else
            echo "ERROR: Sudoers validation failed. Removing broken file."
            rm -f "${SUDOERS_FILE}"
            exit 1
        fi
    fi

    # ── Add user to systemd-journal group (journal access without sudo) ───────
    if getent group systemd-journal &>/dev/null; then
        if id -nG "${TARGET_USER}" | grep -qw systemd-journal; then
            echo "[setup] User '${TARGET_USER}' already in systemd-journal group."
        else
            usermod -aG systemd-journal "${TARGET_USER}"
            echo "[setup] Added '${TARGET_USER}' to systemd-journal group."
            echo "        (re-login required for group to take effect)"
        fi
    else
        echo "[setup] systemd-journal group not found. Skipping group membership."
    fi

    # ── Verify passwordless sudo works ────────────────────────────────────────
    echo ""
    echo "[setup] Verifying passwordless sudo ..."

    # Test dmesg
    if sudo -n -u "${TARGET_USER}" -- sudo -n "${DMESG_BIN}" --version &>/dev/null 2>&1; then
        echo "  sudo -n dmesg          — OK"
    else
        echo "  sudo -n dmesg          — installed (cannot verify as ${TARGET_USER})"
    fi

    # Test journalctl
    if sudo -n -u "${TARGET_USER}" -- sudo -n "${JOURNALCTL_BIN}" --version &>/dev/null 2>&1; then
        echo "  sudo -n journalctl     — OK"
    else
        echo "  sudo -n journalctl     — installed (cannot verify as ${TARGET_USER})"
    fi

    # Test systemctl
    echo "  sudo -n systemctl restart dxrt.service — rule installed"

    # ── Summary ───────────────────────────────────────────────────────────────
    echo ""
    echo "=== Setup Complete ==="
    echo "  User:  ${TARGET_USER}"
    echo "  Rule:  ${SUDOERS_FILE}"
    echo "  Group: systemd-journal"
    echo ""
    echo "  Passwordless sudo enabled for:"
    echo "    - systemctl restart dxrt.service  (crash recovery)"
    echo "    - dmesg                           (kernel log collection)"
    echo "    - journalctl                      (service log collection)"
    echo ""
    echo "To remove this configuration later:"
    echo "  sudo rm ${SUDOERS_FILE}"
}

phase_models() {
    mkdir -p "$MODEL_DIR"
    # Download benchmark models listed in model_list.json to $MODEL_DIR (from setup_benchmark_models.sh).
    local BASE_URL="https://sdk.deepx.ai/modelzoo/dxnn"
    local MODEL_LIST_JSON="$SCRIPT_DIR/benchmark/model_list.json"
    local OUTPUT_DIR="$MODEL_DIR"

    if ! command -v jq >/dev/null 2>&1; then
        echo "[ERROR] jq is required. Install with: sudo apt-get install -y jq"
        exit 1
    fi

    if [ ! -f "$MODEL_LIST_JSON" ]; then
        echo "[ERROR] model_list.json not found: $MODEL_LIST_JSON"
        exit 1
    fi

    local MODEL_VERSION
    MODEL_VERSION=$(jq -r '.version' "$MODEL_LIST_JSON")
    local MODEL_FILES
    mapfile -t MODEL_FILES < <(jq -r '.models[].file' "$MODEL_LIST_JSON")

    mkdir -p "$OUTPUT_DIR"

    echo "[INFO] Downloading ${#MODEL_FILES[@]} models (version=$MODEL_VERSION) to $OUTPUT_DIR"

    local model dest url tmp_dest
    for model in "${MODEL_FILES[@]}"; do
        dest="$OUTPUT_DIR/$model"
        if [ -s "$dest" ]; then
            echo "  [SKIP] $model (already exists)"
            continue
        fi
        if [ -e "$dest" ]; then
            echo "  [REDO] $model (empty or incomplete file)"
        fi
        url="$BASE_URL/$MODEL_VERSION/$model"
        tmp_dest=$(mktemp "$OUTPUT_DIR/.${model}.XXXXXX.part")
        echo "  [GET]  $model"
        if ! curl -fSL -o "$tmp_dest" "$url"; then
            echo "[ERROR] Failed to download $url"
            rm -f "$tmp_dest"
            exit 1
        fi
        mv "$tmp_dest" "$dest"
    done

    for model in "${MODEL_FILES[@]}"; do
        dest="$OUTPUT_DIR/$model"
        if [ ! -s "$dest" ]; then
            echo "[ERROR] Required model is still missing or empty: $dest"
            exit 1
        fi
    done

    echo "[OK] All models ready in $OUTPUT_DIR"
}

phase_videos() {
    mkdir -p "$VIDEO_DIR"
    # Download benchmark videos from AWS and extract to $VIDEO_DIR (from setup_benchmark_videos.sh).
    local BASE_URL="https://sdk.deepx.ai"
    local SOURCE_PATH="res/video/benchmark_videos.tar.gz"
    local OUTPUT_DIR="$VIDEO_DIR"
    local REQUIRED_VIDEOS=(
        "od_benchmark_video.mp4"
        "obb_benchmark_video.mp4"
    )

    mkdir -p "$OUTPUT_DIR"

    local missing_videos=()
    local video
    for video in "${REQUIRED_VIDEOS[@]}"; do
        if [ ! -s "$OUTPUT_DIR/$video" ]; then
            missing_videos+=("$video")
        fi
    done

    if [ ${#missing_videos[@]} -eq 0 ]; then
        echo "[OK] Benchmark videos already ready in $OUTPUT_DIR"
        ls -lh "$OUTPUT_DIR"/*.mp4 2>/dev/null || true
        return 0
    fi

    local ARCHIVE EXTRACT_DIR
    ARCHIVE=$(mktemp "$OUTPUT_DIR/.benchmark_video.XXXXXX.tar.gz")
    EXTRACT_DIR=$(mktemp -d "$OUTPUT_DIR/.benchmark_video_extract.XXXXXX")

    cleanup() {
        rm -f "$ARCHIVE"
        rm -rf "$EXTRACT_DIR"
    }

    trap cleanup EXIT

    echo "[INFO] Missing benchmark videos: ${missing_videos[*]}"
    echo "[INFO] Downloading benchmark videos archive to $OUTPUT_DIR"
    if ! curl -fSL -o "$ARCHIVE" "$BASE_URL/$SOURCE_PATH"; then
        echo "[ERROR] Failed to download $BASE_URL/$SOURCE_PATH"
        exit 1
    fi

    echo "[INFO] Extracting ..."
    tar -xzf "$ARCHIVE" -C "$EXTRACT_DIR"

    local extracted
    for video in "${REQUIRED_VIDEOS[@]}"; do
        extracted=$(find "$EXTRACT_DIR" -type f -name "$video" -print -quit)
        if [ -z "$extracted" ]; then
            echo "[ERROR] Required benchmark video not found after extraction: $video"
            exit 1
        fi
        mv "$extracted" "$OUTPUT_DIR/$video"
    done

    echo "[OK] Benchmark videos ready in $OUTPUT_DIR"
    ls -lh "$OUTPUT_DIR"/*.mp4 2>/dev/null || true
}

case "${1:-all}" in
    all)    phase_env; phase_models; phase_videos ;;
    env)    phase_env ;;
    models) phase_models ;;
    videos) phase_videos ;;
    *) echo "Usage: $0 [all|env|models|videos]" >&2; exit 1 ;;
esac
echo "[setup.sh] done: ${1:-all}"
