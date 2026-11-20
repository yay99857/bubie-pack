"""Uploads screenshots to a mod's Modrinth gallery (the first one is the featured image).

usage: python tools/modrinth_gallery.py <bubie|voltaic|blueprint>   (images and titles listed below)
Big PNGs are sent as JPEG (quality 90) to stay well under Modrinth's size limit.
"""
import io
import json
import os
import sys
import urllib.parse
import urllib.request

from PIL import Image

WWW = os.path.expanduser('~/www')
IDS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modrinth-projects.json')))

GALLERIES = {
    'bubie': ('bubie-mod/docs/screenshots', [
        ('lineup.png', 'Dress your crew', 'Every Bubie can have its own casing, hoodie, screen light, eyes and mouth.'),
        ('portrait.png', 'Meet Bubie', 'A little CRT robot in a hoodie that works for you.'),
        ('lumberjack.png', 'Lumberjack', 'Fells whole trees around its chest and replants the saplings.'),
        ('quarry.png', 'Quarry', 'Digs out an area in layers, leaving a staircase, and plugs lava and water first.'),
        ('farmer.png', 'Farmer', 'Harvests ripe crops and replants them.'),
        ('builder.png', 'Builder', 'Raises a Base Blueprint base block by block from its chest.'),
        ('station.png', 'Station', 'Its home: charges it with FE from any cable or with coal.'),
        ('night.png', 'At night', 'The screens glow in the dark.'),
        ('menu_job.png', 'The menu', 'Mode, job, area, status and a DJ tab.'),
        ('editor.png', 'Edit my Bubie', 'Pick colours, eyes and mouth with a turning preview.'),
    ]),
    'blueprint': ('base-blueprint/docs/screenshots', [
        ('overview.jpg', 'One click, one base', 'Pick a shape and a size, and place the whole base at once.'),
        ('preview.jpg', 'Preview in the world', 'Green where it can be built, red where something is in the way.'),
        ('menu.jpg', 'The menu', 'Shape, size, floor, walls, storeys, door, roof and foundation.'),
        ('dome.jpg', 'Domes', 'Circles can have a dome on top.'),
        ('tower.jpg', 'Towers', 'Stack storeys with a floor between them.'),
        ('octagon.jpg', 'Octagons', 'Circle, square, octagon and hexagon, any size.'),
        ('hexagon.jpg', 'Hexagons', 'Separate materials for the floor and the walls.'),
        ('foundation.jpg', 'Foundation', 'Fills the ground under the floor on uneven terrain.'),
        ('inside.jpg', 'Inside', 'A ready room to start your base.'),
    ]),
    'voltaic': ('voltaic-dynamics/docs/screenshots', [
        ('workshop.jpg', 'A Voltaic workshop', 'Generators, batteries and machines on one lag-free cable network.'),
        ('generators.jpg', 'Generators', 'Combustion, fluid (lava) and thermoelectric generators, feeding the accumulators.'),
        ('machines.jpg', 'Machines', 'Electric Furnace, Alloy Smelter and Pulverizer, with speed and efficiency upgrades.'),
        ('cables.jpg', 'Item cables', 'Pull from a chest straight into a machine, with no items in transit.'),
        ('alloy_smelter.jpg', 'Alloy Smelter', 'Up to three ingredients into alloys: iron, copper and redstone become voltaic ingots.'),
        ('night.jpg', 'At night', 'Working machines light up.'),
    ]),
}


def main(key):
    folder, images = GALLERIES[key]
    pid = IDS[key]
    token = open(os.path.expanduser('~/.config/bubie-pack/modrinth-token'), encoding='utf-8').read().strip()
    for order, (name, title, desc) in enumerate(images):
        path = os.path.join(WWW, folder, name)
        data = open(path, 'rb').read()
        ext = os.path.splitext(name)[1][1:].replace('jpeg', 'jpg')
        if ext == 'png' and len(data) > 1_500_000:
            buf = io.BytesIO()
            Image.open(path).convert('RGB').save(buf, 'JPEG', quality=90)
            data, ext = buf.getvalue(), 'jpg'
        query = urllib.parse.urlencode(dict(ext=ext, featured='true' if order == 0 else 'false', title=title,
                                            description=desc, ordering=order))
        req = urllib.request.Request(f'https://api.modrinth.com/v2/project/{pid}/gallery?{query}', data=data, method='POST',
                                     headers={'Authorization': token, 'User-Agent': 'bubie-pack-tools/1.0',
                                              'Content-Type': f'image/{"jpeg" if ext == "jpg" else ext}'})
        with urllib.request.urlopen(req, timeout=120) as r:
            print(f'{key}: {name} ({len(data) // 1024} KB) -> HTTP {r.status}')


for k in sys.argv[1:]:
    main(k)
