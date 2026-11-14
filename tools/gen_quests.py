# Uso: python3 tools/gen_quests.py pack/overrides/config/ftbquests
import hashlib, os, sys
OUT = sys.argv[1]

def hid(key):
    v = int(hashlib.sha1(('bubiepack:' + key).encode()).hexdigest()[:16], 16) & 0x7FFFFFFFFFFFFFFF
    v |= 0x1000000000000000 if v < 0x1000000000000000 else 0
    return f'{v:016X}'

def s(x): return '"' + x.replace('\\', '\\\\').replace('"', '\\"') + '"'
def tag(t): return f'ftbfiltersystem:item_tag({t})'

CH = []
def chapter(fn, pt, en, icon, order):
    c = {'fn': fn, 'title': {'pt': pt, 'en': en}, 'icon': icon, 'order': order, 'quests': []}
    CH.append(c); return c

def q(c, key, x, y, title, pt, en, tasks, deps=(), xp=10, shape=None, size=None, items=()):
    c['quests'].append(dict(key=f"{c['fn']}/{key}", x=x, y=y, title={'pt': title[0], 'en': title[1]},
        desc={'pt': pt, 'en': en}, tasks=tasks, deps=[d if '/' in d else f"{c['fn']}/{d}" for d in deps],
        xp=xp, shape=shape, size=size, items=items))

I = lambda i, n=1: ('item', i, n)
T = lambda t, n, icon: ('tag', t, n, icon)
C = ('check',)
REC = ('&aRecomendado:&r ', '&aRecommended:&r ')
def rec(pt, en): return (REC[0] + pt, REC[1] + en)

# ================= Bem-vindo =================
c = chapter('bem_vindo', '&bBem-vindo ao Bubie Pack', '&bWelcome to Bubie Pack', 'ftbquests:book', 0)
q(c, 'inicio', 0, 0, ('&bBem-vindo ao Bubie Pack!', '&bWelcome to Bubie Pack!'),
  ['Um pack para jogar com os amigos: tecnologia, magia, exploração e automação, sem pressa.', '',
   'As quests são &aopcionais&r: nenhum mod está travado atrás delas. Elas servem de guia, principalmente no começo.'],
  ['A pack to play with friends: tech, magic, exploration and automation, at your own pace.', '',
   'Quests are &aoptional&r: no mod is locked behind them. They are a guide, especially early on.'],
  [C], shape='pentagon', size=2.0)
q(c, 'receitas', -2.5, 0, ('Ver receitas: EMI', 'Recipes: EMI'),
  ['Passe o mouse em qualquer item e aperte &eR&r para ver como fazer e &eU&r para ver onde é usado.', '',
   'Clique com o botão direito numa receita e escolha &eárvore de receitas&r (recipe tree) para ver tudo que falta até a matéria-prima.',
   'Itens favoritos ficam fixados na lateral: arraste um item para a coluna da esquerda.'],
  ['Hover any item and press &eR&r to see how to make it and &eU&r to see what uses it.', '',
   'Right-click a recipe and pick &erecipe tree&r to see everything you still need, down to raw materials.',
   'Drag an item to the left column to pin it as a favorite.'],
  [C], deps=['inicio'])
q(c, 'comandos', 2.5, 0, ('Comandos úteis', 'Useful commands'),
  ['&e/sethome&r e &e/home&r: uma casa por jogador.', '&e/spawn&r: volta para o spawn.',
   '&e/back&r: volta para onde você morreu ou de onde teleportou.', '&e/rtp&r: teleporte aleatório (recarga de 10 minutos).',
   '&e/tpa <jogador>&r: pede para teleportar até um amigo.'],
  ['&e/sethome&r and &e/home&r: one home per player.', '&e/spawn&r: back to spawn.',
   '&e/back&r: back to where you died or teleported from.', '&e/rtp&r: random teleport (10 minute cooldown).',
   '&e/tpa <player>&r: ask to teleport to a friend.'],
  [C], deps=['inicio'])
q(c, 'time', 0, 2.5, ('Jogando em time', 'Playing as a team'),
  ['Crie um time com &a/ftbteams party create <nome>&r e convide os amigos.',
   'O time compartilha o progresso das quests e as áreas protegidas.'],
  ['Create a team with &a/ftbteams party create <name>&r and invite your friends.',
   'The team shares quest progress and claimed chunks.'],
  [C], deps=['inicio'])
q(c, 'chunks', -2.5, 2.5, ('Proteger a base', 'Protect your base'),
  ['Abra o mapa do &eFTB Chunks&r (a tecla está em Opções → Controles) e clique em &aClaimed Chunks&r.',
   'Clique e arraste para proteger chunks. &eShift + clique&r mantém o chunk carregado, para as máquinas continuarem rodando quando você estiver longe.'],
  ['Open the &eFTB Chunks&r map (see Options → Controls for the key) and click &aClaimed Chunks&r.',
   'Click and drag to claim chunks. &eShift + click&r force-loads a chunk so machines keep running while you are away.'],
  [C], deps=['time'])
q(c, 'voz', 2.5, 2.5, ('Chat de voz', 'Voice chat'),
  ['O &eSimple Voice Chat&r está instalado: quem está perto ouve você.',
   'Aperte &eV&r para abrir o menu e configurar microfone e volume. Por padrão, o push-to-talk fica no &eCaps Lock&r.', '',
   '&7Em servidor dedicado, o dono precisa liberar a porta UDP 24454.'],
  ['&eSimple Voice Chat&r is installed: players near you can hear you.',
   'Press &eV&r to open its menu and set up your microphone and volume. Push-to-talk is &eCaps Lock&r by default.', '',
   '&7On a dedicated server, the owner must open UDP port 24454.'],
  [C], deps=['time'])
q(c, 'morte', 0, -2.5, ('Se você morrer', 'If you die'),
  ['Ao morrer, seus itens ficam guardados num &etúmulo&r (Corail Tombstone) no local da morte.',
   'Use &e/back&r para voltar até ele e clique no túmulo para recuperar tudo.'],
  ['When you die, your items are stored in a &egrave&r (Corail Tombstone) where you died.',
   'Use &e/back&r to return and click the grave to get everything back.'],
  [C], deps=['inicio'])

# ================= Primeiros passos =================
c = chapter('primeiros_passos', '&aPrimeiros Passos', '&aFirst Steps', 'minecraft:iron_pickaxe', 1)
q(c, 'ferro', 0, 0, ('Ferro, o começo de tudo', 'Iron, where it all begins'),
  ['Quase tudo no começo pede ferro. Os minérios do pack vêm em veias pequenas e espalhadas: explore cavernas e o deepslate.'],
  ['Almost everything early on needs iron. Ores in this pack come in small, spread-out veins: explore caves and the deepslate layer.'],
  [T('c:ingots/iron', 16, 'minecraft:iron_ingot')], shape='pentagon', size=1.5, xp=25)
q(c, 'fornalha', 2, -1.5, ('Fornalha melhor', 'A better furnace'),
  ['As fornalhas do &eIron Furnaces&r são mais rápidas e gastam menos combustível. Dá para melhorar depois sem quebrar.'],
  ['&eIron Furnaces&r are faster and use less fuel. You can upgrade them later without breaking them.'],
  [I('ironfurnaces:iron_furnace')], deps=['ferro'])
q(c, 'mochila', 2, 1.5, ('Mochila', 'Backpack'),
  ['A mochila do &eSophisticated Backpacks&r guarda bastante coisa e aceita upgrades (coletar itens, autoalimentação, filtros...).'],
  ['The &eSophisticated Backpacks&r backpack holds a lot and takes upgrades (pickup, auto-feeding, filters...).'],
  [I('sophisticatedbackpacks:backpack')], deps=['ferro'])
q(c, 'waystone', -2, -1.5, ('Waystones', 'Waystones'),
  ['Ative toda waystone que encontrar nas vilas. Depois dá para viajar entre elas.',
   'Fazer a sua própria waystone na base é uma das melhores coisas do começo.'],
  ['Activate every waystone you find in villages. You can then travel between them.',
   'Making your own waystone at your base is one of the best early-game moves.'],
  [I('waystones:waystone')], deps=['ferro'], xp=25)
q(c, 'comida', -2, 1.5, ('Comida de verdade', 'Real food'),
  ["O &eFarmer's Delight&r tem refeições que alimentam muito mais. Comece pela panela."],
  ["&eFarmer's Delight&r meals are far more filling. Start with the cooking pot."],
  [I('farmersdelight:cooking_pot')], deps=['ferro'])
q(c, 'megatocha', -4, 0, ('Base sem mobs', 'A mob-free base'),
  ['A &eMega Torch&r impede que monstros nasçam num raio grande. Coloque uma no meio da base.'],
  ['The &eMega Torch&r stops monsters from spawning in a large radius. Put one in the middle of your base.'],
  [I('torchmaster:megatorch')], deps=['waystone'])
q(c, 'andesite', 4, 0, ('Create: liga de andesito', 'Create: andesite alloy'),
  ['A liga de andesito é a base do &eCreate&r: eixos, engrenagens, prensas.',
   'Ela também é o caminho para energia sem combustível no capítulo de Energia.'],
  ['Andesite alloy is the foundation of &eCreate&r: shafts, cogs, presses.',
   'It is also the path to fuel-free power in the Power chapter.'],
  [I('create:andesite_alloy', 16)], deps=['fornalha'], xp=25)
q(c, 'prensa', 6, 0, ('Prensa mecânica', 'Mechanical press'),
  ["Com uma roda d'água girando, a prensa transforma lingotes em chapas automaticamente."],
  ['With a water wheel turning it, the press turns ingots into plates automatically.'],
  [I('create:mechanical_press')], deps=['andesite'])
q(c, 'baú', 0, 3, ('Organizando os baús', 'Organizing your chests'),
  ['Os baús do &eSophisticated Storage&r aceitam upgrades de tamanho e de automação. Comece por um baú de madeira e melhore com o tempo.'],
  ['&eSophisticated Storage&r chests take size and automation upgrades. Start with a wooden one and upgrade it over time.'],
  [I('sophisticatedstorage:chest')], deps=['mochila'])

# ================= Energia =================
c = chapter('energia', '&eEnergia: o Começo', '&ePower: Getting Started', 'powah:furnator_starter', 2)
q(c, 'inicio', 0, 0, ('Energia: por onde começar?', 'Power: where to start?'),
  ['Quase toda a tecnologia do pack usa &eFE&r (energia). Recomendação para o começo:', '',
   '&a1.&r &eFurnator (Starter)&r do Powah: queima carvão ou qualquer combustível. É o mais barato.',
   "&a2.&r &eRoda d'água + Alternator&r (Create): energia infinita, sem combustível.",
   '&a3.&r &ePainéis solares&r: complemento de dia.',
   '&a4.&r &eThermo Generator&r do Powah: o melhor do começo ao meio do jogo.', '',
   'Guarde a energia numa &ebateria&r e leve até as máquinas com &ecabos&r.'],
  ['Almost all tech in this pack runs on &eFE&r (energy). Recommended path:', '',
   '&a1.&r Powah &eFurnator (Starter)&r: burns coal or any fuel. The cheapest option.',
   '&a2.&r &eWater wheel + Alternator&r (Create): endless power, no fuel.',
   '&a3.&r &eSolar panels&r: a daytime extra.',
   '&a4.&r Powah &eThermo Generator&r: the best generator from early to mid game.', '',
   'Store energy in a &ebattery&r and move it to machines with &ecables&r.'],
  [C], shape='pentagon', size=2.0)
q(c, 'paste', -2.5, -2, ('Pasta dielétrica', 'Dielectric paste'),
  ['Quase tudo do &ePowah&r começa com pasta dielétrica (carvão + argila + lava).'],
  ['Almost everything in &ePowah&r starts with dielectric paste (coal + clay + lava).'],
  [I('powah:dielectric_paste', 8)], deps=['inicio'])
q(c, 'furnator', -5, -2, rec('Furnator', 'Furnator'),
  ['Gerador do Powah que queima combustível. Simples e barato.', 'Coloque carvão e ligue um cabo ou uma bateria do lado.'],
  ['Powah generator that burns fuel. Simple and cheap.', 'Add coal and connect a cable or a battery next to it.'],
  [I('powah:furnator_starter')], deps=['paste'], xp=50, size=1.3, items=[('minecraft:coal', 16)])
q(c, 'stirling', -5, 0, ('Alternativa: Stirling Generator', 'Alternative: Stirling Generator'),
  ['O gerador do &eEnder IO&r também queima combustível. Use se já estiver fazendo máquinas do Ender IO.'],
  ['The &eEnder IO&r generator also burns fuel. Use it if you are already building Ender IO machines.'],
  [I('enderio:stirling_generator')], deps=['inicio'])
q(c, 'roda', 2.5, -2, ("Roda d'água", 'Water wheel'),
  ['Coloque a roda na água corrente: ela gira para sempre. Mais rodas = mais força (stress).'],
  ['Place the wheel in flowing water: it spins forever. More wheels = more stress capacity.'],
  [I('create:water_wheel', 2)], deps=['inicio', 'primeiros_passos/andesite'])
q(c, 'alternator', 5, -2, rec('Alternator', 'Alternator'),
  ['O &eAlternator&r (Crafts & Additions) transforma rotação do Create em FE.',
   "Uma fileira de rodas d'água ligada nele dá energia constante sem gastar nada."],
  ['The &eAlternator&r (Crafts & Additions) turns Create rotation into FE.',
   'A row of water wheels connected to it gives steady power for free.'],
  [I('createaddition:alternator')], deps=['roda'], xp=50, size=1.3)
q(c, 'solar', 0, -3, ('Energia solar', 'Solar power'),
  ['Os painéis solares funcionam sozinhos durante o dia. Bom complemento, mas de noite não geram nada.',
   'O &eSolar Panel (Starter)&r do Powah é o mais barato; o &eSolar Generator&r do Mekanism rende um pouco mais.'],
  ['Solar panels work on their own during the day. A good extra, but they make nothing at night.',
   "Powah's &eSolar Panel (Starter)&r is the cheapest; Mekanism's &eSolar Generator&r makes a bit more."],
  [I('powah:solar_panel_starter'), I('mekanismgenerators:solar_generator')], deps=['inicio'])
q(c, 'heat', 2.5, 0, ('Heat Generator', 'Heat Generator'),
  ['O gerador de calor do &eMekanism&r queima combustível e também gera um pouco sozinho se tiver lava encostada nele.'],
  ["&eMekanism&r's Heat Generator burns fuel and also makes a little on its own when lava touches it."],
  [I('mekanismgenerators:heat_generator')], deps=['inicio'])
q(c, 'thermo', -2.5, -4, ('Thermo Generator', 'Thermo Generator'),
  ['Coloque-o em cima de uma fonte de calor (lava, magma) e alimente com água.',
   'Rende bem mais que o Furnator e não gasta combustível: é o melhor gerador do começo ao meio do jogo.'],
  ['Place it on top of a heat source (lava, magma) and feed it water.',
   'It makes far more than the Furnator and needs no fuel: the best generator from early to mid game.'],
  [I('powah:thermo_generator_starter')], deps=['paste'], xp=50)
q(c, 'bateria', 0, 2.5, rec('Bateria', 'Battery'),
  ['A &eEnergy Cell (Starter)&r guarda a energia que sobra. Ponha entre o gerador e as máquinas.'],
  ['The &eEnergy Cell (Starter)&r stores spare energy. Put it between your generators and machines.'],
  [I('powah:energy_cell_starter')], deps=['paste'], xp=25, size=1.3)
q(c, 'cubo', 2.5, 2.5, ('Energy Cube', 'Energy Cube'),
  ['O cubo de energia do &eMekanism&r guarda mais e pode carregar itens. Precisa de aço (veja o capítulo do Mekanism).'],
  ['The &eMekanism&r Energy Cube stores more and can charge items. It needs steel (see the Mekanism chapter).'],
  [I('mekanism:basic_energy_cube')], deps=['bateria', 'processamento/casing'])
q(c, 'cabos', -2.5, 2.5, ('Cabos', 'Cables'),
  ['O &eEnergy Pipe&r do Pipez é barato e transporta bastante. Use a chave (Pipe Wrench) para escolher os lados que puxam ou empurram.',
   'O &eUniversal Cable&r do Mekanism é a alternativa.'],
  ["Pipez's &eEnergy Pipe&r is cheap and moves a lot. Use the Pipe Wrench to choose which sides pull or push.",
   "Mekanism's &eUniversal Cable&r is the alternative."],
  [I('pipez:energy_pipe', 16)], deps=['inicio'])
q(c, 'orb', 0, 5, ('Energizing Orb', 'Energizing Orb'),
  ['O Orb, com &eEnergizing Rods&r em volta, &eenergiza&r itens. É assim que se avança de nível no Powah.'],
  ['The Orb, surrounded by &eEnergizing Rods&r, &eenergizes&r items. This is how you tier up in Powah.'],
  [I('powah:energizing_orb'), I('powah:energizing_rod_starter', 2)], deps=['bateria'], xp=25)
q(c, 'aco', 2.5, 5, ('Aço energizado', 'Energized steel'),
  ['Ferro + ouro no Orb = &eaço energizado&r, o material do nível Basic do Powah.'],
  ['Iron + gold in the Orb = &eenergized steel&r, the material for the Basic tier of Powah.'],
  [I('powah:steel_energized', 8)], deps=['orb'])
q(c, 'bateria2', 5, 5, ('Bateria maior', 'A bigger battery'),
  ['Com aço energizado dá para fazer a &eEnergy Cell (Basic)&r, que guarda bem mais.'],
  ['Energized steel unlocks the &eEnergy Cell (Basic)&r, which stores much more.'],
  [I('powah:energy_cell_basic')], deps=['aco'], xp=25)
q(c, 'flux', -2.5, 5, ('Flux Networks', 'Flux Networks'),
  ['Leva energia sem fio entre &eFlux Plugs&r (entrada) e &eFlux Points&r (saída), até entre dimensões.',
   'O pó de flux sai de redstone esmagada entre bedrock e obsidiana: veja como no EMI.', '',
   '&cNo Bubie Pack&r, o carregamento sem fio do Flux Controller &cnão carrega jetpacks nem a MekaSuit&r. Leve energia de reserva quando for longe!'],
  ['Moves energy wirelessly from &eFlux Plugs&r (input) to &eFlux Points&r (output), even across dimensions.',
   'Flux dust comes from redstone crushed between bedrock and obsidian: check EMI for how.', '',
   '&cIn Bubie Pack&r, the Flux Controller wireless charging &cdoes not charge jetpacks or the MekaSuit&r. Bring spare energy on long trips!'],
  [I('fluxnetworks:flux_plug'), I('fluxnetworks:flux_point')], deps=['cabos'], xp=50)

# ================= Mekanism: processamento =================
c = chapter('processamento', '&dMekanism: Minérios em Dobro', '&dMekanism: Double Your Ores', 'mekanism:enrichment_chamber', 3)
q(c, 'osmio', 0, 0, ('Ósmio', 'Osmium'),
  ['O ósmio é o metal principal do &eMekanism&r. Ele aparece no deepslate (minério do ATO).', 'Qualquer lingote de ósmio serve.'],
  ['Osmium is the core metal of &eMekanism&r. It is found in the deepslate layer (ATO ore).', 'Any osmium ingot counts.'],
  [T('c:ingots/osmium', 16, 'mekanism:ingot_osmium')], shape='pentagon', size=1.5, xp=25)
q(c, 'infuser', 2.5, 0, ('Metallurgic Infuser', 'Metallurgic Infuser'),
  ['A primeira máquina do Mekanism: mistura metais com carvão, redstone e outros. Precisa de energia.'],
  ['The first Mekanism machine: infuses metals with coal, redstone and more. It needs power.'],
  [I('mekanism:metallurgic_infuser')], deps=['osmio', 'energia/inicio'], xp=25)
q(c, 'aco', 5, -1.5, ('Aço', 'Steel'),
  ['Ferro + carvão no Infuser = &eaço&r. Você vai precisar de muito.'],
  ['Iron + coal in the Infuser = &esteel&r. You will need a lot of it.'],
  [T('c:ingots/steel', 16, 'mekanism:ingot_steel')], deps=['infuser'])
q(c, 'circuito', 5, 1.5, ('Circuito básico', 'Basic circuit'),
  ['Ósmio + redstone no Infuser = liga infundida; com ela, faça os circuitos básicos.'],
  ['Osmium + redstone in the Infuser = infused alloy; use it to make basic circuits.'],
  [I('mekanism:basic_control_circuit', 4)], deps=['infuser'])
q(c, 'casing', 7.5, 0, ('Steel Casing', 'Steel Casing'),
  ['A carcaça de aço é a base de quase todas as máquinas do Mekanism.'],
  ['The steel casing is the base of almost every Mekanism machine.'],
  [I('mekanism:steel_casing', 2)], deps=['aco', 'circuito'], xp=25)
q(c, 'enrichment', 10, 0, rec('Enrichment Chamber', 'Enrichment Chamber'),
  ['&eDobra os minérios&r: cada minério vira 2 pós, que você funde em 2 lingotes.', 'Coloque-a entre a mineração e a fornalha.'],
  ['&eDoubles your ores&r: each ore becomes 2 dusts, which you smelt into 2 ingots.', 'Put it between your mining and your furnace.'],
  [I('mekanism:enrichment_chamber')], deps=['casing'], xp=50, size=1.3, items=[('minecraft:raw_iron', 8)])
q(c, 'smelter', 12.5, -1.5, ('Energized Smelter', 'Energized Smelter'),
  ['Uma fornalha elétrica, rápida e sem combustível. Ligue logo depois da Enrichment Chamber.'],
  ['An electric furnace: fast and fuel-free. Put it right after the Enrichment Chamber.'],
  [I('mekanism:energized_smelter')], deps=['enrichment'])
q(c, 'purification', 12.5, 1.5, ('Triplicando', 'Tripling'),
  ['A &ePurification Chamber&r usa oxigênio para tirar &e3 lingotes&r por minério. É o próximo passo.'],
  ['The &ePurification Chamber&r uses oxygen to get &e3 ingots&r per ore. That is the next step.'],
  [I('mekanism:purification_chamber')], deps=['enrichment'], xp=50)
q(c, 'configurator', 10, 2.5, ('Configurator', 'Configurator'),
  ['Shift + clique com o Configurator muda os lados de entrada e saída das máquinas.'],
  ['Shift + click with the Configurator to change machine input and output sides.'],
  [I('mekanism:configurator')], deps=['casing'])

# ================= Armazenamento =================
c = chapter('armazenamento', '&9Armazenamento', '&9Storage', 'ae2:terminal', 4)
q(c, 'gaveta', 0, 0, ('Gavetas', 'Drawers'),
  ['As gavetas do &eFunctional Storage&r guardam muitas unidades de um item só. Ótimas para minérios e blocos.'],
  ['&eFunctional Storage&r drawers hold huge amounts of a single item. Great for ores and blocks.'],
  [I('functionalstorage:oak_1', 4)], shape='pentagon', size=1.5)
q(c, 'controller', 2.5, 0, ('Storage Controller', 'Storage Controller'),
  ['Junta todas as gavetas encostadas: você coloca e tira itens de todas pelo controlador.'],
  ['Links all touching drawers: insert and extract from all of them through the controller.'],
  [I('functionalstorage:storage_controller')], deps=['gaveta'], xp=25)
q(c, 'meteoro', 0, 3, ('Applied Energistics 2', 'Applied Energistics 2'),
  ['O &eAE2&r guarda tudo digitalmente. Para começar, ache um meteorito com a bússola: dentro dele estão as prensas do Inscriber.'],
  ['&eAE2&r stores everything digitally. To start, find a meteorite with the compass: the Inscriber presses are inside.'],
  [I('ae2:meteorite_compass')], deps=['gaveta'])
q(c, 'prensas', 2.5, 3, ('As prensas', 'The presses'),
  ['Pegue as 4 prensas no meteorito: lógica, cálculo, engenharia e silício.'],
  ['Collect the 4 presses from the meteorite: logic, calculation, engineering and silicon.'],
  [I('ae2:logic_processor_press'), I('ae2:calculation_processor_press'), I('ae2:engineering_processor_press'), I('ae2:silicon_press')],
  deps=['meteoro'], xp=50)
q(c, 'inscriber', 5, 3, ('Inscriber e Charger', 'Inscriber and Charger'),
  ['O Inscriber usa as prensas para fazer os processadores. O Charger carrega o quartzo de certus.'],
  ['The Inscriber uses the presses to make processors. The Charger charges certus quartz.'],
  [I('ae2:inscriber'), I('ae2:charger')], deps=['prensas', 'energia/inicio'], xp=25)
q(c, 'processadores', 7.5, 3, ('Processadores', 'Processors'),
  ['Faça um de cada. Eles aparecem em quase todas as peças do AE2.'],
  ['Make one of each. They are used in almost every AE2 part.'],
  [I('ae2:logic_processor'), I('ae2:calculation_processor'), I('ae2:engineering_processor')], deps=['inscriber'], xp=25)
q(c, 'rede', 10, 3, ('&aSua primeira rede ME', '&aYour first ME network'),
  ['O mínimo: &eME Drive&r + &eTerminal&r + &eEnergy Acceptor&r ligados por cabos, e uma célula de 1k no drive.',
   'Sem Controller, a rede aceita até 8 dispositivos: mais que suficiente para começar.'],
  ['The minimum: &eME Drive&r + &eTerminal&r + &eEnergy Acceptor&r joined by cables, with a 1k cell in the drive.',
   'Without a Controller the network supports up to 8 devices: plenty to get started.'],
  [I('ae2:drive'), I('ae2:terminal'), I('ae2:energy_acceptor'), I('ae2:item_storage_cell_1k')],
  deps=['processadores'], xp=100, size=1.5, shape='hexagon')
q(c, 'quimicos', 12.5, 3, ('Químicos no AE2', 'Chemicals in AE2'),
  ['Com o &eApplied Mekanistics&r, células químicas guardam gases e químicos do Mekanism na mesma rede.'],
  ['With &eApplied Mekanistics&r, chemical cells store Mekanism gases and chemicals in the same network.'],
  [I('appmek:chemical_storage_cell_1k')], deps=['rede'])

# ================= AE2: autocrafting =================
c = chapter('ae2_autocrafting', '&9AE2: Autocrafting', '&9AE2: Autocrafting', 'ae2:pattern_provider', 5)
q(c, 'controller', 0, 0, ('ME Controller', 'ME Controller'),
  ['Com o &eController&r, a rede deixa de ter o limite de 8 dispositivos: cada lado dele leva 32 canais.',
   'Ele não pode encostar em outro Controller fora do mesmo bloco multibloco.'],
  ['With a &eController&r, the network is no longer limited to 8 devices: each face carries 32 channels.',
   'Controllers must not touch another Controller unless they form one multiblock.'],
  [I('ae2:controller')], deps=['armazenamento/rede'], shape='pentagon', size=1.5, xp=50)
q(c, 'cabos', 2.5, -1.5, ('Cabos inteligentes', 'Smart cables'),
  ['O &eSmart Cable&r mostra os canais usados com luzes. O &eDense Cable&r leva 32 canais num cabo só.'],
  ['&eSmart Cables&r show used channels with lights. &eDense Cables&r carry 32 channels in one cable.'],
  [I('ae2:fluix_smart_cable', 16), I('ae2:fluix_smart_dense_cable', 2)], deps=['controller'])
q(c, 'celula4k', 2.5, 1.5, ('Mais espaço', 'More space'),
  ['A célula de &e4k&r guarda 4 vezes mais que a de 1k. Os tipos diferentes de item também ocupam espaço.'],
  ['A &e4k&r cell holds 4 times more than a 1k. Each different item type also takes up space.'],
  [I('ae2:item_storage_cell_4k')], deps=['controller'])
q(c, 'cpu', 5, 0, ('Crafting CPU', 'Crafting CPU'),
  ['Monte um bloco de &eCrafting Units&r com pelo menos um &eCrafting Storage&r: essa é a CPU que faz os pedidos.',
   'Mais storage = pedidos maiores. &eCo-Processing Units&r (aceleradores) fazem vários passos ao mesmo tempo.'],
  ['Build a block of &eCrafting Units&r with at least one &eCrafting Storage&r: that is the CPU that runs crafting jobs.',
   'More storage = bigger jobs. &eCo-Processing Units&r (accelerators) run several steps at once.'],
  [I('ae2:1k_crafting_storage'), I('ae2:crafting_accelerator')], deps=['controller'], xp=50)
q(c, 'padroes', 7.5, -1.5, ('Padrões', 'Patterns'),
  ['No &ePattern Encoding Terminal&r você grava receitas em &eBlank Patterns&r. Use o EMI para preencher a receita com um clique.'],
  ['In the &ePattern Encoding Terminal&r you write recipes onto &eBlank Patterns&r. Use EMI to fill in the recipe with one click.'],
  [I('ae2:pattern_encoding_terminal'), I('ae2:blank_pattern', 8)], deps=['cpu'])
q(c, 'assembler', 7.5, 1.5, rec('Molecular Assembler', 'Molecular Assembler'),
  ['Encoste um &ePattern Provider&r num &eMolecular Assembler&r e coloque os padrões de crafting no Provider.',
   'Agora peça qualquer item no terminal: a rede fabrica sozinha.'],
  ['Place a &ePattern Provider&r against a &eMolecular Assembler&r and put your crafting patterns in the Provider.',
   'Now request any item from the terminal: the network crafts it on its own.'],
  [I('ae2:pattern_provider'), I('ae2:molecular_assembler')], deps=['cpu'], xp=100, size=1.3)
q(c, 'maquinas', 10, 1.5, ('Autocrafting com máquinas', 'Autocrafting with machines'),
  ['Padrões de &eprocessamento&r servem para máquinas: o Pattern Provider manda os ingredientes para a máquina encostada nele',
   'e o resultado volta para a rede por uma &eInterface&r ou pelo próprio Provider.'],
  ['&eProcessing&r patterns are for machines: the Pattern Provider pushes the ingredients into the machine next to it,',
   'and the output comes back into the network through an &eInterface&r or the Provider itself.'],
  [I('ae2:interface')], deps=['assembler'], xp=25)
q(c, 'barramentos', 10, -1.5, ('Import, Export e Storage Bus', 'Import, Export and Storage Bus'),
  ['O &eImport Bus&r puxa itens de um baú ou máquina para a rede; o &eExport Bus&r empurra para fora.',
   'O &eStorage Bus&r num Storage Controller do Functional Storage faz a rede enxergar todas as gavetas.'],
  ['The &eImport Bus&r pulls items into the network; the &eExport Bus&r pushes them out.',
   'A &eStorage Bus&r on a Functional Storage controller lets the network see all your drawers.'],
  [I('ae2:import_bus'), I('ae2:export_bus'), I('ae2:storage_bus')], deps=['padroes'])
q(c, 'wireless', 12.5, 0, ('Terminal sem fio', 'Wireless terminal'),
  ['Com um &eWireless Access Point&r ligado à rede, o &eWireless Terminal&r acessa tudo de longe. Carregue-o no Charger.'],
  ['With a &eWireless Access Point&r on the network, the &eWireless Terminal&r reaches everything from afar. Charge it in the Charger.'],
  [I('ae2:wireless_access_point'), I('ae2:wireless_terminal')], deps=['maquinas', 'barramentos'], xp=50)

# ================= Mekanism: avançado =================
c = chapter('mekanism_avancado', '&dMekanism: Avançado', '&dMekanism: Advanced', 'mekanism:chemical_injection_chamber', 6)
q(c, 'circuito', 0, 0, ('Circuito avançado', 'Advanced circuit'),
  ['Liga reforçada (liga infundida + diamante no Infuser) leva aos &ecircuitos avançados&r e às máquinas melhores.'],
  ['Reinforced alloy (infused alloy + diamond in the Infuser) leads to &eadvanced circuits&r and better machines.'],
  [I('mekanism:advanced_control_circuit', 4)], deps=['processamento/casing'], shape='pentagon', size=1.5, xp=25)
q(c, 'upgrades', 2.5, -2, ('Upgrades', 'Upgrades'),
  ['&eSpeed Upgrades&r deixam as máquinas mais rápidas; &eEnergy Upgrades&r reduzem o gasto. Coloque no slot de upgrade da máquina.'],
  ['&eSpeed Upgrades&r make machines faster; &eEnergy Upgrades&r cut their power use. Put them in the machine upgrade slot.'],
  [I('mekanism:upgrade_speed'), I('mekanism:upgrade_energy')], deps=['circuito'])
q(c, 'installer', 2.5, 2, ('Tier Installers', 'Tier Installers'),
  ['Os &eTier Installers&r transformam uma máquina comum numa Factory, que processa vários itens ao mesmo tempo, sem quebrar nada.'],
  ['&eTier Installers&r turn a regular machine into a Factory that processes several items at once, without breaking it.'],
  [I('mekanism:basic_tier_installer')], deps=['circuito'])
q(c, 'separador', 5, 0, ('Electrolytic Separator', 'Electrolytic Separator'),
  ['Separa água em &ehidrogênio&r e &eoxigênio&r. O oxigênio vai para a Purification Chamber; o hidrogênio é combustível.'],
  ['Splits water into &ehydrogen&r and &eoxygen&r. Oxygen feeds the Purification Chamber; hydrogen is fuel.'],
  [I('mekanism:electrolytic_separator')], deps=['circuito'], xp=25)
q(c, 'jetpack', 7.5, -2, ('Jetpack a hidrogênio', 'Hydrogen jetpack'),
  ['O &eJetpack&r do Mekanism voa com hidrogênio, não com energia. Abasteça num &eChemical Tank&r cheio de hidrogênio.',
   'Ótimo para o Nether, já que o Flux não carrega jetpacks neste pack.'],
  ["Mekanism's &eJetpack&r flies on hydrogen, not energy. Fill it in a &eChemical Tank&r full of hydrogen.",
   'Great for the Nether, since Flux does not charge jetpacks in this pack.'],
  [I('mekanism:jetpack'), I('mekanism:basic_chemical_tank')], deps=['separador'], xp=25)
q(c, 'gas_gen', 7.5, 2, ('Energia de hidrogênio', 'Hydrogen power'),
  ['O &eGas-Burning Generator&r queima hidrogênio (ou etileno). Funciona, mas o separador gasta mais energia do que o hidrogênio devolve: use etileno para lucrar.'],
  ['The &eGas-Burning Generator&r burns hydrogen (or ethylene). It works, but the separator uses more power than hydrogen gives back: use ethylene for a profit.'],
  [I('mekanismgenerators:gas_burning_generator')], deps=['separador'])
q(c, 'injecao', 10, 0, ('4x: Chemical Injection', '4x: Chemical Injection'),
  ['A &eChemical Injection Chamber&r com cloreto de hidrogênio tira &e4 lingotes&r por minério.',
   'O cloreto de hidrogênio vem do &eChemical Infuser&r (hidrogênio + cloro). O cloro sai da salmoura no Electrolytic Separator.'],
  ['The &eChemical Injection Chamber&r with hydrogen chloride gets &e4 ingots&r per ore.',
   'Hydrogen chloride comes from the &eChemical Infuser&r (hydrogen + chlorine). Chlorine comes from brine in the Electrolytic Separator.'],
  [I('mekanism:chemical_injection_chamber'), I('mekanism:chemical_infuser')], deps=['separador'], xp=50, size=1.3)
q(c, 'dissolucao', 12.5, 0, ('5x: Dissolution', '5x: Dissolution'),
  ['O topo do processamento: &eChemical Dissolution Chamber&r (ácido sulfúrico) → &eChemical Washer&r → &eChemical Crystallizer&r.',
   'Resultado: &e5 lingotes&r por minério.'],
  ['The top of ore processing: &eChemical Dissolution Chamber&r (sulfuric acid) → &eChemical Washer&r → &eChemical Crystallizer&r.',
   'Result: &e5 ingots&r per ore.'],
  [I('mekanism:chemical_dissolution_chamber'), I('mekanism:chemical_washer'), I('mekanism:chemical_crystallizer')],
  deps=['injecao'], xp=100, size=1.3, shape='hexagon')
q(c, 'miner', 10, -2.5, ('Digital Miner', 'Digital Miner'),
  ['O &eDigital Miner&r minera só os minérios que você filtrar, num raio grande, sem cavar o mapa. Gasta bastante energia.'],
  ['The &eDigital Miner&r mines only the ores you filter for, in a large radius, without digging up the map. It uses a lot of power.'],
  [I('mekanism:digital_miner')], deps=['upgrades'], xp=50)

# ================= Create =================
c = chapter('create', '&6Create: Automação', '&6Create: Automation', 'create:cogwheel', 7)
q(c, 'engrenagens', 0, 0, ('Engrenagens e óculos', 'Cogs and goggles'),
  ['Engrenagens passam rotação; a engrenagem grande muda a velocidade. Os &eóculos do engenheiro&r mostram velocidade e stress.'],
  ["Cogs pass rotation along; large cogs change the speed. The &eEngineer's Goggles&r show speed and stress."],
  [I('create:cogwheel', 8), I('create:large_cogwheel', 2), I('create:goggles')], deps=['primeiros_passos/andesite'], shape='pentagon', size=1.5, xp=25)
q(c, 'esteira', 2.5, -2, ('Esteiras e depósitos', 'Belts and depots'),
  ['A &eesteira&r leva itens entre máquinas. O &eDepot&r segura um item para a prensa ou outra máquina trabalhar.'],
  ['&eBelts&r carry items between machines. The &eDepot&r holds an item for a press or other machine to work on.'],
  [I('create:belt_connector', 4), I('create:depot')], deps=['engrenagens'])
q(c, 'moinho', 2.5, 2, ('Moer e lavar', 'Milling and washing'),
  ['O &eMillstone&r mói itens. Um &eEncased Fan&r soprando através de água &elava&r itens; através de lava, &efunde&r; através de fogo de alma, &eassombra&r.'],
  ['The &eMillstone&r grinds items. An &eEncased Fan&r blowing through water &ewashes&r items; through lava it &esmelts&r; through soul fire it &ehaunts&r.'],
  [I('create:millstone'), I('create:encased_fan')], deps=['engrenagens'])
q(c, 'crushing', 5, 2, ('Crushing Wheels', 'Crushing Wheels'),
  ['Duas &eCrushing Wheels&r transformam minério bruto em minério triturado, com chance de extra e XP.',
   'Lave o minério triturado com o ventilador para ganhar pepitas a mais: rende mais do que fundir direto.'],
  ['Two &eCrushing Wheels&r turn raw ore into crushed ore, with a chance of extras and XP.',
   'Wash crushed ore with a fan for bonus nuggets: better yield than smelting directly.'],
  [I('create:crushing_wheel', 2), I('create:crushed_raw_iron', 8)], deps=['moinho'], xp=50)
q(c, 'latao', 5, -2, ('Latão', 'Brass'),
  ['Misture cobre e zinco num &eBasin&r com um &eMechanical Mixer&r em cima e um &eBlaze Burner&r embaixo.',
   'O Blaze Burner vazio é carregado clicando num blaze com ele.'],
  ['Mix copper and zinc in a &eBasin&r with a &eMechanical Mixer&r above and a &eBlaze Burner&r below.',
   'Fill an empty Blaze Burner by clicking a blaze with it.'],
  [I('create:mechanical_mixer'), I('create:basin'), I('create:blaze_burner'), T('c:ingots/brass', 16, 'create:brass_ingot')],
  deps=['esteira'], xp=50)
q(c, 'mecanismo', 7.5, -2, ('Mecanismo de precisão', 'Precision mechanism'),
  ['O &emecanismo de precisão&r é feito numa linha de montagem com deployers. Ele libera as peças de latão do Create.'],
  ['The &eprecision mechanism&r is made on a sequenced assembly line with deployers. It unlocks Create brass parts.'],
  [I('create:precision_mechanism', 4), I('create:deployer')], deps=['latao'], xp=50)
q(c, 'braco', 10, -2, ('Braço mecânico', 'Mechanical arm'),
  ['O &eMechanical Arm&r pega itens de um lugar e coloca em outro: ótimo para alimentar máquinas e depósitos.'],
  ['The &eMechanical Arm&r moves items from one spot to another: great for feeding machines and depots.'],
  [I('create:mechanical_arm')], deps=['mecanismo'])
q(c, 'farm', 2.5, 4.5, ('Farm automática', 'Automatic farm'),
  ['Uma &eMechanical Harvester&r numa estrutura que se move colhe plantações sozinha. Uma &eMechanical Drill&r faz o mesmo com pedra.'],
  ['A &eMechanical Harvester&r on a moving contraption harvests crops by itself. A &eMechanical Drill&r does the same with stone.'],
  [I('create:mechanical_harvester'), I('create:mechanical_drill')], deps=['engrenagens'])
q(c, 'motor', 10, 2, ('Motor elétrico', 'Electric motor'),
  ['O &eElectric Motor&r (Crafts & Additions) faz o contrário do Alternator: usa FE para gerar rotação, sem rodas.'],
  ['The &eElectric Motor&r (Crafts & Additions) does the opposite of the Alternator: it turns FE into rotation, no wheels needed.'],
  [I('createaddition:electric_motor')], deps=['mecanismo', 'energia/alternator'], xp=25)
q(c, 'vapor', 12.5, 0, ('Motor a vapor', 'Steam engine'),
  ['Um &eFluid Tank&r com Blaze Burners embaixo vira caldeira; o &eSteam Engine&r em cima dá muita força. É a energia forte do Create.'],
  ['A &eFluid Tank&r with Blaze Burners below becomes a boiler; a &eSteam Engine&r on it gives lots of stress. Create\'s big power source.'],
  [I('create:steam_engine'), I('create:fluid_tank', 4)], deps=['braco', 'motor'], xp=100, size=1.3, shape='hexagon')

# ================= Mystical Agriculture =================
c = chapter('mystical', '&2Mystical Agriculture', '&2Mystical Agriculture', 'mysticalagriculture:inferium_essence', 8)
q(c, 'essencia', 0, 0, ('Essência de inferium', 'Inferium essence'),
  ['A &eessência de inferium&r vem do minério de inferium e às vezes cai de mobs. É a base de todo o mod.'],
  ['&eInferium essence&r comes from inferium ore and sometimes drops from mobs. It is the base of the whole mod.'],
  [I('mysticalagriculture:inferium_essence', 32)], shape='pentagon', size=1.5, xp=25)
q(c, 'sementes', 2.5, -1.5, ('Sementes de inferium', 'Inferium seeds'),
  ['Plante as &esementes de inferium&r para colher mais essência. Em terra de inferium, rendem um pouco mais.'],
  ['Plant &einferium seeds&r to grow more essence. On inferium farmland they yield a bit more.'],
  [I('mysticalagriculture:inferium_seeds'), I('mysticalagriculture:inferium_farmland', 4)], deps=['essencia'])
q(c, 'prosperidade', 2.5, 1.5, ('Fragmentos de prosperidade', 'Prosperity shards'),
  ['O &eminério de prosperidade&r dá fragmentos, usados em quase todas as sementes de recurso.'],
  ['&eProsperity ore&r drops shards, used in almost every resource seed.'],
  [I('mysticalagriculture:prosperity_shard', 16)], deps=['essencia'])
q(c, 'altar', 5, 0, ('Altar de infusão', 'Infusion altar'),
  ['As sementes de recurso são feitas no &eInfusion Altar&r com 8 &epedestais&r em volta. Ative com redstone.'],
  ['Resource seeds are made on the &eInfusion Altar&r with 8 &epedestals&r around it. Activate it with redstone.'],
  [I('mysticalagriculture:infusion_altar'), I('mysticalagriculture:infusion_pedestal', 8)], deps=['sementes', 'prosperidade'], xp=50)
q(c, 'ferro', 7.5, 0, rec('Sementes de ferro', 'Iron seeds'),
  ['A primeira semente de recurso que vale a pena: ferro infinito sem minerar.'],
  ['The first resource seed worth making: endless iron without mining.'],
  [I('mysticalagriculture:iron_seeds')], deps=['altar'], xp=50, size=1.3)
q(c, 'tiers', 5, 2.5, ('Essências melhores', 'Better essences'),
  ['4 essências de um nível viram 1 do próximo: inferium → prudentium → tertium → imperium → supremium.',
   'Sementes melhores pedem essências melhores.'],
  ['4 essences of one tier craft into 1 of the next: inferium → prudentium → tertium → imperium → supremium.',
   'Better seeds need better essences.'],
  [I('mysticalagriculture:prudentium_essence', 16), I('mysticalagriculture:tertium_essence', 4)], deps=['altar'])
q(c, 'regador', 5, -2.5, ('Regador', 'Watering can'),
  ['O &eregador&r acelera as plantas em volta enquanto você segura o clique. Melhore com essências.'],
  ['The &ewatering can&r speeds up nearby crops while you hold right-click. Upgrade it with essences.'],
  [I('mysticalagriculture:inferium_watering_can')], deps=['sementes'])
q(c, 'cristal', 10, 0, ('Cristal de infusão', 'Infusion crystal'),
  ['O &eInfusion Crystal&r substitui a essência nas receitas de crafting e dura vários usos. O &eMaster Infusion Crystal&r não acaba.'],
  ['The &eInfusion Crystal&r replaces essence in crafting recipes and lasts many uses. The &eMaster Infusion Crystal&r never breaks.'],
  [I('mysticalagriculture:infusion_crystal')], deps=['ferro'])
q(c, 'botany', 10, 2.5, ('Botany Pots', 'Botany Pots'),
  ['As sementes do Mystical Agriculture funcionam nos &eBotany Pots&r: farms compactas que dá para automatizar com funis.'],
  ['Mystical Agriculture seeds work in &eBotany Pots&r: compact farms you can automate with hoppers.'],
  [C], deps=['ferro'])

# ================= Ars Nouveau =================
c = chapter('ars', '&5Ars Nouveau', '&5Ars Nouveau', 'ars_nouveau:novice_spell_book', 9)
q(c, 'livro', 0, 0, ('Livro de feitiços', 'Spell book'),
  ['O &eNovice Spell Book&r é o começo do Ars Nouveau. O &eWorn Notebook&r é o guia do mod: leia quando tiver dúvida.'],
  ['The &eNovice Spell Book&r is where Ars Nouveau begins. The &eWorn Notebook&r is the mod guide: read it when in doubt.'],
  [I('ars_nouveau:novice_spell_book')], shape='pentagon', size=1.5, xp=25)
q(c, 'feitico', 2.5, -2, ('Seu primeiro feitiço', 'Your first spell'),
  ['Um feitiço é uma &eforma&r (Projectile, Touch, Self) mais &eefeitos&r (Break, Harm...).',
   'Abra o livro, monte &eProjectile + Break&r e você tem uma picareta à distância.'],
  ['A spell is a &eform&r (Projectile, Touch, Self) plus &eeffects&r (Break, Harm...).',
   'Open the book, build &eProjectile + Break&r and you have a ranged pickaxe.'],
  [C], deps=['livro'])
q(c, 'source', 2.5, 2, ('Source gems', 'Source gems'),
  ['As &esource gems&r saem de ametista na &eImbuement Chamber&r.'],
  ['&eSource gems&r come from amethyst in the &eImbuement Chamber&r.'],
  [I('ars_nouveau:source_gem', 8)], deps=['livro'])
q(c, 'jarro', 5, 2, ('Gerando source', 'Making source'),
  ['A &eSource&r é a energia da magia. Guarde num &eSource Jar&r.',
   'Os &eSourcelinks&r geram source: o Agronomic com plantas crescendo, o Volcanic queimando combustível, o Vitalic com mobs.'],
  ['&eSource&r is the energy of magic. Store it in a &eSource Jar&r.',
   '&eSourcelinks&r generate it: Agronomic from growing crops, Volcanic from burning fuel, Vitalic from mobs.'],
  [I('ars_nouveau:source_jar'), I('ars_nouveau:agronomic_sourcelink')], deps=['source'], xp=25)
q(c, 'imbuement', 7.5, 2, ('Imbuement Chamber', 'Imbuement Chamber'),
  ['A &eImbuement Chamber&r usa source para transformar itens: source gems e as &eessências&r dos elementos.'],
  ['The &eImbuement Chamber&r uses source to transform items: source gems and the elemental &eessences&r.'],
  [I('ars_nouveau:imbuement_chamber')], deps=['jarro'])
q(c, 'glifos', 5, -2, ('Mesa do escriba', "Scribe's Table"),
  ['Novos &eglifos&r (peças de feitiço) são feitos na &eScribe\'s Table&r. Comece pelos básicos: Projectile, Touch, Break e Harm.'],
  ["New &eglyphs&r (spell parts) are made at the &eScribe's Table&r. Start with the basics: Projectile, Touch, Break and Harm."],
  [I('ars_nouveau:scribes_table'), I('ars_nouveau:glyph_projectile'), I('ars_nouveau:glyph_break')], deps=['feitico'], xp=25)
q(c, 'aparato', 10, 0, ('Enchanting Apparatus', 'Enchanting Apparatus'),
  ['O &eEnchanting Apparatus&r em cima de um &eArcane Core&r, com &epedestais&r em volta, faz os itens mágicos mais fortes.'],
  ['The &eEnchanting Apparatus&r on an &eArcane Core&r, with &epedestals&r around it, crafts the strongest magic items.'],
  [I('ars_nouveau:enchanting_apparatus'), I('ars_nouveau:arcane_core'), I('ars_nouveau:arcane_pedestal', 4)], deps=['glifos', 'imbuement'], xp=50)
q(c, 'aprendiz', 12.5, 0, ('Livro de aprendiz', 'Apprentice book'),
  ['O &eApprentice Spell Book&r guarda feitiços maiores e libera glifos de nível 2.'],
  ['The &eApprentice Spell Book&r holds bigger spells and unlocks tier 2 glyphs.'],
  [I('ars_nouveau:apprentice_spell_book')], deps=['aparato'], xp=50, size=1.3)
q(c, 'familiares', 10, 2.5, ('Ajudantes', 'Helpers'),
  ['O &eStarbuncle&r carrega itens entre baús; o &eWixie&r faz crafting e poções para você. Use os amuletos (charms) para invocá-los.'],
  ['The &eStarbuncle&r carries items between chests; the &eWixie&r crafts items and potions for you. Use their charms to summon them.'],
  [I('ars_nouveau:starbuncle_charm')], deps=['aparato'])

# ================= write =================
qd = os.path.join(OUT, 'quests'); os.makedirs(os.path.join(qd, 'chapters'), exist_ok=True)
os.makedirs(os.path.join(qd, 'lang'), exist_ok=True)
seen = {}
def uid(k):
    v = hid(k); assert seen.setdefault(v, k) == k, (k, seen[v]); return v
allq = {qq['key'] for ch in CH for qq in ch['quests']}
open(os.path.join(qd, 'data.snbt'), 'w').write('''{
	default_autoclaim_rewards: "disabled"
	default_consume_items: false
	default_quest_disable_jei: false
	default_quest_shape: "circle"
	default_reward_team: false
	detection_delay: 20
	disable_gui: false
	drop_loot_crates: false
	emergency_items_cooldown: 300
	grid_scale: 0.5d
	icon: {
		id: "ftbquests:book"
	}
	lock_message: ""
	loot_crate_no_drop: {
		boss: 0
		monster: 600
		passive: 4000
	}
	pause_game: false
	progression_mode: "flexible"
	show_lock_icons: true
	version: 13
}
''')
open(os.path.join(qd, 'chapter_groups.snbt'), 'w').write('{\n\tchapter_groups: [ ]\n}\n')
LANG = {'pt': {'file.0000000000000001.title': 'Bubie Pack'}, 'en': {'file.0000000000000001.title': 'Bubie Pack'}}
total = 0
for ch in CH:
    cid = uid('chapter:' + ch['fn'])
    for l in LANG: LANG[l][f'chapter.{cid}.title'] = ch['title'][l]
    L = ['{', '\tdefault_hide_dependency_lines: false', '\tdefault_quest_shape: ""', f'\tfilename: {s(ch["fn"])}', '\tgroup: ""',
         f'\ticon: {{ id: {s(ch["icon"])} }}', f'\tid: {s(cid)}', f'\torder_index: {ch["order"]}', '\tquest_links: [ ]', '\tquests: [']
    for qq in ch['quests']:
        total += 1; qid = uid('quest:' + qq['key'])
        for d in qq['deps']: assert d in allq, d
        L.append('\t\t{')
        if qq['deps']: L.append('\t\t\tdependencies: [' + ', '.join(s(hid('quest:' + d)) for d in qq['deps']) + ']')
        L.append(f'\t\t\tid: {s(qid)}')
        rw = [f'{{ id: {s(uid("rxp:" + qq["key"]))}, type: "xp", xp: {qq["xp"]} }}']
        for n, (iid, cnt) in enumerate(qq['items']):
            rw.append(f'{{ id: {s(uid(f"ritem:{qq["key"]}:{n}"))}, item: {{ count: {cnt}, id: {s(iid)} }}, type: "item" }}')
        L.append('\t\t\trewards: [' + ', '.join(rw) + ']')
        if qq['shape']: L.append(f'\t\t\tshape: {s(qq["shape"])}')
        if qq['size']: L.append(f'\t\t\tsize: {qq["size"]}d')
        ts = []
        for n, t in enumerate(qq['tasks']):
            tid = s(uid(f'task:{qq["key"]}:{n}'))
            if t[0] == 'check': ts.append(f'{{ id: {tid}, type: "checkmark" }}')
            elif t[0] == 'item': ts.append((f'{{ count: {t[2]}L, ' if t[2] > 1 else '{ ') + f'id: {tid}, item: {{ count: 1, id: {s(t[1])} }}, type: "item" }}')
            else: ts.append(f'{{ count: {t[2]}L, icon: {{ id: {s(t[3])} }}, id: {tid}, item: {{ components: {{ "ftbfiltersystem:filter": {s(tag(t[1]))} }}, count: 1, id: "ftbfiltersystem:smart_filter" }}, type: "item" }}')
        L.append('\t\t\ttasks: [' + ', '.join(ts) + ']')
        L.append(f'\t\t\tx: {float(qq["x"])}d'); L.append(f'\t\t\ty: {float(qq["y"])}d'); L.append('\t\t}')
        for l in LANG:
            LANG[l][f'quest.{qid}.title'] = qq['title'][l]
            LANG[l][f'quest.{qid}.quest_desc'] = qq['desc'][l]
    L += ['\t]', '}', '']
    open(os.path.join(qd, 'chapters', ch['fn'] + '.snbt'), 'w').write('\n'.join(L))
for l, loc in (('en', 'en_us'), ('pt', 'pt_br')):
    body = '{\n' + '\n'.join(f'\t{k}: ' + ('[' + ', '.join(s(x) for x in v) + ']' if isinstance(v, list) else s(v)) for k, v in sorted(LANG[l].items())) + '\n}\n'
    open(os.path.join(qd, 'lang', loc + '.snbt'), 'w').write(body)
print(len(CH), 'chapters', total, 'quests', len(LANG['en']), 'lang keys per locale')
