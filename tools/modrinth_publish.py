"""Publishes our three mods (Bubie, Voltaic Dynamics, Base Blueprint) on Modrinth: creates each project the first time
(with its page, icon and license) and uploads the current jar as a release.

The Bubie Pack itself stays on CurseForge: 75 of its mods are not on Modrinth (the FTB family, Sophisticated, Integrated
Dynamics, XyCraft...), and a Modrinth pack may only link to Modrinth files.

Token: ~/.config/bubie-pack/modrinth-token (scopes: Create projects, Create versions, Read projects, Write projects).
usage: python tools/modrinth_publish.py [bubie|voltaic|blueprint ...]   (all three by default; DRY_RUN=1 prints only)
New projects stay drafts until Modrinth's moderators approve them; the script submits them for review.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
import uuid

API = 'https://api.modrinth.com/v2'
WWW = os.path.expanduser('~/www')
STATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modrinth-projects.json')
UA = 'bubie-pack-tools/1.0'
# all three must be installed on the client and on the server
ENVIRONMENT = 'client_and_server'

MODS = {
    'blueprint': dict(repo='base-blueprint', slug='base-blueprint', title='Base Blueprint', jar='baseblueprint-{v}.jar',
                      icon='src/main/resources/baseblueprint_logo.png', categories=['utility', 'decoration'],
                      client='required', server='required', deps=[]),
    'voltaic': dict(repo='voltaic-dynamics', slug='voltaic-dynamics', title='Voltaic Dynamics', jar='voltaicdynamics-{v}.jar',
                    icon='src/main/resources/voltaicdynamics_logo.png', categories=['technology', 'utility'],
                    client='required', server='required', deps=[]),
    'bubie': dict(repo='bubie-mod', slug='bubie', title='Bubie', jar='bubie-{v}.jar',
                  icon='src/main/resources/bubie_logo.png', categories=['technology', 'utility', 'mobs'],
                  client='required', server='required', deps=[('blueprint', 'optional')]),
}


def token():
    return open(os.path.expanduser('~/.config/bubie-pack/modrinth-token'), encoding='utf-8').read().strip()


def request(method, path, body=None, files=None):
    headers = {'Authorization': token(), 'User-Agent': UA}
    data = None
    if files is not None:
        boundary = uuid.uuid4().hex
        parts = []
        for name, (filename, content, ctype) in files.items():
            disp = f'form-data; name="{name}"' + (f'; filename="{filename}"' if filename else '')
            parts.append(f'--{boundary}\r\nContent-Disposition: {disp}\r\nContent-Type: {ctype}\r\n\r\n'.encode() + content + b'\r\n')
        data = b''.join(parts) + f'--{boundary}--\r\n'.encode()
        headers['Content-Type'] = f'multipart/form-data; boundary={boundary}'
    elif body is not None:
        data = json.dumps(body).encode()
        headers['Content-Type'] = 'application/json'
    url = path if path.startswith('http') else API + path
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            raw = r.read()
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        raise SystemExit(f'{method} {path}: HTTP {e.code} {e.read().decode(errors="replace")}')


def version_of(repo):
    props = open(os.path.join(WWW, repo, 'gradle.properties'), encoding='utf-8').read()
    return re.search(r'^mod_version=(.+)$', props, re.M).group(1).strip()


def page(repo):
    """The CurseForge page text works for Modrinth too, minus the publishing notes at its end."""
    text = open(os.path.join(WWW, repo, 'CURSEFORGE.md'), encoding='utf-8').read()
    text = re.split(r'^## Publishing checklist', text, flags=re.M)[0]
    summary = re.search(r'^\*\*(.+?)\*\*', text, re.M).group(1)
    return summary[:256], text.strip()


def changelog(repo, version):
    readme = open(os.path.join(WWW, repo, 'README.md'), encoding='utf-8').read()
    m = re.search(rf'^### {re.escape(version)}\b[^\n]*\n(.*?)(?=^### |^## |\Z)', readme, re.M | re.S)
    return m.group(1).strip() if m else f'Version {version}.'


def main():
    which = sys.argv[1:] or list(MODS)
    state = json.load(open(STATE)) if os.path.exists(STATE) else {}
    for key in which:
        mod = MODS[key]
        repo = os.path.join(WWW, mod['repo'])
        v = version_of(mod['repo'])
        jar = os.path.join(repo, 'build', 'libs', mod['jar'].format(v=v))
        if not os.path.exists(jar):
            raise SystemExit(f'{jar} missing: build {mod["repo"]} first')
        summary, body = page(mod['repo'])
        print(f'{mod["title"]} {v}: {os.path.basename(jar)}')
        if os.environ.get('DRY_RUN'):
            continue
        pid = state.get(key)
        if pid is None:
            data = dict(slug=mod['slug'], title=mod['title'], description=summary, body=body, categories=mod['categories'],
                        client_side=mod['client'], server_side=mod['server'], license_id='MIT', project_type='mod',
                        initial_versions=[], is_draft=True)
            icon = open(os.path.join(repo, mod['icon']), 'rb').read()
            created = request('POST', '/project', files={'data': (None, json.dumps(data).encode(), 'application/json'),
                                                         'icon': ('icon.png', icon, 'image/png')})
            pid = state[key] = created['id']
            json.dump(state, open(STATE, 'w'), indent=1)
            print('  project created:', pid)
        deps = [dict(project_id=state[d], dependency_type=t) for d, t in mod['deps'] if d in state]
        meta = dict(name=f'{mod["title"]} {v}', version_number=v, changelog=changelog(mod['repo'], v), dependencies=deps,
                    game_versions=['1.21.1'], version_type='release', loaders=['neoforge'], featured=True,
                    project_id=pid, file_parts=['file'])
        made = request('POST', '/version', files={'data': (None, json.dumps(meta).encode(), 'application/json'),
                                                  'file': (os.path.basename(jar), open(jar, 'rb').read(), 'application/java-archive')})
        print('  version uploaded:', made['id'])
        # which side it runs on is a v3 field (v2 accepts it but ignores it); review needs it set
        request('PATCH', f'https://api.modrinth.com/v3/version/{made["id"]}', body={'environment': ENVIRONMENT})
        project = request('GET', f'/project/{pid}')
        if project.get('status') == 'draft':
            request('PATCH', f'/project/{pid}', body={'status': 'processing'})
            print('  submitted for review')


main()
