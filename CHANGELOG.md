# Changelog — Bubie Pack

## 0.1.11 (2026-11-14)
Menos recurso infinito: minerar, processar e automatizar voltam a valer a pena. **Comece um mundo novo** com esta versão.
### Removido
- Replication. Ele copiava qualquer item a partir de matéria e deixava as fábricas e a mineração sem sentido.
  O Titanium continua: o Functional Storage e o Industrial Foregoing dependem dele.
- Capítulo de quests do Replication (agora são 95 quests em 10 capítulos).
### GeOre
- Os geodos agora só aparecem para carvão, cobre, ferro e quartzo (Overworld e Nether).
  Diamante, esmeralda, ouro, lapis, redstone e ancient debris não geram mais geodos (`config/geore-common.toml`).
  Vale só para chunks novos. O GeOre Nouveau (geodos de source gem do Ars Nouveau) continua igual.

## 0.1.10 (2026-11-13)
### Agricultura
- Adicionado: Farming for Blockheads 21.1.14 (BlayTheNinth; usa o Balm que já estava no pack).
  Traz o Mercado (troca esmeraldas por sementes, mudas e animais), a Caixa de Envio, aspersores, cocho de alimentação,
  fertilizantes e o Chicken Nest. Combina com o Cooking for Blockheads, que já estava no pack.

## 0.1.9 (2026-11-13)
### Unificação
- Adicionado: Almost Unified 1.4.2. Lingotes, pós, pepitas, placas, bastões, engrenagens, blocos e minérios do mesmo metal
  agora saem sempre do mesmo mod (76 tags). Antes, zinco e latão vinham do ATO ou do Create, alumínio do ATO ou do XyCraft,
  e os itens não empilhavam entre si.
  Prioridade (`config/almostunified/unification/materials.json`): minecraft → alltheores → create → mekanism → xycraft_world.
  O ATO já gera todos os minérios do pack, então quase tudo vira item do ATO. O yellorium do Extreme Reactors vira urânio do ATO,
  que os reatores aceitam como combustível (`c:ingots/uranium`).
  Os itens duplicados somem do EMI. Os que você já tem continuam funcionando nas receitas.
### Desempenho
- Distâncias padrão para PC modesto: renderização 8 e simulação 6 (o vanilla usa 12 e 12).
  Vêm do Default Options 21.1.8 (BlayTheNinth; o Balm já estava no pack), que só cria o `options.txt` na primeira abertura.
  Quem já jogou mantém o que configurou: ajuste em *Opções → Vídeo*.
- Servidor: `start.sh`/`start.bat` criam o `server.properties` com `view-distance=8` e `simulation-distance=6` se ele ainda não existir.
  O Default Options não vai no server pack (só cliente).
### Correções
- Shift + clique em carvão/charcoal com a fornalha aberta agora vai para o slot de combustível.
  O Extreme Reactors tinha receitas de fornalha carvão → grafite, e o vanilla manda para a entrada tudo o que tem receita.
  Essas 3 receitas de fornalha foram desligadas (`kubejs/data/bigreactors/recipe/smelting/`); o grafite continua saindo no **alto-forno**.
### Configurações do jogador
- As preferências pessoais não são mais sobrescritas a cada atualização: vídeo do Sodium, shader do Iris, minimapa e mapa do Xaero
  e config de cliente do FTB Chunks foram para `config/defaultoptions/extra/` e só são criadas se ainda não existirem.
  As configs que o pack precisa (Xaero `common.cfg`, categorias do radar, Entity Culling) continuam em `overrides`.
- Removidos `sodium-fingerprint.json` (hashes da máquina de quem montou o pack) e `xaeropatreon.txt` (vazio). Os mods recriam os dois.
- O server pack não leva mais a pasta `config/defaultoptions`.

## 0.1.8 (2026-11-13)
- Adicionado: Replication 1.2.7 (Buuz135). Desintegra itens em matéria, pesquisa padrões e replica qualquer item com receita. Depende do Titanium, que já estava no pack.
  O minério de replica (deepslate, veia 10, 5 por chunk) já fica na faixa das veias do ATO; nada foi ajustado.
- Novo capítulo de quests: Replication (5 quests, 100 no total).
- Ícone do pack no zip (`profileImage/bubie-pack.png`).

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
