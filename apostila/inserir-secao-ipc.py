#!/usr/bin/env python3
"""
Insere a seção "Normas IPC" como §2.3 do capítulo 2.

Por que um script
-----------------
A seção é conteúdo novo, não uma correção de conversão. Foi inserida por script
porque editar `apostila/02-principios-elementos.md` pela interface depois que
`corrigir-legendas.py` reescreveu o arquivo em disco resultou em perda silenciosa
da edição (o buffer do editor foi descartado). O script garante a gravação.

A seção entra como §2.3 porque a numeração do material original salta de 2.2.5
para 2.4 — a lacuna é preenchida, e não criada.

Fonte de todo o conteúdo: `livros/IPC Class 3 Design Guide.pdf`. Nada foi
afirmado além do que esse material declara.

Uso:  python3 apostila/inserir-secao-ipc.py
Idempotente: não faz nada se a seção já existir.
"""
from __future__ import annotations

from pathlib import Path

RAIZ = Path(__file__).resolve().parent
ALVO = RAIZ / '02-principios-elementos.md'

TABELA_ANTIGA = """| Classe | Aplicação | Confiabilidade e defeitos admitidos | Exemplos |
|---|---|---|---|
| **Classe 1** | Produtos eletrônicos de uso geral | Vida útil limitada e função simples. Admite vários defeitos cosméticos, desde que não afetem o funcionamento; a confiabilidade não é fator crítico. É a placa mais barata de fabricar. | Controles remotos de TV, lâmpadas LED, brinquedos infantis |
| **Classe 2** | Produtos eletrônicos de serviço dedicado | Confiabilidade maior e vida útil estendida; normas mais rigorosas que a classe 1, mas ainda se admitem algumas imperfeições cosméticas. O serviço ininterrupto é preferível, porém não crítico, e não há exposição a condições ambientais extremas. | Notebooks, smartphones, tablets, equipamentos de comunicação |
| **Classe 3** | Produtos eletrônicos de alto desempenho | Deve fornecer desempenho contínuo, ou sob demanda, **sem parada** do equipamento; o ambiente de uso pode ser excepcionalmente severo. Exige níveis elevados de inspeção e ensaio, o que a torna altamente confiável. | Equipamentos de suporte à vida, equipamentos militares, sistemas de monitoramento eletrônico, automotivo |
| **Classe 3/A** | Circuitos impressos de uso espacial e aviônica militar (IPC-6012) | Categoria mais alta para circuitos impressos. Critérios de fabricação muito rigorosos, pois a placa deve continuar operando em condições críticas. Consideravelmente mais cara, por precisar estar próxima da perfeição. | Aeroespacial, sistemas aéreos militares, sistemas de mísseis |"""

# 3 colunas, com larguras proporcionais ao conteúdo: 10 / 24 / 55 no separador.
# O pandoc deriva a largura relativa de cada coluna do número de traços, e 4
# colunas iguais (0,25 cada) deixavam a primeira e a última apertadas demais.
# Os exemplos passam a integrar a coluna de aplicação, como fazê-lo o material de
# referência (que cita os exemplos dentro da descrição de cada classe).
TABELA_NOVA = """| Classe | Aplicação típica | Confiabilidade exigida e defeitos admitidos |
|:---------|:-----------------------|:--------------------------------------------------------|
| **Classe 1** | Produtos eletrônicos de uso geral — controles remotos de TV, lâmpadas LED, brinquedos infantis | Vida útil limitada e função simples. Admite vários defeitos cosméticos, desde que não afetem o funcionamento; a confiabilidade não é fator crítico. É a placa mais barata de fabricar. |
| **Classe 2** | Produtos eletrônicos de serviço dedicado — notebooks, smartphones, tablets, equipamentos de comunicação | Confiabilidade maior e vida útil estendida; normas mais rigorosas que a classe 1, mas ainda se admitem algumas imperfeições cosméticas. O serviço ininterrupto é preferível, porém não crítico, e não há exposição a condições ambientais extremas. |
| **Classe 3** | Produtos eletrônicos de alto desempenho — suporte à vida, equipamentos militares, monitoramento eletrônico, automotivo | Deve fornecer desempenho contínuo, ou sob demanda, **sem parada** do equipamento; o ambiente de uso pode ser excepcionalmente severo. Exige níveis elevados de inspeção e ensaio, o que a torna altamente confiável. |
| **Classe 3/A** | Circuitos impressos de uso espacial e aviônica militar (IPC-6012) — aeroespacial, sistemas aéreos militares, sistemas de mísseis | Categoria mais alta para circuitos impressos. Critérios de fabricação muito rigorosos, pois a placa deve continuar operando em condições críticas. Consideravelmente mais cara, por precisar estar próxima da perfeição. |"""

ANCORA = '## 2.4. Categorias de PCBs'

SECAO = """## 2.3. Normas IPC

Uma placa que funciona na bancada não é automaticamente uma placa que pode ser fabricada em série. Para que projetista, fabricante e montador cheguem ao mesmo entendimento sobre o que é uma placa **aceitável**, a indústria eletrônica se apoia em normas — e a mais difundida delas é publicada pela **IPC**.

### 2.3.1. O que é a IPC

A IPC é a associação global da indústria de interconexão eletrônica. O nome veio de *Institute for Printed Circuits* e depois foi alterado para *Institute for Interconnecting and Packaging Electronic Circuits*; hoje a sigla é usada como nome próprio da organização.

Trata-se de uma associação mantida por seus membros, que publica especificações de forma periódica. As normas IPC são as regras **mais amplamente aceitas** pela indústria eletrônica e cobrem todas as etapas do ciclo de desenvolvimento de um produto: projeto, compras, montagem, empacotamento e inspeção. Segui-las ajuda a fabricar placas seguras, confiáveis e de alta qualidade — e, para o projetista, produz um efeito prático imediato: **mantém projetista e fabricante no mesmo entendimento** sobre o que a placa precisa cumprir.

::: {.quadro tipo="nota" titulo="Por que isso importa no seu projeto"}
Uma norma não é uma formalidade. As classes IPC existem porque a **mesma** placa pode ser considerada aprovada ou reprovada dependendo do critério adotado. Ao especificar a classe, você deixa explícito qual nível de inspeção e qual tolerância a defeito são aceitáveis para o seu produto — e evita que cada lado julgue a placa por uma régua diferente.
:::

### 2.3.2. As classes de qualidade

A **IPC-6011** descreve as classes de PCB e os **defeitos permitidos** em cada tipo de placa. São três classes, com o acréscimo posterior de uma quarta, definida pela **IPC-6012**:

| Classe | Aplicação | Confiabilidade e defeitos admitidos | Exemplos |
|---|---|---|---|
| **Classe 1** | Produtos eletrônicos de uso geral | Vida útil limitada e função simples. Admite vários defeitos cosméticos, desde que não afetem o funcionamento; a confiabilidade não é fator crítico. É a placa mais barata de fabricar. | Controles remotos de TV, lâmpadas LED, brinquedos infantis |
| **Classe 2** | Produtos eletrônicos de serviço dedicado | Confiabilidade maior e vida útil estendida; normas mais rigorosas que a classe 1, mas ainda se admitem algumas imperfeições cosméticas. O serviço ininterrupto é preferível, porém não crítico, e não há exposição a condições ambientais extremas. | Notebooks, smartphones, tablets, equipamentos de comunicação |
| **Classe 3** | Produtos eletrônicos de alto desempenho | Deve fornecer desempenho contínuo, ou sob demanda, **sem parada** do equipamento; o ambiente de uso pode ser excepcionalmente severo. Exige níveis elevados de inspeção e ensaio, o que a torna altamente confiável. | Equipamentos de suporte à vida, equipamentos militares, sistemas de monitoramento eletrônico, automotivo |
| **Classe 3/A** | Circuitos impressos de uso espacial e aviônica militar (IPC-6012) | Categoria mais alta para circuitos impressos. Critérios de fabricação muito rigorosos, pois a placa deve continuar operando em condições críticas. Consideravelmente mais cara, por precisar estar próxima da perfeição. | Aeroespacial, sistemas aéreos militares, sistemas de mísseis |

A diferença central entre as classes **não está no desenho da placa, e sim no grau de inspeção**: são as classes que definem quais defeitos são admissíveis durante a fabricação.

Vale desfazer um equívoco comum: as classes 3 e 3/A são usadas principalmente em equipamentos militares e aeroespaciais, mas **não são exclusivas** dessas áreas. Elas podem ser aplicadas a qualquer produto — inclusive aos exemplos citados na classe 2 —, porém deixam de ser economicamente viáveis pelo esforço de fabricação e de inspeção que exigem.

### 2.3.3. Como escolher a classe

Ao escolher a classe, o projetista está escolhendo a **vida útil** do produto. Muitas vezes a classe 2 atende a todos os requisitos e sai mais econômica. Se, além de a aplicação ser crítica, espera-se que a placa dure muitos anos, a classe 3 passa a ser a escolha adequada. O ambiente em que o produto vai operar também precisa entrar na conta, porque é ele que determina o grau de confiabilidade exigido do projeto.

::: {.quadro tipo="dica" titulo="Qual classe escolher"}
A escolha é econômica antes de ser técnica. A **classe 2** costuma atender à maior parte dos produtos — e sai mais barata. Reserve a **classe 3** para aplicações críticas ou para produtos que precisem durar muitos anos: o material de referência cita a fronteira de **15 anos** como um dos critérios de decisão. O ambiente de operação do produto é o outro critério a considerar.
:::

### 2.3.4. Onde a IPC aparece na prática

Duas situações concretas em que a norma entra no dia a dia do projetista:

- **Anel anular:** a IPC define a posição dos furos sobre a ilha de solda (*pad*) e a largura do anel externo que resta depois da furação. Quando a ilha não circunda completamente o furo, tem-se um *annular ring breakout* — condição que a norma trata explicitamente, com limites de aceitação próprios para cada classe.
- **Juntas de solda e defeitos aceitáveis:** a IPC trata separadamente os defeitos que comprometem o desempenho da placa e as imperfeições puramente cosméticas, e estabelece padrões de aceitação para os processos de montagem. O **mesmo** defeito pode ser aprovado na classe 1 e reprovado na classe 3: o defeito não muda, o critério é que muda.

O Capítulo 7 traz os valores de anel anular e de furação praticados por um fabricante real — é com esses números, e não com valores arbitrários, que o seu projeto é conferido no DRC.

Fonte: IPC, *IPC Class 3 Design Guide* (material de apoio da disciplina).

"""


def main() -> None:
    texto = ALVO.read_text(encoding='utf-8')

    if 'Normas IPC' not in texto:
        if ANCORA not in texto:
            raise SystemExit(f'âncora não encontrada em {ALVO.name}: {ANCORA!r}')
        texto = texto.replace(ANCORA, SECAO.replace(TABELA_ANTIGA, TABELA_NOVA) + ANCORA, 1)
        ALVO.write_text(texto, encoding='utf-8')
        print(f'{ALVO.name}: seção inserida')
        return

    if TABELA_ANTIGA in texto:
        texto = texto.replace(TABELA_ANTIGA, TABELA_NOVA, 1)
        ALVO.write_text(texto, encoding='utf-8')
        print(f'{ALVO.name}: tabela das classes ajustada para 3 colunas')
        return

    print('seção já presente e atualizada — nada a fazer.')


if __name__ == '__main__':
    main()
