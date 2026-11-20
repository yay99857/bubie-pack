# Define $PY com um Python 3 que funcione. No Windows, `python3` costuma ser só o atalho da Microsoft Store.
# Uso: . tools/python.sh
PY=
for c in python3 python py; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(sys.version_info < (3, 8))' >/dev/null 2>&1; then
    PY=$c; break
  fi
done
[ -n "$PY" ] || { echo "Python 3 não encontrado. No Windows: winget install Python.Python.3.12" >&2; exit 1; }
# No Windows o Python usa cp1252 por padrão; os scripts do pack são UTF-8.
export PYTHONUTF8=1
