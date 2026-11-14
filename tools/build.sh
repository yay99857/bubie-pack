#!/usr/bin/env bash
# Gera o zip do pack (CurseForge App) e, com --server, o server pack.
set -euo pipefail
cd "$(dirname "$0")/.."
VER=$(python3 -c "import json;print(json.load(open('pack/manifest.json'))['version'])")
mkdir -p dist
# Better Compatibility Checker: a lista de servidores compara esta versão com a do servidor.
python3 - "$VER" <<'PY'
import json, sys
p = 'pack/overrides/config/bcc-common.json'
cfg = {
    'modpackName': {'value': 'Bubie Pack', 'comments': ['The name of the modpack']},
    'modpackVersion': {'value': sys.argv[1], 'comments': ['The version of the modpack']},
    'useMetadata': {'value': False, 'comments': ['Use the metadata.json to determine the modpack version',
                                                 'ONLY ENABLE THIS IF YOU KNOW WHAT YOU ARE DOING']},
}
open(p, 'w').write(json.dumps(cfg, indent=2) + '\n')
PY
rm -f "dist/BubiePack-$VER.zip"
(cd pack && zip -qr "../dist/BubiePack-$VER.zip" manifest.json modlist.html overrides profileImage)
echo "dist/BubiePack-$VER.zip"
if [ "${1:-}" = "--server" ]; then
  python3 tools/build_server.py "dist/server-$VER"
  rm -f "dist/BubiePack-$VER-server.zip"
  (cd "dist/server-$VER" && zip -qr "../BubiePack-$VER-server.zip" .)
  echo "dist/BubiePack-$VER-server.zip"
fi
