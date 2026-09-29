# 9. Controle de impedância em circuitos de alta frequência

O **controle de impedância** no design de PCBs é essencial em projetos que envolvem sinais de alta frequência ou transmissão de dados em alta velocidade. Ele garante que as características elétricas das trilhas estejam adequadas para preservar a integridade do sinal, minimizar perdas e evitar reflexões ou interferências.

### 9.1. Importância do controle de impedância

1. **Integridade do Sinal**: Garante que o sinal transmitido não se degrade ao
longo das trilhas, especialmente em frequências altas.

2. **Redução de Reflexões**: Impedâncias inadequadas causam reflexões de
sinal, o que pode introduzir ruídos e dificultar a comunicação.

3. **Minimização de Crosstalk**: Trilhas próximas com impedância
desbalanceada podem gerar interferências entre si.

4. **Conformidade com Padrões**: Muitas interfaces, como USB, Ethernet e
HDMI, exigem controle de impedância para atender especificações.

### 9.2. Exemplos de casos onde é necessário o controle de impedância

1. **Linhas Diferenciais**: Interfaces como USB, Ethernet, PCIe e HDMI
requerem pares de trilhas com impedância controlada (tipicamente 90 Ω ou 100 Ω).

2. **Sistemas RF (Rádio Frequência)**: Trilhas para antenas ou sinais de
comunicação sem fio, como Wi-Fi e LoRa, precisam de impedância controlada (tipicamente 50 Ω).

3. **Roteamento de Clock e Dados de Alta Velocidade**: Linhas de sinal para
memórias DDRx ou barramentos de alta velocidade como SPI e LVDS.

4. **Redes de Comunicação Industrial**: Interfaces como CAN e RS485
dependem de impedância consistente para evitar falhas.

### 9.3. Consequências da Falta de Controle de Impedância

1. Perda de Dados: Em interfaces digitais, sinais distorcidos podem causar erros de transmissão e recepção.
2. Ruído e Interferências: Reflexões nos sinais podem gerar interferência eletromagnética (EMI).
3. Falhas no Circuito: Sistemas RF podem perder potência ou sofrer desajustes na frequência de operação.
4. Desempenho Degradado: Em circuitos de alta velocidade, sinais com alta distorção podem prejudicar a eficiência do sistema.

## 9.4. Controle de impedância com KiCad

A USB será utilizada como exemplo para o entendimento de como realizar o controle de impedância.

::: {.quadro tipo="importante" titulo="Impedância do par diferencial USB"}
O **USB 2.0** exige **90 Ω ±15%** no par diferencial. O **±10%** que aparece nas calculadoras e nas páginas dos fabricantes **não** é o requisito da interface: é a *tolerância de fabricação* da impedância controlada. O guia da Sierra Circuits registra ±10% como tolerância padrão e ±5% como opção mais apertada; a JLCPCB adota os mesmos valores. Ao criar a classe de rede no KiCAD, use o valor da interface que está sendo roteada e confirme a tolerância com o fabricante.

*Fontes: Texas Instruments, "USB layout basics" (90 Ω ±15%); Sierra Circuits, "Controlled Impedance Design Guide", out./2022, §1.5 (±10% padrão, ±5% apertada — em `livros/`); JLCPCB, "PCB Manufacturing & Assembly Capabilities" (consultado em 2026-09-29).*
:::

**1º PASSO** Previamente, no editor do esquemático, é necessário identificar com rótulos (*labels*) as trilhas que terão controle de impedância. Observe os dois exemplos das figuras: no primeiro, as trilhas são identificadas com USB_D+ e USB_D-; no segundo, com a classe DP_90R e os rótulos DP e DN. Os rótulos do par diferencial devem fazer parte de uma classe de rede que terá o controle de impedância. No KiCAD, a identificação dos rótulos das vias diferenciais deve ser finalizada com **+/-** ou **P/N**.

Na USB geralmente são empregados diodos de proteção. O LESD5D5.0 é um diodo de proteção de resposta rápida, capaz de proteger contra ESD (*Electrostatic Discharge* — descarga eletrostática) e transientes de tensão.

![Figura 60: Label nas trilhas de comunicação USB com diodos de proteção](figuras/figura-60.png)

*Figura 60: Label nas trilhas de comunicação USB com diodos de proteção*


![Figura 61: Definição dos labels do par diferencial e atribuição a classe DP_90R](figuras/figura-61.png)

*Figura 61: Definição dos labels do par diferencial e atribuição a classe DP_90R*


![Figura 62: Label nas trilhas de comunicação USB sem diodos de proteção](figuras/figura-62.png)

*Figura 62: Label nas trilhas de comunicação USB sem diodos de proteção*

**2º PASSO** Após definir o fabricante de sua escolha, acesse as informações relativas ao controle de impedância. O caso apresentado trata da JLCPCB.

Acesse [https://jlcpcb.com/pt/impedance](https://jlcpcb.com/pt/impedance) e verifique os parâmetros para multicamada. Os dados contidos nessa página serão importantes para uso posterior. A figura a seguir apresenta os parâmetros para PCB multicamada.

![Figura 63: Estrutura com parâmetros para o controle de impedância](figuras/figura-63.png)

*Figura 63: Estrutura com parâmetros para o controle de impedância*


Esses parâmetros devem ser inseridos no KiCAD em configuração da placa conforme a figura a seguir.

![Figura 64: Configuração da placa com edição dos parâmetros conforme compatibilidade da JLCPCB](figuras/figura-64.png)

*Figura 64: Configuração da placa com edição dos parâmetros conforme compatibilidade da JLCPCB*


Pode-se também realizar o acesso pelo link contido na página de compatibilidades da JLCPCB

![Figura 65: Página de compatibilidades da JLCPCB. Link para guia e calculadora de impedância](figuras/figura-65.png)

*Figura 65: Página de compatibilidades da JLCPCB. Link para guia e calculadora de impedância*

**3º PASSO** Use a calculadora de impedância para definir os parâmetros do par diferencial. A calculadora da JLCPCB está em [https://jlcpcb.com/pcb-impedance-calculator](https://jlcpcb.com/pcb-impedance-calculator); a da Sierra Circuits, em [https://www.protoexpress.com/tools/pcb-impedance-calculator/](https://www.protoexpress.com/tools/pcb-impedance-calculator/). Selecione **sem revestimento** (*uncoated*) e **par diferencial** e clique em **OPEN**. Em seguida, troque a unidade para milímetros.

![Figura 66: Trilhas não revestidas (uncoated) par diferencial](figuras/figura-66.png)

*Figura 66: Trilhas não revestidas (uncoated) par diferencial*


No site da JLCPCB, na página de controle de impedância, obtenha a constante dielétrica do material prepreg 7628, que corresponde a 4,4.

![Figura 67: Estrutura com parâmetros para o controle de impedância](figuras/figura-67.png)

*Figura 67: Estrutura com parâmetros para o controle de impedância*

![Figura 68: Constantes dielétricas obtidas nas páginas de controle de impedância do JLCPCB](figuras/figura-68.png)

*Figura 68: Constantes dielétricas obtidas nas páginas de controle de impedância do JLCPCB*


Além da constante dielétrica obtenha a altura do material prepreg 7628 (0,21040 mm) conforme a figura anterior. Inclua na calculadora a distância entre trilhas (0,2 mm em Trace Separation (S) ( mm )) valor obtido na configuração da placa classe de rede DP_90R.

![Figura 69: Parâmetros da classe DP_90R](figuras/figura-69.png)

*Figura 69: Parâmetros da classe DP_90R*


Insira o valor de 90 ohms para a impedância alvo. Outros tipos de barramento possuem impedâncias próprias.

![Figura 70: Calculadora de impedância da Sierra Circuits](figuras/figura-70.png)

*Figura 70: Calculadora de impedância da Sierra Circuits*


Após selecionar a unidade para milímetros, preencha os parâmetros:

- **Altura do dielétrico:** 0,2104 mm;
- **Constante dielétrica** do material prepreg 7628: 4,4;
- **Separação entre trilhas** (*Trace Separation*, S): 0,2 mm;
- **Impedância alvo:** 90 Ω.

Clique em **Calcular W** e será obtido o valor da largura da trilha.

Insira o valor calculado da trilha na classe DP_90R conforme a figura.

![Figura 71: Largura da trilha para a classe DP_90R](figuras/figura-71.png)

*Figura 71: Largura da trilha para a classe DP_90R*

**4º PASSO** Realize o roteamento do par diferencial. Utilize a **tecla de atalho “6”**.

![Figura 72: Roteamento do par diferencial](figuras/figura-72.png)

*Figura 72: Roteamento do par diferencial*


Devido à geometria das trilhas do par diferencial, as duas não possuem o mesmo comprimento. Logo, será necessário realizar alguns ajustes para garantir que os sinais elétricos sejam recebidos no mesmo instante.

Se houver uma diferença de comprimento (ou de atraso), chamada de **skew**, isso pode causar:

- *Jitter* (variação temporal) no sinal;
- degradação da imunidade a ruído — o modo comum deixa de ser cancelado corretamente;
- erros de comunicação em altas frequências.

A correção é acrescentar *serpentinas* na trilha mais curta, o mais próximo possível do ponto onde a diferença começou (uma via, uma curva ou um conector). Uma serpentina colocada longe desse ponto iguala o comprimento total, mas não corrige o trecho em que os sinais estavam desalinhados. Como a velocidade de propagação muda de uma camada para outra, mantenha as duas trilhas do par na mesma camada sempre que houver casamento de comprimento a fazer.

*Fonte: Sierra Circuits, "Controlled Impedance Design Guide", out./2022, §3.5.5 (Length matching) — em `livros/`.*

Verifique o comprimento de cada trilha; para isso, use a **tecla de atalho “7”**.

![Figura 73: Comprimento da trilha do par diferencial](figuras/figura-73.png)

*Figura 73: Comprimento da trilha do par diferencial*


![Figura 74: Comprimento da trilha do par diferencial](figuras/figura-74.png)

*Figura 74: Comprimento da trilha do par diferencial*

Conforme as figuras anteriores, pode-se observar que as trilhas possuem comprimentos de 31,45 mm e 29,9588 mm. Deve-se proceder aos ajustes de comprimento para equalização.

Use a **tecla de atalho “8”** e clique com o botão direito do mouse na maior trilha; em seguida, selecione **Configurações do ajuste de comprimento**. Observe a figura a seguir.

![Figura 75: Ajuste do comprimento desejado](figuras/figura-75.png)

*Figura 75: Ajuste do comprimento desejado*


Defina o comprimento alvo igual ao comprimento da maior trilha ou pouco superior; no exemplo, o valor é de 33 mm.

![Figura 76: Maior trilha com comprimento 33](figuras/figura-76.png)

*Figura 76: Maior trilha com comprimento 33*


A tecla de atalho 7 deverá ser usada para o ajuste de comprimento da outra trilha.

![Figura 77: Ajuste de comprimento da trilha](figuras/figura-77.png)

*Figura 77: Ajuste de comprimento da trilha*


A figura a seguir apresenta o resultado final, cujo comprimento de cada trilha é de 33 mm.

![Figura 78: Trilhas par diferencial com comprimentos iguais e impedância ajustada](figuras/figura-78.png)

*Figura 78: Trilhas par diferencial com comprimentos iguais e impedância ajustada*
