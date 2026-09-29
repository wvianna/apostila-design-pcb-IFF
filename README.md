# Apostila de Design de PCB com KiCad

[![Licença: CC BY-SA 4.0](https://img.shields.io/badge/Licen%C3%A7a-CC%20BY--SA%204.0-green.svg)](https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br)

|  |  |
|---|---|
| **Título completo** | Design de PCB com uso do KiCad para leitura e acionamento de sinais discretos |
| **Autores** | D.Sc. William da Silva Vianna · M.Sc. Luciano Resende Dias |
| **Instituição** | Instituto Federal Fluminense (IFF) |
| **Edição** | setembro/2026 |
| **Documento final** | [`latex/apostila.pdf`](latex/apostila.pdf) — 106 páginas |
| **Fonte do texto** | [`apostila/*.md`](apostila/) — 10 capítulos + Referências WEB |
| **Figuras** | 83 imagens em [`apostila/figuras/`](apostila/figuras/) |
| **Licença** | CC BY-SA 4.0 — ver [Licença](#licença) |

---

## Sobre a apostila

Material didático de projeto e design de placas de circuito impresso (PCB) para a
disciplina optativa de KiCad. Percorre o ciclo completo do projeto: princípios e
elementos básicos da placa, boas práticas de layout, normas IPC, processo de
fabricação, prototipagem, ferramentas de EDA, o fluxo de trabalho no KiCad,
controle de impedância em alta frequência e circuitos de interfaceamento de
entrada e saída digital com microcontrolador.

O repositório é **autossuficiente e reprodutível**: o texto-fonte está em
Markdown, as figuras foram extraídas do PDF original e o PDF final é gerado por
um pipeline aberto (`pandoc` + `pdflatex`), com um gate de qualidade automatizado.
Não há dependência de software proprietário para recompilar o documento.

### Estado atual do documento

| Métrica | Valor |
|---|---|
| Páginas do PDF final | 107 |
| Capítulos numerados | 10 (+ Apresentação e Referências WEB sem número) |
| Linhas de texto-fonte (`apostila/[0-9]*.md`) | 1 400 |
| Figuras extraídas e catalogadas | 83 |
| Quadros de destaque | 9 |
| Erros de compilação LaTeX | 0 |
| Avisos *Overfull* | 0 |

---

## Sumário

| # | Arquivo | Título | Seções |
|---|---|---|---|
| 1 | [`01-introducao.md`](apostila/01-introducao.md) | Introdução | 1 |
| 2 | [`02-principios-elementos.md`](apostila/02-principios-elementos.md) | Princípios e elementos básicos das PCBs | 4 |
| 3 | [`03-boas-praticas-design.md`](apostila/03-boas-praticas-design.md) | Boas Práticas de Design | 14 |
| 4 | [`04-fabricacao-pcb.md`](apostila/04-fabricacao-pcb.md) | Processo básico de fabricação de PCB | 7 |
| 5 | [`05-prototipo-pcb.md`](apostila/05-prototipo-pcb.md) | Protótipo de PCB | 3 |
| 6 | [`06-opcoes-eda.md`](apostila/06-opcoes-eda.md) | Opções de EDA (*Electronic Design Automation*) | — |
| 7 | [`07-kicad.md`](apostila/07-kicad.md) | KiCad | 9 |
| 8 | [`08-projetos-kicad.md`](apostila/08-projetos-kicad.md) | Diversos projetos feitos com KiCad | — |
| 9 | [`09-controle-impedancia.md`](apostila/09-controle-impedancia.md) | Controle de impedância em circuitos de alta frequência | 4 |
| 10 | [`10-interfaceamento-io.md`](apostila/10-interfaceamento-io.md) | Interfaceamento de E/S digital com microcontrolador | 5 |
| — | [`99-referencias-web.md`](apostila/99-referencias-web.md) | Referências WEB | — |

**Índice** — [`apostila/indice.md`](apostila/indice.md) (capa: título, autores,
instituição, data, e a seção `## Apresentação`, que o pipeline converte em
`build/apresentacao.tex`) e
[`apostila/indice-figuras.md`](apostila/indice-figuras.md) (manifesto das figuras
com o número, a página de origem no PDF, o arquivo e a legenda).

---

## Estrutura do repositório

```text
novaApostila/
├── README.md                    ← este arquivo
├── LICENSE                      ← CC BY-SA 4.0
├── AGENTS.md                    ← regras permanentes de trabalho no repositório
├── AVALIACAO.md                 ← avaliação dos artefatos SDD e dos agentes
├── README-AGENTIC.md            ← pacote agêntico: instalação e estratégia de uso
│
├── apostila/                    ← FONTE DE VERDADE do texto
│   ├── indice.md                ← capa
│   ├── 01-introducao.md … 10-interfaceamento-io.md
│   ├── 99-referencias-web.md
│   ├── indice-figuras.md        ← manifesto das figuras (rastreabilidade)
│   ├── figuras/                 ← 83 PNGs (figura-01.png … figura-83.png)
│   └── *.py                     ← pipeline de migração e correção
│
├── latex/                       ← projeto LaTeX e PDF final
│   ├── apostila.tex             ← preâmbulo, capa, sumário, índice de figuras
│   ├── build-tex.py             ← consolida apostila/*.md → build/corpo.tex
│   ├── quadros.lua              ← filtro pandoc dos quadros de destaque
│   ├── build-pdf.sh             ← build completo (pandoc + pdflatex ×3 + gate)
│   ├── build/                   ← GERADOS — não editar
│   ├── apostila.pdf             ← PDF final (cópia de build/apostila.pdf)
│   └── README.md                ← decisões de formatação do LaTeX
│
├── docs/                        ← planejamento, auditoria e material recebido
│   ├── auditoria-apostila-pcb.md   ← auditoria técnica e editorial (achados A-01…A-17)
│   ├── memorial.md                 ← especificação da skill de refatoração
│   ├── materialApoioKicad_Optativa_R9.pdf   ← apostila original (98 páginas)
│   ├── kicad.pdf, Exportar-JLCPCB.pdf       ← anexos recebidos
│   └── agentic/                    ← protocolo de contexto, fluxo, DoD, rastreabilidade
│
├── livros/                      ← guias de fabricantes e normas usados como referência
├── .github/                     ← agentes, instruções e skills do fluxo SDD
├── .agents/, .vscode/           ← configuração das ferramentas de IA
└── .gitignore
```

---

## Como gerar o PDF

### Pré-requisitos

| Ferramenta | Versão validada | Para quê |
|---|---|---|
| `python3` | 3.12 | `build-tex.py` e os scripts de correção |
| `pandoc` | 3.1 | conversão Markdown → LaTeX e filtro Lua dos quadros |
| `pdflatex` (TeX Live) | pdfTeX 1.40.25 / TeX Live 2023 | compilação do documento |
| Pacotes LaTeX | `texlive-latex-recommended`, `texlive-latex-extra` | `tcolorbox`, `titlesec`, `adjustbox`, `xcolor`, `booktabs`, `microtype`, … |
| *Opcional*: `mupdf-tools`, `poppler-utils`, `python3-pil` | — | apenas para reextrair figuras do PDF original |

Instalação em Debian/Ubuntu:

```bash
sudo apt install pandoc texlive-latex-recommended texlive-latex-extra \
                 texlive-fonts-recommended texlive-lang-portuguese
# opcional, só para reextrair figuras:
sudo apt install mupdf-tools poppler-utils python3-pil
```

### Build

```bash
cd latex
./build-pdf.sh
```

O script executa quatro etapas:

1. `python3 build-tex.py` — consolida `apostila/*.md` em `build/corpo.md`, normaliza
   a estrutura (numeração de seções, legendas, tabelas, figuras) e chama o `pandoc`
   com o filtro `quadros.lua` para gerar `build/corpo.tex`;
2. três passadas de `pdflatex` (necessárias para sumário, índice de figuras e
   referências cruzadas);
3. **gate**: conta erros (linhas iniciadas por `!`) e avisos *Overfull* no log da terceira passada;
4. copia `build/apostila.pdf` para `latex/apostila.pdf`.

O script **interrompe** se houver qualquer erro de LaTeX. Avisos *Overfull* são
reportados no final, sem interromper o build — o objetivo, porém, é mantê-los em
zero.

### Gate de qualidade

```bash
grep -c '^! '        latex/build/passada3.log   # deve imprimir 0
grep -c '^Overfull'  latex/build/passada3.log   # deve imprimir 0
```

### Outros comandos úteis

```bash
# inspecionar o PDF em texto (buscar uma frase, conferir o que saiu de fato)
mutool draw -F txt -o /tmp/pdf.txt latex/apostila.pdf

# renderizar páginas específicas para inspeção visual
pdftoppm -r 110 -f 5 -l 5 -png latex/apostila.pdf /tmp/pagina
```

---

## Como editar o conteúdo

`apostila/*.md` é a **fonte de verdade**. O PDF é um artefato derivado: nunca
edite `latex/build/*` (é gerado) nem o PDF.

### Ordem obrigatória de trabalho

```text
1. gravar os arquivos no editor
2. rodar os scripts de correção de apostila/ (quando aplicável)
3. compilar:  cd latex && ./build-pdf.sh
4. verificar com Python (não com grep) lendo o arquivo ou o texto do PDF
```

> **Atenção — quatro regras que já causaram retrabalho neste repositório:**
>
> 1. **Grave os buffers *antes* de rodar os scripts, nunca depois.**
>    Os scripts de correção reescrevem `apostila/*.md` direto no disco. Se um
>    desses arquivos estiver aberto no editor com um buffer defasado, um *save*
>    posterior grava o buffer por cima e **reverte o script em silêncio**: os
>    scripts relatam sucesso, o build passa com 0 erros e 0 *Overfull*, mas o
>    conteúdo novo não está no PDF. Só o arquivo aberto no editor é afetado.
> 2. **`apostila/build-md.py` é migração de uso único e é destrutivo.** Ele
>    **sobrescreve todos** os `apostila/*.md` a partir do PDF convertido — inclusive
>    `indice.md`, o que leva junto a capa e a seção `## Apresentação`. Rodá-lo de
>    novo apaga as correções editoriais feitas à mão.
> 3. **Ao corrigir um trecho tratado por um script, edite a lista de dados do
>    script e reexecute-o** (todos são idempotentes) em vez de editar o
>    resultado — a próxima execução desfaria a edição manual.
> 4. **O build lê do disco**, não do buffer do editor. Um PDF "desatualizado"
>    quase sempre significa arquivo não gravado.

### Convenções de marcação

**Figuras** — a imagem e a legenda em itálico (o LaTeX usa o texto alternativo
como legenda e suprime o contador, porque a numeração já vem no texto):

```markdown
![Figura 12: Título da figura](figuras/figura-12.png)

*Figura 12: Título da figura*
```

Toda figura nova precisa também de uma linha no manifesto
[`apostila/indice-figuras.md`](apostila/indice-figuras.md), que alimenta o
índice de figuras do PDF:

```markdown
| 12 | 23 | `figuras/figura-12.png` | Título da figura |
```

**Quadros de destaque**:

```markdown
::: {.quadro tipo="dica" titulo="Qual classe escolher"}
Texto do quadro. Aceita **negrito**, listas e equações.
:::
```

| `tipo` | Cor | Uso |
|---|---|---|
| `nota` | azul | informação complementar |
| `dica` | verde | recomendação prática |
| `atencao` | laranja | risco ou armadilha comum |
| `importante` | vermelho | restrição que não pode ser violada |

As cercas `:::` são reconhecidas por `latex/build-tex.py` como estrutura — sem
isso o normalizador as absorveria e o quadro não seria gerado. O ambiente
`quadro` é um `tcolorbox` quebrável entre páginas, definido em
[`latex/apostila.tex`](latex/apostila.tex); a conversão é feita por
[`latex/quadros.lua`](latex/quadros.lua).

**Tabelas** — a largura de cada coluna no `pandoc` vem do **número de traços** na
linha separadora, e não do conteúdo. Quatro colunas com `|---|---|---|---|` saem
com 25 % cada; para larguras proporcionais é preciso variar os traços:

```markdown
|:---------|:-----------------------|:-------------------------|
```

### Cores e elementos gráficos

O esquema usa quatro tons de azul (`xcolor`), do mais escuro no capítulo ao mais
claro na subsubseção, para reforçar a hierarquia:

| Elemento | Cor |
|---|---|
| Capa: título | `#10305A` |
| Capítulo | `#10305A` |
| Seção | `#1A4A85` |
| Subseção | `#2A63A8` |
| Subsubseção | `#3D7BC0` |
| Cabeçalho corrente (nome na margem + nº de página) | `#1A4A85` |
| Filete do cabeçalho | `#2A63A8` |
| Sumário e links internos | `#1A4A85` |

A **capa** é montada por `capa_tex()` em [`latex/build-tex.py`](latex/build-tex.py)
a partir de [`apostila/indice.md`](apostila/indice.md): título em azul, **filete
duplo** (2,4 pt + 0,6 pt) abrindo e fechando o bloco do título, um filete curto
centralizado entre os professores e a instituição, e um filete duplo fechando a
página. Os filetes usam `\hrule` — e não `\rule` — para não consumirem uma linha
de texto inteira cada um.

O capítulo usa a forma `display` ("CAPÍTULO N" em azul médio, título em azul
profundo, filete de 1,2 pt); as seções levam filete de 0,7 pt.

O **sumário** sai azul porque as entradas do sumário são os **únicos links
internos** do documento (o corpo não usa `\ref`): o `hyperref` passou a usar
`linkcolor` em vez de `hidelinks`, com `pdfborder={0 0 0}` para não desenhar
moldura. Por isso as cores são definidas **antes** do `hyperref` no preâmbulo.

O esquema não vaza cor para o corpo do texto e a hierarquia continua legível em
impressão preto e branco.

---

## Pipeline de migração PDF → Markdown

Os scripts em `apostila/` documentam e automatizam como o PDF original virou
texto-fonte. Todos, exceto o primeiro, são **idempotentes** e seguros de
reexecutar.

| Script | Papel | Efeito |
|---|---|---|
| [`build-md.py`](apostila/build-md.py) | migração inicial | **DESTRUTIVO** — sobrescreve todos os `apostila/*.md`; converte `**N.. PASSO**` em `**Nº PASSO**` e descarta o `**o**` órfão que o conversor extrai do ordinal |
| [`extrair-figuras.py`](apostila/extrair-figuras.py) | extração | recorta as 83 figuras do PDF (`mutool trace` + `pdftotext -bbox` + `pdftoppm` + Pillow) |
| [`corrigir-legendas.py`](apostila/corrigir-legendas.py) | correção | legendas das Figs. 1 e 2, resíduo das URLs de origem, legendas duplicadas no cap. 9 e o índice de figuras |
| [`inserir-secao-ipc.py`](apostila/inserir-secao-ipc.py) | conteúdo | cria/atualiza a seção §2.3 (Normas IPC) |
| [`juntar-trechos-partidos.py`](apostila/juntar-trechos-partidos.py) | correção | frases partidas por fim de parágrafo falso e espaço introduzido depois de hífen (`curtos- circuitos`) |
| [`reconstruir-tabela-jlcpcb.py`](apostila/reconstruir-tabela-jlcpcb.py) | correção | tabelas de capacidade de fabricação do cap. 7, reescritas a partir das capacidades publicadas pela JLCPCB |

Cada script traz no cabeçalho o defeito que corrige e a fonte da informação. A
lista consolidada de achados — com o que já foi corrigido e o que permanece
aberto — está em
[`docs/auditoria-apostila-pcb.md`](docs/auditoria-apostila-pcb.md).

---

## Materiais de referência

Os PDFs abaixo são fontes externas: **não são editados** e servem de base para a
revisão técnica e para as figuras/tabelas reaproveitadas.

| Arquivo | Origem | Páginas |
|---|---|---|
| [`docs/materialApoioKicad_Optativa_R9.pdf`](docs/materialApoioKicad_Optativa_R9.pdf) | apostila original (jun/2025) — ponto de partida da refatoração | 98 |
| [`docs/kicad.pdf`](docs/kicad.pdf) | documentação do KiCad | 25 |
| [`docs/Exportar-JLCPCB.pdf`](docs/Exportar-JLCPCB.pdf) | tutorial de exportação para a JLCPCB | 9 |
| [`livros/IPC Class 3 Design Guide.pdf`](livros/) | IPC — classes de qualidade (fonte da §2.3) | — |
| [`livros/DFM Handbook_January 2024.pdf`](livros/) | JLCPCB — *Design for Manufacturing* | — |
| [`livros/DFA Handbook_October 2022.pdf`](livros/) | JLCPCB — *Design for Assembly* | — |
| [`livros/High-Speed PCB Design Guide_January 2023.pdf`](livros/) | JLCPCB — alta velocidade | — |
| [`livros/Controlled Impedance Design Guide_October 2022.pdf`](livros/) | JLCPCB — impedância controlada (cap. 9) | — |
| [`livros/Differential_Pairs_in_PCB_Transmission_Lines_eBook_04.pdf`](livros/) | pares diferenciais | — |
| [`livros/Signal Integrity eBook_April 2023.pdf`](livros/) | integridade de sinal | — |
| [`livros/KiCad Design Guide_February 2022.pdf`](livros/) | JLCPCB — guia de KiCad | — |

---

## Documentação de apoio

| Arquivo | Conteúdo |
|---|---|
| [`docs/auditoria-apostila-pcb.md`](docs/auditoria-apostila-pcb.md) | auditoria técnica e editorial: critérios, método, achados `A-01`…`A-17`, resolução dos `[VERIFICAR]`, quadros, limitações, pipeline e pendências |
| [`docs/memorial.md`](docs/memorial.md) | especificação da skill de refatoração de apostila de PCB (escopo, princípios, entregáveis) |
| [`docs/agentic/`](docs/agentic/) | protocolo de contexto, modo de operação, fluxo, *Definition of Done* e matriz de rastreabilidade |
| [`latex/README.md`](latex/README.md) | decisões de formatação do LaTeX, gate, quadros, cores e limitações do build |
| [`AGENTS.md`](AGENTS.md) | regras permanentes de trabalho no repositório |
| [`AVALIACAO.md`](AVALIACAO.md) | diagnóstico dos artefatos SDD e oportunidades de melhoria |
| [`README-AGENTIC.md`](README-AGENTIC.md) | como instalar e usar o pacote agêntico em outro projeto |

---

## Automação agêntica

O repositório inclui um fluxo SDD adaptativo em `.github/`:

- **[`.github/agents/`](.github/agents/)** — 15 agentes encadeados, do roteamento
  (`00-task-router`) ao *handoff* (`14-handoff-manager`), com um
  `13-verification-gate` dedicado a impedir que uma tarefa seja declarada
  concluída sem evidência.
- **[`.github/instructions/`](.github/instructions/)** — regras permanentes de
  economia de contexto, engenharia embarcada, artefatos SDD e controle de
  mudanças.
- **[`.github/skills/`](.github/skills/)** — skills de domínio:
  [`refatoracao-apostila-pcb`](.github/skills/refatoracao-apostila-pcb/SKILL.md)
  (a que rege este material), `artigo-cientifico-latex`,
  `monografia-engenharia-latex`, `sdd-software` e `sdd-embarcado`.

A regra que mais impacta o dia a dia está em
`.github/instructions/03-change-control.instructions.md`: inspecionar o estado
real do repositório antes de alterar, fazer a menor mudança suficiente e só
declarar concluído com evidência.

---

## Limitações conhecidas e pendências

As correções desta rodada — A-02, A-03, A-04, A-06, A-09, A-10, A-12, A-13, A-18
e o crédito das Figs. 1 e 2 — estão registradas com evidência em
[`docs/auditoria-apostila-pcb.md`](docs/auditoria-apostila-pcb.md).

Pendências que continuam abertas:

- **A-07** (cap. 6) — a lista de ferramentas EDA ainda cita "Eagle" e "Mentor
  Graphics PADS". As duas informações já foram verificadas e o texto precisa ser
  reescrito, com alternativas atuais.
- **A-08** — cerca de metade dos links das Referências WEB é blog ou vídeo, não
  fonte técnica primária. Os guias de fabricante usados no cap. 9 já foram
  acrescentados.
- **Galeria do cap. 8** — os títulos dos projetos foram linearizados dentro do
  parágrafo de descrição da figura. Padronizar exige decisão editorial.
- **§7.8 — confirmação do autor**: a tabela de capacidades foi transcrita da
  página da JLCPCB, não recuperada do PDF de origem, e os valores do fabricante
  mudam com o tempo.
- **`apostila/build-md.py` sobrescreve tudo** — a migração é de uso único. Rodá-la
  de novo apaga todas as correções editoriais feitas à mão nos `apostila/*.md`.
- **Sem revisão externa** — o PDF compila e está estruturalmente correto, o que
  não equivale a conteúdo revisado por terceiros.

---

## Licença

Este material é distribuído sob a
**[Creative Commons Atribuição–CompartilhaIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br)**.

**Você pode:**

- **Compartilhar** — copiar e redistribuir o material em qualquer suporte ou
  formato, para qualquer fim, inclusive comercial.
- **Adaptar** — remixar, transformar e criar a partir do material, para qualquer
  fim, inclusive comercial.

**Desde que respeite as condições:**

- **Atribuição (BY)** — dar o crédito adequado, indicar as mudanças feitas e
  fornecer um link para a licença.
- **CompartilhaIgual (SA)** — se remixar, transformar ou criar a partir do
  material, as contribuições devem ser distribuídas sob a **mesma licença** do
  original.

O licenciante não pode revogar essas liberdades desde que as condições sejam
respeitadas. O material é oferecido **sem garantias** de qualquer tipo, expressas
ou implícitas.

- Texto legal completo: <https://creativecommons.org/licenses/by-sa/4.0/legalcode.pt>
- Resumo em português: <https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br>
- Arquivo do repositório: [`LICENSE`](LICENSE)

### Como atribuir

> VIANNA, William da Silva; DIAS, Luciano Resende. **Design de PCB com uso do
> KiCad para leitura e acionamento de sinais discretos**. Instituto Federal
> Fluminense, setembro/2026. Licenciado sob CC BY-SA 4.0.
> <https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br>

Ao publicar uma versão modificada, deixe explícito que se trata de versão
adaptada, para não atribuir aos autores originais afirmações que não são deles.

### Exceção: material de terceiros

A licença CC BY-SA 4.0 cobre **o texto, a organização didática e as figuras
originais** desta apostila. **Não** cobre material reaproveitado de terceiros,
que permanece sob o licenciamento original e cuja titularidade é dos respectivos
autores e fabricantes:

- figuras, tabelas e dados de fabricação extraídos dos guias e normas de
  `livros/` (IPC, JLCPCB, KiCad) e dos anexos em `docs/`;
- nomes, logotipos e capturas de tela de ferramentas de EDA, que são marcas de
  seus titulares.

Ao reutilizar este material, verifique a procedência de cada figura antes de
redistribuí-la.

---

Copyright © 2026 William da Silva Vianna e Luciano Resende Dias.
