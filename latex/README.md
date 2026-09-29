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
| `apostila.tex` | preâmbulo, capa, sumário, índice de figuras, `\input{build/corpo}` |
| `build-tex.py` | consolida `apostila/*.md` → `build/corpo.tex` (normaliza + pandoc) |
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

- **O build lê do disco.** Depois de editar `../apostila/*.md`, grave o arquivo
  antes de rodar `./build-pdf.sh` — caso contrário o PDF sai com a versão anterior.
- `apostila/build-md.py` é migração de uso único e **sobrescreve** os capítulos;
  não rodar depois de fazer correções editoriais à mão.
- Os títulos de nível 4 que são, na origem, **cabeçalhos de tabela** ("Tecla de",
  "Descrição", "Atalho") aparecem como subtítulos sem número. Correção pendente:
  reconstruir as tabelas de atalho a partir do original.
- Não há `\ref{}` no corpo do texto: o material original não referencia figuras por
  número, apenas pela legenda.
