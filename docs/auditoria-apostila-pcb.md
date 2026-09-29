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
| 4 | Legendas das Figuras 1 e 2 | CORRIGIR (pendente) | Mantidas como URL, crédito registrado | o material original usa a URL como legenda; não se inventou descrição |
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
| A-05 | cap. 7 §7.8 | VERIFICAR | tabela de capacidades sem atribuição de fabricante nem data; estrutura corrompida (colunas deslocadas) | `07-kicad.md` |
| A-06 | cap. 9 | VERIFICAR | "USB requer 90 ohms com tolerância de 10 %" sem fonte | `09-controle-impedancia.md` |
| A-07 | cap. 6 | DESATUALIZAR | "Eagle", "Mentor Graphics PADS" — nomenclatura/status provavelmente superados; lista omite alternativas atuais | `06-opcoes-eda.md` |
| A-08 | Referências WEB | INCOMPLETO | ~metade dos links são blogs/vídeos (não são fonte técnica primária) e os guias de fabricante usados no cap. 9 não estão citados | `99-referencias-web.md` |
| A-09 | Referências WEB | CORRIGIR | 2 URLs partidas por quebra de linha; tags `<u>` residuais | `99-referencias-web.md` |
| A-10 | Figura 68 | CORRIGIR | a legenda está **encoberta** pela imagem da Figura 67 no PDF — a figura não é visível no documento renderizado | página 88; verificado por render |
| A-11 | Geral | INCOMPLETO | nenhuma menção a norma IPC no texto, apesar de o repositório ter `livros/IPC Class 3 Design Guide.pdf` | varredura `IPC` = 0 ocorrências |
| A-12 | cap. 9 | CORRIGIR | texto com artefatos de conversão ("requer um uma", `**o**` solto) | `09-controle-impedancia.md` |
| A-13 | Geral | INCOMPLETO | capa sem seção de Apresentação; pipeline espera `## Apresentação` em `indice.md` | `apostila/indice.md` |
| A-14 | cap. 7 | INCOMPLETO | valores de capacidade (0,2 mm, 0,25 mm, 1 oz, anel anular ≧0,45 mm) sem indicação de que são limites de **um** fabricante em determinada data | `07-kicad.md` |
| A-15 | Geral (geração do markdown) | CORRIGIDO | **7 linhas de conteúdo perdidas** na geração anterior: a heurística de continuação de legenda consumia bolinhas em negrito e parágrafos em negrito | §9.1 |

Nada foi corrigido além do que a tabela §3 registra: os achados A-01 a A-14 são **propostas**, não alterações aplicadas, exceto as marcações `[VERIFICAR]`.

## 5. Pendências `[VERIFICAR]`

| Local | O que falta confirmar |
|---|---|
| `06-opcoes-eda.md` | status atual e fim de suporte do Eagle |
| `06-opcoes-eda.md` | nome e fornecedor atuais do PADS |
| `07-kicad.md` §7.8 | fabricante, documento e data da tabela de capacidades |
| `09-controle-impedancia.md` (2 pontos) | impedância característica e tolerância do USB na especificação oficial |
| `apostila/indice-figuras.md` | descrição real das Figuras 1 e 2 (originais citam apenas a URL) |

## 6. Limitações e riscos residuais

- A auditoria é **dirigida por varredura automatizada**; não é leitura integral das 98 páginas. Achados de conteúdo técnico não capturáveis por padrão (afirmação incorreta sem valor numérico) podem existir.
- A tabela de capacidades do cap. 7 exige **revisão manual** contra a fonte do fabricante: a perda de estrutura na conversão impede correção automática. No PDF ela aparece como tabela, com o corpo reduzido, mas o conteúdo das células continua embaralhado.
- **Não houve validação com o autor** do conteúdo técnico: o PDF compila e está estruturalmente correto, o que não equivale a conteúdo revisado.
- O pipeline depende do markdown intermediário de `@firecrawl/anydoc` (`/tmp/apostila-src.md`), que precisa ser regerado antes de rodar `apostila/build-md.py`.
- A origem de cada figura é o PDF da apostila, não o material original de terceiros; os créditos das Figuras 1 e 2 apontam para os URLs citados no documento.
- Títulos de nível 4 que na origem são cabeçalhos de tabela aparecem como subtítulos sem número (A-04).

## 7. Pipeline reproduzível

| Etapa | Comando |
|---|---|
| Extrair texto do PDF | `npx -y @firecrawl/anydoc docs/materialApoioKicad_Optativa_R9.pdf -o /tmp/apostila-src.md` |
| Extrair as figuras | `python3 apostila/extrair-figuras.py docs/materialApoioKicad_Optativa_R9.pdf apostila/figuras --report /tmp/figuras-report.json` |
| Gerar `apostila/*.md` | `python3 apostila/build-md.py` |
| Compilar o PDF | `cd latex && ./build-pdf.sh` |

## 8. Próximo passo sugerido

1. Resolver as pendências `[VERIFICAR]` (§5) — começando pela tabela do cap. 7 e pela tolerância do USB.
2. Aplicar as correções A-02, A-03, A-09, A-12 (mecânicas, sem risco editorial).
3. Reconstruir as tabelas de atalho do cap. 7 e a tabela de capacidades a partir da fonte do fabricante, com atribuição e data (A-04, A-05, A-14).
4. Atualizar a lista de ferramentas EDA do cap. 6 e as Referências WEB (A-07, A-08).
5. Criar a seção de Apresentação em `apostila/indice.md` (A-13).

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
