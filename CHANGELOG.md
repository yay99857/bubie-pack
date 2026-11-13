# Changelog — Bubie Pack

## 0.1.7 (2026-11-13)
### Quests
- 95 quests em 10 capítulos (eram 49 em 5). Novos: AE2: Autocrafting, Mekanism: Avançado, Create: Automação, Mystical Agriculture e Ars Nouveau.
- Todas as quests agora têm texto em inglês e português (`lang/en_us.snbt` e `lang/pt_br.snbt`). O progresso das quests antigas é mantido.
- Gerador das quests em `tools/gen_quests.py`.
### Servidor
- Server pack (`BubiePack-0.1.7-server.zip`): 174 mods, sem os 10 mods só de cliente (lista em `server/client-only-mods.txt`).
  `start.sh`/`start.bat` baixam e instalam o NeoForge 21.1.265 na primeira execução. Memória em `user_jvm_args.txt` (8 GB).
### Descrição
- `CURSEFORGE.md`: seções de quests e de servidor atualizadas.

## 0.1.6 (2026-11-13)
- Corrigido: textos das quests não apareciam. O FTB Quests 2101.1.38 só lê `lang/<idioma>.snbt` (um arquivo por idioma), e não pastas.
- Adicionado: Flux Networks 8.0.0, com nerf do carregamento sem fio do Flux Controller (`defaultconfigs/fluxnetworks-server.toml`):
  não carrega Iron Jetpacks nem MekaSuit. Antes, um Controller num gerador dava energia infinita ao jetpack em qualquer dimensão.
  Plugs e Points continuam funcionando para máquinas, inclusive entre dimensões.
- Nova quest de Flux Networks no capítulo Energia (49 quests no total).

## 0.1.5 (2026-11-13)
### Desempenho
- ImmediatelyFast, Lithium, Clumps (junta orbes de XP), spark (profiler).
### Qualidade de vida
- Mouse Tweaks, Pick Up Notifier, AttributeFix (corrige o limite de atributos do Apotheosis e Artifacts).
- Simple Voice Chat: chat de voz por proximidade. Em servidor dedicado, liberar a porta UDP 24454.
- Chunky: pré-gera o mapa (`/chunky radius 3000` e `/chunky start`).
### Integrações
- Applied Mekanistics (químicos do Mekanism no AE2), Mining Gadgets, LaserIO, Create Crafts & Additions (energia do Create ↔ FE).
- GeOre Nouveau: geodos do GeOre para o Ars Nouveau (source gem).
### Vilas
- ChoiceTheorem's Overhauled Village (+ Lithostitched): vilas maiores e variadas por bioma.
- Vilas um pouco mais frequentes: `minecraft:villages` com spacing de 34 para 28 (separation 8), cerca de 1,5x mais vilas.
  Override em `overrides/kubejs/data/minecraft/worldgen/structure_set/villages.json`. Vale também para as vilas do CTOV.
### Quests
- FTB Quests + FTB XMod Compat + FTB Filter System.
- 48 quests de early game em 5 capítulos (textos em português, em `config/ftbquests/quests/`):
  Bem-vindo, Primeiros Passos, Energia: o Começo, Mekanism: Minérios em Dobro e Armazenamento.
- Recomendações de energia nas quests: Furnator (Powah) para começar, roda d'água + Alternator (Create) para energia grátis,
  Thermo Generator como melhor gerador do começo ao meio do jogo, Energy Cell como bateria e Energy Pipe (Pipez) como cabo.
- Tarefas de ósmio e aço aceitam qualquer lingote com a tag (`c:ingots/osmium`, `c:ingots/steel`), porque o ósmio vem do ATO.
### Não incluído
- YUNG's Better Mineshafts/Dungeons/Strongholds: não têm versão para NeoForge 1.21.1 (só Forge 1.21.1 ou NeoForge 1.21.4+).

## 0.1.4 (2026-11-13)
- Adicionado: Hostile Neural Networks 6.5.1 (dependência Placebo já presente).
- Adicionado: EMI 1.1.24 como interface de receitas. O JEI continua instalado como base, para o EMI carregar as integrações feitas para o JEI.
- Removido: AE2 JEI Integration. O AE2 da 1.21 já tem integração nativa com o EMI, e o addon duplicaria as categorias do AE2.

## 0.1.3 (2026-11-13)
- Removidos os scripts de exemplo do KubeJS (main.js "Hello World").

## 0.1.2 (2026-11-13)
- Removidos dos overrides os caches e arquivos de exemplo que o CurseForge App marcava como "não estão no CurseForge": índice de busca do Ars Nouveau, .ini do JEI, backups .bak e imagens de exemplo do KubeJS.

## 0.1.1 (2026-11-13)
### Geração de minérios
- 0.1.0 tinha nerfado demais (ex.: osmium ficou com ~4% do volume original). Agora as veias continuam pequenas, mas há mais veias por chunk.
- ATO (`overrides/kubejs/data/alltheores/worldgen/`), em tamanho da veia × veias por chunk:
  - tin 9×16, osmium 9×14, lead 9×12, aluminum 9×8, nickel 9×6, zinc 9×6, silver 8×6
  - fluorite 10×8, cinnabar 10×5, salt 12×5, sulfur 8×2
  - uranium 6×10, platinum 5×3, iridium 4×4, ruby/sapphire/peridot 5×4
  - Descarte por exposição ao ar: 0 nos comuns, 0.3 nos raros e gemas.

## 0.1.0 (2026-11-13)
- Veias do ATO reduzidas (tamanho 24 → 9 nos metais comuns).
- Mekanism: geração própria de tin, osmium, uranium, fluorite e lead desligada (`config/Mekanism/world.toml`), porque duplicava a do ATO. O sal continua.
- Removidos: Essential Mod, Chisel Reborn.
