# Skill: Refatoração Técnica de Apostila de Design de PCB

## 1. Finalidade

Criar uma skill especializada **exclusivamente na refatoração, atualização, organização e aprimoramento técnico de uma apostila sobre projeto e design de placas de circuito impresso (PCB — Printed Circuit Board)**.

A skill deverá trabalhar prioritariamente sobre os materiais existentes no **workspace atual**, utilizando-os como fonte principal de referência.

O objetivo não é simplesmente reescrever a apostila, mas produzir uma versão **tecnicamente mais correta, didática, atualizada, coerente, organizada e adequada ao ensino de projeto de PCB**.

---

## 2. Escopo obrigatório

A skill deve atuar somente em tarefas relacionadas à apostila de:

* projeto de PCB;
* design de placas de circuito impresso;
* captura de esquemáticos;
* seleção e associação de footprints;
* posicionamento de componentes;
* definição de stackup;
* regras de projeto (DRC);
* roteamento;
* planos e zonas de cobre;
* alimentação e distribuição de potência;
* sinais digitais;
* sinais analógicos;
* integridade de sinal;
* retorno de corrente;
* EMI/EMC;
* aterramento;
* desacoplamento;
* vias;
* componentes SMD e THT;
* fabricação de PCB;
* DFM/DFA;
* montagem;
* inspeção e testes;
* documentação de fabricação;
* gerbers, drill files e arquivos relacionados;
* boas práticas de layout;
* ferramentas de EDA, quando pertinentes ao conteúdo da apostila.

Não transformar a skill em uma skill genérica de eletrônica.

O foco deve permanecer sempre na **refatoração da apostila de PCB**.

---

## 3. Fontes de informação e prioridade

Utilize as fontes na seguinte ordem de prioridade:

### Prioridade 1 — Materiais existentes no workspace

Antes de produzir ou modificar conteúdo, examine os materiais relevantes disponíveis no workspace.

Esses materiais constituem a principal base documental da refatoração.

Utilize, quando disponíveis:

* apostilas;
* PDFs;
* documentos;
* apresentações;
* notas técnicas;
* projetos;
* esquemáticos;
* arquivos de PCB;
* imagens;
* diagramas;
* referências bibliográficas;
* exemplos de projetos;
* documentação de ferramentas EDA;
* normas e manuais existentes no workspace.

Não ignore informações relevantes já existentes no workspace.

### Prioridade 2 — Fontes técnicas externas

Quando houver necessidade de complementar, corrigir ou atualizar o conteúdo, podem ser realizadas consultas na Internet.

Priorize:

1. documentação oficial de fabricantes;
2. documentação oficial de ferramentas EDA;
3. normas e organismos técnicos;
4. fabricantes de componentes;
5. fabricantes de materiais e processos de PCB;
6. universidades e instituições técnicas;
7. artigos técnicos e publicações reconhecidas;
8. outras fontes técnicas confiáveis.

Sempre que uma informação externa for incorporada ao material, registre a fonte utilizada.

Não trate blogs, fóruns ou conteúdo sem autoria clara como fonte técnica primária.

---

## 4. Regra fundamental contra alucinação

**NÃO INVENTE INFORMAÇÕES.**

Quando uma informação não puder ser confirmada:

* não apresente como fato;
* não invente valores;
* não invente normas;
* não invente referências;
* não invente características de componentes;
* não invente capacidades de processos de fabricação;
* não invente recomendações atribuídas a fabricantes;
* não invente resultados de simulação;
* não invente figuras;
* não invente citações.

Se houver dúvida técnica relevante, procure uma fonte confiável.

Se ainda assim não for possível confirmar a informação, marque explicitamente a questão como:

> **[VERIFICAR]**

ou explique que a informação não pôde ser confirmada.

É preferível deixar uma lacuna identificada a preencher a apostila com informação possivelmente incorreta.

---

## 5. Preservação do conteúdo original

A refatoração não deve destruir indiscriminadamente o conteúdo existente.

Para cada seção da apostila:

1. identifique o conteúdo original;
2. avalie sua relevância;
3. identifique erros ou inconsistências;
4. identifique conteúdo desatualizado;
5. identifique informações incompletas;
6. reorganize quando necessário;
7. preserve o que estiver tecnicamente correto e didaticamente útil;
8. complemente somente quando houver justificativa técnica.

Evite reescrever simplesmente por preferência estilística.

A alteração deve possuir uma razão clara:

* correção técnica;
* atualização;
* melhoria didática;
* eliminação de redundância;
* melhoria da organização;
* melhoria da precisão;
* inclusão de informação importante;
* adequação ao fluxo pedagógico.

---

## 6. Figuras e imagens existentes

As **figuras, imagens, diagramas, capturas de tela e ilustrações existentes na apostila indicada devem ser reaproveitadas sempre que possível**.

Não substituir uma figura existente apenas porque uma nova figura poderia parecer mais bonita.

Antes de substituir uma imagem:

* verifique sua função didática;
* avalie sua qualidade;
* verifique se seu conteúdo ainda está correto;
* preserve-a caso continue adequada.

Quando a figura estiver tecnicamente desatualizada, incorreta ou insuficiente, ela poderá ser:

* atualizada;
* complementada;
* substituída;
* redesenhada.

Sempre que possível, preserve a relação entre a figura e o conteúdo que ela explica.

---

## 7. Novas figuras e diagramas

É permitido inserir:

* diagramas;
* fluxogramas;
* esquemas explicativos;
* ilustrações;
* diagramas de stackup;
* diagramas de retorno de corrente;
* exemplos de roteamento;
* exemplos de posicionamento;
* comparações de layouts;
* diagramas de vias;
* representações de planos;
* diagramas de EMI/EMC;
* fluxos de fabricação;
* diagramas de processos;
* figuras técnicas adicionais.

As novas figuras devem possuir **função didática clara**.

Não inserir imagens apenas para preencher espaço.

Sempre que um conceito puder ser explicado melhor visualmente, considere a criação de um diagrama.

---

## 8. Atualização técnica

A apostila deve ser avaliada quanto à atualidade das técnicas apresentadas.

Quando pertinente, verificar e incorporar conceitos modernos relacionados a:

* HDI;
* microvias;
* vias empilhadas e escalonadas;
* componentes BGA;
* montagem SMD moderna;
* impedância controlada;
* pares diferenciais;
* sinais de alta velocidade;
* USB;
* Ethernet;
* DDR;
* RF, quando aplicável;
* power integrity;
* signal integrity;
* EMI/EMC;
* controlled impedance;
* thermal management;
* DFM;
* DFA;
* testes de fabricação;
* automação de projeto;
* ferramentas EDA atuais;
* bibliotecas de componentes;
* gerenciamento de footprints;
* regras automatizadas de projeto.

Não inserir uma tecnologia apenas por ser moderna.

Ela deve ser relevante para o nível e objetivo da apostila.

---

## 9. Normas e padrões

Quando a apostila fizer referência a normas, padrões ou recomendações técnicas:

* confirme a existência da norma;
* confirme sua identificação;
* confirme sua aplicabilidade;
* evite afirmar que uma recomendação é "obrigatória" quando ela é apenas uma boa prática;
* diferencie claramente norma, recomendação de fabricante e prática de engenharia.

Não invente números ou títulos de normas.

Quando houver acesso à fonte original, utilize-a preferencialmente.

---

## 10. Valores numéricos

Tenha cuidado especial com:

* largura de trilhas;
* espessura de cobre;
* espaçamentos;
* diâmetro de vias;
* annular ring;
* corrente;
* capacidade térmica;
* impedância;
* tolerâncias;
* dimensões;
* clearance;

