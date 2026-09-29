# Introdução

Os avanços tecnológicos frequentemente dependem de PCBs bem projetadas, capazes de garantir desempenho, eficiência e confiabilidade. Seja para aplicações acadêmicas, profissionais ou projetos pessoais, dominar o design de PCBs tornou-se uma habilidade indispensável para inovadores no campo da eletrônica.

## O que é uma PCB?

Uma PCB, ou placa de circuito impresso, é composta por um material isolante — geralmente fibra de vidro (FR4) — combinado com camadas de material condutor, como cobre, que possibilitam a interconexão dos componentes eletrônicos. Este design substitui os métodos antigos de fiação ponto a ponto, proporcionando maior confiabilidade, precisão e miniaturização.


# Princípios e elementos básicos das PCBs

As Placas de Circuito Impresso (PCBs) constituem elementos fundamentais no universo da eletrônica, projetadas para interconectar e sustentar componentes eletrônicos de forma organizada e funcional. Neste capítulo, serão apresentados os princípios que norteiam o funcionamento das PCBs, além de uma análise dos principais elementos que as compõem.

## Funções principais de uma PCB

- **Suporte físico**: Proporciona estrutura mecânica para fixação e posicionamento dos componentes eletrônicos.
- **Conexão elétrica**: Viabiliza a transmissão de sinais elétricos entre os componentes, por meio de trilhas condutoras.
- **Isolamento elétrico**: Mantém circuitos isolados, prevenindo curtos-circuitos e interferências indesejadas.
- **Dissipação térmica**: Facilita a transferência do calor gerado pelos componentes durante sua operação, contribuindo para a estabilidade térmica do sistema

## Principais elementos da PCB

A fabricação de Placas de Circuito Impresso (PCBs) depende diretamente da seleção criteriosa dos materiais constituintes, que são determinantes para a qualidade, confiabilidade e desempenho final da placa.

### Substrato

O substrato é a base estrutural das PCBs, servindo como suporte para a montagem dos componentes eletrônicos. O material mais comumente utilizado é a fibra de vidro (FR4), amplamente adotada por sua estabilidade térmica, alta resistência à decomposição e baixo custo. Em projetos que exigem alta frequência, materiais como PTFE (politetrafluoretileno) são preferidos devido à sua constante dielétrica mais baixa e perdas reduzidas, embora apresentem maior dificuldade de processamento. Em projetos de alta frequência, onde a constante dielétrica e baixas perdas são cruciais, placas à base de PTFE (politetrafluoretileno) podem ser utilizadas, embora sejam mais difíceis de processar. O substrato de fenolite também pode ser utilizado, mas as propriedades mecânicas são inferiores quando comparado com o FR4.

### Cobre

O cobre é um elemento essencial nas PCBs, utilizado para formar as trilhas condutoras que conectam os componentes eletrônicos. Essas trilhas, criadas a partir de placas revestidas com camadas de cobre, garantem a condução eficiente de sinais elétricos. Para projetos de dupla face ou multicamadas, a aderência do cobre ao substrato, especialmente ao FR4, é uma característica crucial para a durabilidade e desempenho do circuito. As placas de cobre revestidas são obtidas a partir do substrato (geralmente FR4) com uma camada de cobre aderida, geralmente em ambos os lados (dupla face). A aderência do cobre ao FR4 é bastante sólida, enquanto a aderência ao PTFE pode ser mais desafiadora.

### Máscara de solda

A máscara de solda é uma camada de polímero aplicada sobre as áreas expostas de cobre nas PCBs, com a função de proteger contra oxidação, prevenir curtos-circuitos e facilitar o processo de soldagem. Disponível em várias cores, como verde, vermelho e azul, essa camada contribui para a durabilidade e confiabilidade da placa, ao mesmo tempo que oferece um acabamento estético. A máscara de solda geralmente é composta por uma camada de polímero e apresenta cores como verde escuro, vermelho, azul, preto, branco ou outra cor disponível no fabricante.

![Figura 1: Exemplos de PCBs](figuras/figura-01.png)


### Camada de serigrafia

A camada de serigrafia é composta por tinta aplicada na superfície da PCB, destinada a fornecer informações úteis, como identificação de componentes, orientações de montagem e dados de fabricação. Essa camada desempenha um papel crucial na montagem e manutenção de dispositivos eletrônicos, facilitando a localização precisa de componentes e contribuindo para uma montagem eficiente e com menor probabilidade de erros.

Ao compreender os principais elementos das Placas de Circuito Impresso e suas funções, é possível garantir que o processo de fabricação de PCBs resulte em produtos de alta qualidade, atendendo às demandas específicas de cada projeto eletrônico.

![Figura 2: Exemplos de serigrafias](figuras/figura-02.png)


### Acabamento de superfície

Surface finish, ou Acabamento de Superfície, compõe uma interface crítica entre os componentes e o local onde serão posicionados para solda, também chamada de SMOBC (Solder Mask Over Bare Copper) – Máscara de solda sobre cobre exposto. Essa superfície, sem nenhum tratamento, ficaria com os pads de cobre expostos, o que resultaria em oxidação, deterioração e consequente perda de funcionalidade.

O acabamento de superfície possui essencialmente duas funções:

- Proteger o circuito de cobre exposto;
- Prover uma superfície com maior solderabilidade, bem como reforçar o processo de montagem, promovendo uma junta de solda confiável com alto desempenho da PCB a longo prazo. O processo de acabamento superficial consiste em cobrir com metal o material
orgânico os elementos de cobre não cobertos pela máscara de solda. Este processo protege o cobre e facilita a soldagem dos componentes seja pelo processo manual, forno ou outra técnica.

As técnicas mais comuns para realizar o acabamento superficial são:

- **HASL/HASL Lead free (Hot Air Solder Level)**

![Figura 3: Hot Air Solder Level-A](figuras/figura-03.png)



![Figura 4: Hot Air Solder Level-B](figuras/figura-04.png)



- **Imersão em Estanho**

![Figura 5: Imersão em Estanho-A](figuras/figura-05.png)



![Figura 6: Imersão em Estanho-B](figuras/figura-06.png)



- **Imersão em Prata**

![Figura 7: Imersão em Prata-A](figuras/figura-07.png)



![Figura 8: Imersão em Prata-B](figuras/figura-08.png)



- **OSP (Organic Solderability Preservative)**

![Figura 9: Organic Solderability Preservative-A](figuras/figura-09.png)



![Figura 10: Organic Solderability Preservative-B](figuras/figura-10.png)



- **GOLD – ENIG (Electroless Nickel Immersion Gold)**

![Figura 11: Electroless Nickel Immersion Gold) - A](figuras/figura-11.png)



![Figura 12: Electroless Nickel Immersion Gold) - B](figuras/figura-12.png)



•*Immersion Gold) - B*

*Immersion Gold) - A*

#### ENEPIG (Electroless Nickel Electroless

#### Palladium Immersion Gold)

![Figura 13: Electroless Nickel Electroless Palladium Immersion Gold-A](figuras/figura-13.png)



![Figura 14: Electroless Nickel Electroless Palladium Immersion Gold-B](figuras/figura-14.png)



- **Gold – Hard Gold**

![Figura 15: Hard Gold-A](figuras/figura-15.png)



![Figura 16: Hard Gold-B](figuras/figura-16.png)



## Normas IPC

Uma placa que funciona na bancada não é automaticamente uma placa que pode ser fabricada em série. Para que projetista, fabricante e montador cheguem ao mesmo entendimento sobre o que é uma placa **aceitável**, a indústria eletrônica se apoia em normas — e a mais difundida delas é publicada pela **IPC**.

### O que é a IPC

A IPC é a associação global da indústria de interconexão eletrônica. O nome veio de *Institute for Printed Circuits* e depois foi alterado para *Institute for Interconnecting and Packaging Electronic Circuits*; hoje a sigla é usada como nome próprio da organização.

Trata-se de uma associação mantida por seus membros, que publica especificações de forma periódica. As normas IPC são as regras **mais amplamente aceitas** pela indústria eletrônica e cobrem todas as etapas do ciclo de desenvolvimento de um produto: projeto, compras, montagem, empacotamento e inspeção. Segui-las ajuda a fabricar placas seguras, confiáveis e de alta qualidade — e, para o projetista, produz um efeito prático imediato: **mantém projetista e fabricante no mesmo entendimento** sobre o que a placa precisa cumprir.

::: {.quadro tipo="nota" titulo="Por que isso importa no seu projeto"}
Uma norma não é uma formalidade. As classes IPC existem porque a **mesma** placa pode ser considerada aprovada ou reprovada dependendo do critério adotado. Ao especificar a classe, você deixa explícito qual nível de inspeção e qual tolerância a defeito são aceitáveis para o seu produto — e evita que cada lado julgue a placa por uma régua diferente.

:::

### As classes de qualidade

A **IPC-6011** descreve as classes de PCB e os **defeitos permitidos** em cada tipo de placa. São três classes, com o acréscimo posterior de uma quarta, definida pela **IPC-6012**:

| Classe | Aplicação típica | Confiabilidade exigida e defeitos admitidos |
|:---------|:-----------------------|:--------------------------------------------------------|
| **Classe 1** | Produtos eletrônicos de uso geral — controles remotos de TV, lâmpadas LED, brinquedos infantis | Vida útil limitada e função simples. Admite vários defeitos cosméticos, desde que não afetem o funcionamento; a confiabilidade não é fator crítico. É a placa mais barata de fabricar. |
| **Classe 2** | Produtos eletrônicos de serviço dedicado — notebooks, smartphones, tablets, equipamentos de comunicação | Confiabilidade maior e vida útil estendida; normas mais rigorosas que a classe 1, mas ainda se admitem algumas imperfeições cosméticas. O serviço ininterrupto é preferível, porém não crítico, e não há exposição a condições ambientais extremas. |
| **Classe 3** | Produtos eletrônicos de alto desempenho — suporte à vida, equipamentos militares, monitoramento eletrônico, automotivo | Deve fornecer desempenho contínuo, ou sob demanda, **sem parada** do equipamento; o ambiente de uso pode ser excepcionalmente severo. Exige níveis elevados de inspeção e ensaio, o que a torna altamente confiável. |
| **Classe 3/A** | Circuitos impressos de uso espacial e aviônica militar (IPC-6012) — aeroespacial, sistemas aéreos militares, sistemas de mísseis | Categoria mais alta para circuitos impressos. Critérios de fabricação muito rigorosos, pois a placa deve continuar operando em condições críticas. Consideravelmente mais cara, por precisar estar próxima da perfeição. |

A diferença central entre as classes **não está no desenho da placa, e sim no grau de inspeção**: são as classes que definem quais defeitos são admissíveis durante a fabricação.

Vale desfazer um equívoco comum: as classes 3 e 3/A são usadas principalmente em equipamentos militares e aeroespaciais, mas **não são exclusivas** dessas áreas. Elas podem ser aplicadas a qualquer produto — inclusive aos exemplos citados na classe 2 —, porém deixam de ser economicamente viáveis pelo esforço de fabricação e de inspeção que exigem.

### Como escolher a classe

Ao escolher a classe, o projetista está escolhendo a **vida útil** do produto. Muitas vezes a classe 2 atende a todos os requisitos e sai mais econômica. Se, além de a aplicação ser crítica, espera-se que a placa dure muitos anos, a classe 3 passa a ser a escolha adequada. O ambiente em que o produto vai operar também precisa entrar na conta, porque é ele que determina o grau de confiabilidade exigido do projeto.

::: {.quadro tipo="dica" titulo="Qual classe escolher"}
A escolha é econômica antes de ser técnica. A **classe 2** costuma atender à maior parte dos produtos — e sai mais barata. Reserve a **classe 3** para aplicações críticas ou para produtos que precisem durar muitos anos: o material de referência cita a fronteira de **15 anos** como um dos critérios de decisão. O ambiente de operação do produto é o outro critério a considerar.

:::

### Onde a IPC aparece na prática

Duas situações concretas em que a norma entra no dia a dia do projetista:

- **Anel anular:** a IPC define a posição dos furos sobre a ilha de solda (*pad*) e
  a largura do anel externo que resta depois da furação. Quando a ilha não circunda completamente o furo, tem-se um *annular ring breakout* — condição que a norma trata explicitamente, com limites de aceitação próprios para cada classe.
- **Juntas de solda e defeitos aceitáveis:** a IPC trata separadamente os defeitos
  que comprometem o desempenho da placa e as imperfeições puramente cosméticas, e estabelece padrões de aceitação para os processos de montagem. O **mesmo** defeito pode ser aprovado na classe 1 e reprovado na classe 3: o defeito não muda, o critério é que muda.

O Capítulo 7 traz os valores de anel anular e de furação praticados por um fabricante real — é com esses números, e não com valores arbitrários, que o seu projeto é conferido no DRC.

Fonte: IPC, *IPC Class 3 Design Guide* (material de apoio da disciplina).

## Categorias de PCBs

- **PCBs de Face Única**: Contêm uma única camada de cobre em um dos lados do substrato, utilizadas em circuitos simples e de baixo custo.
- **PCBs de Dupla Face**: Possuem trilhas condutoras em ambos os lados do substrato, conectadas por vias, sendo amplamente usadas em designs intermediários.
- **PCBs Multicamadas**: Incorporam múltiplas camadas de cobre intercaladas com materiais isolantes, permitindo designs mais complexos e de alta densidade, comuns em dispositivos como smartphones e computadores. Compreender os princípios e os elementos que compõem as PCBs é o primeiro
passo para dominar o design dessas placas essenciais.


# Boas Práticas de Design

O sucesso de um projeto de PCB depende não apenas de sua funcionalidade, mas também da facilidade de produção e da confiabilidade durante o uso. Para garantir que sua placa seja eficiente, econômica e durável, é essencial adotar boas práticas de design. Neste capítulo, abordaremos estratégias para evitar falhas comuns e melhorar a manufaturabilidade do seu projeto.

## Planejamento Inicial

Antes de começar o roteamento, faça um planejamento cuidadoso do layout da placa, colocando os componentes de forma lógica e otimizada. Agrupe componentes relacionados e posicione-os de maneira que minimize os trajetos de conexão.

- Defina as camadas de PCB: determine quantas camadas de PCB você irá utilizar. Camadas adicionais podem permitir trajetos mais curtos e reduzir a interferência entre sinais.
- Rotas Críticas: identifique os sinais críticos, como sinais de alta velocidade, alimentação e terra. Roteie esses sinais primeiro, minimizando interferências e distâncias.

- Plano de Terra Adequado: certifique-se de criar uma área de plano de terra sólido na placa, conectando-a adequadamente a todos os pontos de terra. Isso ajuda a reduzir interferências e proporciona um retorno confiável para os sinais.
- Rotas Diretas e Curtas: mantenha os trajetos de roteamento o mais curtos e diretos possível para evitar atrasos de sinal, interferência eletromagnética e perda de sinal.
- Separação de Sinais: mantenha diferentes tipos de sinais separados para reduzir a interferência. Isso é especialmente importante para sinais analógicos e digitais, que podem interferir entre si.
- Regras de Projeto: defina regras de projeto no software de layout de PCB para garantir espaçamentos adequados entre trilhas, vias e componentes, evitando problemas como curtos-circuitos.
- Uso de Vias: utilize vias para conectar camadas diferentes de PCB. Coloque as vias de forma eficiente, evitando congestionamentos, e distribua-as uniformemente para ajudar na distribuição de energia e terra.
- Roteamento Manual vs. Automático: embora o roteamento automático possa ser útil, em muitos casos, um roteamento manual oferece mais controle sobre o layout. Comece com o roteamento manual e use o roteamento automático como uma ferramenta auxiliar, se necessário.
- Revisão e Simulação: antes de finalizar o layout, revise cuidadosamente todas as trilhas, vias e conexões. Além disso, é recomendável realizar simulações para verificar o desempenho do circuito, especialmente em termos de integridade de sinal.

## Planejamento do Design

Antes de começar a desenhar a PCB, tenha um esquema elétrico bem elaborado e documentado. Planeje o layout considerando:

- **Fluxo do sinal:** Posicione os componentes para otimizar o percurso das conexões.

- **Gerenciamento de espaço:** Evite agrupamentos excessivos e deixe espaço suficiente para trilhas e pads.
- **Restrições mecânicas:** Considere dimensões da placa, pontos de fixação e encaixes.

## Separação de Áreas Funcionais

Divida a placa em zonas, agrupando componentes relacionados. Por exemplo:

- Zona de potência: Para fontes e reguladores.
- Zona de sinal: Para circuitos de baixa tensão e alta frequência.
- Zona de controle: Para microcontroladores e circuitos lógicos. Essa separação reduz interferências e facilita o diagnóstico e a manutenção.
Veja a figura.

![Figura 17: Separação dos componentes em grupos de função](figuras/figura-17.png)



## Largura de Trilhas e Distância Mínima

Calcule a largura das trilhas com base na corrente que elas suportarão, mas a largura necessária **não depende só da corrente**: dependem também a elevação de temperatura admitida, a espessura do cobre e a camada (externa ou interna). Trilhas mais largas são necessárias para correntes maiores. Use a tabela ou calculadora do fabricante para o valor final. Além disso:

- Respeite as distâncias mínimas entre trilhas para evitar curtos-circuitos.

- Utilize ferramentas de verificação de regras de design (DRC) no software para garantir conformidade com os requisitos do fabricante ou equipamento a ser utilizado na fabricação.

## Gerenciamento Térmico

- Posicione dissipadores de calor e vias térmicas próximas a componentes que geram muito calor.
- Utilize planos de aterramento e alimentação para distribuir o calor de forma eficiente. Evite áreas isoladas de cobre que podem atuar como hotspots.

## Trilhas de Alimentação

Mantenha as trilhas de alimentação largas o suficiente para minimizar a queda de tensão devido à resistência.

## Planos de Terra

- **Plano de Terra Sólido:** Crie um plano de terra contínuo em uma camada interna da PCB para fornecer um retorno eficiente para os sinais.
- **Conexão de Terra:** Conecte o plano de terra a todos os pontos de terra do circuito. Use várias vias para conectar as camadas de terra.

::: {.quadro tipo="importante" titulo="Plano de terra: um só, contínuo"}
Prefira **um plano de terra contínuo** a dividi-lo em regiões analógica e digital. O plano contínuo minimiza a impedância entre dois pontos de terra quaisquer e garante o caminho de retorno da corrente. A separação em regiões só se justifica em casos específicos e precisa de **um único ponto de interligação controlado** entre elas: dividir sem esse ponto transforma a emenda em antena e piora a integridade do sinal.

:::

- **Costura de vias (*stitching*):** posicione vias de terra na origem e no destino do sinal, para que a corrente de retorno possa voltar pelo plano de referência.

![Figura 18: Plano de terra e furos de passagem](figuras/figura-18.png)


![Figura 19: Cada seção do circuito deve ter seu plano de terra, havendo a interligação entre eles](figuras/figura-19.png)



![Figura 20: A ligação de todos os grupos na mesma linha de alimentação e terra não é recomendada](figuras/figura-20.png)



## Minimização de Interferências

- **Roteamento Paralelo e Perpendicular:** o acoplamento indutivo e capacitivo (*crosstalk*) **cresce com o comprimento em que duas trilhas correm paralelas e próximas**, e é mínimo quando elas se cruzam perpendicularmente. Portanto: mantenha o trecho paralelo entre trilhas sensíveis o mais curto possível, cruze-as em ângulo reto quando o cruzamento for inevitável e afaste-as onde o paralelismo for necessário.

::: {.quadro tipo="dica" titulo="Regra prática: espaçamento entre trilhas (3W)"}
Para reduzir *crosstalk*, mantenha o centro de uma trilha a pelo menos **3 vezes a sua largura (3W)** de outra trilha; **2W** é o mínimo aceitável. A regra **não** se aplica ao espaçamento interno de um par diferencial.

:::

- Trilhas de Sinal de Referência: Para sinais diferenciais, como USB ou Ethernet, mantenha as trilhas de sinal e referência equidistantes e paralelas respeitando a impedância necessária.
- **Referência de terra próxima ao sinal:** o plano de terra adjacente é o **caminho de retorno da corrente** e deve ficar contínuo e próximo da trilha de sinal — afastar o sinal do plano de referência aumenta a impedância e a emissão. O que precisa de afastamento são as trilhas de **outros sinais**, não o plano de referência.
- **Use Camadas de Sinal:** Utilize camadas de sinal adjacentes para trilhas de sinais complementares, como um plano de terra entre camadas de sinal.

- **Filtros e Blindagem:** Utilize componentes de filtragem, como capacitores e indutores, para reduzir o ruído de alta frequência. Considere a utilização de placas de blindagem para componentes sensíveis.
- **Roteamento Diferencial:** Para sinais de alta velocidade, como USB, HDMI ou PCIe, utilize roteamento diferencial e respeita a impedância pelo tipo de interface para reduzir a interferência e melhorar a integridade do sinal.
- Mantenha trilhas de alta frequência curtas e bem separadas de sinais sensíveis.
- **Use planos de referência (GND)** contínuos para reduzir ruídos e melhorar a integridade do sinal.
- **Adicione capacitores de desacoplamento** próximos aos pinos de alimentação de componentes IC.
- **Coloque sinais e trilhas de terra relacionados próximos** um do outro para minimizar a impedância e a interferência

## Otimização de Pads e Vias

- Certifique-se de que os pads sejam grandes o suficiente para facilitar a soldagem.
- Evite vias muito próximas aos pads, o que pode causar problemas de soldagem.
- Use vias metalizadas para conexões confiáveis entre camadas.

## Simplificação do Layout

::: {.quadro tipo="atencao" titulo="Ângulos na trilha: use 45°"}
Evite ângulos agudos e cantos fechados; prefira ângulos de 45°. A razão principal é de **fabricação**: ângulos agudos formam armadilha de ácido (*acid trap*) na etapa de corrosão, o que pode supercorroer a trilha e abrir o circuito.

:::
- Minimize o uso de vias desnecessárias, pois elas aumentam o custo e podem reduzir a confiabilidade.

## Serigrafia Clara e Informativa

- Inclua rótulos claros para identificação de componentes e orientações de montagem.
- Evite sobrepor a serigrafia em pads ou vias.

## Considerações de Fabricação

- Utilize espessuras de cobre padrão (geralmente 1 oz/ft²) para facilitar a produção.
- Respeite as tolerâncias do fabricante em relação a furos, espessura de trilhas e distâncias mínimas.
- Geração de arquivos de produção (Gerber) compatíveis com os requisitos da fabricante.

## Testabilidade

Inclua pontos de teste para verificar as principais funções do circuito.

Garanta acesso físico aos pontos de teste durante a fase de inspeção e depuração.

## Ligação das E/S do MCU com os conectores

::: {.quadro tipo="atencao" titulo="Nunca ligue o microcontrolador direto no conector"}
Nunca ligue diretamente os terminais de um microcontrolador nos conectores ou bornes da placa. Use uma interface entre as seções do sistema, como mostra a Figura 21.

:::

![Figura 21: É recomendado o uso de interfaces entre seções do sistema](figuras/figura-21.png)



# Processo básico de fabricação de PCB

A fabricação de Placas de Circuito Impresso (PCB) envolve uma série de etapas cuidadosamente planejadas e executadas.

## Etapa fotográfica para criação do padrão de trilhas

O processo começa com a criação de um padrão das trilhas condutoras a serem impressas na placa. Para isso, é realizada uma etapa fotográfica, onde o desenho das trilhas é transferido para uma máscara fotográfica, também conhecida como fotolito.

## Utilização de foto-resistente e máscara fotográfica

A placa de cobre revestida é então preparada com uma camada de foto-resistente, um material sensível à luz que reage quando exposto à radiação ultravioleta (UV). A máscara fotográfica é posicionada sobre a placa e, em seguida, a luz UV é aplicada. As áreas do foto-resistente expostas à luz UV endurecem, enquanto as áreas protegidas pela máscara permanecem inalteradas.

## Etapa de corrosão do cobre com cloreto férrico

Após a exposição à luz UV, a placa é submersa em uma solução de cloreto férrico, um agente corrosivo que remove o cobre nas áreas não protegidas pelo foto-resistente endurecido. Dessa forma, apenas as trilhas desejadas permanecem na placa.

## Alternativas: Fresagem CNC e serigrafia com tintas resistentes à corrosão

Além do processo fotográfico, existem outras técnicas para a criação do padrão de trilhas nas PCBs. A fresagem CNC (Controle Numérico Computadorizado) é uma opção que utiliza máquinas de precisão para cortar diretamente o cobre, formando as trilhas. A serigrafia com tintas resistentes à corrosão é outra alternativa, onde a tinta é aplicada diretamente sobre a placa de cobre, agindo como uma máscara protetora contra a corrosão.

Ao compreender o processo básico de fabricação de PCB, é possível ter uma visão clara das etapas envolvidas na produção de placas de circuito impresso de alta qualidade, fundamentais para a indústria eletrônica atual.

## Furos e vias na PCB

Os furos e vias desempenham um papel essencial nas placas de circuito impresso (PCBs), garantindo a conexão entre camadas e a montagem de componentes.

### Conexão entre camadas e montagem de componentes

Os furos e vias na PCB servem para conectar as trilhas condutoras entre as diferentes camadas de uma PCB multicamadas e para fixar componentes eletrônicos na placa. Os componentes são geralmente soldados nos furos, enquanto as vias garantem a comunicação entre as camadas.

### Perfuração controlada numericamente (CNC) a partir de dados do software CAD

A perfuração dos furos e vias nas PCBs é realizada por máquinas de perfuração controlada numericamente (CNC). Os dados para a perfuração são gerados a partir de arquivos de projeto de software CAD e convertidos em instruções específicas para a máquina CNC. Isso garante a precisão e a repetibilidade na criação dos furos e vias.

### Vias cegas ou microvias: conexões internas entre camadas

Além das vias tradicionais, que atravessam todas as camadas de uma PCB, existem as vias cegas. As vias cegas são usadas para conectar trilhas condutoras entre camadas internas sem atravessar a placa inteira. Isso permite um design de PCB mais compacto e eficiente em termos de espaço.

### Redução do número de tamanhos de furos para diminuir custos

Um dos fatores que afetam o custo de fabricação de uma PCB é o número de tamanhos de furos diferentes usados no projeto. Reduzir o número de tamanhos de furos pode ajudar a diminuir os custos de fabricação, pois menos ferramentas e trocas de brocas são necessárias durante o processo de perfuração. É importante equilibrar essa redução de custos com as necessidades de design e desempenho do circuito eletrônico.

Em resumo, os furos e vias são componentes cruciais na fabricação de placas de circuito impresso, garantindo a conexão entre camadas e a montagem adequada dos componentes eletrônicos. O uso de tecnologias como a perfuração controlada numericamente (CNC) e a implementação de vias cegas, além da redução do número de tamanhos de furos, pode melhorar a eficiência e reduzir os custos na fabricação de PCBs.

## Revestimento de solda e resistência à solda

O revestimento de solda e a resistência à solda são etapas fundamentais no processo de fabricação de placas de circuito impresso (PCBs). Eles garantem a proteção das áreas não-soldadas e facilitam a soldagem de componentes.

### Proteção de áreas não-soldadas por meio de resistência à solda

A resistência à solda é uma camada de material aplicada sobre a superfície da PCB para proteger as áreas não-soldadas. Essa camada ajuda a evitar a aderência de solda nas áreas indesejadas e garante que a solda seja aplicada apenas nas áreas onde os componentes devem ser fixados (máscara de solda).

Cores comuns de resistência à solda: verde escuro e vermelho – A resistência à solda pode ser encontrada em diversas cores, sendo as mais comuns o verde escuro e o vermelho. A escolha da cor pode ser baseada em considerações estéticas, requisitos de identificação ou especificações do cliente. No entanto, a cor da resistência à solda não afeta o desempenho da PCB.

### Estanho ou ouro para facilitar a soldagem de componentes

A fim de melhorar a adesão da solda e a qualidade das conexões elétricas, as áreas onde os componentes serão soldados recebem um revestimento de solda. Os materiais comuns utilizados para o revestimento de solda incluem o estanho e o ouro. Esses metais proporcionam uma superfície propícia para a soldagem e garantem conexões elétricas confiáveis (acabamento superficial).

Em resumo, o revestimento de solda e a resistência à solda são elementos críticos na fabricação de placas de circuito impresso, garantindo a proteção das áreas não-soldadas e facilitando a soldagem de componentes eletrônicos. A escolha dos materiais e das cores utilizadas pode variar, mas a função principal dessas camadas é garantir a qualidade e a durabilidade das conexões elétricas na PCB.

## Serigrafia na PCB

A serigrafia é uma etapa importante no processo de fabricação de placas de circuito impresso (PCB), pois auxilia na identificação e localização de componentes durante a montagem e manutenção.

### Impressão de textos e identificadores na placa

A serigrafia consiste em imprimir informações na superfície da PCB por meio de um processo de impressão semelhante à tela de seda. Essas informações podem incluir textos e identificadores, como a designação dos componentes, referências de pinos, logotipos da empresa e informações de conformidade.

### Auxílio na identificação e localização de componentes

A serigrafia facilita a identificação e a localização dos componentes na PCB durante a montagem, teste e manutenção do dispositivo eletrônico. Ao fornecer informações claras e legíveis, os técnicos e engenheiros podem trabalhar de maneira mais eficiente, reduzindo o risco de erros na montagem e soldagem de componentes.

### Uso de tela de seda gerada pelo software de design de PCB

Durante o processo de design da PCB, os engenheiros utilizam softwares de design de PCB para criar a tela de seda que será usada na etapa de serigrafia. Essa tela contém todas as informações necessárias para a identificação dos componentes e conexões elétricas. O arquivo gerado é então enviado ao fabricante da PCB, que utiliza a tela de seda como base para imprimir as informações na placa.

Em resumo, a serigrafia é uma etapa essencial na fabricação de placas de circuito impresso, pois facilita a identificação e localização de componentes durante a montagem e manutenção dos dispositivos eletrônicos. Através da utilização de softwares de design de PCB, os engenheiros podem criar telas de seda precisas e detalhadas que garantem a qualidade e a funcionalidade das PCBs.


# Protótipo de PCB

A criação de protótipos de PCB é um passo fundamental no desenvolvimento de produtos eletrônicos, pois permite testar e aprimorar o design antes da produção em massa.

## Importância da criação de protótipos antes da produção em massa

O desenvolvimento de um protótipo de PCB permite que os engenheiros e designers validem a funcionalidade, desempenho e confiabilidade do design antes de passar para a produção em larga escala. Isso reduz o risco de falhas e retrabalho no futuro, economizando tempo e recursos.

## Possíveis diferenças no processo de fabricação do protótipo

Embora o processo de fabricação de um protótipo de PCB seja geralmente semelhante ao processo de fabricação em larga escala, pode haver algumas diferenças. Por exemplo, os fabricantes podem usar técnicas de produção manual ou semiautomatizada para os protótipos, enquanto a produção em massa geralmente utiliza técnicas totalmente automatizadas. Além disso, os materiais e processos usados na fabricação do protótipo podem variar, dependendo das necessidades específicas do projeto.

## Recomendação de manter o processo do protótipo próximo ao processo final

Para garantir que os resultados obtidos durante a fase de prototipagem sejam aplicáveis à produção em massa, é importante que o processo de fabricação do protótipo seja o mais próximo possível do processo final. Isso inclui a seleção de materiais, processos de fabricação e fornecedores que sejam consistentes com os usados na produção em larga escala. Dessa forma, os engenheiros e designers podem ter maior confiança de que o produto final atenderá às expectativas de desempenho e qualidade.

O protótipo de PCB desempenha um papel crítico no desenvolvimento de produtos eletrônicos, permitindo que os engenheiros e designers validem e aprimorem o design antes de passar para a produção em massa. Ao garantir que o processo de fabricação do protótipo seja o mais próximo possível do processo final, é possível minimizar os riscos associados à produção em larga escala e assegurar a qualidade e o desempenho do produto final.


# Opções de "EDA" - "Electronic Design Automation" (Automação de Design Eletrônico)

Existem várias outras ferramentas de design eletrônico disponíveis no mercado que competem com o KiCad. Algumas das principais concorrentes são:

- **Altium Designer:** É uma poderosa suíte de design eletrônico amplamente utilizada na indústria. Oferece recursos avançados de esquemáticos, layout de PCB, simulação e gerenciamento de bibliotecas.
- **Eagle (descontinuado):** foi uma ferramenta popular de design eletrônico, com versão gratuita para projetos pequenos. A Autodesk encerrou o produto: o EAGLE deixou de ser vendido e suportado em 07/06/2026, e o fluxo de PCB da empresa passou para o Fusion 360. *[fonte: Autodesk, "Autodesk EAGLE is no longer available — Next steps and FAQ", consultado em 2026-09-29]*
- **OrCAD:** Desenvolvido pela Cadence Design Systems, o OrCAD é uma suíte de design eletrônico completa que inclui esquemáticos, layout de PCB e simulação.
- **Siemens PADS Professional:** Outra suíte de design eletrônico amplamente utilizada na indústria. Oferece recursos de design de alta qualidade e integração com ferramentas de simulação. O produto era da Mentor Graphics (PADS) e hoje é da Siemens. *[fonte: Siemens, "PADS PCB design software", siemens.com, consultado em 2026-09-29]*
- **DipTrace:** Uma alternativa ao KiCad com versões gratuitas e pagas. Oferece uma interface amigável e recursos adequados para projetos de PCB de tamanho médio.

- **DesignSpark PCB:** Uma ferramenta gratuita de design eletrônico desenvolvida pela RS Components. É adequada para projetos pequenos e médios.
- **Proteus:** Oferece recursos de simulação, esquemáticos e layout de PCB, tornando-o uma opção abrangente para designers eletrônicos.


# KiCad

O KiCad é um conjunto de softwares de código aberto voltado para a criação de projetos de design eletrônico. Ele é amplamente utilizado para desenvolver esquemáticos de circuitos eletrônicos e layouts de placas de circuito impresso (PCBs). O nome "KiCad" é uma abreviação de "Kicad-Computer-Aided Design".

O KiCad é uma ferramenta muito popular entre engenheiros eletrônicos, entusiastas e estudantes, oferecendo uma solução completa e gratuita para projetos eletrônicos. Ele é multiplataforma, o que significa que está disponível para Windows, macOS e Linux.

#### As principais funcionalidades do KiCad incluem:

- **Editor esquemático:** Permite criar esquemas eletrônicos, onde os componentes são conectados para formar um circuito funcional;
- **Editor de PCB:** Uma vez que o esquema esteja pronto, o KiCad permite projetar a PCB, posicionando os componentes e traçando as trilhas de cobre para conectar os componentes adequadamente;
- **Bibliotecas de componentes:** O KiCad inclui bibliotecas de componentes eletrônicos padrão, mas também permite a criação e gerenciamento de bibliotecas personalizadas.
- **Visualização 3D:** É possível visualizar o PCB em 3D, ajudando a verificar a colocação dos componentes e identificar possíveis problemas de interferência.
- **Simulação de circuitos:** o KiCad possui recursos de simulação, mas com algumas particularidades. Ele integra o ngspice, que é uma ferramenta de simulação SPICE amplamente utilizada para análises de circuitos eletrônicos. Essa funcionalidade permite simular circuitos analógicos e mistos diretamente no KiCad.
- **Gerenciamento de projetos:** O KiCad oferece uma interface para gerenciar facilmente os arquivos e recursos do projeto.

Devido à sua natureza de código aberto, o KiCad conta com uma comunidade ativa de desenvolvedores e usuários, o que significa que existem recursos adicionais, bibliotecas e plugins disponíveis para expandir suas funcionalidades.

## Motivos para usar o Kicad

O KiCad apresenta diversas vantagens em relação a outros softwares concorrentes de design eletrônico. Algumas dessas vantagens incluem:

- **Código aberto e gratuito:** O KiCad é um software de código aberto, o que significa que você pode utilizá-lo sem custo e ter acesso ao código-fonte. Isso facilita a colaboração e permite que a comunidade de usuários contribua com melhorias e correções.
- **Multiplataforma:** O KiCad é compatível com Windows, macOS e Linux, o que o torna uma opção acessível para diferentes sistemas operacionais.
- **Comunidade ativa:** O KiCad possui uma comunidade grande e ativa de desenvolvedores e usuários. Isso significa que você pode encontrar suporte, tutoriais, bibliotecas adicionais e recursos para melhorar sua experiência com a ferramenta.
- **Integração e recursos completos:** O KiCad oferece um conjunto completo de recursos, incluindo editor esquemático, editor de PCB, bibliotecas de componentes, visualização 3D e gerenciamento de projetos. Isso permite que você realize todo o processo de design em uma única ferramenta, evitando a necessidade de importar e exportar projetos entre diferentes aplicativos.
- **Bibliotecas de componentes atualizadas:** O KiCad inclui uma biblioteca de componentes eletrônicos padrão e também permite que você crie e gerencie suas próprias bibliotecas. Além disso, a comunidade contribui com bibliotecas de alta qualidade, garantindo que você tenha acesso a uma ampla variedade de componentes para seus projetos.
- **Atualizações frequentes:** O KiCad é continuamente atualizado e melhorado pela comunidade de desenvolvedores, garantindo que você tenha acesso a recursos e correções de bugs mais recentes.

- **Sem limitações de tamanho de projeto:** Ao contrário de algumas ferramentas concorrentes que impõem restrições ao tamanho dos projetos na versão gratuita, o KiCad não possui essas limitações, permitindo que você trabalhe em projetos de qualquer tamanho sem custos adicionais.
- **Importação de arquivos de outros EDAs:** Documentos esquemáticos do Altium Designer, Circuit Studio, Circuit Maker; PCB de designer Altium; Fabricante de circuitos Altium PCB; Altium Circuito Estúdio PCB;; CB ASCII P- Cad 200x; PCB Fabmaster

## Instalação do KiCAD

- Existem versões para Windows, Linux, macOS e Docker. Utilize a url apresentada para obter a versão desejada. <u>[https://www.kicad.org/download/](https://www.kicad.org/download/)</u>

## Usando o gerenciador de projetos KiCad

O gerenciador de projetos KiCad é uma ferramenta que cria e abre projetos KiCad e inicia as outras ferramentas KiCad (editores de esquemas e placas, visualizador Gerber e ferramentas utilitárias).

![Figura 22: Gerenciador de Projetos. Fonte: [https://docs.kicad.org/8.0/en/kicad/kicad.html#:~:text=Usando%20o](https://docs.kicad.org/8.0/en/kicad/kicad.html#:~:text=Usando%20o) %20gerenciador,editores%20e%20ferramentas](figuras/figura-22.png)



A janela do gerenciador de projetos do KiCad é composta por uma visualização em árvore à esquerda, mostrando os arquivos associados ao projeto aberto, e um iniciador à direita, contendo atalhos para os vários editores e ferramentas.

## Arquivos e pastas KiCad

O KiCad cria e usa arquivos com as seguintes extensões de arquivo (e pastas) específicas para edição de esquemas e placas.

### Arquivos de projeto

Arquivo de projeto, contendo configurações que são compartilhadas *.kicad_pro entre o esquema e o PCB

*.pro Arquivo de projeto Legacy (KiCad 5.x e anterior). Pode ser lido e será

convertido em um.kicad_proarquivo pelo gerente de projeto.

#### Arquivos do editor esquemático

Arquivos esquemáticos contendo todas as informações e os próprios *.kicad_sch componentes.

Arquivo de biblioteca de símbolos esquemáticos, contendo as *.kicad_sym descrições dos componentes: forma gráfica, pinos, campos.

Arquivo esquemático legado (KiCad 5.x e anterior). Pode ser lido e *.sch será convertido em um.kicad_scharquivo na gravação.

Arquivo de biblioteca esquemática Legacy (KiCad 5.x e anteriores). *.lib Pode ser lido, mas não escrito.

Documentação da biblioteca esquemática legada (KiCad 5.x e *.dcm anterior). Pode ser lida, mas não escrita.

Arquivo de cache de biblioteca de componentes esquemáticos legados *-cache.lib (KiCad 5.x e anteriores). Necessário para o carregamento adequado de um.scharquivo esquemático legado ( ).

Tabela de biblioteca de símbolos: sym-lib-table, lista de bibliotecas de símbolos disponíveis no editor de esquemáticos.

#### Arquivos e pastas do editor de PCB

Arquivo do quadro contendo todas as informações, exceto o layout da *.kicad_pcb página.

*.pretty Pastas da biblioteca Footprint. A pasta em si é a biblioteca.

*.kicad_mod Arquivos de pegada, contendo uma descrição de pegada cada.

Arquivo de regras de design, contendo regras de design *.kicad_dru personalizadas para um.kicad_pcbarquivo específico.

Arquivo de placa Legacy (KiCad 4.x e anteriores). Pode ser lido, mas *.brd não escrito, pelo editor de placa atual.

|*.mod fp-lib-table fp-info-cache|Arquivo de biblioteca de footprint legado (KiCad 4.x e anterior). Pode ser lido pelo footprint ou pelo editor de placa, mas não escrito. Tabela de biblioteca de footprint: lista de bibliotecas de footprint disponíveis no editor de quadro. Cache para acelerar o carregamento de bibliotecas de footprint. Não precisa ser distribuído com o projeto ou colocado sob controle de versão.|
|---|---|
||Arquivos comuns|
|*.kicad_prl|Configurações locais para o projeto atual; ajuda o KiCad a lembrar as últimas configurações usadas, como visibilidade de camada ou filtro de seleção. Pode não precisar ser distribuído com o projeto ou colocado sob controle de versão.|
|*.kicad_wks|Arquivo de descrição do layout da página (borda do desenho e bloco de título)|
|*.net *.cmp|Arquivo netlist criado a partir do esquema e lido pelo editor de placa. Observe que o fluxo de trabalho recomendado para transferir informações do esquema para a placa não requer o uso de arquivos netlist. Associação entre componentes usados no esquemático e seus footprints. Pode ser criado pelo Board Editor e importado pelo Schematic Editor. Seu propósito é importar alterações do board para o esquemático, para usuários que alteram footprints no Board Editor (por exemplo, usando o comando Exchange Footprints) e querem importar essas alterações de volta para o esquemático. Observe que o fluxo de trabalho recomendado para transferir informações do board para o esquemático não requer o uso de.cmparquivos. Instituto Federal Fluminense 36|

#### Arquivos de fabricação e documentação

|*.gbr|Arquivo Gerber, para fabricação.|
|---|---|
|*.drl|Arquivo de perfuração (formato Excellon), para fabricação.|
|*.pos|Arquivos de posição (formato ASCII), para máquinas de inserção automática.|
|*.rpt|Arquivos de relatório (formato ASCII), para documentação.|
|*.ps|Arquivos de plotagem (Postscript), para documentação.|
|*.pdf|Arquivos de plotagem (formato PDF), para documentação.|
|*.svg|Arquivos de plotagem (formato SVG), para documentação.|
|*.dxf|Arquivos de plotagem (formato DXF), para documentação.|

*.plt Arquivos de plotagem (formato HPGL), para documentação.

### Armazenando e enviando arquivos KiCad

Os arquivos de esquema e placa do KiCad contêm todos os símbolos esquemáticos e footprints usados no design, então você pode fazer backup ou enviar esses arquivos por si só sem problemas. Algumas informações importantes do design são armazenadas no arquivo do projeto (.kicad_pro), então se você estiver enviando um design completo, certifique-se de incluí-lo. Alguns arquivos, como o arquivo project-local settings (.kicad_prl) e o arquivo fp-info-cache, não são necessários para enviar com seu projeto. Se você usa um sistema de controle de versão como o Git para manter o controle de seus projetos KiCad, você pode querer adicionar esses arquivos à lista de arquivos ignorados para que eles não sejam rastreados. Outros detalhes inclusive de configurações pode ser obtidos em:

<u>[https://docs.kicad.org/8.0/en/kicad/kicad.html](https://docs.kicad.org/8.0/en/kicad/kicad.html)</u>

## Workflow do Kicad

O fluxo de trabalho (workflow) do KiCad geralmente segue as etapas comuns de projeto de circuitos eletrônicos e design de PCB. Entretanto, conforme o desejo do projetista, algumas etapas do workflow podem ser alteradas ou até suprimidas durante o design. Ver exemplo na figura.

![Figura 23: Workflow básico KiCAD. fonte: [https://www.slideshare.net/baoshi1/why-](https://www.slideshare.net/baoshi1/why-) and-how-to-switch-to-kicad](figuras/figura-23.png)



Abaixo estão as principais etapas do workflow do KiCad:

### Esquemático (Schematic):

- Crie um novo projeto no KiCad.
- Configure a página e esquemático.
- Desenhe o esquemático do circuito eletrônico usando o editor esquemático do KiCad.
- Adicione componentes eletrônicos ao esquemático, selecionando-os a partir da biblioteca de componentes ou criando novos componentes, se necessário.
- Conecte os componentes eletrônicos usando os símbolos de fios ou barramentos.

- Preencha os designadores dos componentes eletrônicos

### Associação de Footprints (Assigning Footprints):

- Após finalizar o esquemático, associe os componentes com suas respectivas footprints no layout da PCB. O footprint é a representação física do componente na placa de circuito impresso.

### Layout da PCB (PCB Layout):

- Abra o editor de PCB e importe o netlist do esquemático para criar o layout da placa de circuito impresso (PCB).
- Posicione os componentes na placa e organize-os de acordo com suas preferências e requisitos de design.
- Trace as trilhas de cobre para conectar os componentes eletrônicos corretamente.
- Realize o roteamento das trilhas de forma a evitar cruzamentos indesejados e garantir o melhor desempenho do circuito.

### Visualização 3D (3D Visualization):

- Utilize a visualização 3D do KiCad para verificar a colocação dos componentes na PCB e garantir que não haja interferências ou problemas de montagem.

### Verificação do Design (Design Verification):

- Realize uma revisão completa do projeto, verificando a conformidade das trilhas, a ausência de erros de conexão, e garantindo que todas as regras de projeto estejam sendo seguidas.

### Geração dos Arquivos de Fabricação (Manufacturing Files):

- Após concluir o design da PCB, gere os arquivos necessários para a fabricação da placa, incluindo Gerber files, Drill files, entre outros.

## Importação e utilização de bibliotecas de componentes no KiCad

O KiCad possui várias bibliotecas de componentes, mas existem outras disponíveis online.

#### As bibliotecas são:

- symbols → símbolos utilizados no editor de esquemático do KiCad
- footprints → footprints utilizados no editor da PCB
- packages3D → modelos 3D utilizados na renderização feita no visualizador da PCB
![Figura 25: Exemplo de footprint](figuras/figura-25.png)



![Figura 26: Exemplo de modelos 3D](figuras/figura-26.png)



![Figura 24: Exemplo de símbolo](figuras/figura-24.png)



### Utilização de novas bibliotecas

As seguintes bibliotecas são as oficiais:

<u>[https://gitlab.com/kicad/libraries/kicad-symbols](https://gitlab.com/kicad/libraries/kicad-symbols)</u>

<u>[https://gitlab.com/kicad/libraries/kicad-footprints](https://gitlab.com/kicad/libraries/kicad-footprints)</u>

<u>[https://gitlab.com/kicad/libraries/kicad-packages3D](https://gitlab.com/kicad/libraries/kicad-packages3D)</u>

<u>[https://gitlab.com/kicad/libraries/kicad-packages3D-source](https://gitlab.com/kicad/libraries/kicad-packages3D-source)</u>

<u>[https://gitlab.com/kicad/libraries/kicad-templates](https://gitlab.com/kicad/libraries/kicad-templates)</u>

Entretanto, existem outras fontes on-line que podem ser utilizadas para obtenção de bibliotecas. Exemplos:

<u>[https://www.ultralibrarian.com/](https://www.ultralibrarian.com/)</u>

<u>[https://www.snapeda.com/](https://www.snapeda.com/)</u>

Também pode-se encontrar bibliotecas específicas de fabricantes, ou ainda, é possível criar seus próprios símbolos, footprints e modelos 3D.

O plugin que aumenta a produtividade é o easyeda2kicad.

O projeto com instruções pode ser acessado pela url: <u>[https://pypi.org/project/easyeda2kicad/](https://pypi.org/project/easyeda2kicad/)</u>

No Linux ou Windows é possível instalar a partir dos comandos:

    python3 -m venv kicadlib

***source kicadlib/bin/activate***

    pip install easyeda2kicad

    easyeda2kicad --full –lcsc_id=C2040

Onde C2040 pode ser substituído pelo id do componente disponível em

<u>[https://jlcpcb.com/PARTS](https://jlcpcb.com/PARTS)</u>

Por exemplo: pretende-se incluir no Kicad as bibliotecas do componente ATGM336H-5N31.

![Figura 27: Exemplo de indentificação do Part na JLCPCB](figuras/figura-27.png)



Então digite o comando:

    easyeda2kicad --full –lcsc_id=C90770

Símbolo, Footprint e modelo 3D serão baixados para o seu PC em diretório padrão, mas é possível especificar o diretório de destino.

    easyeda2kicad --full --lcsc_id=C2040 --output ~/libs/my_lib

No KiCad, vá em Preferências > Configurar Caminhos e adicione as variáveis de ambiente EASYEDA2KICAD:

    Windows : C:/Users/your_username/Documents/Kicad/easyeda2kicad/,

    Linux:/home/your_username/libs

Vá para Preferências > Gerenciar Bibliotecas de Símbolos e Adicione a biblioteca global

**easyeda2kicad:${EASYEDA2KICAD}/my_lib.kicad_sym**

Vá para Preferências > Gerenciar bibliotecas do Footprint e adicione a biblioteca global

**easyeda2kicad:${EASYEDA2KICAD}/my_lib.pretty**

Nesse caso o componente já estará com o campo “LCSC Part” contendo o código exato que fará parte da lista BOM (veja a figura).

![Figura 28: Identificação do componente a ser utilizado na lista BOM para fabricação na JLCPCB](figuras/figura-28.png)



![Figura 29: Configuração das bibliotecas de símbolos](figuras/figura-29.png)



Caso as biblioteca seja específica do projeto e altamente recomendável que esteja em um diretório do projeto.

Caso deseje incluir as bibliotecas apenas no projeto e dentro dos respectivos diretórios do mesmo, use o caminho da seguinte forma:

    ${KIPRJMOD}/libs/my_libs.kicad_sym

## Principais teclas de atalho

### Editor de Esquemáticos (Eeschema)

|Tecla de Atalho|Descrição|
|---|---|
|A|Adicionar um novo componente ao esquemático.|
|M|Mover o componente selecionado.|
|G|Mover o componente sem desconectar as conexões.|
|R|Girar o componente selecionado (90° no sentido horário).|
|Ctrl + R|Girar no sentido anti-horário.|
|X|Adicionar um fio elétrico.|
|Shift + X|Adicionar um fio de barramento.|
|L|Adicionar uma etiqueta do fio (Label).|
|Ctrl + B|Alternar exibição de nomes de barramento e rótulos.|
|F5, F6, F7, F8|Alternar entre diferentes folhas do projeto hierárquico.|
|Ctrl + E|Editar o componente selecionado.|
|Ctrl + Shift + E|Editar as propriedades do componente.|
|Delete|Excluir o item selecionado.|
|Ctrl + Z|Desfazer a última ação.|
|Ctrl + Y|Refazer a última ação desfeita.|
|Ctrl + F|Localizar componentes ou rótulos.|
|Ctrl + G|Gerar netlist (rede elétrica).|

### Editor de PCB (Pcbnew)

|Tecla de Atalho|Descrição|
|---|---|
|A|Adicionar um componente à PCB.|
|M|Mover o componente selecionado.|
|G|Mover o componente mantendo as conexões (empurrar e ajustar).|
|R|Rotacionar o componente selecionado.|
|Ctrl + R|Rotacionar no sentido anti-horário.|
|F|Alternar entre os lados da PCB (superior/inferior).|
|Ctrl + H|Alternar exibição de vias e trilhas invisíveis.|
|X|Adicionar uma trilha.|
|V|Adicionar uma via.|
|Shift + X|Entra no modo de "Roteamento" para adicionar trilhas conectadas.|
|Ctrl + Shift + B|Atualizar os componentes da PCB com base no esquemático.|
|Ctrl + Z|Desfazer a última ação.|
|Ctrl + Y|Refazer a última ação desfeita.|
|Delete|Excluir o item selecionado.|
|Ctrl + Alt + V|Adicionar trilha em via (Jump).|
|Ctrl + F|Localizar componentes na PCB.|
|Ctrl + Shift + D|Alterar as dimensões do contorno da PCB.|
|Ctrl + M|Medir distâncias entre dois pontos.|

### Teclas Globais

Estas teclas funcionam em ambos os editores:

#### Tecla de

#### Descrição

#### Atalho

|Ctrl + S|Salvar o projeto.|
|---|---|
|Ctrl + O|Abrir um projeto existente.|
|Ctrl + N|Criar um novo projeto.|
|Ctrl + P|Imprimir o projeto atual.|

#### Tecla de

#### Descrição

#### Atalho

**F11** Alternar para modo tela cheia. Acessar o menu de ajuda/documentação do **F1** KiCad.

Essas teclas de atalho são padrão no KiCad 8 e podem ser ajustadas em **Preferências > Configuração de Atalhos** caso você precise personalizá-las.

## Compatibilidade do Design da PCB para fabricação

As empresas que realizam a manufatura das PCBs de forma comercial possuem limites técnicos que por vezes impossibilitam a fabricação caso o projetista não esteja atendo aos limites imposto pelo fabricante. Nesse caso é muito importante consultar os parâmetros definidos pelo fabricante e inseri-los nas no verificados de regras da PCB.

As configurações de restrição podem ser inseridas no KiCAD “Configuração da Placa → Regras de Desenho → Restrições”. Ver figura.

::: {.quadro tipo="dica" titulo="Antes de mandar fabricar"}
Insira no KiCAD as restrições técnicas de fabricação, para que o próprio KiCAD aponte inconsistências no projeto, e trabalhe com **margem de pelo menos 20%** em relação aos limites do fabricante.

**Nota:** a estrutura desta tabela foi corrompida na conversão (células desalinhadas). Os valores precisam ser conferidos na página do fabricante antes do uso — a revisão está pendente.

:::

![Figura 30: Interface de configuração das restrições de desenho da PCB](figuras/figura-30.png)



As compatibilidades apresentadas foram conferidas na JLCPCB em 09/2026, a partir da url [jlcpcb.com/capabilities/pcb-capabilities](https://jlcpcb.com/capabilities/pcb-capabilities). Os valores são os publicados pelo fabricante nessa data e mudam com o tempo — confira a página antes de usar.

#### Especificações do PCB

| Característica | Capacidade | Descrição |
|---|---|---|
| Contagem de camadas | 1–32 | Número de camadas de cobre da placa. |
| Impedância controlada | 4/6/8/10/12/14/16/18/20/…/32 camadas | Ver a calculadora de impedância da JLCPCB. |
| Tolerância de impedância | ±10% | Tolerância padrão do serviço; ±5% sob consulta. |
| Material | FR-4 | Laminados grau A de fornecedores como Nan Ya, KB e Shengyi. |
| HDI | 1-step / 2-step / 3-step | Via cega de 0,075–0,15 mm (perfuração a laser); via enterrada de 0,15–0,55 mm padrão e até 0,10 mm em casos extremos; trilha/espaço mínimo de 3/3 mil (2,7/2,7 mil extremo); dimensões de 5 × 5 mm a 576 × 469 mm. |
| Núcleo de alumínio | 1 camada | PCBs de núcleo de alumínio de uma camada. |
| Núcleo de cobre | 1 camada | PCBs de núcleo de cobre de uma camada, com contato direto do dissipador ao núcleo (≥ 1 × 1 mm). |
| PCB de RF | 2 camadas, 1 oz | Núcleos de Rogers e PTFE. |
| Constantes dielétricas do FR-4 | 4,5 (placa de 2 camadas) | Prepreg 7628: 4,4; 3313: 4,1; 2116: 4,16. |
| Dimensões máximas | FR-4 (1 camada): 606 × 510 mm; FR-4 (2 camadas): 670 × 600 mm; FR-4 (4 camadas): 663 × 593 mm; FR-4 (6+ camadas): 656 × 586 mm; Rogers/PTFE: 590 × 438 mm; alumínio: 602 × 506 mm; cobre: 480 × 286 mm | Válido para placas com espessura ≥ 0,8 mm; FR-4 mais fino chega a 599 × 497 mm. Placas de 2 camadas podem atingir 1020 × 600 mm e as de 4 camadas, 1016 × 596 mm. |
| Dimensões mínimas | FR-4/Rogers/PTFE: 3 × 3 mm; bordas chapeadas ou casteladas: 10 × 10 mm; alumínio/cobre: 5 × 5 mm | Válido para espessuras ≥ 0,6 mm; abaixo disso exige revisão manual. A painelização é recomendada para placas pequenas. |
| Tolerância dimensional | ±0,1 mm | ±0,1 mm (precisão) e ±0,2 mm (regular) no roteamento CNC; ±0,4 mm no corte em V. |
| Espessura | 0,4–4,5 mm | FR-4 em 0,4/0,6/0,8/1,0/1,2/1,6/2,0 mm (2,5 mm ou mais apenas para placas de 12 camadas ou mais). |
| Tolerância de espessura (≥ 1,0 mm) | ±10% | Ex.: placa de 1,6 mm → acabada entre 1,44 mm e 1,76 mm. |
| Tolerância de espessura (< 1,0 mm) | ±0,1 mm | Ex.: placa de 0,8 mm → acabada entre 0,7 mm e 0,9 mm. |
| Cobre acabado — camada externa | 2 camadas: 1/2/2,5/3,5/4,5 oz; multicamadas: 1/2 oz | — |
| Cobre acabado — camada interna | 0,5/1/2 oz | 0,5 oz por padrão na camada interna. |
| Máscara de solda | Verde, roxo, vermelho, amarelo, azul, branco e preto | Máscara LPI (*Liquid Photo Imageable*), a mais comum. A de tinta curada a calor aparece em placas de baixo custo e de um lado só. |
| Acabamento de superfície | HASL (com e sem chumbo), ENIG, OSP | OSP não está disponível para FR-4 de face única, FPC e placas de alumínio; placas de alumínio aceitam apenas HASL. FR-4/HDI com 6 camadas ou mais, espessura ≤ 0,4 mm, alta frequência, núcleo de cobre e FPC não suportam HASL. |

#### Perfuração

| Característica | Capacidade | Descrição |
|---|---|---|
| Diâmetro de broca | 1 camada: 0,3–6,3 mm; 2 camadas e multicamadas: 0,15–6,3 mm | Microvias de 0,1 mm apenas com espessura ≤ 1 mm e acabamento ENIG ou OSP. Furos ≥ 6,3 mm são roteados por CNC a partir de um furo menor. Diâmetro mínimo para 2 ou mais camadas: 0,1 mm (mais caro); núcleo de alumínio: 0,65 mm; núcleo de cobre: 1,0 mm. |
| Tolerância do tamanho do furo | Furos passantes: +0,13/−0,08 mm; encaixe por pressão: ±0,05 mm (placas ENIG multicamadas, só furos circulares) | Ex.: furo de 0,6 mm → acabado entre 0,52 mm e 0,73 mm. Recomendado PTH ≥ 0,5 mm para evitar máscara ou estanho presos no furo. |
| Espessura média do revestimento do furo | 18 µm | — |
| Tolerância de posição do furo | ±0,075 mm | — |
| Furo e diâmetro mínimo de via | 0,15/0,25 mm | 0,1/0,2 mm apenas com espessura ≤ 1 mm e ENIG/OSP. Uma camada (só NPTH): furo de 0,3 mm e via de 0,5 mm. O diâmetro da via deve ser 0,1 mm (0,15 mm de preferência) maior que o furo; furo mínimo preferido: 0,2 mm. |
| Furos não metalizados (NPTH) mínimos | 0,50 mm | Desenhe os NPTH na camada mecânica ou na camada de *keep-out*. |
| Largura mínima de rasgo metalizado | 2 camadas: 0,5 mm; multicamadas: 0,35 mm | O comprimento do rasgo deve ser ao menos 2 vezes a largura. |
| Rasgo não metalizado mínimo | 1,0 mm | Desenhe o contorno do rasgo na camada mecânica (GM1 ou GKO). |
| Tolerância do tamanho do rasgo | Metalizado: +0,13/−0,08 mm; não metalizado: ±0,2 mm | Rasgo metalizado é feito com broca; não metalizado, por CNC. |
| Espaçamento furo a furo (vias) | 0,2 mm | — |
| Espaçamento furo a furo (almofadas) | 0,45 mm | — |
| Furos castelados mínimos | 0,5 mm | São meios-furos metalizados na borda da placa, usados em placas-filhas para soldar na placa-mãe. Diâmetro ≥ 0,5 mm; furo à borda ≥ 1 mm; furo a furo ≥ 0,5 mm; placa ≥ 10 × 10 mm; espessura ≥ 0,6 mm. |
| Bordas chapeadas | 10 × 10 mm | Bordas com cobre e acabamento ENIG (HASL não é suportado). Placa ≥ 10 × 10 mm; espessura ≥ 0,6 mm; ao menos 3 rupturas no revestimento para as abas de suporte. |
| Rasgos cegos | — | Largura ≥ 1,0 mm; profundidade ≥ 0,2 mm; anel ≥ 0,3 mm; distância de segurança ≥ 0,2 mm; espessura remanescente ≥ 0,2 mm. FR-4 de 2 a 32 camadas com espessura ≥ 0,8 mm. |
| Backdrill | — | Furação secundária que controla a profundidade do furo e remove o cobre excedente, reduzindo a interferência no sinal. FR-4 de 4 a 32 camadas com espessura ≥ 0,8 mm. |
| Furos e rasgos retangulares | Não suportado | Furos e rasgos retangulares sem cantos arredondados não são suportados. |

#### Larguras

| Característica | Capacidade | Descrição |
|---|---|---|
| Largura e espaçamento mínimos de trilha (1 oz) | 0,10/0,10 mm (4/4 mil) | 1 e 2 camadas: 0,10/0,10 mm. Multicamadas: 0,09/0,09 mm (3,5/3,5 mil); 3 mil é aceitável em *fan-out* de BGA. |
| Largura e espaçamento mínimos de trilha (2 oz) | 0,16/0,16 mm (6,5/6,5 mil) | 2 camadas: 0,16/0,16 mm. Multicamadas: 0,15/0,15 mm (6/6 mil). |
| Largura e espaçamento mínimos de trilha (2,5 oz) | 2 camadas: 0,2/0,2 mm (8/8 mil) | — |
| Largura e espaçamento mínimos de trilha (3,5 oz) | 2 camadas: 0,25/0,25 mm (10/10 mil) | — |
| Largura e espaçamento mínimos de trilha (4,5 oz) | 2 camadas: 0,3/0,3 mm (12/12 mil) | — |
| Tolerância da largura da trilha | ±20% | Ex.: trilha de 0,1 mm → acabada entre 0,08 mm e 0,12 mm. |
| Anel anular PTH | ≥ 0,20 mm | 2 camadas — 1 oz: recomendado 0,25 mm ou mais, mínimo absoluto 0,18 mm; 2 oz: 0,254 mm ou mais. Multicamadas — 1 oz: recomendado 0,20 mm ou mais, mínimo absoluto 0,15 mm; 2 oz: 0,254 mm ou mais. |
| Anel anular de almofada NPTH | ≥ 0,45 mm | Recomendado 0,45 mm ou mais, para permitir remover 0,2 mm de cobre ao redor do furo e fixar o filme de vedação. Abaixo disso o anel pode ficar muito fino ou ausente. |
| BGA | 0,2 mm | Almofada de 0,2 a 0,25 mm exige ENIG. Folga almofada–trilha ≥ 0,1 mm (mínimo 0,09 mm em multicamadas). Vias podem ficar dentro das almofadas BGA, preenchidas e cobertas. |
| Bobinas de trilha (*trace coils*) | 0,15/0,15 mm | Largura/folga mínima de 0,15/0,15 mm com trilhas cobertas por máscara (1 oz) e de 0,25/0,25 mm sem cobertura (1 oz). Somente ENIG, pelo risco de curto com HASL. |
| Grade hachurada — largura e espaçamento | 0,25 mm | — |
| Espaçamento de trilhas de mesma rede | 0,25 mm | — |
| Folga via–cobre na camada interna | 0,2 mm | — |
| Folga furo de almofada PTH–cobre na camada interna | 0,3 mm | — |
| Folga almofada–trilha (1 oz) | 0,1 mm | Mínimo 0,1 mm, ficando bem acima se possível; 0,09 mm localmente para almofadas BGA. |
| Folga entre almofadas SMD (redes diferentes) | 0,15 mm | Almofada SMD mínima: 0,25 × 0,25 mm. |
| Folga furo de via–trilha | 0,2 mm | — |
| Folga PTH–trilha | 0,28 mm | Recomendado 0,35 mm; mínimo 0,28 mm. |
| Folga NPTH–trilha | 0,2 mm | — |

#### Máscara de solda

| Característica | Capacidade | Descrição |
|---|---|---|
| Expansão da máscara de solda | 1:1 | Equipamento LDI atualizado em junho de 2025: a abertura da máscara pode ter a mesma medida da almofada. Mantenha ao menos 0,09 mm de folga entre as aberturas da máscara e as trilhas vizinhas. |
| Ponte de máscara de solda | 0,10 mm | 1 oz — espaçamento mínimo entre almofadas de 0,10 mm (verde, vermelho, amarelo, azul, roxo) e 0,13 mm (preto, branco). 2 oz — 0,20 mm em qualquer cor. |
| Vias plugadas | Preenchidas com máscara de solda | Acabamento opaco. Vias preenchidas não podem ter abertura de máscara em nenhum dos lados, precisam de ≥ 0,35 mm de folga de outras aberturas e não podem passar de 0,5 mm de diâmetro. |
| Via-in-pad (processo JLCPCB) | Epóxi preenchido e coberto; pasta de cobre preenchida e tampada | Vias preenchidas com resina epóxi ou pasta de cobre e depois cobertas, para acabamento opaco e liso. É o padrão para placas multicamadas de 6 camadas ou mais e é compatível com vias de 0,15 a 0,55 mm. |
| Constante dielétrica da máscara de solda | 3,8 | — |
| Espessura da tinta da máscara de solda | ≥ 10 µm | — |

#### Lenda

| Característica | Capacidade | Descrição |
|---|---|---|

| Largura mínima de linha | ≥ 0,15 mm (6 mil) | Caracteres com largura menor que 0,15 mm não são identificáveis. |
| Altura mínima do texto | 1,0 mm (40 mil) | Caracteres com altura inferior a 1,0 mm não são identificáveis. |
| Proporção largura/altura do caractere | 1:6 | Proporção preferida entre largura e altura. |
| Proporção largura/altura (caractere vazado) | 1:6 | Proporção preferida entre largura e altura do caractere esculpido em cavidade. |
| Almofada → serigrafia | 0,15 mm | Distância mínima entre a almofada e a serigrafia. |

#### Contorno

| Característica | Capacidade | Descrição |
|---|---|---|
| Roteado | 0,2 mm | Folga de cobre das bordas roteadas: ≥ 0,2 mm; folga de cobre das ranhuras roteadas: ≥ 0,2 mm; tolerância dimensional das bordas roteadas: ±0,2 mm (precisão regular) e ±0,1 mm (alta precisão). |
| Corte em V (*V-cut*) | 0,4 mm | Folga de cobre das bordas: ≥ 0,4 mm; tolerância dimensional: ±0,4 mm, com espessura de PCB ≥ 0,6 mm; dimensões do painel: de 70 × 70 mm a 475 × 475 mm; ângulo da ranhura: 25°; espaçamento mínimo entre dois cortes em V: 2 mm (3 mm recomendado). |
| Painel com mordidas (*mouse bites*) | 0,2 mm | Folga de cobre das bordas: ≥ 0,2 mm; tolerância dimensional: ±0,2 mm (regular) e ±0,1 mm (alta precisão); espaçamento entre placas: 1,6 ou 2 mm; largura mínima da aresta de ferramenta: 3 mm (5 mm para montagem SMT na JLCPCB); diâmetro recomendado da mordida: 0,5 a 0,8 mm, com 0,2 a 0,3 mm entre mordidas. |
| Painelização com espaçamento | 2 mm | O espaçamento entre as placas deve ser ≥ 2 mm: espaçamentos estreitos dificultam o roteamento e o corte em V. |
| Painel de PCBs circulares | ≥ 20 × 20 mm | O tamanho da placa redonda individual deve ser ≥ 20 × 20 mm ao usar a painelização da JLCPCB. |


# Diversos projetos feitos com KiCAD

Uma das formas de melhoras o conhecimento é alisando projetos finalizados e funcionais. A partir da url <u>[https://www.kicad.org/made-with-kicad/](https://www.kicad.org/made-with-kicad/)</u> pode-se ter acesso a vários projetos feitos utilizando o KiCAD que servem como inspiração e estudo para outros a serem desenvolvidos. Entre os projetos estão computadores, dispositivos wireless, dispositivos hacker, sensores especiais, controladores para drones. Seguem alguns exemplos:

![Figura 31: A64-OLinuXino é um computador de placa única que roda Linux e Android](figuras/figura-31.png)


A64-OLinuXino Olimex A64-OlinuXino é um computador de placa única que roda Linux e Android. O design é baseado em uma CPU ARM de 64 bits e inclui 1 ou 2 GB DDR3 RAM, 4 GB de memória flash, soquete para cartão microSD, WiFi e BLE4.0, Ethernet, HDMI e saída de áudio.

Uma câmera infravermelha de imagem térmica de código aberto CircuitoDigest Com o objetivo de tornar a Câmera Térmica acessível para amadores e fabricantes, construímos esta câmera térmica DIY usando um microcontrolador ESP32 e um sensor térmico MLX90640. A câmera captura


![Figura 32: Uma câmera infravermelha de imagem térmica de código aberto](figuras/figura-32.png)


imagens térmicas com uma resolução de 32x24 pixels e possui uma tela de 2,4 polegadas para visualização. Ela oferece taxas de atualização ajustáveis, várias paletas de cores e recursos de medição de temperatura entre -40°C e 300°C.

![Figura 33: ANAVI Flex é um Raspberry Pi Shield de código aberto para prototipagem de IoT e aplicações de automação residencial](figuras/figura-33.png)


Shield Flex ANAVI Leon Anavi ANAVI Flex é um Shield Raspberry Pi de código aberto para prototipagem de IoT e aplicações de automação residencial. Ele tem receptor e transmissor infravermelho, relé, campainha, botão, LED RGB e pinos UART para depuração. A placa também suporta módulo de display LCD 1602 e até 5 sensores I2C


![Figura 34: ANAVI Infrared pHAT é uma placa adicional que converte o Raspberry Pi em um poderoso controle remoto](figuras/figura-34.png)


ANAVI pHAT infravermelho Leon Anavi ANAVI Infrared pHAT é uma placa adicional que converte o Raspberry Pi em um poderoso controle remoto. Ela possui dois transmissores IR, receptor IR, três slots para módulos de sensor I2C, pinos UART para depuração e EEPROM com informações do fabricante da placa.

![Figura 35: ANAVI Light pHAT é uma placa add-on Raspberry Pi para controlar tiras de LED RGB de 12 V](figuras/figura-35.png)


ANAVI pHAT leve Leon Anavi ANAVI Light pHAT é uma placa add-on Raspberry Pi para controlar tiras de LED RGB de 12 V. Além disso, tem três slots para módulos de sensor I2C, slot para sensor de movimento PIR, pinos UART para depuração e EEPROM com informações do fabricante da placa.


![Figura 36: controlador de motor de uso geral projetado com kicad em torno do microcontrolador ATmega328 e driver de motor L298P](figuras/figura-36.png)


Placa ATMEGA328 para motor Antonio Morales Um controlador de motor de uso geral projetado com kicad em torno do microcontrolador ATmega328 e driver de motor L298P. Ele pode acionar quatro motores com várias opções de entrada.

![Figura 37: Projetos de energia elétrica EV Inc. Axiom é um controlador de motor de 100kW+ de alta potência e alto desempenho baseado na plataforma VESC](figuras/figura-37.png)


Controlador de motor Axiom Projetos de energia elétrica EV Inc. Axiom é um controlador de motor de 100kW+ de alta potência e alto desempenho baseado na plataforma VESC para compatibilidade com firmware e GUI. Ele é projetado para acionar IGBTs de 650V 600A e vem com muitos recursos de segurança.


![Figura 38: O Projeto CIAA é um projeto de hardware e software aberto iniciado para alavancar o ambiente industrial argentino](figuras/figura-38.png)


CIAA-ACC (HPC) O Projeto CIAA O Projeto CIAA é um projeto de hardware e software aberto iniciado para alavancar o ambiente industrial argentino. O CIAA-ACC é um projeto de PCB de 12 camadas para Computação de Alto Desempenho. Ele tem um Xilinx Zynq-7000 SoC com uma CPU ARM 2x Cortex A9 e um FPGA Kintex-7. O fator de forma é o PCIe-104 expansível. Periféricos: memória DDR3 de 1 GB, Quad SPI Flash, Gbit Ethernet, Micro SDHC, USB 2.0, HDMI de dupla função, PCIe 1x

![Figura 39: O Crazyflie 1.0 é uma plataforma de desenvolvimento de voo aberto](figuras/figura-39.png)


Crazyflie 1.0 Bitcraze AB O Crazyflie 1.0 é uma plataforma de desenvolvimento de voo aberto. É uma plataforma versátil que inclui um poderoso MCU Cortex-M4, rádio de baixa latência de 2,4 GHz e bluetooth de baixa energia. Ele também tem uma porta de expansão que permite adicionar facilmente hardware extra.


![Figura 40: Driverino-Shield é um controlador simples e de baixo consumo para motores BLDC sensorizados](figuras/figura-40.png)


Shield Driverino Michele Santucci Driverino-Shield é um controlador simples e de baixo consumo para motores BLDC sensorizados. O objetivo do projeto era criar um shield Arduino capaz de acionar um motor PM BLDC com potência de cerca de 50-100 W. A placa é equipada com driver TI MCT8316Z BLDC.

![Figura 41: Glasgow é uma ferramenta para explorar interfaces digitais, destinada a desenvolvedores embarcados, engenharia reversa e outras utilidades](figuras/figura-41.png)


RevC de Glasgow Catarina 'quark branco' Glasgow é uma ferramenta para explorar interfaces digitais, destinada a desenvolvedores embarcados, engenharia reversa, arquivamento digitais, entusiastas de eletrônica e todos os outros que desejam se comunicar com uma ampla seleção de dispositivos digitais com alta confiabilidade e o mínimo de complicações.


![Figura 42: HackRF One da Great Scott Gadgets é um periférico de Rádio Definido por Software capaz de transmitir ou receber sinais de rádio de 1 MHz a 6 GHz](figuras/figura-42.png)


HackRF Grandes Gadgets Scott HackRF One da Great Scott Gadgets é um periférico de Rádio Definido por Software capaz de transmitir ou receber sinais de rádio de 1 MHz a 6 GHz. Projetado para permitir testes e desenvolvimento de tecnologias de rádio modernas e de próxima geração, HackRF One é uma plataforma de hardware de código aberto que pode ser usada como um periférico USB ou programada para operação autônoma.

![Figura 43: CSEduino é a resposta para uma placa DIY Arduino de custo muito baixo](figuras/figura-43.png)


CSEduino v4 João Alves CSEduino é a resposta para uma placa DIY Arduino de custo muito baixo. Esta versão tem um pcb de 2 camadas criado com kicad.


![Figura 44: HADES FCS é um sistema de controle de voo de código aberto para veículos aéreos não tripulados (UAVs) projetado completamente do zero](figuras/figura-44.png)


Sistema de controle de voo HADES Filipe Salmony HADES FCS é um sistema de controle de voo de código aberto para veículos aéreos não tripulados (UAVs) projetado completamente do zero. Isso inclui o hardware (PCBs de controle de voo personalizados), firmware STM32 (usando FreeRTOS), filtragem de Kalman para estimativa de estado, algoritmos de controle, estação base, protocolo de comunicação, simulador de voo, processamento de sinal e muito, muito mais.

![Figura 45: O JEMTech-ILDA-Node é um DAC de 16 bits e 6 canais para ILDA de até 400 kpps](figuras/figura-45.png)


JEMTech-ILDA-Node Jan-Erik Matthies O JEMTech-ILDA-Node é um DAC de 16 bits e 6 canais para ILDA de até 400 kpps. Este Projeto é um DAC (conversor digital para analógico) que gera seis sinais diferenciais com base no padrão ILDA (International Laser Display Association) ISP-DB25. O DAC é controlado via barramento SPI (Serial Peripheral Interface).


![Figura 46: Quadro Suculento-JuicyBoard do plugg.ee Labs é uma plataforma de robótica modular de código aberto que pode ser usada para construir impressoras 3D personalizadas, máquinas CNC e muito mais](figuras/figura-46.png)


Quadro Suculento Laboratórios plugg.ee JuicyBoard do plugg.ee Labs é uma plataforma de robótica modular de código aberto que pode ser usada para construir impressoras 3D personalizadas, máquinas CNC e muito mais.

![Figura 47: LABDOS-espectrômetro de radiação ionizante](figuras/figura-47.png)


LABDOS-espectrômetro de radiação ionizante baseado em semicondutores Tecnologias Científicas Universais sro (UST) LABDOS01 é um espectrômetro-dosímetro de código aberto baseado em um diodo PIN de silício e é destinado a pesquisas científicas e propósitos experimentais. Uma porta USB-C ou conector JST-GH protege a energia e a comunicação. O dispositivo pode ser usado estaticamente (localizado em um local específico, por exemplo, laboratório ou base) ou em aplicações móveis (como carros ou UAVs). O espectrômetro é alojado em uma caixa impressa em 3D, que traz resistência mecânica essencial e permite o desenvolvimento futuro de gabinetes de usuário e novas integrações. O objetivo do LABDOS01 é criar um dispositivo de medição de código aberto, acessível, de alta qualidade, confiável e simples — um espectrômetro de energia de radiação para a comunidade científica.

![Figura 48: NUCO-V-placa de desenvolvimento compatível com NUCLEO-64© para as séries STM32F7 e STM32H7 com Black Magic Probe integrado](figuras/figura-48.png)


NUCO-V Dmitry Filimonchuk NUCO-V é uma placa de desenvolvimento compatível com NUCLEO-64© para as séries STM32F7 e STM32H7 com Black Magic Probe integrado


![Figura 49: Open Smartwatch é um relógio inteligente completamente aberto (ECAD/MCAD e software)](figuras/figura-49.png)


Smartwatch aberto pauls_coisas_3d Open Smartwatch é um relógio inteligente completamente aberto (ECAD/MCAD e software). O objetivo é construir um smartwatch de código aberto, com rastreamento por GPS e mapas. Os recursos incluem: ESP32, GPS, Time, sensores MEMS, bateria de íons de lítio, USB serial e armazenamento em cartão microSD.

![Figura 50: display POV de código aberto com resolução de 128 pixels e uma taxa de quadros máxima de 20 FPS](figuras/figura-50.png)


Exibição POV de código aberto usando ESP32 Jóbito José Um display POV de código aberto com resolução de 128 pixels e uma taxa de quadros máxima de 20 FPS. Este display é capaz de exibir imagens e animações. O display é construído em torno do ESP32 SoC e usa registradores de deslocamento 74HC595 para controlar cada pixel. Também criamos uma ferramenta da web, que converterá cada imagem em uma matriz que precisa de apenas aproximadamente 2 KB de espaço de código para cada imagem. Isso faz com que seja possível integrar facilmente vários números de imagens no código sem se preocupar com a limitação de armazenamento.


![Figura 51: O Picuno é a mistura do RP2040 e do Arduino UNO](figuras/figura-51.png)


Picuno Atul Ravi O Picuno é a mistura do RP2040 e do Arduino UNO. Um substituto para o UNO compatível com derivados C e python.

![Figura 52: Saturn é uma placa de desenvolvimento FPGA fácil de usar com Xilinx Spartan-6 FPGA](figuras/figura-52.png)


Saturno Numato Saturn é uma placa de desenvolvimento FPGA fácil de usar com Xilinx Spartan-6 FPGA. Saturn é especialmente projetada para experimentar e aprender design de sistemas com FPGAs. Esta placa de desenvolvimento apresenta FPGA da série Xilinx XC6SLX com dispositivo USB de canal duplo FT2232H da FTDI. A interface USB 2.0 de alta velocidade fornece download de configuração rápido e fácil para o flash SPI integrado. Nenhum programador ou cabo de downloader especial é necessário para baixar o fluxo de bits para a placa.


![Figura 53: ScopeFun é uma plataforma de instrumentação tudo-em-um de código aberto](figuras/figura-53.png)


ScopeFun Dejan Priversek e David Kosenina ScopeFun é uma plataforma de instrumentação tudo-em-um de código aberto. Inclui um osciloscópio, gerador de forma de onda arbitrária, analisador de espectro, analisador lógico e gerador de padrão digital.

![Figura 54: SmartPrintCoreH7x-controladora 3D](figuras/figura-54.png)


SmartPrintCoreH7x Boltz P&D Mergulhe no coração da inovação com o SmartPrintCoreH7x, uma inovadora placa-mãe de impressora 3D de código aberto projetada com paixão pela comunidade e um foco claro em durabilidade, confiabilidade e facilidade de uso. Nascida de uma visão para capacitar fabricantes, inventores e engenheiros ao redor do mundo, a SmartPrintCoreH7x se prepara para se tornar um farol de desenvolvimento colaborativo no mundo da impressão 3D


#### Dosímetros SPACEDOS

Tecnologias Científicas Universais sro (UST)

Os dosímetros SPACEDOS são espectrômetros e dosímetros de radiação ionizante baseados em detectores semicondutores <u>de código aberto</u>. Eles já

![Figura 55: dosímetros SPACEDOS são espectrômetros e dosímetros de radiação ionizante baseados em detectores semicondutores de código aberto](figuras/figura-55.png)



participaram com sucesso de várias

*espectrômetros e dosímetros de radiação*

missões espaciais. O SPACEDOS02 mede,

*ionizante baseados em detectores*

*semicondutores de código aberto.*

por um período de troca regular de tripulação com duração de vários meses, a bordo da Estação Espacial Internacional (ISS). O dosímetro SPACEDOS01 foi modificado para montagem dentro de CubeSats e foi enviado para a órbita da Terra como parte do satélite SOCRAT-R.

![Figura 56: O TERES I é um laptop de hardware e software de código aberto](figuras/figura-56.png)


Teres I Olimex O TERES I é um laptop de hardware e software de código aberto do tipo "faça você mesmo" com processadores ARM64 e x86, incluindo arquivos MCAD.

![Figura 57: Tokay Lite: Câmera ESP32 Edge AIMAXLAB.IO](figuras/figura-57.png)


Tokay Lite: Câmera ESP32 Edge AI MAXLAB.IO Tokay Lite é a placa de desenvolvimento de câmera ESP32 ideal para aplicações de processamento de imagem de baixo consumo de energia na borda. O Tokay Lite pode ser usado como um devkit independente para auxiliar desenvolvedores com uma ferramenta conveniente ou ser incorporado a um sistema maior para aumentá-lo com dados de visão e processamento de imagem.


![Figura 58: O primeiro satélite da UPSat Cubesat 2U construído e entregue pela Libre Space](figuras/figura-58.png)


UPSat Fundação Espaço Livre O primeiro satélite de código aberto O UPSat é um satélite Cubesat 2U construído e entregue pela Libre Space Foundation, iniciado pela Universidade de Patras como parte da missão upsatQB50 com ID GR-02.

![Figura 59: O arsenal USB 2 da Inverse Path é um projeto de hardware de código aberto que implementa um computador do tamanho de um pen drive](figuras/figura-59.png)


Armaria USB Mk II Caminho inverso / F-Secure O arsenal USB da Inverse Path é um projeto de hardware de código aberto que implementa um computador do tamanho de um pen drive. O dispositivo compacto alimentado por USB fornece uma plataforma para desenvolver e executar uma variedade de aplicativos.


# Controle de impedância em circuitos de alta frequência

O **controle de impedância** no design de PCBs é essencial em projetos que envolvem sinais de alta frequência ou transmissão de dados em alta velocidade. Ele garante que as características elétricas das trilhas estejam adequadas para preservar a integridade do sinal, minimizar perdas e evitar reflexões ou interferências.

## Importância do controle de impedância

1. **Integridade do Sinal**: Garante que o sinal transmitido não se degrade ao
longo das trilhas, especialmente em frequências altas.

2. **Redução de Reflexões**: Impedâncias inadequadas causam reflexões de
sinal, o que pode introduzir ruídos e dificultar a comunicação.

3. **Minimização de Crosstalk**: Trilhas próximas com impedância
desbalanceada podem gerar interferências entre si.

4. **Conformidade com Padrões**: Muitas interfaces, como USB, Ethernet e
HDMI, exigem controle de impedância para atender especificações.

## Exemplos de casos onde é necessário o controle de impedância

1. **Linhas Diferenciais**: Interfaces como USB, Ethernet, PCIe e HDMI
requerem pares de trilhas com impedância controlada (tipicamente 90 Ω ou 100 Ω).

2. **Sistemas RF (Rádio Frequência)**: Trilhas para antenas ou sinais de
comunicação sem fio, como Wi-Fi e LoRa, precisam de impedância controlada (tipicamente 50 Ω).

3. **Roteamento de Clock e Dados de Alta Velocidade**: Linhas de sinal para
memórias DDRx ou barramentos de alta velocidade como SPI e LVDS.

4. **Redes de Comunicação Industrial**: Interfaces como CAN e RS485
dependem de impedância consistente para evitar falhas.

## Consequências da Falta de Controle de Impedância

1. Perda de Dados: Em interfaces digitais, sinais distorcidos podem causar erros de transmissão e recepção.
2. Ruído e Interferências: Reflexões nos sinais podem gerar interferência eletromagnética (EMI).
3. Falhas no Circuito: Sistemas RF podem perder potência ou sofrer desajustes na frequência de operação.
4. Desempenho Degradado: Em circuitos de alta velocidade, sinais com alta distorção podem prejudicar a eficiência do sistema.

## Controle de impedância com Kicad

A USB será utilizada como exemplo para o entendimento de como realizar o controle de impedância.

::: {.quadro tipo="importante" titulo="Impedância do par diferencial USB"}
O **USB 2.0** exige **90 Ω ±15%** no par diferencial. O valor de **±10%** que aparece em calculadoras de fabricante é a *tolerância de fabricação* da impedância controlada — a JLCPCB, por exemplo, declara ±10% — e não o requisito da interface. Ao criar a classe de rede no KiCAD, use o valor e a tolerância da interface que está sendo roteada.

*Fontes: Texas Instruments, "USB layout basics"; JLCPCB, "PCB Manufacturing & Assembly Capabilities" (consultado em 2026-09-29).*

:::

**1.. PASSO** Previamente, no editor do esquemático, é necessário identificar com Label as trilhas que terão controle de impedância. Observe os dois exemplos das figuras onde as trilhas são identificadas com USB_D+ e USB_D- e no segundo exemplo classe DP_90R com rótulos pertencentes DP e DN. Os Label’s do par diferencial devem fazer parte de uma classe de rede que terão o controle de impedância. No KiCAD a identificação dos rótulos dias vias diferenciais deve ser finalizadas com +/- ou P/N.

Na USB geralmente são empregados diodos de proteção. O LESD5D5.0 é um diodo de proteção de rápidas resposta capaz de realizar o proteção contra EDS (Electrostatic Discharge Sensitivity) e transientes de tensão.

![Figura 60: Label nas trilhas de comunicação USB com diodos de proteção](figuras/figura-60.png)



![Figura 61: Definição dos labels do par diferencial e atribuição a classe DP_90R](figuras/figura-61.png)



![Figura 62: Label nas trilhas de comunicação USB sem diodos de proteção](figuras/figura-62.png)


controle de impedância. O caso apresentado trata da JLCPCB.

#### Acesse <u>[https://jlcpcb.com/pt/impedance](https://jlcpcb.com/pt/impedance)</u>

e verifique os parâmetros para multicamada. Os dados contidos nessa página serão importantes para uso posterior. A figura a seguir apresenta os parâmetros para PCB multicamada.

![Figura 63: Estrutura com parâmetros para o controle de impedância](figuras/figura-63.png)



Esses parâmetros devem ser inseridos no KiCAD em configuração da placa conforme a figura a seguir.

![Figura 64: Configuração da placa com edição dos parâmetros conforme compatibilidade da JLCPCB](figuras/figura-64.png)



Pode-se também realizar o acesso pelo link contido na página de compatibilidades da JLCPCB

![Figura 65: Página de compatibilidades da JLCPCB. Link para guia e calculadora de impedância](figuras/figura-65.png)


#### Troque a unidade para mm.

![Figura 66: Trilhas não revestidas (uncoated) par diferencial](figuras/figura-66.png)



No site da JLCPCB, na página de controle de impedância, obtenha a constante dielétrica do material prepreg 7628, que corresponde a 4,4.

![Figura 67: Estrutura com parâmetros para o controle de impedância](figuras/figura-67.png)


![Figura 68: Constantes dielétricas obtidas nas páginas de controle de impedância do JLCPCB](figuras/figura-68.png)



Além da constante dielétrica obtenha a altura do material prepreg 7628 (0,21040 mm) conforme a figura anterior. Inclua na calculadora a distância entre trilhas (0,2 mm em Trace Separation (S) ( mm )) valor obtido na configuração da placa classe de rede DP_90R.

![Figura 69: Parâmetros da classe DP_90R](figuras/figura-69.png)



Insira o valor de 90 ohms para a impedância alvo. Outros tipos de barramento possuem impedâncias próprias.

![Figura 70: Calculadora de impedância da Sierra Circuits](figuras/figura-70.png)



Após selecionar a unidade para mm, preencher os parâmetros:

#### Altura do dielétrico: 0,2104 mm

Constante dielétrica para o material prepreg 7628: 4,4

#### Separação entre trilhas: 0,2 mm

#### Impedância alvo: 90 ohms

Clique em **Calcular W** e será obtido o valor da largura da trilha.

Insira o valor calculado da trilha na classe DP_90R conforme a figura.

![Figura 71: Largura da trilha para a classe DP_90R](figuras/figura-71.png)


![Figura 72: Roteamento do par diferencial](figuras/figura-72.png)



Devido a geometria das trilhas do par diferencial, mas mesmas não possuem o mesmo comprimento. Logo, será necessário realizar alguns ajustes para garantir que os sinais elétricos sejam recebidos no mesmo tempo.

Se houver uma diferença de comprimento (ou atraso), chamada de **skew**, isso pode causar:

- Jitter (variação temporal) no sinal.
- Degradação da imunidade a ruído (o modo comum não é cancelado corretamente).
- Erros de comunicação em altas frequências. Verifique o comprimento de cada trilha, para isso use **a tecla de atalho “7”.**
![Figura 73: Comprimento da trilha do par diferencial](figuras/figura-73.png)



![Figura 74: Comprimento da trilha do par diferencial](figuras/figura-74.png)


 Conforme as figuras anteriores, pode-se observar que as trilhas possuem comprimentos de 31,45 mm e 29,9588 mm. Deve-se preceder com os ajuste de comprimento para equalização.

Use a **tecla de atalho “8”**, para clique com o botão direito do mouse na maior trilha e selecione ***Configurações do ajuste de comprimento***. Observe a figura a seguir.

![Figura 75: Ajuste do comprimento desejado](figuras/figura-75.png)



Defina o comprimento alvo igual o comprimento da maior trilha ou pouco superior, no exemplo o valor é de 33 mm.

![Figura 76: Maior trilha com comprimento 33](figuras/figura-76.png)



A tecla de atalho 7 deverá ser usada para o ajuste de comprimento da outra trilha.

![Figura 77: Ajuste de comprimento da trilha](figuras/figura-77.png)



A figura a seguir apresenta resultado final cujo comprimento de cada trilha é de 33mm.

![Figura 78: Trilhas par diferencial com comprimentos iguais e impedância ajustada](figuras/figura-78.png)



# Circuitos para interfaceamento de entrada e saída digital com microcontrolador

As entradas e saídas digitais atuam como interface entre o MCU e os transdutores ou atuadores no campo. Há diversas formas de projetar os circuitos de entrada e saída, adaptáveis aos diferentes sinais utilizados.

## Entradas digitais em C.C.

Detectam e convertem sinais de comutação de entrada em níveis lógicos de tensão usados na porta digital do MCU. Os módulos de entradas e saídas digitais podem ser projetados para trabalhar tanto com sinais de tensão contínua, quanto sinais alternados. Para os níveis de C.C., o padrão industrial adotado é de 24 V, o qual possui uma relação sinal/ruído adequada para ambientes industriais e 110 e 220 V, para níveis CA. A figura a seguir apresenta um exemplo esquemático para sinal da entrada digital.

![Figura 79: Exemplo esquemático para sinal discreto de campo tipo P](figuras/figura-79.png)



Um aspecto importante a ser considerado no esquema das entradas é que a parte lógica do circuito é desacoplada do sinal de entrada através de um acoplador óptico, o que assegura a integridade do circuito, caso ocorram problemas com o sinal de entrada, além de aumentar a imunidade a ruídos do sistema.

No fotoacoplador existe um filtro formado por C1, R3 e R4, este filtro fará com que ruídos existentes na alimentação, típicas de ambientes de redes elétricas industriais, não causem um acionamento indevido na porta do MCU, devido ao filtro, normalmente as entradas digitais não deverão responder a uma freqüência maior que 1 kHz, exceto naquelas entradas especiais de contadores rápidos.

## Entradas digitais em C.A.

Semelhante às entradas de corrente contínua, as entradas digitais de corrente alternada leem sinais do processo, oferecendo a vantagem de permitir maior distância entre o MCU e o transdutor devido à melhor relação sinal/ruído em tensões de 110 V ou 220 V. Geralmente, em distâncias superiores a 50 m em ambientes ruidosos, é recomendável considerar o uso de entradas CA. Contudo, ao trabalhar com níveis de tensão alternada, é fundamental adotar cuidados extras com a isolação geral da instalação para garantir segurança e confiabilidade.

![Figura 80: Exemplo esquemático para sinal CA discreto de campo](figuras/figura-80.png)



## Saída digitais em C.C.

No exemplo do esquemático deve-se ligar a carga entre o potencial negativo da fonte de alimentação de 24 VCC e o ponto de saída (J4 e J5). A figura a seguir exemplifica o circuito de uma saída digital tipo P.

![Figura 81: Exemplo esquemático para saída digital CC](figuras/figura-81.png)



## Saída digitais em C.A. com TRIAC

A saída em corrente alternada pode ser usado para acionar diretamente bobinas de contatores CA ou outra carga conforme os dimensionamento dos circuitos de saída. A alimentação normalmente é do tipo full range, ou seja, é possível ligar cargas cuja alimentação esteja entre 90 VAC a 240 VAC. A figura a seguir exemplifica o circuito de uma saída digital em corrente alternada.

![Figura 82: Exemplo esquemático para saída digital com acionamento de carga CA. 97](figuras/figura-82.png)



No exemplo do circuito pode-se observar alguns elementos importantes:

- Varistor: protege contra o surto de tensão;
- RC: protege contra disparo indevido do TRIAC que está isolado do sistema por acoplador ótico;
- TRIAC Isolado: normalmente é utilizado TRIAC Isolado com função de zero crossing; assim, só ocorrerá o acionamento ou desacionamento no momento da passagem do “0” da senóide, evitando, por exemplo, a formação de faíscas quando chaveamos cargas indutivas.

## Saída digitais a Rele

Esse tipo de saída é bem versátil, pois pode comutar tanto cargas em corrente contínua (C.C.) quanto em corrente alternada (C.A.). No entanto, as saídas a relé apresentam desgaste mecânico proporcional ao número de chaveamentos e à corrente que passa pelos contatos. Para aumentar a vida útil do relé, pode-se utilizar um relé auxiliar externo, inserindo-o entre a saída do esquemático e a carga, ou ainda, intercalar um relé de maior potência ou uma chave estática, o que ajuda a "proteger" os contatos do relé interno. As saídas a relé geralmente têm um tempo de resposta mais lento quando comparadas às saídas a transistor ou a TRIAC. A figura a seguir ilustra o circuito de uma saída com contato seco ou relé.

![Figura 83: Exemplo esquemático para saída digital com acionamento de carga CA ou CC](figuras/figura-83.png)



# Referências WEB

- <u>[https://jlcpcb.com](https://jlcpcb.com)</u>
- <u>[https://docs.kicad.org/8.0/en/kicad/kicad.html](https://docs.kicad.org/8.0/en/kicad/kicad.html)</u>
- <u>[https://www.protoexpress.com/tools/](https://www.protoexpress.com/tools/)</u>
- <u>[https://blog.raisa.com.br/analise-do-processo-de-fabricacao-de-placas-de-](https://blog.raisa.com.br/analise-do-processo-de-fabricacao-de-placas-de-)</u> <u>circuito-impresso-pcb/</u>
- <u>[https://embarcados.com.br/acabamento-de-superficie-em-pci/](https://embarcados.com.br/acabamento-de-superficie-em-pci/)</u>
- <u>[https://embarcados.com.br/10-mandamentos-da-pcb/#1-Planos-de-Terra-de-](https://embarcados.com.br/10-mandamentos-da-pcb/#1-Planos-de-Terra-de-)</u> <u>uma-PCB</u>
- <u>[https://delorenzoglobal.com/](https://delorenzoglobal.com/)</u>
- <u>[https://youtu.be/NYrRZNzBmsk](https://youtu.be/NYrRZNzBmsk)</u>

