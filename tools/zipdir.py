"""Compacta arquivos e pastas num zip, como `zip -r`, sem depender do comando zip (que falta no Windows).

Uso: python tools/zipdir.py <saída.zip> <pasta base> <item> [<item> ...]
Os caminhos dentro do zip são relativos à pasta base e sempre usam '/'. Arquivos .sh entram como executáveis.
"""
import os, sys, zipfile

out, base, items = os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3:]


def add(z, path):
    arc = os.path.relpath(path, base).replace(os.sep, '/')
    info = zipfile.ZipInfo.from_file(path, arc)
    info.compress_type = zipfile.ZIP_DEFLATED
    mode = 0o755 if path.endswith('.sh') else 0o644
    info.external_attr = (0o100000 | mode) << 16
    with open(path, 'rb') as f:
        z.writestr(info, f.read())


with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    for item in items:
        p = os.path.join(base, item)
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs.sort()
                for name in sorted(files):
                    add(z, os.path.join(root, name))
        else:
            add(z, p)
