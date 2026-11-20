#!/usr/bin/env bash
# Publica a versão do pack/manifest.json: gera os zips, envia ao CurseForge e cria o GitHub Release.
# Uso: tools/release.sh [--skip-curseforge]   (DRY_RUN=1 gera tudo e para antes de enviar)
# Antes de enviar: confere que todo arquivo do manifest está aprovado no CurseForge (SKIP_FILE_CHECK=1 pula) e roda
# os GameTests do Bubie com os mods do server pack, se ../bubie-mod existir (SKIP_PACK_TEST=1 pula).
#      tools/release.sh --server-only <fileID do pack no CurseForge>   (reenvia só o server pack)
# Token do CurseForge: variável CURSEFORGE_TOKEN ou o arquivo ~/.config/bubie-pack/curseforge-token
set -euo pipefail
cd "$(dirname "$0")/.."

SKIP_CF=false
SERVER_ONLY=""
[ "${1:-}" = "--skip-curseforge" ] && SKIP_CF=true
[ "${1:-}" = "--server-only" ] && SERVER_ONLY="${2:?informe o fileID do pack}"
CF_PROJECT_ID=${CF_PROJECT_ID:-1801989}
CF_RELEASE_TYPE=${CF_RELEASE_TYPE:-beta}
# IDs do CurseForge: 11779 = Minecraft 1.21.1, 10150 = NeoForge (GET /api/game/versions)
. tools/python.sh
VER=$($PY -c "import json;print(json.load(open('pack/manifest.json', encoding='utf-8'))['version'])")

cf_token() {
  local t=${CURSEFORGE_TOKEN:-}
  [ -z "$t" ] && [ -f ~/.config/bubie-pack/curseforge-token ] && t=$(tr -d '[:space:]' < ~/.config/bubie-pack/curseforge-token)
  [ -n "$t" ] || { echo "Falta o token do CurseForge (CURSEFORGE_TOKEN)." >&2; return 1; }
  echo "$t"
}
URL="https://minecraft.curseforge.com/api/projects/$CF_PROJECT_ID/upload-file"

# Envia o server pack como arquivo adicional do pack. Tenta 3 vezes; o CurseForge às vezes responde 524 em arquivos grandes.
upload_server() {
  local parent=$1 token; token=$(cf_token)
  jq -n --rawfile cl dist/notes.md --arg dn "Bubie Pack $VER Server" --arg rt "$CF_RELEASE_TYPE" --argjson p "$parent" \
    '{changelog:$cl, changelogType:"markdown", displayName:$dn, releaseType:$rt, parentFileID:$p}' > dist/meta-server.json
  for n in 1 2 3; do
    if SERVER=$(curl --fail-with-body -sS --max-time 3600 -H "X-Api-Token: $token" \
      -F "metadata=<dist/meta-server.json;type=application/json" -F "file=@dist/BubiePack-$VER-server.zip" "$URL"); then
      echo "CurseForge server pack: $SERVER"; return 0
    fi
    echo "Envio do server pack falhou (tentativa $n). Confira na aba Files antes de reenviar: um 524 às vezes chega mesmo assim."
    [ "$n" = 3 ] || sleep 60
  done
  echo "::warning::Server pack não enviado. Reenvie com: tools/release.sh --server-only $parent"
  return 0
}

if [ -n "$SERVER_ONLY" ]; then
  [ -f "dist/BubiePack-$VER-server.zip" ] || tools/build.sh --server
  $PY tools/release_notes.py "$VER" > dist/notes.md
  upload_server "$SERVER_ONLY"; exit 0
fi

if git ls-remote --exit-code --tags origin "refs/tags/v$VER" >/dev/null; then
  echo "A tag v$VER já existe: nada para publicar."; exit 0
fi
if [ -z "${CI:-}" ]; then
  git fetch -q origin main
  [ -z "$(git status --porcelain)" ] || { echo "Há mudanças sem commit."; exit 1; }
  [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] || { echo "Faça push antes de publicar."; exit 1; }
fi

mkdir -p dist
[ -n "${SKIP_FILE_CHECK:-}" ] || $PY tools/check_files.py
$PY tools/release_notes.py "$VER" > dist/notes.md
# O server pack (~350 MB) às vezes leva 524 no CurseForge; o do GitHub Release sempre fica, e o link vai nas notas.
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
printf '\n\nServer pack: https://github.com/%s/releases/download/v%s/BubiePack-%s-server.zip\n' "$REPO" "$VER" "$VER" >> dist/notes.md
echo "--- Notas da versão $VER ---"; cat dist/notes.md; echo "---"
tools/build.sh --server
if [ -z "${SKIP_PACK_TEST:-}" ] && [ -d ../bubie-mod ]; then
  echo "--- GameTests do Bubie com os mods do pack ---"
  (cd ../bubie-mod && tools/prepare-pack-test.sh "../minecraft-modpack/dist/server-$VER" && ./gradlew -q runPackGameTest) \
    || { echo "Os GameTests falharam: nada foi publicado. (SKIP_PACK_TEST=1 pula)"; exit 1; }
fi

if [ -n "${DRY_RUN:-}" ]; then
  jq -n --rawfile cl dist/notes.md --arg dn "Bubie Pack $VER" --arg rt "$CF_RELEASE_TYPE" \
    '{changelog:$cl, changelogType:"markdown", displayName:$dn, releaseType:$rt, gameVersions:[11779,10150]}'
  ls -la "dist/BubiePack-$VER.zip" "dist/BubiePack-$VER-server.zip"
  echo "DRY_RUN: nada foi enviado."; exit 0
fi

if [ "$SKIP_CF" = false ]; then
  TOKEN=$(cf_token)
  jq -n --rawfile cl dist/notes.md --arg dn "Bubie Pack $VER" --arg rt "$CF_RELEASE_TYPE" \
    '{changelog:$cl, changelogType:"markdown", displayName:$dn, releaseType:$rt, gameVersions:[11779,10150]}' > dist/meta.json
  MAIN=$(curl --fail-with-body -sS --max-time 1800 -H "X-Api-Token: $TOKEN" \
    -F "metadata=<dist/meta.json;type=application/json" -F "file=@dist/BubiePack-$VER.zip" "$URL")
  echo "CurseForge pack: $MAIN"
fi

gh release create "v$VER" --target "$(git rev-parse HEAD)" --title "Bubie Pack $VER" --notes-file dist/notes.md \
  "dist/BubiePack-$VER.zip" "dist/BubiePack-$VER-server.zip"
echo "GitHub: v$VER"
[ "$SKIP_CF" = true ] || upload_server "$(echo "$MAIN" | jq -r .id)"
echo "Publicado: v$VER"
