"""Confere, antes de publicar, que todo arquivo do manifest já está aprovado no CurseForge.

Um pack que cita um arquivo ainda em revisão é recusado (aconteceu na 0.6.3). Confere os mods feitos para o pack
(Bubie, Voltaic, Base Blueprint) e todo arquivo que mudou desde a última tag. A api.cfwidget.com só lista arquivos
públicos, ou seja, aprovados. Ela guarda cache por alguns minutos: um arquivo recém-aprovado pode demorar a aparecer.

Uso: python tools/check_files.py   (sai com 1 se algum arquivo não estiver aprovado)
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWN = {1818331: 'Bubie', 1809423: 'Voltaic Dynamics', 1809447: 'Base Blueprint'}


def get(url):
    for n in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'bubie-pack-release-check'})
            return json.loads(urllib.request.urlopen(req, timeout=60).read())
        except Exception as e:  # noqa: BLE001
            if n == 2:
                raise
            print(f'  {url}: {e}, tentando de novo', flush=True)
            time.sleep(5 * (n + 1))


def previous_files():
    tags = subprocess.run(['git', 'tag', '--sort=-v:refname'], cwd=ROOT, capture_output=True, text=True).stdout.split()
    if not tags:
        return set()
    old = subprocess.run(['git', 'show', f'{tags[0]}:pack/manifest.json'], cwd=ROOT, capture_output=True, text=True)
    if old.returncode != 0:
        return set()
    return {f['fileID'] for f in json.loads(old.stdout)['files']}


manifest = json.load(open(os.path.join(ROOT, 'pack', 'manifest.json'), encoding='utf-8'))
before = previous_files()
check = [f for f in manifest['files'] if f['projectID'] in OWN or f['fileID'] not in before]
print(f'Conferindo {len(check)} arquivo(s) no CurseForge...', flush=True)
missing = []
for f in check:
    info = get(f"https://api.cfwidget.com/{f['projectID']}")
    files = {x['id']: x for x in info.get('files', [])}
    name = OWN.get(f['projectID'], info.get('title', f['projectID']))
    if f['fileID'] in files:
        print(f"  ok   {name}: {files[f['fileID']]['name']}")
    else:
        print(f"  FALTA {name}: arquivo {f['fileID']} não está público (em revisão ou recusado)")
        missing.append(f)
if missing:
    print('Não publique ainda: espere o CurseForge aprovar os arquivos acima.'
          ' (Para pular esta conferência: SKIP_FILE_CHECK=1)')
    sys.exit(1)
print('Todos os arquivos estão aprovados.')
