#!/usr/bin/env bash
# Gera o zip do pack (CurseForge App) e, com --server, o server pack.
set -euo pipefail
cd "$(dirname "$0")/.."
. tools/python.sh
VER=$($PY -c "import json;print(json.load(open('pack/manifest.json', encoding='utf-8'))['version'])")
mkdir -p dist
# Better Compatibility Checker: a lista de servidores compara esta versão com a do servidor.
# O BCC 21.x lê o .toml (o .json era do formato antigo).
$PY - "$VER" <<'PY'
import sys
open('pack/overrides/config/bcc-common.toml', 'w', encoding='utf-8', newline='').write(f'''#General settings
[general]
	#modpackProjectID is now deprecated and will be removed soon
	# Default: 0
	# Range: > 0
	modpackProjectID = 0
	#The name of the modpack
	modpackName = "Bubie Pack"
	#The version of the modpack
	modpackVersion = "{sys.argv[1]}"
	#Use the metadata.json to determine the modpack version
	#ONLY ENABLE THIS IF YOU KNOW WHAT YOU ARE DOING
	useMetadata = false
''')
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
