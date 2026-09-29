# LaTeX da apostila

Documento consolidado gerado a partir de `../apostila/*.md`.

## Build

```bash
./build-pdf.sh          # consolida + pdflatex ×3 + gate
```

Saída: `apostila.pdf` (cópia de `build/apostila.pdf`).

## Gate

- `0` erros LaTeX (`grep -c '^! ' build/passada3.log`)
- `0` `Overfull` (hbox/vbox)
- `0` referências pendentes (`undefined`)

## Arquivos

| Arquivo | Papel |
|---|---|
| `apostila.tex` | preâmbulo, capa, Apresentação, sumário, índice de figuras, `\input{build/corpo}` |
| `build-tex.py` | consolida `apostila/*.md` → `build/corpo.tex` (normaliza + pandoc) e gera `build/capa.tex`, `build/apresentacao.tex` e `build/indice-figuras.tex` |
| `build-pdf.sh` | executa o script acima e compila até estabilizar |
| `build/` | gerados — não editar |

## Decisões de formatação

- **Numeração de figuras**: o material já traz o número na legenda ("Figura N: …") e
  a numeração não é sequencial por capítulo. Por isso o contador do LaTeX **não** é
  impresso (`\captionsetup{labelformat=empty,labelsep=none}`) e o índice de figuras
  é gerado a partir de `../apostila/indice-figuras.md`, com `\pageref`.
- **Numeração de seções**: o número digitado no texto é removido e o LaTeX numera.
  O nível vem da profundidade do próprio número (`9.1` → `\section`, `7.5.2` →
  `\subsection`), o que corrige títulos que o conversor colocou um nível acima ou
  abaixo.
- **Figuras**: posicionadas com `[H]` (sem fila de floats) e limitadas a
  `max width=\linewidth`, `max height=0.82\textheight`.
- **Referências WEB**: capítulo sem número, como no original.
- **Apresentação**: página pré-textual gerada por `apresentacao_tex()` a partir da
  seção `## Apresentação` de `../apostila/indice.md`. Entra antes do sumário, em
  página própria, com `\chapter*` (sem número, sem `\leftmark`) e numeração romana.
- **Cores dos títulos**: `xcolor` + `titlesec` definem quatro tons de azul, do mais
  escuro no capítulo ao mais claro na subsubseção — capítulo `#10305A`, seção
  `#1A4A85`, subseção `#2A63A8`, subsubseção `#3D7BC0`. O capítulo usa a forma
  `display` ("CAPÍTULO N" em azul médio, título em azul profundo, filete de
  1,2 pt); as seções levam filete de 0,7 pt. O esquema **não** vaza cor para o
  corpo do texto e a hierarquia continua legível em impressão preto e branco.
- **Capa**: gerada por `capa_tex()` em `build-tex.py` a partir de
  `../apostila/indice.md`. Título em azul profundo e **filetes duplos**
  (2,4 pt + 0,6 pt) abrindo e fechando o título e a página, mais um filete curto
  centralizado entre os professores e a instituição. Os filetes usam `\hrule`
  (não `\rule`) para não consumirem uma linha de texto inteira cada um — com
  `\rule` o par de filetes abre ~14 pt de espaço em vez dos 2,4 pt pretendidos.
- **Cabeçalho corrente**: nome do capítulo/seção e número de página em `azulSec`;
  o filete é azul claro. O `\headrule` do `fancyhdr` é redefinido porque o
  original é preto e não aceita cor.
- **Sumário em azul**: as entradas do sumário são os **únicos links internos** do
  documento (o corpo não usa `\ref`), então o `hyperref` passou a usar
  `linkcolor=azulSec` + `pdfborder={0 0 0}` no lugar de `hidelinks`. Consequência:
  as cores precisam ser definidas **antes** do `hyperref` no preâmbulo, e as
  URLs do capítulo de referências também ficaram azuis.
- **Ordem no preâmbulo**: `xcolor`/`\definecolor` → `hyperref` → `titlesec`.

## Correções editoriais no markdown

`../apostila/*.md` é a fonte de verdade, mas três defeitos herdados da conversão do
PDF são corrigidos por script (todos idempotentes, em `../apostila/`):

| Script | Defeito que corrige |
|---|---|
| `corrigir-legendas.py` | legenda que virou URL e o resíduo da URL quebrada em itálico; legendas duplicadas no cap. 9 |
| `inserir-secao-ipc.py` | cria/atualiza a seção §2.3 (Normas IPC) |
| `juntar-trechos-partidos.py` | frases partidas por fim de parágrafo falso e espaço depois de hífen (`curtos- circuitos`) |
| `reconstruir-tabela-jlcpcb.py` | células desalinhadas nas tabelas de capacidade do cap. 7 |

**A largura de uma coluna no pandoc vem do número de traços** na linha separadora
da tabela em markdown. Quatro colunas com `|---|---|---|---|` saem com 0,25 cada,
independentemente do conteúdo; para larguras proporcionais é preciso variar os
traços (ex.: `|:---------|:-----------------------|:----------|` → 0,11 / 0,26 / 0,63).

## Quadros de destaque

No markdown da apostila:

```markdown
::: {.quadro tipo="dica" titulo="Rótulo do quadro"}
Texto do quadro. Aceita **negrito**, listas e equações.
:::
```

`tipo`: `nota` (azul), `dica` (verde), `atencao` (laranja), `importante` (vermelho).
A conversão é feita por [`quadros.lua`](./quadros.lua); o ambiente `quadro` está
definido em `apostila.tex` (tcolorbox, quebrável entre páginas).

As cercas `:::` são reconhecidas por `build-tex.py` como estrutura — sem isso o
juntador de parágrafos as absorveria e o quadro não seria gerado.

## Limitações conhecidas

- **O build lê do disco.** Grave os arquivos antes de rodar `./build-pdf.sh` — caso
  contrário o PDF sai com a versão anterior.
- **Grave os buffers ANTES de rodar os scripts, nunca depois.** Os scripts de
  correção reescrevem `../apostila/*.md` direto no disco. Se um desses arquivos
  estiver aberto no editor com um buffer defasado, um save posterior grava o buffer
  por cima e **reverte o script sem aviso** — os scripts relatam sucesso, o build
  passa 0/0 e o PDF não tem o conteúdo novo. Ordem correta: gravar → rodar os
  scripts → compilar.
- `apostila/build-md.py` é migração de uso único e **sobrescreve** os capítulos;
  não rodar depois de fazer correções editoriais à mão.
- Os títulos de nível 4 que são, na origem, **cabeçalhos de tabela** ("Tecla de",
  "Descrição", "Atalho") aparecem como subtítulos sem número. Correção pendente:
  reconstruir as tabelas de atalho a partir do original.
- Não há `\ref{}` no corpo do texto: o material original não referencia figuras por
  número, apenas pela legenda.
