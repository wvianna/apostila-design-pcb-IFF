# Figuras

## Preservar primeiro

Figuras, imagens, diagramas, capturas de tela e ilustrações **existentes na
apostila devem ser reaproveitadas sempre que possível**. Não substitua uma figura
existente apenas porque uma nova poderia parecer mais bonita.

Antes de substituir, verifique:

- [ ] qual é a função didática da figura;
- [ ] a qualidade é suficiente (legível na versão renderizada/impressa);
- [ ] o conteúdo continua tecnicamente correto;
- [ ] a figura continua correspondendo ao texto que ela explica.

Se os quatro pontos estiverem atendidos, **preserve**.

## Quando substituir

Apenas se a figura estiver desatualizada, incorreta, insuficiente ou ilegível.
Nesses casos, atualize, complemente, substitua ou redesenhe — e registre o motivo
da troca. Preserve, sempre que possível, a relação entre a figura e o texto que
ela explica (posição, legenda, chamada no texto).

## Criar figuras novas

É permitido inserir figuras que ajudem a explicar: stackup, retorno de corrente,
roteamento, posicionamento, comparação de layouts, vias, planos, EMI/EMC, fluxo
de fabricação, diagramas de processo, fluxogramas e esquemas explicativos.

Regras:

- função didática clara;
- nada inserido para preencher espaço;
- se um conceito é melhor explicado visualmente do que em texto, considere criar
  o diagrama.

## Convenções obrigatórias

- Toda figura precisa de legenda, numeração e referência (chamada) no texto.
- Crédito de figura de terceiro fora da legenda, se o sistema da obra separar
  crédito de legenda — siga o padrão já usado no material.
- Mantenha a macro/comando de figura que a obra já define. Não invente macro
  nova.
- Ao renumerar, propague para índice/lista de figuras e para todas as chamadas.

## Extração de figuras de PDF de origem

Quando a apostila reaproveita figuras de apostilas antigas ou de PDFs do
repositório, a receita abaixo funcionou em sessão anterior neste repositório —
**revalide os caminhos antes de usar**:

1. Posição exata da imagem na página:
   `mutool trace "arq.pdf" PAGINA | grep fill_image`
   → `transform="a 0 -0 d e f"` dá a caixa; figura em `x = e .. e+a`,
   `y = f .. f+d` (y medido do topo; `d` negativo = imagem espelhada).
2. Recorte: `pdftoppm -r 300 -png -f P -l P <pdf> <prefixo>` e recorte a faixa de
   tinta (pixels < 245) com `getbbox()` para aparar margens. Funciona para
   vetorial e raster.

Armadilhas verificadas:

- `pdfimages` **não resolve sozinho**: perde figuras vetoriais e devolve
  espelhada a imagem cuja matriz tem `d` negativo.
- A ordem de `pdfimages` por página é a ordem de leitura, mas não dá posição.
- Faixa de tinta ≠ figura quando a figura contém texto real fragmentado: filtrar
  por "tinta fora das caixas de texto", não por "fração coberta".
- Ao apagar legenda sobreposta por palavra-chave, restrinja a busca à faixa `y` da
  figura — senão a palavra no corpo do texto casa primeiro e o apagamento sai no
  lugar errado.
- Pare o recorte antes da linha de legenda, senão o topo dos glifos entra no
  quadro.
- `pdftotext -bbox` devolve `<word>`: ao agrupar em linhas, ordene por
  (yMin, xMin) — ordenar só por y embaralha títulos.

## Diagramas (Mermaid ou similar)

Se a obra usar Mermaid, valide o diagrama antes de commitar — o parser falha por
detalhes pequenos:

- parênteses em rótulo de nó de `flowchart`/`graph` quebram o parse
  (`B[MQTT Broker (Mosquitto)]` falha). Aspire: `B["MQTT Broker (Mosquitto)"]`.
- id de nó/participante que colida com palavra reservada quebra o parse, e a
  colisão é case-insensitive (`LOOP` é lido como `loop`, `OPT` como `opt`).
  Renomeie.
- fan-out largo estoura a proporção da figura. Cadeia vertical de decisão rende
  proporção melhor que um nó abrindo várias colunas.
- em cadeia linear, aumentar o texto do rótulo **não** melhora a proporção: o
  renderizador quebra o texto e mantém a largura. Reduza o número de nós.

Se a figura não puder ser validada, não a publique como se estivesse correta.
