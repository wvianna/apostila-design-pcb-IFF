# 7. KiCad

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

## 7.1. Motivos para usar o Kicad

O KiCad apresenta diversas vantagens em relação a outros softwares concorrentes de design eletrônico. Algumas dessas vantagens incluem:

- **Código aberto e gratuito:** O KiCad é um software de código aberto, o que significa que você pode utilizá-lo sem custo e ter acesso ao código-fonte. Isso facilita a colaboração e permite que a comunidade de usuários contribua com melhorias e correções.
- **Multiplataforma:** O KiCad é compatível com Windows, macOS e Linux, o que o torna uma opção acessível para diferentes sistemas operacionais.
- **Comunidade ativa:** O KiCad possui uma comunidade grande e ativa de desenvolvedores e usuários. Isso significa que você pode encontrar suporte, tutoriais, bibliotecas adicionais e recursos para melhorar sua experiência com a ferramenta.
- **Integração e recursos completos:** O KiCad oferece um conjunto completo de recursos, incluindo editor esquemático, editor de PCB, bibliotecas de componentes, visualização 3D e gerenciamento de projetos. Isso permite que você realize todo o processo de design em uma única ferramenta, evitando a necessidade de importar e exportar projetos entre diferentes aplicativos.
- **Bibliotecas de componentes atualizadas:** O KiCad inclui uma biblioteca de componentes eletrônicos padrão e também permite que você crie e gerencie suas próprias bibliotecas. Além disso, a comunidade contribui com bibliotecas de alta qualidade, garantindo que você tenha acesso a uma ampla variedade de componentes para seus projetos.
- **Atualizações frequentes:** O KiCad é continuamente atualizado e melhorado pela comunidade de desenvolvedores, garantindo que você tenha acesso a recursos e correções de bugs mais recentes.

- **Sem limitações de tamanho de projeto:** Ao contrário de algumas ferramentas concorrentes que impõem restrições ao tamanho dos projetos na versão gratuita, o KiCad não possui essas limitações, permitindo que você trabalhe em projetos de qualquer tamanho sem custos adicionais.
- **Importação de arquivos de outros EDAs:** Documentos esquemáticos do Altium Designer, Circuit Studio, Circuit Maker; PCB de designer Altium; Fabricante de circuitos Altium PCB; Altium Circuito Estúdio PCB;; CB ASCII P- Cad 200x; PCB Fabmaster
## 7.2. Instalação do KiCAD

- Existem versões para Windows, Linux, macOS e Docker. Utilize a url apresentada para obter a versão desejada. <u>[https://www.kicad.org/download/](https://www.kicad.org/download/)</u>
## 7.3. Usando o gerenciador de projetos KiCad

O gerenciador de projetos KiCad é uma ferramenta que cria e abre projetos KiCad e inicia as outras ferramentas KiCad (editores de esquemas e placas, visualizador Gerber e ferramentas utilitárias).

![Figura 22: Gerenciador de Projetos. Fonte: [https://docs.kicad.org/8.0/en/kicad/kicad.html#:~:text=Usando%20o](https://docs.kicad.org/8.0/en/kicad/kicad.html#:~:text=Usando%20o) %20gerenciador,editores%20e%20ferramentas](figuras/figura-22.png)

*Figura 22: Gerenciador de Projetos. Fonte: [https://docs.kicad.org/8.0/en/kicad/kicad.html#:~:text=Usando%20o](https://docs.kicad.org/8.0/en/kicad/kicad.html#:~:text=Usando%20o) %20gerenciador,editores%20e%20ferramentas*


A janela do gerenciador de projetos do KiCad é composta por uma visualização em árvore à esquerda, mostrando os arquivos associados ao projeto aberto, e um iniciador à direita, contendo atalhos para os vários editores e ferramentas.

## 7.4. Arquivos e pastas KiCad

O KiCad cria e usa arquivos com as seguintes extensões de arquivo (e pastas) específicas para edição de esquemas e placas.

### 7.4.1. Arquivos de projeto

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

Tabela de biblioteca de símbolos: lista de bibliotecas de símbolos

sym-lib-table disponíveis no editor de esquemáticos.

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

### 7.4.2. Armazenando e enviando arquivos KiCad

Os arquivos de esquema e placa do KiCad contêm todos os símbolos esquemáticos e footprints usados no design, então você pode fazer backup ou enviar esses arquivos por si só sem problemas. Algumas informações importantes do design são armazenadas no arquivo do projeto (.kicad_pro), então se você estiver enviando um design completo, certifique-se de incluí-lo. Alguns arquivos, como o arquivo project-local settings (.kicad_prl) e o fp- info-cachearquivo, não são necessários para enviar com seu projeto. Se você usa um sistema de controle de versão como o Git para manter o controle de seus projetos KiCad, você pode querer adicionar esses arquivos à lista de arquivos ignorados para que eles não sejam rastreados. Outros detalhes inclusive de configurações pode ser obtidos em:

<u>[https://docs.kicad.org/8.0/en/kicad/kicad.html](https://docs.kicad.org/8.0/en/kicad/kicad.html)</u>

## 7.5. Workflow do Kicad

O fluxo de trabalho (workflow) do KiCad geralmente segue as etapas comuns de projeto de circuitos eletrônicos e design de PCB. Entretanto, conforme o desejo do

projetista, algumas etapas do workflow podem ser alteradas ou até suprimidas durante o design. Ver exemplo na figura.

![Figura 23: Workflow básico KiCAD. fonte: [https://www.slideshare.net/baoshi1/why-](https://www.slideshare.net/baoshi1/why-) and-how-to-switch-to-kicad](figuras/figura-23.png)

*Figura 23: Workflow básico KiCAD. fonte: [https://www.slideshare.net/baoshi1/why-](https://www.slideshare.net/baoshi1/why-) and-how-to-switch-to-kicad*


Abaixo estão as principais etapas do workflow do KiCad:

### 7.5.1. Esquemático (Schematic):

- Crie um novo projeto no KiCad.
- Configure a página e esquemático.
- Desenhe o esquemático do circuito eletrônico usando o editor esquemático do KiCad.
- Adicione componentes eletrônicos ao esquemático, selecionando-os a partir da biblioteca de componentes ou criando novos componentes, se necessário.
- Conecte os componentes eletrônicos usando os símbolos de fios ou barramentos.

- Preencha os designadores dos componentes eletrônicos
## 7.5.2. Associação de Footprints (Assigning Footprints):

- Após finalizar o esquemático, associe os componentes com suas respectivas footprints no layout da PCB. O footprint é a representação física do componente na placa de circuito impresso.
### 7.5.3. Layout da PCB (PCB Layout):

- Abra o editor de PCB e importe o netlist do esquemático para criar o layout da placa de circuito impresso (PCB).
- Posicione os componentes na placa e organize-os de acordo com suas preferências e requisitos de design.
- Trace as trilhas de cobre para conectar os componentes eletrônicos corretamente.
- Realize o roteamento das trilhas de forma a evitar cruzamentos indesejados e garantir o melhor desempenho do circuito.
### 7.5.4. Visualização 3D (3D Visualization):

- Utilize a visualização 3D do KiCad para verificar a colocação dos componentes na PCB e garantir que não haja interferências ou problemas de montagem.
### 7.5.5. Verificação do Design (Design Verification):

- Realize uma revisão completa do projeto, verificando a conformidade das trilhas, a ausência de erros de conexão, e garantindo que todas as regras de projeto estejam sendo seguidas.

### 7.5.6. Geração dos Arquivos de Fabricação (Manufacturing Files):

- Após concluir o design da PCB, gere os arquivos necessários para a fabricação da placa, incluindo Gerber files, Drill files, entre outros.
## 7.6. Importação e utilização de bibliotecas de componentes no KiCad

O KiCad possui várias bibliotecas de componentes, mas existem outras disponíveis online.

#### As bibliotecas são:

- symbols → símbolos utilizados no editor de esquemático do KiCad
- footprints → footprints utilizados no editor da PCB
- packages3D → modelos 3D utilizados na renderização feita no visualizador da PCB
![Figura 25: Exemplo de footprint](figuras/figura-25.png)

*Figura 25: Exemplo de footprint*


![Figura 26: Exemplo de modelos 3D](figuras/figura-26.png)

*Figura 26: Exemplo de modelos 3D*


![Figura 24: Exemplo de símbolo](figuras/figura-24.png)

*Figura 24: Exemplo de símbolo*


### 7.6.1. Utilização de novas bibliotecas

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

#### python3 -m venv kicadlib

***source kicadlib/bin/activate***

#### pip install easyeda2kicad

#### easyeda2kicad --full –lcsc_id=C2040

Onde C2040 pode ser substituído pelo id do componente disponível em

<u>[https://jlcpcb.com/PARTS](https://jlcpcb.com/PARTS)</u>

Por exemplo: pretende-se incluir no Kicad as bibliotecas do componente ATGM336H-5N31.

![Figura 27: Exemplo de indentificação do Part na JLCPCB](figuras/figura-27.png)

*Figura 27: Exemplo de indentificação do Part na JLCPCB*


Então digite o comando:

#### easyeda2kicad --full –lcsc_id=C90770

Símbolo, Footprint e modelo 3D serão baixados para o seu PC em diretório padrão, mas é possível especificar o diretório de destino.

#### easyeda2kicad --full --lcsc_id=C2040 --output ~/libs/my_lib

No KiCad, vá em Preferências > Configurar Caminhos e adicione as variáveis de ambiente EASYEDA2KICAD:

#### Windows : C:/Users/your_username/Documents/Kicad/easyeda2kicad/,

#### Linux:/home/your_username/libs

Vá para Preferências > Gerenciar Bibliotecas de Símbolos e Adicione a biblioteca global

**easyeda2kicad:${EASYEDA2KICAD}/my_lib.kicad_sym**

Vá para Preferências > Gerenciar bibliotecas do Footprint e adicione a biblioteca global

**easyeda2kicad:${EASYEDA2KICAD}/my_lib.pretty**

Nesse caso o componente já estará com o campo “LCSC Part” contendo o código exato que fará parte da lista BOM (veja a figura).

![Figura 28: Identificação do componente a ser utilizado na lista BOM para fabricação na JLCPCB](figuras/figura-28.png)

*Figura 28: Identificação do componente a ser utilizado na lista BOM para fabricação na JLCPCB*


![Figura 29: Configuração das bibliotecas de símbolos](figuras/figura-29.png)

*Figura 29: Configuração das bibliotecas de símbolos*


Caso as biblioteca seja específica do projeto e altamente recomendável que esteja em um diretório do projeto.

Caso deseje incluir as bibliotecas apenas no projeto e dentro dos respectivos diretórios do mesmo, use o caminho da seguinte forma:

#### ${KIPRJMOD}/libs/my_libs.kicad_sym

## 7.7. Principais teclas de atalho

#### 7.7.1. Editor de Esquemáticos (Eeschema)

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

#### 7.7.2. Editor de PCB (Pcbnew)

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

#### 7.7.3. Teclas Globais

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

## 7.8. Compatibilidade do Design da PCB para fabricação

As empresas que realizam a manufatura das PCBs de forma comercial possuem limites técnicos que por vezes impossibilitam a fabricação caso o projetista não esteja atendo aos limites imposto pelo fabricante. Nesse caso é muito importante consultar os parâmetros definidos pelo fabricante e inseri-los nas no verificados de regras da PCB.

As configurações de restrição podem ser inseridas no KiCAD “Configuração da Placa → Regras de Desenho → Restrições”. Ver figura.

::: {.quadro tipo="dica" titulo="Antes de mandar fabricar"}
Insira no KiCAD as restrições técnicas de fabricação, para que o próprio KiCAD aponte inconsistências no projeto, e trabalhe com **margem de pelo menos 20%** em relação aos limites do fabricante.

**Nota:** a estrutura desta tabela foi corrompida na conversão (células desalinhadas). Os valores precisam ser conferidos na página do fabricante antes do uso — a revisão está pendente.
:::

![Figura 30: Interface de configuração das restrições de desenho da PCB](figuras/figura-30.png)

*Figura 30: Interface de configuração das restrições de desenho da PCB*


As compatibilidades apresentadas foram obtidas na JLCPCB em 11/2024, a partir da url [jlcpcb.com/capabilities/pcb-capabilities](https://jlcpcb.com/capabilities/pcb-capabilities).

#### Especificações do PCB

**Característic** **Capacidade Descrição Padrões as**

|Contagem de camadas Camadas|1-32|O número de camadas de cobre no PCB||
|---|---|---|---|
|Impedância Controlada|4/6/8/10/12/1 4/16/18/20/.../ 32 camadas|Guia do usuário para a calculadora de impedância JLCPCB Calculadora de Impedância JLCPCB||
|Material|FR-4|Laminados de grau A de fornecedores como Nan Ya, KB, Shengyi e etc.||

|Núcleo de alumínio|PCBs de núcleo de alumínio de 1 camada|||
|---|---|---|---|
|Núcleo de cobre|PCBs de núcleo de cobre de 1 camada com contatos diretos do dissipador de calor para o núcleo (≥ 1 × 1 mm)|||
|PCB de RF|PCBs RF de 2 camadas de cobre de 1 oz com núcleos Rogers e PTFE|||
|Constantes dielétricas FR-4|4.5 (PCB de 2 camadas)|7628 Pré-impregnado 4.4 3313 Perpreg 4.1 2116 Perpreg 4.16||
|Dimensões PTFE: 590 × têm no máximo 500 × 600 máximas Dimensões Regular: 3 × Esses limites se aplicam a|Placa de circuito impresso FR4: 670 × 600 mm Rogers / PCB PCBs com espessura ≥ 0,8 de Teflon 438 mm PCB de alumínio: 602 × 506 mm PCB de cobre: 480 × 286 mm|Esses limites se aplicam a mm. Os PCBs FR4 mais finos mm. PCBs FR4 de 2 camadas podem atingir um tamanho máximo de 1020 × 600 mm.||

|mínimas|3 mm. Bordas castelhadas/ chapeadas: 10 × 10 mm.|PCBs com espessura ≥ 0,6 mm. Revisão manual necessária para PCBs mais finos. A panelização é recomendada para placas de tamanho pequeno.||
|---|---|---|---|
|Tolerância de Dimensão|±0,1 mm|±0,1 mm (precisão) e ±0,2 mm (regular) para roteamento CNC e ±0,4 mm para vinco em V||
|Grossura|0,4 - 4,5 mm|Espessuras para FR4 são: 0,4/0,6/0,8/1,0/1,2/1,6/2,0 mm (2,5 mm e acima são apenas para PCBs de 12+ camadas)||
|Tolerância de espessura (Espessura ≥1,0mm)|± 10%|por exemplo, para a espessura da placa de 1,6 mm, a espessura da placa acabada varia de 1,44 mm (T- 1,6 × 10%) a 1,76 mm (T + 1,6 × 10%)||
|Tolerância de espessura (Espessura < 1,0 mm)|± 0,1 mm|por exemplo, para a espessura da placa de 0,8 mm, a espessura da placa acabada varia de 0,7 mm (T- 0,1) a 0,9 mm (T+0,1).||
|Camada externa acabada de cobre|1 onça / 2 onças (35umcamada externa é de 1 onça / 70um)|O peso do cobre acabado da ou 2 onças.||
|Camada interna acabada de / 35um / cobre|0,5 oz / 1 oz / 2 oz (17,5um 70um)|O peso do cobre acabado da camada interna é de 0,5 oz por padrão.||
|Máscara de Verde, roxo, Usamos máscara de solda LPI solda|vermelho, amarelo,|(Liquid Photo Imageable). Este é o tipo mais comum de||

máscara usada hoje. A máscara de solda de tinta azul, branco curada por calor é

||e preto.|geralmente encontrada em|
|---|---|---|
|||PCBs de baixo custo e de um só lado.|
||HASL (com/sem|O FR4 tem todos os três acabamentos disponíveis,|
|Acabament|chumbo),|mais de 6 camadas e as|
|o de|ENIG, OSP|placas RF têm apenas ENIG.|
|superfície|(somente placas com núcleo de cobre)|Placas de núcleo de alumínio têm apenas HASL. Placas de núcleo de cobre têm apenas OSP.|

#### Perfuração

**Característi** **Capacidade Descrição Padrões cas**

|Diâmetro da broca|1 camada: 0,3 – 6,3 mm 2 camadas: 0,15 – 6,3 mm Multicamada s: 0,15 – 6,3 mm|Furos com diâmetro ≥ 6,3 mm são fresados por CNC a partir de um furo menor. O diâmetro mínimo da broca para PCBs de 2 ou mais camadas é de 0,15 mm (mais caro!) O diâmetro mínimo da broca para PCBs com núcleo de alumínio é de 0,65 mm O diâmetro mínimo da broca para PCBs com núcleo de cobre é de 1,0 mm||
|---|---|---|---|
|Tolerância Furos do tamanho do furo (revestido)|passantes: +0,13 / -0,08 mm Furos de|por exemplo, para o tamanho do furo de 0,6 mm, o tamanho do furo acabado entre 0,52 mm e 0,73 mm é aceitável.||

||encaixe por pressão: ± 0,05 mm (somente placas ENIG multicamada s – mencione os furos específicos na observação do PCB)|||
|---|---|---|---|
|Tolerância do tamanho do furo (não revestido)|±0,2 mm|por exemplo, para o furo não revestido de 1,00 mm, o tamanho do furo acabado entre 0,80 mm e 1,20 mm é aceitável.||
|Espessura média do revestimen to do furo|18μm|||
|Vias Cegas/Ocult as|Não suportado|Atualmente não oferecemos suporte para Vias Cegas/Enterradas, somente furos passantes.||
|Tamanho/ diâmetro mínimo do furo de passagem|0,15 mm / 0,25 mm|1 camada (somente NPTH): tamanho do furo de 0,3 mm / diâmetro de passagem de 0,5 mm 2 camadas: tamanho do furo de 0,15 mm / diâmetro da passagem de 0,25 mm Multicamadas: tamanho do furo de 0,15 mm / diâmetro||

|||da via de 0,25 mm ① O diâmetro da via deve ser 0,1 mm (0,15 mm de preferência) maior que o tamanho do furo da via. ② Tamanho do furo de passagem mínimo preferido: 0,2 mm||
|---|---|---|---|
|Min. Furos não revestidos|0,50 mm|Por favor, desenhe NPTHs na camada mecânica ou mantenha-os afastados da camada.||
|Slots banhados mínimos|0,5 mm|A largura mínima da ranhura revestida é de 0,5 mm, que é desenhada com uma almofada.||
|Mín. Slots não banhados|1,0 mm|A largura mínima do slot não revestido é de 1,0 mm, desenhe o contorno do slot na camada mecânica (GM1 ou GKO)||
|Por meio do espaçamen 0,2 mm to furo a furo||||
|Espaçamen to entre furos de almofada|0,45 mm|||

|Min. Buracos acastelados|0,60 mm|Furos castelados são meios- furos metalizados em bordas de PCB, comumente usados em placas-filha para serem soldadas em PCBs portadoras. ① Diâmetro do furo (Φ): ≥ 0,6 mm ② Furo até a borda da placa (L): ≥ 1 mm ≥ Furo a furo (D): ≥ 0,6 mm ④ Tamanho mínimo do PCB: 10 × 10 mm ⑤ Espessura mínima do PCB: 0,6 mm||
|---|---|---|---|
|Bordas Chapeadas|10 x 10 mm|Bordas revestidas são revestidas de cobre e tratadas com ENIG. HASL não é suportado. ① Tamanho mínimo do PCB: 10 × 10 mm ② Espessura mínima do PCB: 0,6 mm ③ São necessárias pelo menos 3 rupturas (mais para PCBs maiores) no revestimento da borda para conexões de aba de suporte||
|Furos / Ranhuras retangularesuportado s|Não|Furos retangulares e ranhuras sem cantos arredondados não são suportados.||

#### Larguras

**Característi** **Capacidade Descrição Padrões cas**

|Largura mínima da 0,10 / 0,10 trilha e espaçamen mil) to (1 oz)|mm (4 / 4|1 e 2 camadas: 0,10 / 0,10 mm (4 / 4 mil) Multicamadas: 0,09 / 0,09 mm (3,5 / 3,5 mil). 3 mil é aceitável em fan-outs BGA.||
|---|---|---|---|
|Largura mínima da 0,16 / 0,16 trilha e espaçamen mil) to (2 oz) Tolerância da largura ±20% da via|mm (6,5 / 6,5|2 camadas: 0,16 / 0,16 mm (6,5 / 6,5 mil) Multicamadas: 0,16 / 0,20 mm (6,5 / 8 mil) por exemplo, para uma pista de 0,1 mm, a largura da pista finalizada varia de 0,08 a 0,12 mm.||
|Anel anular PTH|≧0,20 mm|2 camadas: 1 oz: Recomendado 0,25 mm ou mais; mínimo absoluto 0,18 mm 2 oz: 0,254 mm ou mais Multicamadas: 1 oz: Recomendado 0,20 mm ou mais; mínimo absoluto 0,15 mm 2 oz: 0,254 mm ou mais||
|Anel anular de almofada NPTH|≧0,45 mm|Recomendado 0,45 mm ou mais. Isso é para permitir que um anel de cobre de 0,2 mm seja removido ao redor do furo para a fixação do filme de vedação. Tamanhos de pastilhas menores que o valor recomendado podem resultar em um anel anular muito fino ou completamente ausente.||

|BGA|0,25 mm|① Diâmetro da almofada BGA ≥ 0,25 mm ② Distância entre a pastilha BGA e o traço ≥ 0,1 mm (mín. 0,09 mm para placas multicamadas) ③ As vias podem ser colocadas dentro de pads BGA usando vias preenchidas e revestidas||
|---|---|---|---|
|Bobinas de rastreamen 0,15/0,15 mmLargura/folga mínima do to Largura e espaçamen 0,25 to da grade milímetros hachurada Espaçamen 0,25 mm to de trilhas na mesma rede||Largura/folga mínima do traço: 0,15/0,15 mm, quando os traços são cobertos por máscara de solda (1 onça). traço: 0,25/0,25 mm, quando os traços NÃO são cobertos por máscara de solda (1oz). Somente ENIG (alto risco de curto-circuito com HASL)||

|Camada interna através do furo para folga de cobre|0,2 mm|||
|---|---|---|---|
|Folga do furo da almofada PTH da camada interna para cobre|0,3 mm|||
|Folga da almofada para rastrear|0,1 mm|Mín. 0,1 mm (fique bem acima, se possível). Mín. 0,09 mm localmente para almofadas BGA||
|Folga entre pads SMD (redes diferentes)|0,15 mm|Mais detalhes sobre o espaçamento dos pads SMD: Espaçamento mínimo dos componentes SMD||
|Via buraco para pista|0,2 mm|||

|PTH para rastrear|0,28 mm|0,35 mm é recomendado, mínimo 0,28 mm||
|---|---|---|---|
|NPTH para rastrear|0,2 mm|||

#### Máscara de solda

**Característi** **Capacidade Descrição Padrões cas**

|Expansão da máscara 0,038 mm de solda||2 camadas: expansão de 0,038 mm em cada lado de um pad. Mantenha pelo menos 0,05 mm de folga entre as aberturas da máscara de solda e os traços vizinhos. Multicamadas: Não requer expansão Nota: esta regra não entra em conflito com a folga mínima de 0,1 mm entre a almofada e a pista||
|---|---|---|---|
|Ponte de máscara de solda|0,10 mm|2 camadas (1 oz): Espaçamento mínimo entre as almofadas: 0,20 mm (verde, vermelho, amarelo, azul, roxo) Espaçamento mínimo entre as almofadas: 0,23 mm (preto, branco) Multicamadas (1 oz): Espaçamento mínimo entre as almofadas: 0,10 mm (verde, vermelho, amarelo, azul, roxo) Espaçamento mínimo entre as almofadas: 0,13 mm (preto, branco)||
|Vias plugadas|Cheio de máscara de solda|As vias são preenchidas com máscara de solda para um acabamento opaco. Clique||

|||para uma explicação detalhada ① As vias preenchidas não devem ter aberturas de máscara de solda em nenhum dos lados ② As vias preenchidas devem ter ≥ 0,35 mm de folga de outras aberturas da máscara de solda (por exemplo, almofadas) ③ As vias preenchidas não devem ter diâmetro maior que 0,5 mm||
|---|---|---|---|
|Processo JLCPCB Via- Pasta de in-Pad|Epóxi preenchido e ① As vias são preenchidas e coberto cobre preenchida e exigem alta condutividade tampada|As vias são preenchidas com resina epóxi ou pasta de cobre e então revestidas para obter um acabamento opaco e suave. Clique para uma explicação detalhada revestidas. Escolha o preenchimento de pasta de cobre para aplicações que térmica. ② Este processo é o padrão para placas multicamadas de 6 camadas ou mais. ③ Compatível com diâmetros de via de 0,15 a 0,5 mm.||
|Constante dielétrica da máscara de solda|3.8|||

Espessura da tinta da ≥ 10μm máscara de solda

#### Lenda

**Característic** **Capacidade Descrição Padrões as**

|Largura mínima da linha|6 mil (0,153 mm)|Caracteres com largura menor que 6 mil (0,153 mm) não poderão ser identificados.||
|---|---|---|---|
|Altura mínima do texto|40 mil (1,0 mm)|Caracteres com altura inferior a 40 mil (1,0 mm) não poderão ser identificados.||
|Proporção entre largura e altura do caractere|1:6|A proporção preferida de largura e altura é 1:6.||
|Proporção largura/altu ra do personage m esculpido em cavidade|1:6|A proporção preferida de largura para altura é 1:6||
|Almofada para serigrafia|0,15 mm|A distância mínima entre a almofada e a serigrafia é de 0,15 mm.||

#### Contorno

**Característi** **Capacidade Descrição Padrões cas**

|Roteado|0,2 mm|① Folga de cobre das bordas da placa roteada: ≧0,2 mm ② Folga de cobre das ranhuras roteadas: ≧0,2 mm ③ Tolerância dimensional para bordas de placas roteadas: ±0,2 mm (precisão regular); ±0,1 mm (alta precisão)||
|---|---|---|---|
|Corte em V|0,4 mm|① Folga de cobre das bordas da placa cortada em V: ≧0,4 mm ② Tolerância de dimensão para bordas de placa cortadas em V: ±0,4 mm. Espessura do PCB ≥ 0,6 mm ③ Espaçamento de placa de painel zero por padrão. Alternativamente, corte em V ao longo de uma direção sem espaçamento e roteie ao longo da outra direção com espaçamento de placa de 1,6 ou 2 mm. ④ Dimensões mínimas do painel: 70 × 70 mm; dimensões máximas do painel: 475 × 475 mm ⑤ Ângulo da ranhura em V: 25°||

① Folga de cobre das bordas da placa não-mouse-bite: ≧0,2 mm ② Tolerância de dimensão para bordas de placa não- mouse-bite: ±0,2 mm (precisão regular); ±0,1 mm (alta precisão) ③ Espaçamento do painel: 1,6 ou 2 mm ④ As bordas serrilhadas permanecerão após a despanelização ⑤ Largura mínima da aresta de ferramenta: 3 mm.

|Painel de|Para montagem SMT no|
|---|---|
|mordidas|JLCPCB, use arestas de|
|de rato|ferramenta de 5 mm, furos|

0,2 mm

de ferramenta de 2 mm e fiduciais de 1 mm centralizados a 3,85 mm das arestas do painel. ⑥ O diâmetro recomendado da mordida do mouse é de 0,5 mm a 0,8 mm; A distância recomendada entre as duas mordidas do mouse é de 0,2 a 0,3 mm. A largura mínima da aba de separação é de 4 mm. Para separação com mordidas do mouse, a largura mínima é de 5 mm.

|Panelizaçã o com espaço|2mm|O espaçamento entre as placas deve ser ≥ 2 mm, pois espaçamentos estreitos resultam em dificuldades de roteamento e corte em V.||
|---|---|---|---|
|Painel de PCBs Circulares|≥20mmx20 mm|O tamanho da placa redonda única deve ser ≥20 mm x 20 mm ao escolher o painel da JLCPCB. Painéis com furos de carimbo e adicione tiras de ferramentas em quatro bordas da placa||
