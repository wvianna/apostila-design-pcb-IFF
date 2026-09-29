# Fontes, verificação e valores numéricos

## Ordem de prioridade

### Prioridade 1 — Materiais do workspace

Antes de produzir ou modificar conteúdo, examine os materiais relevantes já
disponíveis. Eles são a base documental principal: apostila, PDFs, documentos,
apresentações, notas técnicas, projetos, esquemáticos, arquivos de PCB, imagens,
diagramas, referências bibliográficas, exemplos, documentação de EDA, normas e
manuais.

Não ignore informação relevante já existente no workspace — verifique se a
resposta já está no material antes de buscar fora.

### Prioridade 2 — Fontes técnicas externas

Quando precisar complementar, corrigir ou atualizar, consulte na ordem:

1. documentação oficial de fabricantes;
2. documentação oficial de ferramentas EDA;
3. normas e organismos técnicos;
4. fabricantes de componentes;
5. fabricantes de materiais e processos de PCB;
6. universidades e instituições técnicas;
7. artigos técnicos e publicações reconhecidas;
8. outras fontes técnicas confiáveis.

Blogs, fóruns e conteúdo sem autoria clara não são fonte técnica primária.
Podem, no máximo, indicar onde procurar a fonte real.

## Registro de fonte

Toda informação externa incorporada precisa de registro. Formato mínimo:

```text
[fonte: <organização/autor>, "<documento>", <versão ou data>, <seção/página>]
```

Registre também a data de consulta quando a informação for volátil (parâmetro de
processo, capacidade de fabricante, versão de ferramenta).

## Nível de autoridade da afirmação

Diferencie sempre no texto:

| Nível | Como escrever | Exemplo de redação |
|---|---|---|
| Norma / padrão | cite identificação e aplicabilidade | "a IPC-2221 estabelece..." |
| Recomendação de fabricante | atribua ao fabricante | "a <fabricante>, em seu guia de DFM, recomenda..." |
| Prática de engenharia consagrada | apresente como prática, não regra | "na prática, costuma-se..." |
| Decisão da própria obra | assuma como escolha didática | "nesta apostila adotamos..." |

Nunca transforme boa prática em obrigação, nem omita a origem de uma
recomendação de fabricante.

## Valores numéricos

Tenha cuidado especial com: largura de trilha, espessura de cobre, espaçamento e
clearance, diâmetro de via, annular ring, corrente, capacidade térmica,
impedância, tolerâncias, dimensões.

Regras:

1. **Nunca cite número sem origem.** Fonte ou `[VERIFICAR]`.
2. **Número isolado quase sempre está errado.** Todo valor depende de contexto —
   declare as condições junto do número.
3. **Não herde número da memória do modelo** nem de versão anterior do texto sem
   conferir.

Contexto que precisa acompanhar cada valor:

| Valor | Depende de |
|---|---|
| Largura de trilha | corrente, elevação de temperatura admissível, espessura de cobre, camada externa/interna |
| Espessura de cobre | processo de fabricação, classe/nível de acabamento, orçamento |
| Clearance / espaçamento | tensão de operação, classe de produto, ambiente, aplicabilidade da norma |
| Diâmetro de via e annular ring | corrente, número de camadas, relação de aspecto do fabricante, classe |
| Impedância | stackup, espessura do dielétrico, largura da trilha, constante dielétrica do material |
| Corrente | seção de cobre, caminho térmico, tempo/regime de sobrecarga |

Nunca apresente um número como universal quando ele é específico de um stackup,
de um fabricante ou de uma classe de produto.

## Política `[VERIFICAR]`

Use quando a informação não pôde ser confirmada com as fontes disponíveis.

- Redija de forma acionável:
  `[VERIFICAR: <o que falta>, <onde provavelmente encontrar>]`.
- Não use `[VERIFICAR]` como desculpa para deixar afirmação central sem
  tratamento: se o trecho é central para o capítulo, busque a fonte antes de
  fechar a tarefa.
- Liste todos os `[VERIFICAR]` remanescentes no relatório final.
- Nunca remova um `[VERIFICAR]` sem ter resolvido a verificação.

## Inventário local (verificado em 2026-09-29)

Fontes de prioridade 1 presentes neste repositório:

- `docs/memorial.md` — especificação desta skill.
- `docs/kicad.pdf`, `docs/materialApoioKicad_Optativa_R9.pdf`,
  `docs/Exportar-JLCPCB.pdf` — material de apoio e de fluxo JLCPCB.
- `livros/` — guias técnicos em PDF: KiCad Design Guide, High-Speed PCB Design
  Guide, Controlled Impedance Design Guide, Signal Integrity eBook,
  Differential Pairs in PCB Transmission Lines, DFM Handbook, DFA Handbook,
  IPC Class 3 Design Guide.
- `docs/agentic/` — protocolo de trabalho dos agentes deste repositório.

Antes de citar qualquer um desses PDFs, abra a primeira página e confirme
autoria, edição e data — guias de fornecedor são **recomendação de fabricante**,
não norma.

O texto da apostila em si pode estar em `apostila/`, `docs/apostila/` ou ainda
não existir neste workspace. Confirme com uma listagem antes de assumir caminho.

Ferramentas úteis para trabalhar com PDF (confirme disponibilidade com
`command -v` antes de usar): `pdftotext`, `pdftoppm`, `mutool`, `pdfimages`,
`pdftocairo`.
