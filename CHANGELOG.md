# Changelog — Bubie Pack

## 1.4.1 (2026-11-27)
Dá para continuar no mundo da 1.4.0.
### Adicionado
- **Just Reactors** 1.2.0, feito para o pack: reatores de fissão multibloco (FE direto ou vapor), turbinas a vapor animadas,
  trocador de calor com circuito fechado de refrigerante, bateria multibloco e reprocessador de cianita.
  Funciona com Mekanism, AE2, Powah e qualquer cabo de FE ou cano de fluido; tem JEI/EMI, Jade e Carry On.
  A 1.2.0 traz vidro conectado, acabamento automático das carcaças, pulso de fissão nas barras de combustível e brilho noturno da turbina.
### Integração
- O combustível é o **urânio do ATO** (`c:ingots/uranium`); o minério de urânio do Just Reactors não é gerado, porque o ATO já gera
  (`kubejs/data/justreactors/neoforge/biome_modifier/`).
- **Almost Unified:** `justreactors` entrou nas prioridades, depois do Mekanism. Grafite, cianita e blutônio do Extreme Reactors
  passam a sair como itens do Just Reactors. Os que você já tem continuam funcionando nas receitas e nos reatores dos dois mods.
- As receitas de fornalha carvão/carvão vegetal → grafite foram desligadas, como as do Extreme Reactors (o shift + clique
  continua mandando o carvão para o slot de combustível); o grafite sai no **alto-forno**.
### Atualizados
- **Bubie 2.0.1** (correções internas de inventário e varredura de área).
- **40 mods** para as versões mais novas de 1.21.1: AE2 19.2.20, Ars Nouveau 5.13.5, Curios 9.6.1, The Bumblezone 7.20.0,
  Supplementaries 4.1.4 (+ Moonlight 3.8.5, Amendments 2.3.1), Integrated Dynamics 1.39.1 (+ Cyclops Core, Integrated Crafting e
  Integrated Terminals), Sophisticated Core/Storage/Backpacks, Titanium 4.0.56, GeckoLib 4.9.5, Hostile Neural Networks 6.6.0,
  FTB Library/Quests/Chunks/Filter System, Waystones, Cooking for Blockheads, RFTools (Base, Utility, Builder) e McJtyLib,
  Entity Culling 1.12.2, Inventory Tweaks ReFoxed 1.4.0, Complementary Reimagined r5.10 (+ Euphoria Patches 1.11.2) e outros.
### Aviso: Extreme Reactors vai sair
- O **Extreme Reactors** continua no pack até a próxima grande versão (**2.0.0**) e depois será **removido**.
  Os reatores e turbinas dele vão sumir do mundo junto com o que estiver dentro.
- Já dá para trocar: construa seus geradores novos com o **Just Reactors**. Vamos avisar de novo nas versões antes da remoção,
  com tempo para desmontar os geradores do Extreme Reactors.

## 1.4.0 (2026-11-27)
**Comece um mundo novo**: a geração do mundo mudou com o Terralith e o Cataclysm, e mods de recursos e blocos antigos foram removidos para equilibrar a progressão.
### Adicionado
- **L_Ender's Cataclysm** (com Lionfish API): chefes desafiadores de endgame, arenas e equipamentos míticos para testar o seu gear.
- **Terralith**: biomas e relevos novos no Overworld usando apenas blocos vanilla.
- **Handcrafted**: mobília e decoração detalhada para as bases.
- **Carry On**: carregue baús, blocos e mobs nas mãos.
- **GraveStone Mod**: túmulo limpo ao morrer (substitui o Corail Tombstone).
- **Chat Heads** (só cliente): mostra a cabeça dos jogadores no chat.
### Removido
- **Equilíbrio e progressão:** Allthemodium, All The Tweaks, Grinding Ball Additions, BBL Strainers (+ In World Recipes e BBL Core), Botany Pots - Mystical Agriculture Compat, Growth Accelerator Tiers e Enchanting Infuser.
- **Redundância e peso:** Agritech: Evolved, Animal Feeding Trough, XyCraft (Core, World, Machines, Override), Ender IO (+ Endergy) e Corail Tombstone.
- Configs antigas desses mods removidas dos overrides e do Almost Unified (`xycraft_world`).
### Quests
- Capítulo novo **Objetivo Final** (8 quests): cace os chefes do Cataclysm (Netherite Monstrosity, Ignis, The Harbinger, Maledictus), domine os seis pilares do pack e complete o **Mestre do Bubie Pack** (**133 quests em 13 capítulos**).
- Atualizadas as quests de túmulo (GraveStone Mod), gerador alternativo (Voltaic Combustion Generator no lugar do Stirling Generator) e fazenda automática do Mystical Agriculture (Bubie Fazendeiro / Create / Industrial Foregoing).
### Correções
- Título da janela passa a ser definido pelo KubeJS (`"Bubie Pack"`).
- Mods puramente de cliente (`justzoom_`, `konkrete_`, `PickUpNotifier-`, `smithingtemplateviewer-`, `JustEnoughMekanismMultiblocks-`, `JustEnoughProfessions-`, `ae2ct-`, `chat_heads-`) filtrados do Server Pack.
- `tools/build_server.py` agora faz URL-encoding no nome dos jars ao baixar do CurseForge.

## 1.3.0
Dá para continuar no mundo da 1.2.2: cada Bubie ganha um disco com tudo o que carregava.
### Bubie 2.0.0
- **HD e SSD:** o que o Bubie carrega fica no **disco** dele, num slot ao lado do combustível. Todo Bubie vem com um **HD** (18 espaços; a receita agora pede um) e um **SSD** dá 36. Tirou o disco, a carga vai junto.
- O **Chip de Armazenamento foi aposentado**: dois deles e um diamante viram um SSD.
- **Dê nome ao Bubie** pelo menu.
- **Abre o próprio caminho:** quando não tem como chegar, cava um poço, faz degraus, túnel ou ponte, sai do buraco no fim e tapa o que abriu. Preso de verdade, mostra um **?** na tela.
- Segure **Alt + B** para ver seus Bubies através das paredes.
### Base Blueprint 1.4.0
- **"Construído por: Você / Bubie"** no menu da planta: com Bubie, clique num bloco e o Bubie mais perto constrói a base ali.
### Voltaic Dynamics 1.7.1
- Cada cabo mostra no núcleo o que está passando.
### Quests
- Quest nova **HD e SSD**; as quests do Bubie, dos chips, do DJ e da Estação descrevem a 2.0.0. As quests do Bubie dão redstone em vez de carvão.

## 1.2.2
Dá para continuar no mundo da 1.2.1.
### Voltaic Dynamics 1.7.0
- **Acumuladores Elite (32M FE) e Supremo (128M FE)**, e um **Acumulador Criativo** que nunca acaba.
- **Tanques de Fluidos Avançado, Elite e Supremo** (64.000 / 128.000 / 256.000 mB) e um **Tanque Criativo**.
- **Instaladores de Nível**: sobem a Fornalha Elétrica, a Fundidora de Ligas e o Pulverizador sem tirar nada de dentro, para processar 2, 4 ou 8 itens ao mesmo tempo com a mesma energia por item.
- Os **Cabos Voltaicos brilham** enquanto passa energia.
- Valores equilibrados com o Mekanism e o Powah.

## 1.2.1 (2026-11-21)
Dá para continuar no mundo da 1.2.0.
### Bubie 1.5.0
- **Funciona com redstone ou FE, não com carvão** (é um robô): um pó de redstone dá 5 minutos de trabalho, um bloco 45. A Estação também aceita redstone, e a redstone que o Bubie minera abastece o slot dele. Carvão que já estiver no slot só fica lá.
- **Slot de disco na aba DJ**: o disco não ocupa mais o inventário nem vai para o baú, e tirar o disco enquanto toca faz a música parar.
- **Links do DJ**: links de compartilhamento do Dropbox, Google Drive, GitHub e Audius tocam direto. YouTube, Spotify e parecidos são recusados com o motivo, e um arquivo do computador explica como compartilhar.
- Mostra **"A ferramenta está sem energia"** quando uma ferramenta elétrica (Atomic Disassembler, qualquer ferramenta com FE) está descarregada.
- O **clique do meio** (Inventory Tweaks) não puxa mais a ferramenta, o combustível, os chips e o disco para o inventário.
- Menu: dicas nos botões, o motivo de ele estar sem fazer nada e a área aparece no mundo ao mudar o raio.
### Voltaic Dynamics 1.6.2
- O Inventory Tweaks não mistura mais os slots das máquinas (entradas, upgrades, baterias do acumulador).
### Quests
- O Bubie dá redstone em vez de carvão; textos do Bubie e do DJ atualizados.

## 1.2.0 (2026-11-20)
Dá para continuar no mundo da 1.1.x. Mundos novos já vêm com a progressão do chip; num mundo antigo, ligue
`advancedJobsNeedChip` em `serverconfig/bubie-server.toml` se quiser.
### Bubie 1.4.0
- **Sem cantos para marcar:** Shift + clique num baú com a Prancheta e o Bubie trabalha em volta dele (raio ajustável no menu). A Pedreira e o Escavador cavam na frente do baú.
- Tarefa nova **Guarda**: enfrenta os monstros da área com a arma do slot de ferramenta e fica de vigia à noite.
- **Chip de programa**: no pack, o Minerador, o Construtor, o Entregador e o Guarda precisam dele (sai da Fundidora de Ligas).
- O menu da **Estação** mostra os Bubies que moram nela.
- **Español** no Bubie, na Voltaic Dynamics (1.6.1) e na Base Blueprint (1.3.1).
### Quests
- Novas: **Chip de programa** e **Bubie Guarda**.

## 1.1.1 (2026-11-20)
Dá para continuar no mundo da 1.1.0.
### Bubie 1.3.0: o DJ
- Aba **DJ** no menu do Bubie: toca os discos de música do inventário (de qualquer mod) e links de `.mp3`/`.ogg`, para todo mundo por perto.
- A tela vira um equalizador, ele dança e solta notas, e os Bubies em volta dançam junto.
- Quest nova **"Bubie DJ"** no capítulo do Bubie (recompensa: um disco).

## 1.1.0 (não publicada)
Dá para continuar no mundo da 1.0.0.
### Bubie 1.2.0
- Tarefa nova **Entregador**: esvazia os baús, funis e saídas de fornalha da área no baú dele. Se o baú é de um Construtor, leva só o que a planta ainda precisa.
- Bubies na mesma área **dividem o trabalho**: cada um reserva o bloco (o Lenhador, a árvore inteira) em que está.
- Um Bubie que fica preso (buraco, porta, cerca) se teleporta para perto do destino ou mostra **Preso**, em vez de ficar parado sem explicação.
- O Construtor mostra o **progresso** (blocos feitos / total) no menu e no Jade, e o balão diz **qual bloco falta e quantos**.
### Base Blueprint 1.3.0
- Botão **Construir com Bubie** no menu da planta: o seu Bubie mais próximo constrói a base onde você está olhando.
### Pack
- Os **chips do Bubie** agora saem da **Fundidora de Ligas** da Voltaic (2 ligas galvânicas, 4 redstone e a peça do chip).
- Quest nova **"Conheça o Bubie"** logo no primeiro capítulo, mostrando o caminho até ele; quest nova do **Entregador**.
- Nome e logo novos: **Bubie Pack - Tech, Magic & Robot Helpers**.

## 1.0.0 (2026-11-20)
Dá para continuar no mundo da 0.6.x: o progresso das quests é mantido.
### Novo: Bubie
- O terceiro mod feito para o pack: o **Bubie**, o robozinho do bubie.gg, como ajudante. Ele segue você, carrega itens e, com uma tarefa e uma área,
  trabalha sozinho e guarda tudo num baú: **Lenhador** (árvores inteiras, replanta), **Escavador** (areia, cascalho, terra, argila),
  **Pedreira** (com escada, tampa lava e água), **Fazendeiro** (inclui Mystical Agriculture e Farmer's Delight), **Minerador** (veios ou túneis, `c:ores`)
  e **Coletor**.
- **Prancheta do Bubie** para marcar área, baú e casa; **Estação do Bubie** que carrega com FE de qualquer cabo ou carvão; 6 **chips** de melhoria.
- **Editar meu Bubie**: cores do casco, do moletom e da luz da tela, olhos e boca do My Bubie do bubie.gg.
- Funciona com o resto do pack: guarda em Sophisticated Storage, Functional Storage, cofres do Create e bins do Mekanism; respeita as áreas do
  FTB Chunks (quebra blocos como o dono); quem é do mesmo time do FTB Teams também dá ordens; Jade mostra o que ele está fazendo.
- **Bubie Construtor (com a Base Blueprint):** entregue uma Planta de Base ao Bubie e ele constrói a base bloco por bloco, pegando o
  material no baú dele. Se o material acaba, ele espera, e outro Bubie (Lenhador, Pedreira) pode ir enchendo o mesmo baú.
- **Integração com a Voltaic:** no pack, o Bubie é feito com **lingotes voltaicos** e a Estação com um **Acumulador Básico**; o **Acumulador de Bolso**
  (ou um tablet do Mekanism) no slot de combustível recarrega o Bubie; o Minerador pode entregar minério direto no **Pulverizador**.
### Quests
- Capítulo novo **Bubie** (9 quests, com uma do Construtor). A última, "Um amigo para o Bubie", dá **outro Bubie**.

## 0.6.5 (2026-11-20)
Dá para continuar no mundo da 0.6.x.
### Corrigido
- A janela do jogo se chamava **"All The Mods CHANGE ME"** e tinha o ícone do All the Mods. Agora mostra **"Bubie Pack" e a versão**, com o ícone do pack.
  O All The Tweaks usava o perfil do ATM porque o nome do pack estava em branco, e a versão vinha do Better Compatibility Checker, que não lia a config do pack
  (o build gravava o `bcc-common.json` do formato antigo; o BCC 21.x lê o `bcc-common.toml`). A lista de servidores também passa a comparar a versão certa.
- O status do Discord não mostra mais "All The Mods 10".

## 0.6.4 (2026-11-20)
A 0.6.3 foi recusada pelo CurseForge: o **No Chat Reports** saiu do CurseForge, e um modpack não pode citar um arquivo que não existe mais lá.
Esta versão tira o mod e traz as mudanças de quests da 0.6.3. Dá para continuar no mundo da 0.6.x: o mod não tem blocos nem itens.
### Removido
- No Chat Reports (o projeto não existe mais no CurseForge).

## 0.6.3 (2026-11-20)
Dá para continuar no mundo da 0.6.x: o progresso das quests é mantido, e quem já completou uma quest pode resgatar a recompensa nova.
### Quests: item em quase toda quest
Comparado com ATM10, Craftoria e Enigmatica 10, que dão item em quase toda quest. Antes, 69 das 112 quests davam só XP; agora são 10 (as de leitura).
- **16 marcos ganharam item fixo** para o próximo passo, por exemplo: 3 Precision Mechanisms, 2 Molecular Assemblers e 1 Pattern Provider,
  2 bombas, 16 canos e 1 Blaze Burner no motor a vapor, 4 Refined Obsidian e 4 Reinforced Alloys na dissolução (5x).
- **43 quests menores dão um sorteio** da tabela do capítulo (Básico, Energia, Mekanism, AE2, Create, Mystical, Ars Nouveau e Voltaic):
  um pacote de 1 a 32 itens, como 16 lingotes de ósmio, 16 silícios ou 32 essências de inferium. Upgrades e diamantes saem menos.
- Os metais dados são os do All the Ores, os mesmos que o Almost Unified usa nas receitas. O XP não mudou.

## 0.6.2 (2026-11-17)
Dá para continuar no mundo da 0.6.x: o progresso das quests é mantido (recompensas já resgatadas não mudam).
### Quests: recompensas maiores
- XP de todas as quests subiu: 10 → 30, 25 → 60, 50 → 120 e 100 → 250.
- As 43 quests com item dão o dobro (até um pack de 64): por exemplo 32 carvões, 16 silícios, 32 cabos de energia, 128 pedregulhos
  na Planta de Base. A quest da primeira rede ME dá um componente de 4k em vez de 1k, e a do ferro dá também 32 tochas.
  Upgrades únicos (Pickup Upgrade, Stack Upgrade) e o balde continuam 1.
### Base Blueprint 1.2.1
- O menu mostra a base em **3D** com os materiais escolhidos: arraste para girar, role para aproximar. O botão 2D/3D troca pela planta em pixels.
- "Paredes" virou **"Altura"** (a altura de cada andar). Com mais de 1 andar a altura mínima é 2; ao subir de 1 para 2 andares, uma altura menor vira 4.
- O contorno da base no mundo usa um buffer próprio, para tentar corrigir ele não aparecer com Sodium e Iris.

## 0.6.1 (2026-11-17)
Atualiza os dois mods do pack. Dá para continuar no mundo da 0.6.0.
### Voltaic Dynamics 1.6.0
- A Liga Galvânica agora sai só da **Fundidora de Ligas**, como as ligas do Mekanism saem do Metallurgic Infuser.
  O Pó Galvânico foi removido (receita à mão, fornalha, alto-forno e Pulverizador): pó vira lingote, liga é feita em máquina.
  Pó Galvânico que já esteja no mundo some.
- A quest da Liga Galvânica agora vem depois da quest da Fundidora de Ligas.
### Base Blueprint 1.2.0
- **Andares:** empilha até 16 andares, cada um com a altura das paredes, um piso entre eles e um buraco para a escada. Faz torres.
- Cada planta faz **8 bases** (no criativo não gasta); conserta na bigorna com papel. Plantas que você já tem também passam a ter 8 usos.

## 0.6.0 (2026-11-16)
Dois mods feitos para o Bubie Pack. Dá para continuar no mundo da 0.5.x: o progresso das quests é mantido.
### Adicionado
- **Voltaic Dynamics 1.5.0:** tecnologia compacta com FE. Geradores a Combustão, Termoelétrico (calor perto de frio) e a Fluido (lava),
  Fornalha Elétrica, Fundidora de Ligas e Pulverizador com Melhorias de Velocidade e Eficiência, Acumuladores de 1M e 8M FE,
  Acumulador de Bolso, Cabos Voltaicos, Cabos de Itens e de Fluidos sem itens em trânsito, Tanque de Fluidos e Chave Voltaica.
  Funciona com os cabos e máquinas do Mekanism, AE2 e Powah; o AlmostUnified unifica os pós dele com os do pack.
- **Base Blueprint 1.1.2:** constrói a primeira base com um clique. Receita: mesa de trabalho + 3 papéis.
  Formas redonda, quadrada, octogonal e hexagonal, paredes com porta, teto plano ou cúpula, fundação em terreno irregular,
  material separado para piso e paredes, blocos do inventário, da mochila e dos baús por perto, e desfazer salvo com o mundo.
### Quests
- Capítulo novo **Voltaic Dynamics** com 16 quests, do primeiro Lingote Voltaico ao Acumulador Avançado.
- Quest da **Planta de Base** em Primeiros Passos.
- Agora são 112 quests em 11 capítulos.

## 0.5.1 (2026-11-14)
Recompensas nas quests. Dá para continuar no mundo da 0.5.0: o progresso das quests é mantido.
### Quests
- 34 quests passam a dar, além do XP, um item pequeno que ajuda no próximo passo, sem pular etapas.
  Exemplos: Pickup Upgrade na quest da mochila, 2 Warp Scrolls na das waystones, 2 Energy Tablets na do Energy Cube,
  8 Silicon na do Inscriber, 8 Blank Patterns na dos padrões, 4 Source Gems na do livro de feitiços.
  Coisas baratas (pasta dielétrica, cabos, gavetas, esteiras, padrões) vêm em cópia; máquinas nunca.
  Agora são 36 quests com item; as outras 59 continuam só com XP.

## 0.5.0 (2026-11-14)
Salto de versão: o pack está perto da 1.0. Esta versão junta 37 mods do ATM10, entre eles os YUNG's, que redesenham as estruturas vanilla.
**Comece um mundo novo**: as estruturas novas só aparecem em chunks novos.
### Adicionado (versões iguais às do ATM10)
- **Estruturas:** YUNG's Better Mineshafts, Dungeons, Strongholds, Nether Fortresses, Desert Temples, Jungle Temples, Ocean Monuments,
  Witch Huts e End Island (com o YUNG's API). Substituem as estruturas vanilla, sem criar estruturas novas.
- **Mobs:** Creeper Overhaul e Enderman Overhaul (variantes que combinam com o bioma; usam o Resourceful Config).
- **Create:** Create: Enchantment Industry (experiência líquida, encantamento e cópia de livros automáticos).
- **Decoração:** Amendments, o complemento do Supplementaries (poções no caldeirão, tapete em escadas, lanternas que balançam e mais).
- **Servidor:** Better Compatibility Checker. A lista de servidores mostra se a versão do pack é a mesma do servidor.
  O `tools/build.sh` grava a versão do `manifest.json` em `config/bcc-common.json` a cada build.
- **AE2:** Polymorphic Energistics (escolhe entre receitas em conflito nos terminais de craft e de padrões).
- **Desempenho:** AI Improvements (IA de mobs mais leve) e Sodium Extra (contador de FPS, liga/desliga partículas, animações, neblina e mais).
- **Shaders:** Euphoria Patches (opções extras para a Complementary incluída) e Iris Search (busca nas configurações do shader).
- **Conforto:** Inventory Tweaks ReFoxed (teclas para organizar o inventário e baús), Tool Belt, Akashic Tome (todos os livros-guia num só),
  Fuel Goes Here, Accelerated Decay (folhas caem rápido), Comforts (saco de dormir e rede) e Cosmetic Armor Reworked.
- **Interface:** Not Enough Animations, Better Advancements, Colorful Hearts, Overloaded Armor Bar, More Overlays (nível de luz e bordas de chunk),
  Smithing Template Viewer, Rebind Narrator e Bad Wither No Cookie (sem o som do wither e do dragão no mundo todo).
- **Tecnologia:** Energy Meter (mede o fluxo de energia).
- Só de cliente, fora do server pack: Sodium Extra, Euphoria Patches, Iris Search, Not Enough Animations, Better Advancements,
  Colorful Hearts, Overloaded Armor Bar, More Overlays, Rebind Narrator e Bad Wither No Cookie.

## 0.1.13 (2026-11-14)
GeOre igual ao do ATM11 e 28 mods leves trazidos do ATM10: correções, conforto e integrações entre os mods que já estavam aqui.
Nenhum traz dimensão, minério ou máquina grande nova. Os geodos novos só aparecem em chunks novos: para ter todos, **comece um mundo novo**.
### GeOre
- Os geodos voltam a aparecer para todos os minérios vanilla, como no ATM11: carvão, cobre, ferro, ouro, diamante,
  esmeralda, lapis, redstone, quartzo (Overworld e Nether) e ancient debris. É a config padrão do GeOre, a mesma que o ATM11 usa.
### Removido
- GeOre Nouveau. O ATM11 não tem: os Dowsing Rods achavam os geodos fácil demais e o GeOre Golem fazia o farm sozinho.
  Agora você acha geodo explorando. Os itens do GeOre Nouveau que já existiam no mundo somem.
### Adicionado (versões iguais às do ATM10)
- **Servidor e amigos:** Simple Backups (backup do mundo a cada 2 horas, guarda os 10 últimos, até 25 GB, na pasta `simplebackups`),
  No Chat Reports e Crash Assistant (mostra o que crashou e qual mod causou).
- **Desempenho e correções:** All The Leaks (vazamentos de memória), Get It Together, Drops! (itens no chão se juntam),
  Fast Workbench, NetherPortalFix e Model Gap Fix.
- **Interface:** Crafting Tweaks, Toast Control, KeybindsPurger, Clean Swing e Just Zoom (com o Konkrete, que ele exige).
- **JEI/EMI:** JEI Stuff (loot de mobs e baús, trocas de aldeão, escambo, pesca, drops de plantas e interações de fluidos),
  Just Enough Mekanism Multiblocks, Just Enough Professions e Just Enough Breeding.
- **AE2:** MEGA Cells, ME Requester, AE2: Crafting Tree, AE2 Network Analyser e Applied Flux (FE em células ME).
- **Ars Nouveau:** Ars Énergistique (Source na rede ME) e Ars Creo (compatibilidade com o Create).
- **Sophisticated:** Sophisticated Backpacks Create Integration, Sophisticated Storage Create Integration e Sophisticated Storage In Motion
  (carrinhos e barcos com baú).
- Toast Control, KeybindsPurger, Model Gap Fix e Crash Assistant são só de cliente e não vão no server pack.
- Removido da lista de mods (`pack/modlist.html`) o Replication, que tinha ficado lá depois da 0.1.11.

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
