"""Monta o server pack: baixa os mods do manifest (menos os só de cliente) e copia configs e scripts."""
import json, os, shutil, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1])
UA = {'User-Agent': 'Mozilla/5.0 bubiepack-builder'}
CLIENT_ONLY = [l.strip() for l in open(os.path.join(ROOT, 'server', 'client-only-mods.txt')) if l.strip() and not l.startswith('#')]

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(os.path.join(OUT, 'mods'))
manifest = json.load(open(os.path.join(ROOT, 'pack', 'manifest.json')))
for f in manifest['files']:
    pid, fid = f['projectID'], f['fileID']
    info = json.loads(get(f'https://api.cfwidget.com/{pid}'))
    name = next(x['name'] for x in info['files'] if x['id'] == fid)
    if not name.endswith('.jar') or any(name.startswith(p) for p in CLIENT_ONLY):
        print('skip', name); continue
    s = str(fid)
    open(os.path.join(OUT, 'mods', name), 'wb').write(get(f'https://edge.forgecdn.net/files/{s[:4]}/{int(s[4:])}/{name}'))
    print('ok  ', name)
for d in ('config', 'defaultconfigs', 'kubejs'):
    shutil.copytree(os.path.join(ROOT, 'pack', 'overrides', d), os.path.join(OUT, d))
for n in ('start.sh', 'start.bat', 'user_jvm_args.txt', 'LEIA-ME_README.txt'):
    shutil.copy2(os.path.join(ROOT, 'server', n), os.path.join(OUT, n))
os.chmod(os.path.join(OUT, 'start.sh'), 0o755)
print(len(os.listdir(os.path.join(OUT, 'mods'))), 'mods')
