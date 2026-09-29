# Escopo e limites

## Coberto

- **Esquemático e bibliotecas**: captura de esquemático, símbolos, seleção e
  associação de footprints, BOM, bibliotecas de componentes, gerenciamento de
  footprints.
- **Mecânica e stackup**: posicionamento de componentes, stackup, número de
  camadas, espessura de cobre, dimensões, tolerâncias.
- **Regras e verificação**: DRC/ERC, clearance, annular ring, regras
  automatizadas de projeto, DFM, DFA.
- **Roteamento**: trilhas, vias (incluindo microvias, empilhadas, escalonadas),
  planos e zonas de cobre, retorno de corrente, impedância controlada, pares
  diferenciais, sinais de alta velocidade.
- **Energia e integridade**: distribuição de potência, alimentação, desacoplamento,
  power integrity, signal integrity, gestão térmica, aterramento.
- **Sinais**: digitais, analógicos, RF quando aplicável ao conteúdo.
- **EMI/EMC**: emissão, suscetibilidade, boas práticas de layout e referência.
- **Componentes**: SMD e THT, incluindo BGA e montagem SMD moderna.
- **Fabricação e montagem**: gerbers, drill files, documentação de fabricação,
  montagem, inspeção e testes de fabricação.
- **Prática de layout**: boas práticas, comparações de layout, exercícios.
- **Ferramentas de EDA** quando pertinentes ao conteúdo da apostila (KiCad e
  outras) — sempre a serviço de ensinar projeto de PCB, não como manual da
  ferramenta.

## Fora de escopo

- Projetar, revisar ou fabricar um PCB real (a skill atua sobre o texto da
  apostila).
- Firmware, software embarcado ou código de aplicação.
- Eletrônica genérica: teoria de circuitos, análise de componentes, projeto
  eletrônico que não seja conteúdo da apostila.
- Manual de uso de ferramenta EDA sem relação com o ensino de PCB da obra.
- Áreas de outra apostila/domínio no mesmo repositório.

A skill não deve se transformar em uma skill genérica de eletrônica.

## Fronteiras de decisão

| Pedido | Como tratar |
|---|---|
| "Corrija/atualize/reorganize esta seção" | Núcleo da skill. |
| "Avalie este capítulo" | Auditar (F1) e entregar tabela de achados, sem editar. |
| "Crie o capítulo que falta sobre X" | Permitido **como complemento** ao material existente, com o mesmo rigor de fontes. |
| "Escreva uma apostila de PCB do zero" | Sem material de base, é produção original — avise que sai do escopo de refatoração e que toda afirmação passará a depender de fonte externa. |
| "Melhore o estilo da introdução" | Fora do escopo se não houver razão técnica/didática. Ofereça auditar o conteúdo. |
| "Verifique se este valor está certo" | Dentro: aplicar `fontes-verificacao-e-numeros.md`. |

## Preservação do conteúdo original

A refatoração não destrói indiscriminadamente. Para cada seção: identifique o
conteúdo original → avalie relevância → aponte erros, desatualização e lacunas →
reorganize se necessário → preserve o que estiver correto e útil → complemente
somente com justificativa técnica.

Toda alteração deve ter uma razão clara: correção técnica, atualização, melhoria
didática, eliminação de redundância, melhoria de organização, melhoria de
precisão, inclusão de informação importante ou adequação ao fluxo pedagógico.

## Rastreabilidade

- Mantenha o estilo de referência já usado pela obra para capítulos, figuras e
  exercícios.
- Se o repositório usar artefatos de especificação (`FR-###`, `NFR-###`,
  `CA-###`, `T-###`), relacione a mudança ao identificador correspondente em vez
  de criar numeração nova.
- Mudança de comportamento/conteúdo exige atualizar o artefato de especificação
  que descreve o material, não apenas o texto.
- Não criar artefato vazio só para cumprir estrutura.
