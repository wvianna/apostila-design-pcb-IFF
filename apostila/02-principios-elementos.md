# 2. Princípios e elementos básicos das PCBs

As Placas de Circuito Impresso (PCBs) constituem elementos fundamentais no universo da eletrônica, projetadas para interconectar e sustentar componentes eletrônicos de forma organizada e funcional. Neste capítulo, serão apresentados os princípios que norteiam o funcionamento das PCBs, além de uma análise dos principais elementos que as compõem.

## 2.1. Funções principais de uma PCB

- **Suporte físico**: Proporciona estrutura mecânica para fixação e posicionamento dos componentes eletrônicos.
- **Conexão elétrica**: Viabiliza a transmissão de sinais elétricos entre os componentes, por meio de trilhas condutoras.
- **Isolamento elétrico**: Mantém circuitos isolados, prevenindo curtos-circuitos e interferências indesejadas.
- **Dissipação térmica**: Facilita a transferência do calor gerado pelos componentes durante sua operação, contribuindo para a estabilidade térmica do sistema

## 2.2. Principais elementos da PCB

A fabricação de Placas de Circuito Impresso (PCBs) depende diretamente da seleção criteriosa dos materiais constituintes, que são determinantes para a qualidade, confiabilidade e desempenho final da placa.

### 2.2.1. Substrato

O substrato é a base estrutural das PCBs, servindo como suporte para a montagem dos componentes eletrônicos. O material mais comumente utilizado é a fibra de vidro (FR4), amplamente adotada por sua estabilidade térmica, alta resistência à decomposição e baixo custo. Em projetos que exigem alta frequência, materiais como PTFE (politetrafluoretileno) são preferidos devido à sua constante dielétrica mais baixa e perdas reduzidas, embora apresentem maior dificuldade de processamento. Em projetos de alta frequência, onde a constante dielétrica e baixas perdas são cruciais, placas à base de PTFE (politetrafluoretileno) podem ser utilizadas, embora sejam mais difíceis de processar. O substrato de fenolite também pode ser utilizado, mas as propriedades mecânicas são inferiores quando comparado com o FR4.

### 2.2.2. Cobre

O cobre é um elemento essencial nas PCBs, utilizado para formar as trilhas condutoras que conectam os componentes eletrônicos. Essas trilhas, criadas a partir de placas revestidas com camadas de cobre, garantem a condução eficiente de sinais elétricos. Para projetos de dupla face ou multicamadas, a aderência do cobre ao substrato, especialmente ao FR4, é uma característica crucial para a durabilidade e desempenho do circuito. As placas de cobre revestidas são obtidas a partir do substrato (geralmente FR4) com uma camada de cobre aderida, geralmente em ambos os lados (dupla face). A aderência do cobre ao FR4 é bastante sólida, enquanto a aderência ao PTFE pode ser mais desafiadora.

### 2.2.3. Máscara de solda

A máscara de solda é uma camada de polímero aplicada sobre as áreas expostas de cobre nas PCBs, com a função de proteger contra oxidação, prevenir curtos- circuitos e facilitar o processo de soldagem. Disponível em várias cores, como verde,

vermelho e azul, essa camada contribui para a durabilidade e confiabilidade da placa, ao mesmo tempo que oferece um acabamento estético. A máscara de solda geralmente é composta por uma camada de polímero e apresenta cores como verde escuro, vermelho, azul, preto, branco ou outra cor disponível no fabricante.

![Figura 1: [https://embarcados.com.br/wp-content/uploads/2016/08/Acabamento-de-](https://embarcados.com.br/wp-content/uploads/2016/08/Acabamento-de-) superf%C3%ADcie-destaque-1.jpg.webp](figuras/figura-01.png)

*Figura 1: [https://embarcados.com.br/wp-content/uploads/2016/08/Acabamento-de-](https://embarcados.com.br/wp-content/uploads/2016/08/Acabamento-de-) superf%C3%ADcie-destaque-1.jpg.webp*


*[https://embarcados.com.br/wp-content/uploads/201*](https://embarcados.com.br/wp-content/uploads/201*)

*6/08/Acabamento-de-superf%C3%ADcie-destaque-*

*1.jpg.webp*

### 2.2.4. Camada de serigrafia

A camada de serigrafia é composta por tinta aplicada na superfície da PCB, destinada a fornecer informações úteis, como identificação de componentes, orientações de montagem e dados de fabricação. Essa camada desempenha um papel crucial na montagem e manutenção de dispositivos eletrônicos, facilitando a localização precisa de componentes e contribuindo para uma montagem eficiente e com menor probabilidade de erros.

Ao compreender os principais elementos das Placas de Circuito Impresso e suas funções, é possível garantir que o processo de fabricação de PCBs resulte em produtos de alta qualidade, atendendo às demandas específicas de cada projeto eletrônico.

![Figura 2: [https://resources.altium.com/sites/default/files/inline-images/pcb-silk-3.png](https://resources.altium.com/sites/default/files/inline-images/pcb-silk-3.png)](figuras/figura-02.png)

*Figura 2: [https://resources.altium.com/sites/default/files/inline-images/pcb-silk-3.png](https://resources.altium.com/sites/default/files/inline-images/pcb-silk-3.png)*


*[https://resources.altium.com/sites/default/files/inli*](https://resources.altium.com/sites/default/files/inli*)

*ne-images/pcb-silk-3.png*

### 2.2.5. Acabamento de superfície

Surface finish, ou Acabamento de Superfície, compõe uma interface crítica entre os componentes e o local onde serão posicionados para solda, também chamada de SMOBC (Solder Mask Over Bare Copper) – Máscara de solda sobre cobre exposto. Essa superfície, sem nenhum tratamento, ficaria com os pads de cobre expostos, o que resultaria em oxidação, deterioração e consequente perda de funcionalidade.

O acabamento de superfície possui essencialmente duas funções:

- Proteger o circuito de cobre exposto;
- Prover uma superfície com maior solderabilidade, bem como reforçar o processo de montagem, promovendo uma junta de solda confiável com alto desempenho da PCB a longo prazo. O processo de acabamento superficial consiste em cobrir com metal o material
orgânico os elementos de cobre não cobertos pela máscara de solda. Este processo protege o cobre e facilita a soldagem dos componentes seja pelo processo manual, forno ou outra técnica.

As técnicas mais comuns para realizar o acabamento superficial são:

- **HASL/HASL Lead free (Hot Air Solder Level)**

![Figura 3: Hot Air Solder Level-A](figuras/figura-03.png)

*Figura 3: Hot Air Solder Level-A*


![Figura 4: Hot Air Solder Level-B](figuras/figura-04.png)

*Figura 4: Hot Air Solder Level-B*


- **Imersão em Estanho**

![Figura 5: Imersão em Estanho-A](figuras/figura-05.png)

*Figura 5: Imersão em Estanho-A*


![Figura 6: Imersão em Estanho-B](figuras/figura-06.png)

*Figura 6: Imersão em Estanho-B*


- **Imersão em Prata**

![Figura 7: Imersão em Prata-A](figuras/figura-07.png)

*Figura 7: Imersão em Prata-A*


![Figura 8: Imersão em Prata-B](figuras/figura-08.png)

*Figura 8: Imersão em Prata-B*


- **OSP (Organic Solderability Preservative)**

![Figura 9: Organic Solderability Preservative-A](figuras/figura-09.png)

*Figura 9: Organic Solderability Preservative-A*


![Figura 10: Organic Solderability Preservative-B](figuras/figura-10.png)

*Figura 10: Organic Solderability Preservative-B*


- **GOLD – ENIG (Electroless Nickel Immersion Gold)**

![Figura 11: Electroless Nickel Immersion Gold) - A](figuras/figura-11.png)

*Figura 11: Electroless Nickel Immersion Gold) - A*


![Figura 12: Electroless Nickel Immersion Gold) - B](figuras/figura-12.png)

*Figura 12: Electroless Nickel Immersion Gold) - B*


•*Immersion Gold) - B*

*Immersion Gold) - A*

#### ENEPIG (Electroless Nickel Electroless

#### Palladium Immersion Gold)

![Figura 13: Electroless Nickel Electroless Palladium Immersion Gold-A](figuras/figura-13.png)

*Figura 13: Electroless Nickel Electroless Palladium Immersion Gold-A*


![Figura 14: Electroless Nickel Electroless Palladium Immersion Gold-B](figuras/figura-14.png)

*Figura 14: Electroless Nickel Electroless Palladium Immersion Gold-B*


- **Gold – Hard Gold**

![Figura 15: Hard Gold-A](figuras/figura-15.png)

*Figura 15: Hard Gold-A*


![Figura 16: Hard Gold-B](figuras/figura-16.png)

*Figura 16: Hard Gold-B*


## 2.4. Categorias de PCBs

- **PCBs de Face Única**: Contêm uma única camada de cobre em um dos lados do substrato, utilizadas em circuitos simples e de baixo custo.
- **PCBs de Dupla Face**: Possuem trilhas condutoras em ambos os lados do substrato, conectadas por vias, sendo amplamente usadas em designs intermediários.
- **PCBs Multicamadas**: Incorporam múltiplas camadas de cobre intercaladas com materiais isolantes, permitindo designs mais complexos e de alta densidade, comuns em dispositivos como smartphones e computadores. Compreender os princípios e os elementos que compõem as PCBs é o primeiro
passo para dominar o design dessas placas essenciais.
