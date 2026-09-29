---
name: refatoracao-apostila-pcb
description: 'Refatora, corrige, atualiza e reorganiza apostila de projeto e design de PCB (KiCad e afins). Use para revisar capítulo de apostila de PCB, corrigir erro técnico de layout, roteamento, stackup, DRC, aterramento, EMI/EMC, DFM/DFA, auditar coerência didática, atualizar conteúdo desatualizado (HDI, microvias, BGA, impedância controlada, pares diferenciais, alta velocidade), preservar ou substituir figuras, verificar norma IPC e conferir valores numéricos (trilha, clearance, via, annular ring, impedância, corrente).'
argument-hint: 'Arquivo/seção da apostila + objetivo: corrigir, atualizar, reorganizar ou revisar.'
---

# Refatoração Técnica de Apostila de Design de PCB

Skill para auditar, corrigir, atualizar, reorganizar e complementar uma apostila
de projeto e design de PCB, atuando como engenheiro de PCB, revisor técnico e
editor didático. A fonte primária é o próprio material do workspace.

Especificação de origem: `docs/memorial.md`. Se o memorial mudar, reconcilie esta
skill com ele — em caso de conflito, o memorial atualizado prevalece.

## Quando usar

- Revisar/corrigir capítulo, seção ou figura da apostila de PCB.
- Atualizar conteúdo técnico desatualizado ou complementar lacuna.
- Criar seção/capítulo que falta, como complemento ao material existente.
- Reorganizar a ordem didática, consolidar redundância, ajustar figuras.
- Conferir norma, valor numérico ou afirmação técnica do texto.
- Auditar coerência entre texto, figuras, exercícios e índice.

## Quando NÃO usar

- Projetar um PCB real, escrever firmware ou revisar código de outro domínio.
- Eletrônica genérica que não seja conteúdo da apostila.
- Produzir obra nova sem material de base (ver `./references/escopo-e-limites.md`).

Teste de pertinência: *a alteração muda texto, figura, exercício ou estrutura da
apostila de PCB?* Se não, não é esta skill.

## Regra zero — não inventar

Nunca apresente como fato algo que não foi confirmado: valores, normas,
características de componente, capacidade de processo de fabricação,
recomendação atribuída a fabricante, resultado de simulação, figura, citação.

Quando não confirmar, marque inline: `[VERIFICAR: <o que falta e onde buscar>]`.
É preferível uma lacuna sinalizada a um texto possivelmente incorreto.
Detalhes em `./references/fontes-verificacao-e-numeros.md`.

## Procedimento

### F0 — Enquadrar (sem editar)

1. **Localizar o alvo**: arquivo + seções exatas. A fonte de verdade do texto é
   `apostila/*.md` (capítulos) e `apostila/indice.md` (capa e Apresentação);
   HTML e LaTeX são gerados. Não refatore a apostila inteira sem que isso tenha
   sido pedido. Se o alvo não existir no workspace, diga isso em vez de supor um
   caminho.
2. **Inventariar fontes de prioridade 1** realmente disponíveis (a própria
   apostila, PDFs técnicos do repositório, materiais de apoio, projetos/exemplos).
   Não leia fontes que não servirão ao alvo.
3. **Estado do workspace**: `git status --short` e `git diff`. Alterações
   pré-existentes não pertencem a esta tarefa — não reverta nem misture.
4. **Declarar** em 3–5 linhas: escopo, fora de escopo, gate da tarefa.
5. Se o alvo envolver número normativo, norma ou processo de fabricação, reserve
   etapa de verificação em fonte externa antes de escrever.

### F1 — Auditar por seção

Classifique cada trecho relevante **antes** de editar:

| Classe | Significado | Ação |
|---|---|---|
| OK | correto e didaticamente útil | preservar |
| CORRIGIR | erro técnico factual | corrigir com fonte |
| DESATUALIZAR | técnica superada no contexto da obra | atualizar ou sinalizar |
| INCOMPLETO | falta informação essencial ao entendimento | complementar |
| REDUNDANTE | repete outra seção | consolidar |
| DESLOCADO | está fora do ponto do fluxo pedagógico | mover |
| REMOVER | incorreto sem correção viável, ou fora do escopo | remover e registrar |
| VERIFICAR | não confirmável com as fontes atuais | marcar `[VERIFICAR]` |

Entregue a tabela de achados antes (ou junto) do plano de edição:

```text
# | Seção | Classe | Achado | Fonte/evidência | Ação proposta
```

### F2 — Verificar e registrar fonte

1. Ordem de prioridade: materiais do workspace → fontes técnicas externas
   (documentação de fabricante/EDA, normas, fabricantes de componente/material,
   universidade, artigo reconhecido).
2. Registre a fonte de toda informação externa incorporada: autor/organização,
   documento, versão/data, localização (página/seção).
3. Diferencie explicitamente **norma**, **recomendação de fabricante** e
   **prática de engenharia**. Nunca promova boa prática a obrigação.
4. Todo número precisa de fonte ou `[VERIFICAR]`. Não cite valor "de memória".

### F3 — Editar o mínimo suficiente

- Cada alteração tem **uma** razão declarada: correção técnica, atualização,
  melhoria didática, redundância, organização, precisão, inclusão de informação
  importante ou adequação ao fluxo pedagógico.
- Nada de reescrita por preferência estilística.
- Preserve o que está correto: exemplos, projetos, esquemáticos, voz do material.
- Ao mudar conteúdo, propague: índice/sumário, numeração de figuras e tabelas,
  chamadas no texto, referências cruzadas, exercícios dependentes.
- Criar seção nova é permitido quando a F1 apontou lacuna e há material de base
  para sustentá-la. Não é produção de obra nova.
- Não refatore conteúdo fora do alvo.

### F4 — Figuras

- Reaproveite a figura existente sempre que ela ainda for adequada; substitua
  apenas com justificativa (desatualizada, incorreta, insuficiente, ilegível).
- Antes de substituir, confira: função didática, qualidade, correção do conteúdo
  e correspondência com o texto que ela explica.
- Figura nova só com função didática clara. Nada decorativo.
- Toda figura precisa de legenda, numeração, referência no texto e crédito de
  fonte de terceiro quando aplicável.
- Detalhes e receita de extração de figuras: `./references/figuras.md`.

### F5 — Verificar e fechar

1. Renderize/compile o alvo afetado seguindo `./references/pipeline-apostila.md`
   e confira que não surgiram erros nem avisos novos.
2. Releia as seções alteradas **na versão renderizada** (HTML e PDF), não só o
   markdown — é onde sumário e numeração quebram.
3. Confira índice/sumário, numeração de figuras e tabelas, e chamadas no texto.
4. Aplique o gate abaixo.
5. Relate: o que mudou e por quê, fontes usadas, `[VERIFICAR]` remanescentes e
   risco residual.

## Gate de conclusão

Este é o DoD da apostila. Ele é independente de
`docs/agentic/DEFINITION-OF-DONE.md` (que governa firmware/SDD) e não o
substitui.

- [ ] Escopo e fora de escopo declarados; alvo identificado por seção.
- [ ] Tabela de achados da F1 emitida.
- [ ] Toda alteração tem razão explícita e não cosmética.
- [ ] Todo valor numérico tem fonte ou `[VERIFICAR]`.
- [ ] Norma citada teve existência, identificação e aplicabilidade confirmadas.
- [ ] Norma/recomendação/prática estão diferenciadas no texto.
- [ ] Nenhuma figura adequada foi descartada; figuras novas têm papel didático e
      chamada no texto.
- [ ] Índice, numeração e referências cruzadas consistentes.
- [ ] HTML e PDF renderizam limpos (0 erros LaTeX, 0 `Overfull`) — ou o estado é
      declarado `PENDENTE`.
- [ ] Fontes externas registradas; `[VERIFICAR]` remanescentes listados.
- [ ] Nada foi declarado validado sem evidência.

## Anti-padrões

- Reescrever para "ficar melhor" sem razão técnica ou didática.
- Inserir tecnologia moderna irrelevante ao nível/objetivo da obra.
- Inventar número, norma, citação, figura ou capacidade de fabricante.
- Trocar figura boa por figura mais bonita.
- Declarar concluído sem renderizar/compilar o alvo.
- Diluir "obrigatório" onde a fonte diz "recomendado".
- Aproveitar a tarefa para refatorar o que não foi pedido.

## Recursos

- `./references/escopo-e-limites.md` — o que a skill cobre, o que não cobre e
  como tratar pedidos na fronteira.
- `./references/fontes-verificacao-e-numeros.md` — hierarquia de fontes, registro
  de fonte, normas, valores numéricos críticos, política `[VERIFICAR]`,
  inventário das fontes locais.
- `./references/atualizacao-tecnica.md` — temas modernos e critério de relevância
  para decidir incluir, citar ou omitir.
- `./references/pipeline-apostila.md` — fonte de verdade, build rápido, gate de
  render (HTML/PDF) e armadilhas do pipeline.
- `./references/figuras.md` — preservação, substituição, criação de figuras,
  extração de figuras de PDF e armadilhas de diagramas.
