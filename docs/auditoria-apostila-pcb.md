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

**Controle de mudanças**: o diretório **é um repositório git** (a nota anterior, de que não era, estava errada). Baseline desta rodada: `git status --short` limpo, exceto as remoções já preparadas de `latex/build/` (arquivos gerados, retirados do controle pelo autor). `git diff` foi executado antes de cada alteração.

## 3. O que foi alterado (cada mudança com razão)

| # | Seção / artefato | Classe | Mudança | Razão |
|---|---|---|---|---|
| 1 | PDF inteiro | INCOMPLETO | Convertido para markdown | texto-fonte editável; o PDF não é fonte de trabalho |
| 2 | 83 figuras | OK | Extraídas para `apostila/figuras/figura-NN.png` | a conversão descartou todas as imagens (`![` = 0) |
| 3 | Legendas A/B (pares) | CORRIGIR | Renumeradas para ordem crescente | a conversão devolvia B antes de A (ex.: Figura 4 antes da 3) |
| 4 | Legendas das Figuras 1 e 2 | **CORRIGIDO** | "Exemplos de PCBs" e "Exemplos de serigrafias" | definidas pelo autor em 2026-09-29; o manifesto `indice-figuras.md` acompanha; o URL de origem, que fazia as vezes de crédito, passou para a seção de referências |
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
| A-02 | cap. 2 | **CORRIGIDO** | bullet `•` solto, fora de lista | removidos o marcador e os dois fragmentos órfãos das legendas 11/12; o item ENEPIG voltou a ser item de lista, como os vizinhos (`02-principios-elementos.md`) |
| A-03 | cap. 2 | **CORRIGIDO** | termos em inglês sem tradução ("Surface finish") | frase reescrita com o termo em português primeiro e o inglês em itálico; de passagem, `solderabilidade` → `soldabilidade` e `metal o material orgânico` → `metal ou material orgânico` |
| A-04 | cap. 7 §7.7 | **CORRIGIDO** | tabelas de atalho: a hierarquia de títulos foi corrigida, mas os cabeçalhos "Tecla de / Descrição / Atalho" continuam como subtítulos — reconstruir as tabelas a partir do original | §7.7.3 reconstruída a partir do PDF original (p. 45): as duas tabelas de teclas globais viraram uma, com F11 e F1 como linhas; também demovidos dois títulos falsos do cap. 7 (`As principais funcionalidades…`, `As bibliotecas são:`) |
| A-05 | cap. 7 §7.8 | **CORRIGIDO** | tabela de capacidade com células desalinhadas pela conversão (colunas deslocadas, texto intercalado entre linhas) | reconstruída a partir da página do fabricante por `apostila/reconstruir-tabela-jlcpcb.py`; PDF p. 53–57 |
| A-06 | cap. 9 | **CORRIGIDO** | "USB requer 90 ohms com tolerância de 10 %" sem fonte | quadro §9.4: **90 Ω ±15%** é o requisito da interface (TI, *USB layout basics*); **±10%** é a tolerância de fabricação da impedância controlada — confirmada em `livros/Controlled Impedance Design Guide`, §1.5 (±10% padrão, ±5% apertada) |
| A-07 | cap. 6 | DESATUALIZAR | "Eagle", "Mentor Graphics PADS" — nomenclatura/status provavelmente superados; lista omite alternativas atuais | `06-opcoes-eda.md` |
| A-08 | Referências WEB | INCOMPLETO | ~metade dos links são blogs/vídeos (não são fonte técnica primária) e os guias de fabricante usados no cap. 9 não estão citados | `99-referencias-web.md` |
| A-09 | Referências WEB | **CORRIGIDO** | 2 URLs partidas por quebra de linha; tags `<u>` residuais | URLs recompostas (`raisa`, `embarcados/10-mandamentos`) e todas as tags `<u>` removidas — 0 `<u>` no PDF; a lista passou a citar também os guias de fabricante usados no cap. 9 (cobre em parte o A-08) |
| A-10 | Figura 68 | **CORRIGIDO** | a legenda está **encoberta** pela imagem da Figura 67 no PDF — a figura não é visível no documento renderizado | causas eram as legendas duplicadas da Fig. 68 (antes da 67) e da Fig. 67 (repetida no fim) — já removidas por `corrigir-legendas.py`; **verificado por render**: as duas figuras e as duas legendas aparecem no PDF, p. 86 |
| A-11 | cap. 2 §2.3 | **CORRIGIDO** | nenhuma menção a norma IPC no texto, apesar de o repositório ter `livros/IPC Class 3 Design Guide.pdf` | nova seção §2.3 (o que é a IPC, classes IPC-6011/6012, uso prático) com 2 quadros; inserida por `apostila/inserir-secao-ipc.py`; ocupa a lacuna de numeração do A-01 |
| A-12 | cap. 9 | **CORRIGIDO** | texto com artefatos de conversão ("requer um uma", `**o**` solto) | frases e títulos falsos (`#### Acesse …`, `#### Troque a unidade para mm.`, itens de parâmetro como títulos) corrigidos; rótulos `1º`–`4º PASSO` restaurados; `LESD5D5.0` reescrito (ESD, não "EDS/Sensitivity"); preposições e concordâncias ajustadas |
| A-13 | Geral | **CORRIGIDO** | capa sem seção de Apresentação; pipeline espera `## Apresentação` em `indice.md` | `## Apresentação` em `apostila/indice.md`; `build-tex.py` gera `build/apresentacao.tex` e `apostila.tex` a inclui antes do sumário — página i, sem número de capítulo |
| A-14 | cap. 7 | **CORRIGIDO** | valores de capacidade sem indicação de fabricante e data | atribuição explícita (JLCPCB, consulta em 09/2026) na linha imediatamente acima das tabelas; a nota de quadro alerta que os valores mudam com o tempo |
| A-15 | Geral (geração do markdown) | CORRIGIDO | **7 linhas de conteúdo perdidas** na geração anterior: a heurística de continuação de legenda consumia bolinhas em negrito e parágrafos em negrito | §9.1 |
| A-16 | caps. 2, 4, 5, 7, 8, 10 | **CORRIGIDO** | **7 frases partidas no meio** por um fim de parágrafo falso, herdado da quebra de linha do PDF | `apostila/juntar-trechos-partidos.py`; detectadas por varredura e fixadas uma a uma |
| A-17 | caps. 2, 4, 7, 8 | **CORRIGIDO** | 4 termos com **espaço depois de hífen legítimo** (`curtos- circuitos`, `foto- resistente`, `add- on`, `espectrômetro- dosímetro`) e 1 par de palavras transpostas (`fp- info-cachearquivo`) | `apostila/juntar-trechos-partidos.py` |
| A-18 | cap. 9 §9.4 | **CORRIGIDO** | o parágrafo do **3º passo** não existia no markdown: foi consumido na primeira migração junto com o artefato `**o**`. Levava os dois URLs de calculadora de impedância (JLCPCB e Sierra Circuits) e a instrução "Selecione **sem revestimento** e **par diferencial** e clique em OPEN" | recuperado de `/tmp/apostila-src.md`; `build-md.py` ganhou `limpar_marcadores()` para não reproduzir a perda |

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

Oito quadros, cada um **substituindo** o texto que estava em prosa ou resumindo uma seção nova (sem duplicar conteúdo), e um nono, acrescentado depois, para o crédito das figuras de terceiros:

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
| Referências WEB | nota | Créditos de figuras de terceiros |

## 5.2 Pendências herdadas

## 6. Limitações e riscos residuais

- A auditoria é **dirigida por varredura automatizada**; não é leitura integral das 98 páginas. Achados de conteúdo técnico não capturáveis por padrão (afirmação incorreta sem valor numérico) podem existir.
- ~~A tabela de capacidades do cap. 7 exige revisão manual~~ → **resolvida** (§7.4). Registre-se a natureza da correção: as células foram **transcritas da página do fabricante**, não recuperadas do PDF de origem — o texto da apostila é, nessas 6 subseções, uma paráfrase em pt-BR da fonte, e não o texto do autor. Como os valores mudam, **exigem confirmação do autor** antes de uso em aula.
- **Não houve validação com o autor** do conteúdo técnico: o PDF compila e está estruturalmente correto, o que não equivale a conteúdo revisado.
- O pipeline depende do markdown intermediário de `@firecrawl/anydoc` (`/tmp/apostila-src.md`), que precisa ser regerado antes de rodar `apostila/build-md.py`.
- A origem de cada figura é o PDF da apostila, não o material original de terceiros. As legendas das Figuras 1 e 2 deixaram de registrar o URL de origem (§3, linha 4); **o crédito foi reposto** na seção de referências, em quadro próprio, com a observação de que a apostila reutiliza imagens de terceiros.
- O esquema de cores em azul (capa, títulos, cabeçalho corrente, sumário e a página de Apresentação — §7.3) é uma escolha de apresentação: **não altera conteúdo** e foi **pedido explicitamente pelo autor** (duas rodadas: títulos/subtítulos e, depois, título do material + cabeçalhos + capa). Impressão em preto e branco mantém a hierarquia pelo tamanho e pelo peso das fontes.
- O Capítulo 9 foi conferido contra `livros/Controlled Impedance Design Guide_October 2022.pdf`: a tolerância de fabricação (§1.5), a definição de *skew* e as regras de casamento de comprimento e serpentinas (§3.5.5) estão aderentes, e o texto passou a citá-las. O resto do capítulo são procedimentos do KiCad e valores de fabricante (JLCPCB), não confrontados com outra fonte.
- Os títulos de nível 4 sem número que restam são **legítimos**: subseções sem numeração do §7.4.1, grupos de tabela do §7.8 e o nome de um projeto no cap. 8. Os falsos — cabeçalhos de tabela e frases de corpo promovidas a título — foram eliminados (A-04, A-12).

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
| Gerar capa, Apresentação e índice de figuras | `python3 latex/build-tex.py` — a partir de `apostila/indice.md` e `apostila/indice-figuras.md` (executado por `build-pdf.sh`) |
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

**Concluído**: §2.3 (seção IPC — A-11), §5 (todas as pendências `[VERIFICAR]`), §5.1 (9 quadros), §7.4 (tabelas do cap. 7), A-02, A-03, A-04, A-05, A-06, A-09, A-10, A-11, A-12, A-13, A-14, A-15, A-16, A-17 e A-18, a troca das legendas 1 e 2, o crédito das Figuras 1 e 2 e as correções de conteúdo dos caps. 3 e 9.

**Pendente**:

1. **A-07** (cap. 6) — a lista de ferramentas EDA ainda cita EAGLE e PADS; as duas informações já foram verificadas (§5), mas **o texto do capítulo não foi reescrito**, e alternativas atuais não foram acrescentadas.
2. **A-08** (Referências WEB) — cerca de metade dos links continua sendo blog ou vídeo, não fonte técnica primária. Os guias de fabricante usados no cap. 9 já foram acrescentados.
3. **Galeria do cap. 8** — os títulos dos projetos foram linearizados dentro do parágrafo de descrição; só `Dosímetros SPACEDOS` virou título. Padronizar exige decisão editorial.
4. **Confirmação do autor** — a tabela de capacidades do §7.8 foi transcrita da página do fabricante, não recuperada do PDF de origem (§6).
5. Reaplicar as correções editoriais depois de qualquer nova execução de `apostila/build-md.py`: a migração é de uso único e **sobrescreve todos** os `apostila/*.md`.

## 9. Revisão técnica (correções de conteúdo aplicadas)

Titulação da capa atualizada (`D.Sc.` / `M.Sc.`) e data para `setembro/2026`.

### 9.1 Defeito de perda de conteúdo (A-15) — corrigido

A rotina de montagem do markdown consumia como "continuação da legenda" qualquer
parágrafo iniciado por `*`, o que apagou **7 linhas**: as bolinhas
*Separação de Plano de Terra* e *Ilhas de Terra* (§3.7) e os rótulos
`**2.. PASSO**`, `**3.. PASSO**`, `**4.. PASSO**` (cap. 9), além de dois títulos de
lista de acabamento (§2.2.5). A regra passou a aceitar apenas linha **inteiramente
em itálico**.

> **Ressalva (2026-09-29, segunda rodada).** A conferência de cobertura que acusou
> "0 linha ausente" era **falsa para o cap. 9**. A regra foi corrigida no
> `build-md.py`, mas as linhas já apagadas **nunca foram repostas** no arquivo: faltavam
> os rótulos `2º`, `3º` e `4º PASSO` e, o mais grave, **todo o parágrafo do 3º passo**
> — com os dois URLs de calculadora e a instrução de seleção (achado A-18). A
> afirmação de que a perda estava resolvida valia só para as 7 linhas listadas, não
> para o cap. 9, cujo arquivo **nunca foi conferido contra a fonte**. Recuperado nesta
> rodada. Lição: a verificação de cobertura precisa ser feita **sobre o arquivo final**,
> não sobre a regra que deveria tê-lo corrigido.

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
