<p align="center"><img src="assets/icon.png" width="128" alt="Bubie Pack"></p>

# Bubie Pack

Modpack kitchen-sink de tecnologia e magia para **Minecraft 1.21.1 / NeoForge 21.1.265**, feito para jogar com os amigos.
*A tech and magic kitchen-sink modpack for Minecraft 1.21.1 / NeoForge, made to play with friends.*

- Create, Mekanism, Applied Energistics 2, Ars Nouveau, Mystical Agriculture, Apotheosis e mais de 200 mods.
- Minérios do All the Ores em veias menores, sem duplicatas do Mekanism.
- Vilas maiores e mais frequentes (ChoiceTheorem's Overhauled Village).
- 95 quests em português e inglês.
- Flux Networks sem carregar jetpacks à distância.

O histórico de mudanças está no [CHANGELOG.md](CHANGELOG.md).

## Instalar

Baixe o pack pelo **CurseForge App**. Para servidor, use o **Server Pack** da aba Files do projeto (veja `server/LEIA-ME_README.txt`).

## Estrutura

| Pasta | O que tem |
|---|---|
| `pack/` | `manifest.json` (lista de mods do CurseForge), `overrides/` (configs, KubeJS, quests) e o ícone |
| `server/` | Scripts de inicialização do servidor e a lista de mods só de cliente |
| `tools/gen_quests.py` | Gera as quests do FTB Quests e os textos em pt_br e en_us |
| `tools/build.sh` | Gera os zips em `dist/` |
| `.github/workflows/release.yml` | Publica no CurseForge e no GitHub quando a versão muda |

## Gerar os zips

```bash
# Quests (depois de editar tools/gen_quests.py)
rm -rf pack/overrides/config/ftbquests
python3 tools/gen_quests.py pack/overrides/config/ftbquests

# Pack para o CurseForge App
tools/build.sh

# Pack + server pack (baixa os mods do CurseForge)
tools/build.sh --server
```

## Publicar uma versão

O workflow `.github/workflows/release.yml` publica sozinho quando a versão do `pack/manifest.json` muda:

1. Escreva a seção `## <versão>` no `CHANGELOG.md`. Para o CurseForge em inglês, crie `release-notes/<versão>.md`.
2. Mude `"version"` no `pack/manifest.json`.
3. `git push`.

Ele gera os dois zips, envia o pack ao CurseForge (com o server pack como arquivo adicional) e cria a tag e o GitHub Release.
Precisa do secret `CURSEFORGE_TOKEN`. A variável `CF_RELEASE_TYPE` (`alpha`, `beta` ou `release`) define o tipo; o padrão é `beta`.

Ao adicionar um mod, `tools/build.sh --server` atualiza `pack/mod-files.json` (nome de cada arquivo). Faça commit desse arquivo junto.

## Licença

[MIT](LICENSE) para o conteúdo deste repositório: quests, scripts, configs e ferramentas.
Os mods pertencem aos seus autores e seguem as licenças deles. O repositório só guarda a lista de mods, e nenhum jar de mod é versionado.
