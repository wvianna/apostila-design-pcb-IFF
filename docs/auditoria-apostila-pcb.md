# Auditoria e refatoração — apostila de Design de PCB

**Fonte**: `docs/materialApoioKicad_Optativa_R9.pdf` (98 páginas, A4, LibreOffice 24.2; texto extraível, sem OCR).
**Destino**: `apostila/` (fonte de verdade do texto) e `apostila/figuras/`.
**Data**: 2026-09-29.

## 1. Critérios de aceitação

| ID | Critério | Resultado | Evidência |
|---|---|---|---|
| CA-001 | Conteúdo do original preservado; nada removido sem registro | PASS | Seções 1–10 e Referências WEB presentes; remoções listadas em §4 |
| CA-002 | Figuras do índice presentes como arquivo e referenciadas no texto | PASS | 83/83 em `apostila/figuras/`; 83/83 referenciadas; `apostila/indice-figuras.md` |
| CA-003 | Afirmação sem fonte confirmada marcada `[VERIFICAR]` | PASS | §5 — 6 marcações inline + 1 bloco |
| CA-004 | Estrutura utilizável pelo pipeline (`apostila/*.md`) | PASS | 11 arquivos de capítulo + `indice.md` |
| CA-005 | Documento LaTeX consolidado compilando sem erro nem `Overfull` | PASS | `latex/apostila.pdf`, 107 páginas, 0 erros / 0 `Overfull` / 0 referência pendente |
| CA-006 | Toda figura do manifesto presente no PDF com legenda | PASS | 83/83 legendas no PDF, 0 duplicata |
| CA-007 | Revisão técnica ancorada em fonte, sem invenção | PASS | 5 correções de conteúdo, todas com fonte em `livros/`; 0 valor numérico novo sem fonte |

## 2. Método

1. **F0** — inventário do PDF (98 páginas, 83 figuras pelo índice próprio) e verificação de ferramentas.
2. **Conversão** — `@firecrawl/anydoc` → markdown, para não ler o PDF página a página.
3. **Figuras** — extração por caixa de imagem (`mutool trace`) casada com a legenda (`pdftotext -bbox`), recorte de render 300 dpi.
4. **Montagem** — divisão em capítulos e reinserção das figuras junto às legendas.
5. **F1** — auditoria por varredura dirigida (numeração, títulos, links, valores, normas).

**Controle de mudanças**: `git status` falhou — o diretório **não é um repositório git**. O passo de `git diff` previsto nas instruções do repositório não pôde ser aplicado; o estado inicial do workspace foi inventariado por listagem.

## 3. O que foi alterado (cada mudança com razão)

| # | Seção / artefato | Classe | Mudança | Razão |
|---|---|---|---|---|
| 1 | PDF inteiro | INCOMPLETO | Convertido para markdown | texto-fonte editável; o PDF não é fonte de trabalho |
| 2 | 83 figuras | OK | Extraídas para `apostila/figuras/figura-NN.png` | a conversão descartou todas as imagens (`![` = 0) |
| 3 | Legendas A/B (pares) | CORRIGIR | Renumeradas para ordem crescente | a conversão devolvia B antes de A (ex.: Figura 4 antes da 3) |
| 4 | Legendas das Figuras 1 e 2 | **CORRIGIDO** | "Exemplos de PCBs" e "Exemplos de serigrafias" | definidas pelo autor em 2026-09-29; o manifesto `indice-figuras.md` acompanha |
| 5 | Sumário e Índice de figuras do original | DESLOCADO | Fora dos capítulos; manifesto em `apostila/indice-figuras.md` | são gerados pelo pipeline; mantê-los no corpo duplicaria a fonte de verdade |
| 6 | Capa | DESLOCADO | `apostila/indice.md` | pré-textual, conforme o pipeline |
| 7 | Galeria do cap. 8 | DESLOCADO | Tabelas de 2 colunas linearizadas em imagem + legenda + descrição | no markdown a tabela chegava corrompida e sem as imagens; nenhum texto perdido |
| 8 | Títulos numerados | CORRIGIR | Nível derivado da profundidade do número (`9.1` → seção) | 7 títulos estavam um nível acima ou abaixo; 9.1–9.3 saíam como `9.0.x` |
| 9 | Blocos colados | CORRIGIR | Linha em branco antes de título e de início de tabela | 140 blocos eram absorvidos pelo parágrafo anterior (o pandoc exige a linha em branco) |
| 10 | Legendas | CORRIGIR | Contador do LaTeX não é impresso | o número já vem na legenda; evitar "Figura 2.3: Figura 20: …" |

## 4. Achados da auditoria (F1)

| # | Local | Classe | Achado | Evidência |
|---|---|---|---|---|
| A-01 | cap. 2 | CORRIGIDO | salto de numeração `2.2` → `2.4` — resolvido por construção: o LaTeX renumera a partir do nível | `apostila/02-principios-elementos.md` |
| A-02 | cap. 2 | CORRIGIR | bullet `•` solto, fora de lista | `07-kicad.md`/`02-*` |
| A-03 | cap. 2 | DESATUALIZAR | termos em inglês sem tradução ("Surface finish") | — |
| A-04 | cap. 7 §7.7 | CORRIGIDO EM PARTE | tabelas de atalho: a hierarquia de títulos foi corrigida, mas os cabeçalhos "Tecla de / Descrição / Atalho" continuam como subtítulos — reconstruir as tabelas a partir do original | `latex/apostila.pdf` p. 50 |
| A-05 | cap. 7 §7.8 | **CORRIGIDO** | tabela de capacidade com células desalinhadas pela conversão (colunas deslocadas, texto intercalado entre linhas) | reconstruída a partir da página do fabricante por `apostila/reconstruir-tabela-jlcpcb.py`; PDF p. 53–57 |
| A-06 | cap. 9 | VERIFICAR | "USB requer 90 ohms com tolerância de 10 %" sem fonte | `09-controle-impedancia.md` |
| A-07 | cap. 6 | DESATUALIZAR | "Eagle", "Mentor Graphics PADS" — nomenclatura/status provavelmente superados; lista omite alternativas atuais | `06-opcoes-eda.md` |
| A-08 | Referências WEB | INCOMPLETO | ~metade dos links são blogs/vídeos (não são fonte técnica primária) e os guias de fabricante usados no cap. 9 não estão citados | `99-referencias-web.md` |
| A-09 | Referências WEB | CORRIGIR | 2 URLs partidas por quebra de linha; tags `<u>` residuais | `99-referencias-web.md` |
| A-10 | Figura 68 | CORRIGIR | a legenda está **encoberta** pela imagem da Figura 67 no PDF — a figura não é visível no documento renderizado | página 88; verificado por render |
| A-11 | cap. 2 §2.3 | **CORRIGIDO** | nenhuma menção a norma IPC no texto, apesar de o repositório ter `livros/IPC Class 3 Design Guide.pdf` | nova seção §2.3 (o que é a IPC, classes IPC-6011/6012, uso prático) com 2 quadros; inserida por `apostila/inserir-secao-ipc.py`; ocupa a lacuna de numeração do A-01 |
| A-12 | cap. 9 | CORRIGIR | texto com artefatos de conversão ("requer um uma", `**o**` solto) | `09-controle-impedancia.md` |
| A-13 | Geral | INCOMPLETO | capa sem seção de Apresentação; pipeline espera `## Apresentação` em `indice.md` | `apostila/indice.md` |
| A-14 | cap. 7 | **CORRIGIDO** | valores de capacidade sem indicação de fabricante e data | atribuição explícita (JLCPCB, consulta em 09/2026) na linha imediatamente acima das tabelas; a nota de quadro alerta que os valores mudam com o tempo |
| A-15 | Geral (geração do markdown) | CORRIGIDO | **7 linhas de conteúdo perdidas** na geração anterior: a heurística de continuação de legenda consumia bolinhas em negrito e parágrafos em negrito | §9.1 |
| A-16 | caps. 2, 4, 5, 7, 8, 10 | **CORRIGIDO** | **7 frases partidas no meio** por um fim de parágrafo falso, herdado da quebra de linha do PDF | `apostila/juntar-trechos-partidos.py`; detectadas por varredura e fixadas uma a uma |
| A-17 | caps. 2, 4, 7, 8 | **CORRIGIDO** | 4 termos com **espaço depois de hífen legítimo** (`curtos- circuitos`, `foto- resistente`, `add- on`, `espectrômetro- dosímetro`) e 1 par de palavras transpostas (`fp- info-cachearquivo`) | `apostila/juntar-trechos-partidos.py` |

Os achados A-01 a A-17 foram **propostas** da fase de auditoria. O que já foi aplicado está marcado como **CORRIGIDO** na coluna «Evidência»: a revisão de conteúdo no §9, os quadros no §5.1, a reconstrução das tabelas do cap. 7 no §7.4 e a seção IPC no §2.3.

## 5. Pendências `[VERIFICAR]` — resolvidas em 2026-09-29

| Local | Situação | Fonte |
|---|---|---|
| `06-opcoes-eda.md` — Eagle | **resolvido**: a Autodesk encerrou o EAGLE — deixou de ser vendido e suportado em 07/06/2026 | Autodesk, *Autodesk EAGLE is no longer available — Next steps and FAQ* |
| `06-opcoes-eda.md` — PADS | **resolvido**: hoje é **Siemens PADS Professional** (o PADS era da Mentor Graphics) | Siemens, *PADS PCB design software* |
| `07-kicad.md` §7.8 — tabela | **resolvido**: a atribuição **já existia** (JLCPCB, 11/2024) — o marcador era falso alarme. A **integridade** foi corrigida pela reconstrução das 6 subseções (§7.4), com a atribuição atualizada para 09/2026 | JLCPCB, *PCB Manufacturing & Assembly Capabilities* |
| `09-controle-impedancia.md` — USB | **corrigido**: o USB 2.0 exige **90 Ω ±15%**; o ±10% que o texto citava é a **tolerância de fabricação** da impedância controlada, não o requisito da interface | Texas Instruments, *USB layout basics*; JLCPCB (impedance tolerance ±10%) |
| `apostila/indice-figuras.md` — Figuras 1 e 2 | **resolvido**: no documento original a legenda era a própria URL. O autor definiu "Exemplos de PCBs" e "Exemplos de serigrafias" em 2026-09-29 | decisão editorial do autor |

Os marcadores inline foram removidos do texto; a informação corrigida passou para o corpo dos capítulos, com a fonte indicada. **0 `[VERIFICAR]` no PDF.**

## 5.1 Quadros de destaque (novo)

Mecanismo: div marcada no markdown → filtro Lua → ambiente `quadro` (tcolorbox) no LaTeX.

```markdown
::: {.quadro tipo="dica" titulo="Rótulo"}
Texto do quadro.
:::
```

Tipos e cores: `nota` (azul), `dica` (verde), `atencao` (laranja), `importante` (vermelho).
Arquivos: `latex/quadros.lua` e o ambiente em `latex/apostila.tex`.

Oito quadros, cada um **substituindo** o texto que estava em prosa ou resumindo uma seção nova (sem duplicar conteúdo):

| Onde | Tipo | Título |
|---|---|---|
| §2.3.1 | nota | Por que isso importa no seu projeto |
| §2.3.3 | dica | Qual classe escolher |
| §3.7 | importante | Plano de terra: um só, contínuo |
| §3.8 | dica | Regra prática: espaçamento entre trilhas (3W) |
| §3.10 | atenção | Ângulos na trilha: use 45° |
| §3.14 | atenção | Nunca ligue o microcontrolador direto no conector |
| §7.8 | dica | Antes de mandar fabricar |
| §9.4 | importante | Impedância do par diferencial USB |

## 5.2 Pendências herdadas

## 6. Limitações e riscos residuais

- A auditoria é **dirigida por varredura automatizada**; não é leitura integral das 98 páginas. Achados de conteúdo técnico não capturáveis por padrão (afirmação incorreta sem valor numérico) podem existir.
- ~~A tabela de capacidades do cap. 7 exige revisão manual~~ → **resolvida** (§7.4). Registre-se a natureza da correção: as células foram **transcritas da página do fabricante**, não recuperadas do PDF de origem — o texto da apostila é, nessas 6 subseções, uma paráfrase em pt-BR da fonte, e não o texto do autor. Como os valores mudam, **exigem confirmação do autor** antes de uso em aula.
- **Não houve validação com o autor** do conteúdo técnico: o PDF compila e está estruturalmente correto, o que não equivale a conteúdo revisado.
- O pipeline depende do markdown intermediário de `@firecrawl/anydoc` (`/tmp/apostila-src.md`), que precisa ser regerado antes de rodar `apostila/build-md.py`.
- A origem de cada figura é o PDF da apostila, não o material original de terceiros. **As legendas das Figuras 1 e 2 deixaram de registrar o URL de origem** (§3, linha 4): o crédito precisa ser reposto na seção de referências, já que a apostila reutiliza imagens de terceiros.
- O esquema de cores em azul (capa, títulos, cabeçalho corrente e sumário — §7.3) é uma escolha de apresentação: **não altera conteúdo** e foi **pedido explicitamente pelo autor** (duas rodadas: títulos/subtítulos e, depois, título do material + cabeçalhos + capa). Impressão em preto e branco mantém a hierarquia pelo tamanho e pelo peso das fontes.
- O Capítulo 9 foi revisado apenas quanto à afirmação sobre o USB (§5), **não** integralmente contra `livros/Controlled Impedance Design Guide.pdf`.
- Títulos de nível 4 que na origem são cabeçalhos de tabela aparecem como subtítulos sem número (A-04).

## 7. Pipeline reproduzível

| Etapa | Comando |
|---|---|
| Extrair texto do PDF | `npx -y @firecrawl/anydoc docs/materialApoioKicad_Optativa_R9.pdf -o /tmp/apostila-src.md` |
| Extrair as figuras | `python3 apostila/extrair-figuras.py docs/materialApoioKicad_Optativa_R9.pdf apostila/figuras --report /tmp/figuras-report.json` |
| Gerar `apostila/*.md` | `python3 apostila/build-md.py` (sobrescreve TODOS os `apostila/*.md`) |
| Corrigir legendas 1 e 2 e o índice | `python3 apostila/corrigir-legendas.py` |
| Inserir/atualizar a seção IPC | `python3 apostila/inserir-secao-ipc.py` |
| Rejuntar trechos partidos pela conversão | `python3 apostila/juntar-trechos-partidos.py` |
| Reconstruir as tabelas do cap. 7 | `python3 apostila/reconstruir-tabela-jlcpcb.py` |
| Compilar o PDF | `cd latex && ./build-pdf.sh` (lê do **disco**) |

Ordem obrigatória: gravar os buffers do editor **antes** de rodar os scripts. Os scripts
reescrevem os arquivos direto no disco e um buffer defasado do editor, ao ser gravado
depois, **reverte** o trabalho do script sem aviso — foi o que apagou as legendas 1 e 2
entre duas compilações.

## 7.1 Scripts de correção editorial

| Script | O que faz |
|---|---|
| `apostila/corrigir-legendas.py` | Legenda das Figuras 1 e 2 (a legenda era a URL de origem) + limpeza do resíduo de URL quebrada em itálico; no cap. 9, remove a legenda duplicada da Figura 68 e a cópia extra da Figura 67. No manifesto `indice-figuras.md`, atualiza as legendas 1 e 2. |
| `apostila/inserir-secao-ipc.py` | Cria o §2.3 (Normas IPC) a partir do texto de `livros/IPC Class 3 Design Guide.pdf`. Só afirma o que essa fonte declara. Atualiza a tabela das classes para 3 colunas se encontrar a versão antiga de 4. |
| `apostila/juntar-trechos-partidos.py` | Rejunta frases partidas por fim de parágrafo falso (A-16) e remove espaço depois de hífen legítimo (A-17). Os casos estão fixados um a um; os modos são **explícitos** nas listas, porque inferir o modo pela pontuação duplicou frases numa versão anterior. |

## 7.2 Formatação de tabelas

### Contagem de traços define a largura da coluna

O pandoc deriva a largura relativa de cada coluna do número de traços na linha
separadora da tabela em markdown. Uma tabela de 4 colunas com `|---|---|---|---|`
sai com 0,25 para todas, e as colunas estreitas ficam ilegíveis. Para a tabela das
classes IPC, `|:---------|:-----------------------|:--------------------------------------------------------|`
produz 0,11 / 0,26 / 0,63.

## 7.3 Esquema de cores e elementos gráficos em azul

`latex/apostila.tex` carrega `xcolor` + `titlesec` e define quatro tons de azul, do
mais escuro no capítulo ao mais claro na subsubseção:

| Elemento | Cor | Hexadecimal |
|---|---|---|
| Capa: título | azul profundo | `#10305A` |
| Capítulo | azul profundo | `#10305A` |
| Seção | azul médio | `#1A4A85` |
| Subseção | azul claro | `#2A63A8` |
| Subsubseção | azul mais claro | `#3D7BC0` |
| Cabeçalho corrente (nome na margem + nº de página) | azul médio | `#1A4A85` |
| Filete do cabeçalho | azul claro | `#2A63A8` |
| Sumário e links internos | azul médio | `#1A4A85` |

O capítulo usa a forma `display`: rótulo "CAPÍTULO N" em azul médio, título em azul
profundo e um filete de 1,2 pt. As seções levam filete de 0,7 pt.

**Capa** (`capa_tex()` em `latex/build-tex.py`, a partir de `apostila/indice.md`):
título em azul profundo, filete duplo (2,4 pt + 0,6 pt) abrindo e fechando o bloco
do título, filete curto centralizado entre os professores e a instituição, e filete
duplo fechando a página. Os filetes usam `\hrule` em vez de `\rule` para não
consumirem uma linha de texto inteira cada um.

**Cabeçalho corrente**: nome do capítulo/seção e número de página em azul médio,
filete em azul claro — o `\headrule` do `fancyhdr` é redefinido porque o original é
preto e não aceita cor.

**Sumário em azul**: as entradas do sumário são os **únicos links internos** do
documento (o corpo não usa `\ref`), então o `hyperref` trocou `hidelinks` por
`linkcolor=azulSec` com `pdfborder={0 0 0}`. Isso obriga a definir as cores
**antes** do `hyperref` no preâmbulo.

Dois cuidados verificados: os quatro tons passam no contraste mínimo para texto
grande sobre branco, e `titlesec` **não** vaza cor para o corpo — as legendas de
figura continuam em preto. O gate seguiu em 0 erros / 0 *Overfull* após a mudança.

## 7.4 Tabelas de capacidade do cap. 7 (reconstrução)

As tabelas de §7.8 vinham da conversão com as células desalinhadas — nas 6 subseções
(Especificações, Perfuração, Larguras, Máscara de solda, Lenda, Contorno), o separador
`|---|---|` aparecia **entre** as linhas de dados, o que quebrava a tabela e fazia o
pandoc imprimir parte delas como texto literal.

Reconstruídas a partir da página de capacidades do fabricante (`jlcpcb.com/capabilities/pcb-capabilities`),
com 3 colunas (Característica · Capacidade · Descrição) e descrições em pt-BR. O script
`apostila/reconstruir-tabela-jlcpcb.py` guarda o conteúdo e substitui o bloco entre
`#### Especificações do PCB` e `#### Lenda`, sendo reexecutável quando o fabricante
atualizar a página.

**Atenção**: os valores passaram a ser os publicados em **09/2026**, não os de 11/2024
que o texto citava antes. As diferenças encontradas incluem a expansão da máscara de
solda (era 0,038 mm, agora 1:1 com LDI atualizado em jun/2025) e o cobre acabado da
camada externa (era 1/2 oz, agora 1 a 4,5 oz em 2 camadas).

## 8. Próximo passo sugerido

**Concluído**: §2.3 (seção IPC — A-11), §5 (todas as pendências `[VERIFICAR]`), §5.1 (8 quadros), §7.4 (tabelas do cap. 7), A-05, A-11, A-14, A-15, A-16, A-17, a troca das legendas 1 e 2 e as correções de conteúdo do cap. 3 (§9.2).

**Pendente**:

1. Aplicar as correções mecânicas restantes: A-02 (bullet `•` solto), A-03 (termos em inglês sem tradução), A-09 (URLs partidas e tags `<u>`), A-12 (artefatos de conversão no cap. 9).
2. Reconstruir as tabelas de atalho do cap. 7 (§7.7), cujos cabeçalhos continuam como subtítulos sem número (A-04).
3. Atualizar a lista de ferramentas EDA do cap. 6 e as Referências WEB (A-07, A-08).
4. Criar a seção de Apresentação em `apostila/indice.md` (A-13).
5. Repor o crédito das Figuras 1 e 2 na seção de referências — a troca da legenda removeu o URL que fazia as vezes de crédito (§6).
6. A-06 (tolerância do USB) e A-10 (Figura 68 encoberta) dependem de decisão editorial — a segunda reproduz um defeito do próprio PDF de origem.

## 9. Revisão técnica (correções de conteúdo aplicadas)

Titulação da capa atualizada (`D.Sc.` / `M.Sc.`) e data para `setembro/2026`.

### 9.1 Defeito de perda de conteúdo (A-15) — corrigido

A rotina de montagem do markdown consumia como "continuação da legenda" qualquer
parágrafo iniciado por `*`, o que apagou **7 linhas**: as bolinhas
*Separação de Plano de Terra* e *Ilhas de Terra* (§3.7) e os rótulos
`**2.. PASSO**`, `**3.. PASSO**`, `**4.. PASSO**` (cap. 9), além de dois títulos de
lista de acabamento (§2.2.5). A regra passou a aceitar apenas linha **inteiramente
em itálico**, e a conferência de cobertura acusa agora **0 linha ausente**.

### 9.2 Correções técnicas (cap. 3)

Todas as fontes estão no próprio repositório (`livros/`).

| # | Local | Defeito | Correção | Fonte |
|---|---|---|---|---|
| 1 | §3.8 | **conselho invertido**: mandava rotear sensível *em paralelo* e evitar cruzar perpendicularmente — o oposto do correto | o acoplamento cresce com o trecho paralelo e é mínimo no cruzamento perpendicular; minimizar paralelismo | `High-Speed PCB Design Guide` |
| 2 | §3.8 | faltava a regra de espaçamento contra *crosstalk* | acrescentada a **regra 3W** (2W mínimo), com a ressalva de não se aplicar dentro do par diferencial | `High-Speed PCB Design Guide` |
| 3 | §3.8 | mandava **afastar o terra do sinal**, o que aumenta a impedância e a emissão | o plano de referência é o caminho de retorno e deve ficar contínuo e próximo; o afastamento é entre sinais | `Signal Integrity eBook` |
| 4 | §3.7 | recomendava **separar planos de terra** analógico e digital e usar ilhas de terra | plano único e contínuo; dividir só com **um ponto de interligação controlado**; costura de vias na origem/destino | `Signal Integrity eBook` ("Avoid ground split planes") |
| 5 | §3.10 | atribuía os 45° a **"reduzir reflexões de sinal"** | a razão documentada é de fabricação: ângulo agudo forma armadilha de ácido (*acid trap*) e pode abrir a trilha | `High-Speed PCB Design Guide`, §10.1 |
| 6 | §3.4 | largura de trilha dependia só da corrente | explicitadas as demais dependências (ΔT admitido, espessura de cobre, camada externa/interna) | conhecimento de engenharia; **valores numéricos continuam pendentes de fonte** |

### 9.3 Marcadores `[VERIFICAR]` restaurados

A regeneração do markdown (A-15) apagou os marcadores editoriais das sessões
anteriores. Foram reaplicados: 2 no cap. 6 (status do Eagle; nome do PADS), 1 no
cap. 7 (fonte e integridade da tabela de capacidades, agora em bloco único) e 2 no
cap. 9 (tolerância do USB). **5 ocorrências `[VERIFICAR]` no PDF.**

Lembrete operacional: `apostila/build-md.py` **sobrescreve** os capítulos — rodá-lo
depois de editar à mão apaga as correções. Os marcadores ficam no arquivo de cada
capítulo, não só no `indice-figuras.md`.

### 9.4 O que a revisão **não** cobriu

- Não houve leitura integral das 108 páginas: a varredura foi dirigida aos capítulos
técnicos (cap. 3) e às afirmações já sinalizadas. Erros em texto corrido sem valor
numérico podem ter escapado.
- O cap. 9 (impedância controlada) só foi revisado na afirmação sobre USB; o restante
do capítulo não passou por verificação contra `livros/Controlled Impedance Design Guide`.
- A tolerância de 10 % do USB continua `[VERIFICAR]`: o valor de 90 Ω é corroborado
pelo guia local, a tolerância não.
