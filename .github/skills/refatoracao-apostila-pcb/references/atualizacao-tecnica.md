# Atualização técnica

Avalie se o conteúdo apresentado ainda representa o estado da prática. Não
insira tecnologia apenas por ser moderna: ela precisa ser relevante para o nível
e o objetivo da apostila.

## Temas a considerar

| Tema | O que verificar no texto |
|---|---|
| HDI e microvias | se o material trata densidade de interconexão; se microvia aparece como caso particular de via, com limitações de fabricação |
| Vias empilhadas / escalonadas | se o texto diferencia os arranjos e explica quando cada um é usado |
| BGA | se há orientação de fanout, escape routing, desacoplamento sob o encapsulamento |
| Montagem SMD moderna | se paste stencil, reflow, tombamento, DFM de montagem estão coerentes |
| Impedância controlada | se stackup, cálculo e comunicação com o fabricante estão ligados |
| Pares diferenciais | se comprimento, skew, espaçamento e referência contínua aparecem juntos |
| Alta velocidade (USB, Ethernet, DDR) | se as regras citadas são específicas da interface e não genéricas |
| Signal integrity | se integridade é tratada por retorno de corrente e referência, não só por "trilha curta" |
| Power integrity | se distribuição de potência e desacoplamento aparecem como sistema, não como lista de capacitores |
| EMI/EMC | se o texto liga layout, loop de corrente e plano de referência |
| Aterramento | se as topologias são apresentadas com critério de escolha, sem dogmatismo |
| Gestão térmica | se cobre, vias térmicas, plano e dissipação estão conectados ao layout |
| DFM / DFA | se as regras são rastreáveis às capacidades de processo e não a números soltos |
| Testes de fabricação | se inspeção, teste elétrico e pontos de teste aparecem no fluxo |
| EDA atual | se o fluxo descrito corresponde às versões usadas pela obra; se comandos/menus citados existem |
| Bibliotecas e footprints | se há orientação de verificação de footprint contra datasheet |
| Regras automatizadas | se DRC/ERC por regra é ensinado como verificação, não como formalidade |

## Critério de relevância

Antes de incluir um tema, responda:

1. O público-alvo da apostila precisa dele para executar o que a obra ensina?
2. Existe pré-requisito já apresentado no texto — ou o tema abriria um buraco
   pedagógico?
3. O tema se conecta a algum capítulo existente, ou ficaria isolado?
4. A obra tem exemplo/projeto onde o tema se aplica?

Se a resposta for "não" na maioria, **omita** — ou registre no relatório que o
tema foi considerado e recusado, com o motivo. Registro de recusa é evidência de
auditoria; inserção de conteúdo decorativo não é.

## Regras

- Confirme nome e versão da tecnologia antes de citar (interface, barramento,
  classe, especificação). Nome aproximado é erro técnico.
- Ao atualizar, preserve o exemplo existente: adapte o exemplo da obra ao
  conceito novo em vez de substituí-lo por exemplo ilustrativo genérico.
- Se a tecnologia exigir revisão de stackup, norma ou capacidade de fabricação
  já afirmada no texto, trate as duas alterações juntas para não deixar o
  capítulo internamente inconsistente.
- Não presuma que "mais recente" significa "aplicável": verifique se o processo
  é acessível ao público da obra (custo, prototipagem, fabricantes acessíveis).
