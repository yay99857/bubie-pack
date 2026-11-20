#!/usr/bin/env bash
# Gera o zip do pack (CurseForge App) e, com --server, o server pack.
set -euo pipefail
cd "$(dirname "$0")/.."
. tools/python.sh
VER=$($PY -c "import json;print(json.load(open('pack/manifest.json', encoding='utf-8'))['version'])")
mkdir -p dist
# Better Compatibility Checker: a lista de servidores compara esta versão com a do servidor.
$PY - "$VER" <<'PY'
import json, sys
p = 'pack/overrides/config/bcc-common.json'
cfg = {
    'modpackName': {'value': 'Bubie Pack', 'comments': ['The name of the modpack']},
    'modpackVersion': {'value': sys.argv[1], 'comments': ['The version of the modpack']},
    'useMetadata': {'value': False, 'comments': ['Use the metadata.json to determine the modpack version',
                                                 'ONLY ENABLE THIS IF YOU KNOW WHAT YOU ARE DOING']},
}
open(p, 'w', encoding='utf-8', newline='').write(json.dumps(cfg, indent=2) + '\n')
PY
rm -f "dist/BubiePack-$VER.zip"
$PY tools/zipdir.py "dist/BubiePack-$VER.zip" pack manifest.json modlist.html overrides profileImage
echo "dist/BubiePack-$VER.zip"
if [ "${1:-}" = "--server" ]; then
  $PY tools/build_server.py "dist/server-$VER"
  rm -f "dist/BubiePack-$VER-server.zip"
  $PY tools/zipdir.py "dist/BubiePack-$VER-server.zip" "dist/server-$VER" .
  echo "dist/BubiePack-$VER-server.zip"
fi
