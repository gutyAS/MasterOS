#!/usr/bin/env bash
set -e

echo "[entrypoint] Starting MasterOS (gutyAS)..."
cd /workspace || mkdir -p /workspace && cd /workspace

if [ ! -d "/workspace/MasterOS" ]; then
  echo "[entrypoint] Cloning repository..."
  git clone https://github.com/gutyAS/MasterOS.git /workspace/MasterOS
fi

cd /workspace/MasterOS
git pull || true

echo "[entrypoint] Running autoscaler..."
python3 runner/notion_sync.py &
python3 runner/vast_control.py &
bash autoscale.ps1 &

echo "[entrypoint] MasterOS is running."
tail -f /dev/null
