#!/usr/bin/env python3
"""Reconstrói as tabelas de capacidade de fabricação do cap. 7 (JLCPCB).

Contexto: as tabelas de `apostila/07-kicad.md` vieram da conversão do PDF com as
células desalinhadas (achado A-05 em `docs/auditoria-apostila-pcb.md`). Este
script substitui o bloco pelas tabelas reescritas a partir da página de
capacidades do fabricante.

Fonte: JLCPCB, "PCB Manufacturing & Assembly Capabilities" —
https://jlcpcb.com/capabilities/pcb-capabilities (consultada em 2026-09-29).
Os valores são os publicados pelo fabricante nessa data e mudam com o tempo;
reexecutar a coleta antes de reusar este script mais tarde.

Uso: python3 apostila/reconstruir-tabela-jlcpcb.py
"""
import re
import sys
from pathlib import Path

CAPITULO = Path(__file__).resolve().parent / '07-kicad.md'
INICIO = '#### Especificações do PCB'
FIM = '#### Lenda'

ESPECIFICACOES = """#### Especificações do PCB

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
"""

PERFURACAO = """#### Perfuração

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
"""

LARGURAS = """#### Larguras

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
"""

MASCARA = """#### Máscara de solda

| Característica | Capacidade | Descrição |
|---|---|---|
| Expansão da máscara de solda | 1:1 | Equipamento LDI atualizado em junho de 2025: a abertura da máscara pode ter a mesma medida da almofada. Mantenha ao menos 0,09 mm de folga entre as aberturas da máscara e as trilhas vizinhas. |
| Ponte de máscara de solda | 0,10 mm | 1 oz — espaçamento mínimo entre almofadas de 0,10 mm (verde, vermelho, amarelo, azul, roxo) e 0,13 mm (preto, branco). 2 oz — 0,20 mm em qualquer cor. |
| Vias plugadas | Preenchidas com máscara de solda | Acabamento opaco. Vias preenchidas não podem ter abertura de máscara em nenhum dos lados, precisam de ≥ 0,35 mm de folga de outras aberturas e não podem passar de 0,5 mm de diâmetro. |
| Via-in-pad (processo JLCPCB) | Epóxi preenchido e coberto; pasta de cobre preenchida e tampada | Vias preenchidas com resina epóxi ou pasta de cobre e depois cobertas, para acabamento opaco e liso. É o padrão para placas multicamadas de 6 camadas ou mais e é compatível com vias de 0,15 a 0,55 mm. |
| Constante dielétrica da máscara de solda | 3,8 | — |
| Espessura da tinta da máscara de solda | ≥ 10 µm | — |
"""

ATRIBUICAO = (
    'As compatibilidades apresentadas foram conferidas na JLCPCB em 09/2026, a partir da url '
    '[jlcpcb.com/capabilities/pcb-capabilities](https://jlcpcb.com/capabilities/pcb-capabilities). '
    'Os valores são os publicados pelo fabricante nessa data e mudam com o tempo — confira a página '
    'antes de usar.'
)


def main():
    texto = CAPITULO.read_text(encoding='utf-8')
    linhas = texto.split('\n')
    try:
        i = next(k for k, l in enumerate(linhas) if l.strip() == INICIO)
        j = next(k for k, l in enumerate(linhas) if l.strip() == FIM)
    except StopIteration:
        sys.exit('marcadores não encontrados — o capítulo já foi reconstruído?')
    if j <= i:
        sys.exit('marcadores fora de ordem')

    novo = (ESPECIFICACOES + '\n' + PERFURACAO + '\n' + LARGURAS + '\n' + MASCARA).rstrip('\n')
    linhas[i:j] = novo.split('\n')
    saida = '\n'.join(linhas)

    saida = re.sub(r'As compatibilidades apresentadas foram[^\n]*', ATRIBUICAO, saida, count=1)
    CAPITULO.write_text(saida, encoding='utf-8')

    tabelas = saida.count('\n|---|')
    print(f'cap. 7 reconstruído: {tabelas} tabelas no arquivo, '
          f'{sum(len(t) for t in (ESPECIFICACOES, PERFURACAO, LARGURAS, MASCARA))} chars de tabela')


if __name__ == '__main__':
    main()
