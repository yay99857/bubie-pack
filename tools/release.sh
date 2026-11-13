#!/usr/bin/env bash
# Publica a versão do pack/manifest.json: gera os zips, envia ao CurseForge e cria o GitHub Release.
# Uso: tools/release.sh [--skip-curseforge]   (DRY_RUN=1 gera tudo e para antes de enviar)
# Token do CurseForge: variável CURSEFORGE_TOKEN ou o arquivo ~/.config/bubie-pack/curseforge-token
set -euo pipefail
cd "$(dirname "$0")/.."

SKIP_CF=false
[ "${1:-}" = "--skip-curseforge" ] && SKIP_CF=true
CF_PROJECT_ID=${CF_PROJECT_ID:-1801989}
CF_RELEASE_TYPE=${CF_RELEASE_TYPE:-beta}
# IDs do CurseForge: 11779 = Minecraft 1.21.1, 10150 = NeoForge (GET /api/game/versions)
VER=$(python3 -c "import json;print(json.load(open('pack/manifest.json'))['version'])")

if git ls-remote --exit-code --tags origin "refs/tags/v$VER" >/dev/null; then
  echo "A tag v$VER já existe: nada para publicar."; exit 0
fi
if [ -z "${CI:-}" ]; then
  git fetch -q origin main
  [ -z "$(git status --porcelain)" ] || { echo "Há mudanças sem commit."; exit 1; }
  [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] || { echo "Faça push antes de publicar."; exit 1; }
fi

mkdir -p dist
python3 tools/release_notes.py "$VER" > dist/notes.md
echo "--- Notas da versão $VER ---"; cat dist/notes.md; echo "---"
tools/build.sh --server

if [ -n "${DRY_RUN:-}" ]; then
  jq -n --rawfile cl dist/notes.md --arg dn "Bubie Pack $VER" --arg rt "$CF_RELEASE_TYPE" \
    '{changelog:$cl, changelogType:"markdown", displayName:$dn, releaseType:$rt, gameVersions:[11779,10150]}'
  ls -la "dist/BubiePack-$VER.zip" "dist/BubiePack-$VER-server.zip"
  echo "DRY_RUN: nada foi enviado."; exit 0
fi

if [ "$SKIP_CF" = false ]; then
  TOKEN=${CURSEFORGE_TOKEN:-}
  [ -z "$TOKEN" ] && [ -f ~/.config/bubie-pack/curseforge-token ] && TOKEN=$(tr -d '[:space:]' < ~/.config/bubie-pack/curseforge-token)
  [ -n "$TOKEN" ] || { echo "Falta o token do CurseForge (CURSEFORGE_TOKEN)."; exit 1; }
  URL="https://minecraft.curseforge.com/api/projects/$CF_PROJECT_ID/upload-file"
  jq -n --rawfile cl dist/notes.md --arg dn "Bubie Pack $VER" --arg rt "$CF_RELEASE_TYPE" \
    '{changelog:$cl, changelogType:"markdown", displayName:$dn, releaseType:$rt, gameVersions:[11779,10150]}' > dist/meta.json
  MAIN=$(curl --fail-with-body -sS --max-time 1800 -H "X-Api-Token: $TOKEN" \
    -F "metadata=<dist/meta.json;type=application/json" -F "file=@dist/BubiePack-$VER.zip" "$URL")
  echo "CurseForge pack: $MAIN"
  MAIN_ID=$(echo "$MAIN" | jq -r .id)
  jq -n --rawfile cl dist/notes.md --arg dn "Bubie Pack $VER Server" --arg rt "$CF_RELEASE_TYPE" --argjson p "$MAIN_ID" \
    '{changelog:$cl, changelogType:"markdown", displayName:$dn, releaseType:$rt, parentFileID:$p}' > dist/meta-server.json
  SERVER=$(curl --fail-with-body -sS --max-time 3600 -H "X-Api-Token: $TOKEN" \
    -F "metadata=<dist/meta-server.json;type=application/json" -F "file=@dist/BubiePack-$VER-server.zip" "$URL")
  echo "CurseForge server pack: $SERVER"
fi

gh release create "v$VER" --target "$(git rev-parse HEAD)" --title "Bubie Pack $VER" --notes-file dist/notes.md \
  "dist/BubiePack-$VER.zip" "dist/BubiePack-$VER-server.zip"
echo "Publicado: v$VER"
