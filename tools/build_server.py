"""Monta o server pack: baixa os mods do manifest (menos os só de cliente) e copia configs e scripts.

Os nomes dos arquivos vêm de pack/mod-files.json (fileID -> nome do jar). Mods que não estiverem lá
são resolvidos pelo cfwidget e gravados de volta no arquivo, para o próximo build não precisar consultar.
"""
import json, os, shutil, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1])
UA = {'User-Agent': 'Mozilla/5.0 bubiepack-builder'}
NAMES_FILE = os.path.join(ROOT, 'pack', 'mod-files.json')
CLIENT_ONLY = [l.strip() for l in open(os.path.join(ROOT, 'server', 'client-only-mods.txt'))
               if l.strip() and not l.startswith('#')]


def get(url, tries=6):
    for n in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()
        except Exception as e:
            if n == tries - 1:
                raise
            print(f'retry {n + 1} {url}: {e}', flush=True)
            time.sleep(5 * (n + 1))


manifest = json.load(open(os.path.join(ROOT, 'pack', 'manifest.json')))
names = json.load(open(NAMES_FILE)) if os.path.exists(NAMES_FILE) else {}
changed = False
for f in manifest['files']:
    fid = str(f['fileID'])
    if fid not in names:
        info = json.loads(get(f"https://api.cfwidget.com/{f['projectID']}"))
        names[fid] = next(x['name'] for x in info['files'] if str(x['id']) == fid)
        changed = True
        print('resolved', names[fid], flush=True)
if changed:
    json.dump(dict(sorted(names.items())), open(NAMES_FILE, 'w'), indent=1)

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(os.path.join(OUT, 'mods'))
jobs = []
for f in manifest['files']:
    fid = str(f['fileID']); name = names[fid]
    if not name.endswith('.jar') or any(name.startswith(p) for p in CLIENT_ONLY):
        print('skip', name, flush=True)
        continue
    jobs.append((fid, name))


def download(job):
    fid, name = job
    data = get(f'https://edge.forgecdn.net/files/{fid[:4]}/{int(fid[4:])}/{name}')
    open(os.path.join(OUT, 'mods', name), 'wb').write(data)
    print('ok  ', name, flush=True)


with ThreadPoolExecutor(8) as pool:
    list(pool.map(download, jobs))

for d in ('config', 'defaultconfigs', 'kubejs'):
    # config/defaultoptions só serve ao Default Options, que é mod de cliente.
    shutil.copytree(os.path.join(ROOT, 'pack', 'overrides', d), os.path.join(OUT, d),
                    ignore=shutil.ignore_patterns('defaultoptions') if d == 'config' else None)
for n in ('start.sh', 'start.bat', 'user_jvm_args.txt', 'LEIA-ME_README.txt'):
    shutil.copy2(os.path.join(ROOT, 'server', n), os.path.join(OUT, n))
os.chmod(os.path.join(OUT, 'start.sh'), 0o755)
count = len(os.listdir(os.path.join(OUT, 'mods')))
print(count, 'mods')
if count != len(jobs):
    sys.exit(f'esperava {len(jobs)} mods, baixou {count}')
