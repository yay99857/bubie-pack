#!/usr/bin/env bash
# Gera o zip do pack (CurseForge App) e, com --server, o server pack.
set -euo pipefail
cd "$(dirname "$0")/.."
VER=$(python3 -c "import json;print(json.load(open('pack/manifest.json'))['version'])")
mkdir -p dist
rm -f "dist/BubiePack-$VER.zip"
(cd pack && zip -qr "../dist/BubiePack-$VER.zip" manifest.json modlist.html overrides profileImage)
echo "dist/BubiePack-$VER.zip"
if [ "${1:-}" = "--server" ]; then
  python3 tools/build_server.py "dist/server-$VER"
  rm -f "dist/BubiePack-$VER-server.zip"
  (cd "dist/server-$VER" && zip -qr "../BubiePack-$VER-server.zip" .)
  echo "dist/BubiePack-$VER-server.zip"
fi
