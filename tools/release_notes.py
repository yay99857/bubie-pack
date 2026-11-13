"""Imprime as notas de uma versão: release-notes/<versão>.md se existir, senão a seção do CHANGELOG.md."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ver = sys.argv[1]
custom = os.path.join(ROOT, 'release-notes', f'{ver}.md')
if os.path.exists(custom):
    print(open(custom, encoding='utf-8').read().strip())
    sys.exit(0)
text = open(os.path.join(ROOT, 'CHANGELOG.md'), encoding='utf-8').read()
m = re.search(rf'^## {re.escape(ver)}\b[^\n]*\n(.*?)(?=^## |\Z)', text, re.M | re.S)
if not m:
    sys.exit(f'CHANGELOG.md não tem a seção "## {ver}"')
print(m.group(1).strip())
