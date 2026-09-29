# Pipeline da apostila (build e render)

## Fonte de verdade vs artefatos gerados

- **Fonte de verdade do texto**: `apostila/*.md` (capítulos).
- **Pré-textuais**: `apostila/indice.md` — capa e seção `## Apresentação`.
- **Gerados** (não editar à mão): `docs/apostila/apostila-scada.html`, `latex/**`
  (`.tex`, `.pdf`).

Regra: edite `apostila/*.md`. Se um artefato gerado estiver divergente,
regenere — não corrija o gerado.

Metadados de capa (`**Autor:**`, `**Versão:**`) são lidos de `apostila/indice.md`
(seção `### Versão X.Y`).

## Build rápido

O passo lento é o re-render dos diagramas Mermaid. Em iteração de texto, use o
caminho rápido:

1. `python3 docs/apostila/rebuild.py` → HTML (requer o pacote Python `markdown`).
2. Extrair `## Apresentação` de `apostila/indice.md` para
   `latex/build/frontmatter.md` e converter com pandoc → `latex/frontmatter.tex`.
3. `cd latex && pdflatex × 3 -output-directory=build` (com `makeindex` na
   primeira passada) e `cp build/apostila.pdf apostila.pdf`.

Confirme que o script e o diretório `latex/` existem antes de rodar. Se não
existirem, o gate de render fica **`PENDENTE`** — e isso precisa ser dito no
relatório, não omitido.

## Gate de build

- 0 erros LaTeX: `grep -c "^! " build/pass3.log` deve retornar 0.
- 0 `Overfull` (hbox/vbox).
- HTML: sem figura ou link quebrado, sem seção ausente em relação ao markdown.

## Armadilhas verificadas

- **Não use títulos `##`/`###` dentro da Apresentação**: sem capítulo numerado, o
  pandoc numera como "0.1" e desloca os contadores do documento. Use negrito no
  início do parágrafo.
- `latex/frontmatter.md` (na raiz de `latex/`) é artefato **órfão**: o build
  escreve em `latex/build/frontmatter.md`. Melhor não editar o órfão; se editar,
  mantenha em sincronia manualmente.
- Mudança de título de capítulo altera sumário e numeração — regenere e confira
  o HTML **e** o PDF, não só o markdown.
