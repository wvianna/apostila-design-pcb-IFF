#!/usr/bin/env python3
"""
Correções de legenda e de texto residual herdadas da conversão do PDF.

Problema tratado
----------------
A extração do PDF transforma a legenda em uma URL (quando é isso que o autor
escreveu no lugar da legenda) e deixa o **resíduo** dessa URL quebrado em várias
linhas em itálico, que o pandoc converte em parágrafos soltos de texto. O
resultado aparece no PDF como blocos de URL órfãos logo abaixo da figura, e em
alguns casos como uma legenda duplicada.

Objeto deste script
-------------------
1. `02-principios-elementos.md`
   - Figura 1: legenda passa a ser "Exemplos de PCBs".
   - Figura 2: legenda passa a ser "Exemplos de serigrafias".
   - Remove os resíduos de URL (blocos em itálico) das duas figuras.
2. `09-controle-impedancia.md`
   - Remove a legenda duplicada da Figura 68 que aparecia **antes** da Figura 67.
   - Remove a legenda da Figura 67 repetida no fim do bloco.
   - Corrige "contante" -> "constante", "Prepeg" -> "prepreg" e
     "na páginas" -> "nas páginas".

Uso:  python3 apostila/corrigir-legendas.py
Idempotente: cada substituição só é contada quando de fato ocorre.
"""
from __future__ import annotations

import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

# Legenda que o autor deve passar a exibir (decisão editorial, não inferência).
LEGENDAS = {
    1: 'Exemplos de PCBs',
    2: 'Exemplos de serigrafias',
}


def _sub(texto: str, padrao: str, troca: str, rotulo: str, flags=0) -> tuple[str, int]:
    """Aplica `re.sub` e devolve (texto, nº de substituições)."""
    novo, n = re.subn(padrao, troca, texto, flags=flags)
    print(f"  {'OK ' if n else '-- '} {rotulo}: {n}")
    return novo, n


def figuras_url() -> None:
    """Figuras 1 e 2: troca a legenda-URL pela legenda editorial e limpa o resíduo."""
    caminho = RAIZ / '02-principios-elementos.md'
    texto = caminho.read_text(encoding='utf-8')

    print('02-principios-elementos.md')

    # Legenda da imagem (texto alternativo) e legenda em itálico logo abaixo.
    # O `.*` é guloso de propósito: o texto alternativo contém `](` internos, e a
    # âncora confiável é o `](figuras/figura-NN.png)` no fim da linha.
    for n, legenda in LEGENDAS.items():
        nn = f'{n:02d}'
        texto, _ = _sub(
            texto,
            rf'!\[Figura {n}:.*\]\(figuras/figura-{nn}\.png\)',
            f'![Figura {n}: {legenda}](figuras/figura-{nn}.png)',
            f'legenda da imagem {n}',
        )
        texto, _ = _sub(
            texto,
            rf'^\*Figura {n}:.*\*$',
            f'*Figura {n}: {legenda}*',
            f'legenda em itálico {n}',
            flags=re.M,
        )

    # Resíduo: a URL quebrada em itálico, logo após a legenda. Nota-se pelo dobro de
    # linha em branco antes (a legenda real fica colada na imagem). O número de linhas
    # do resíduo depende do comprimento do endereço (3 linhas na Figura 1, 2 na
    # Figura 2), por isso a repetição é aberta: ela para quando a linha deixa de
    # começar por `*` — o que acontece no `###` da próxima seção.
    for n, host in ((1, r'embarcados\.com\.br'), (2, r'resources\.altium\.com')):
        texto, _ = _sub(
            texto,
            rf'\n\n\n\*\[https://{host}[^\n]*(\n\n\*[^\n]*){{0,5}}',
            '',
            f'resíduo de URL da figura {n}',
        )

    caminho.write_text(texto, encoding='utf-8')


def capitulo_9() -> None:
    """Legendas duplicadas e erros de digitação do capítulo 9."""
    caminho = RAIZ / '09-controle-impedancia.md'
    texto = caminho.read_text(encoding='utf-8')

    print('09-controle-impedancia.md')

    # Legenda da Figura 68 duplicada, aparecendo antes da Figura 67.
    # Distingue-se da legenda legítima por vir seguida de uma única linha em branco
    # e do bloco `*JLCPCB*`.
    texto, _ = _sub(
        texto,
        r'^\*Figura 68:.*\*\n\n\*JLCPCB\*\n\n',
        '',
        'legenda duplicada da Figura 68',
        flags=re.M,
    )

    # Legenda da Figura 67 repetida no fim do bloco — é a que sobrava na página.
    # O ponto final antes do `*` distingue-a da legenda legítima (sem ponto).
    texto, _ = _sub(
        texto,
        r'\n\n\*Figura 67: Estrutura com parâmetros para o controle de impedância\.\*\n\n',
        '\n\n',
        'legenda repetida da Figura 67',
    )

    for antigo, novo, rotulo in (
        ('na páginas de controle', 'nas páginas de controle', 'concordância "na páginas"'),
        ('obtenha a contante dielétrica', 'obtenha a constante dielétrica', 'digitação "contante"'),
        ('No site da JLC página do controle de impedância, obtenha a constante dielétrica do tipo de material Prepeg 7628 que corresponde a 4,4.',
         'No site da JLCPCB, na página de controle de impedância, obtenha a constante dielétrica do material prepreg 7628, que corresponde a 4,4.',
         'frase de orientação ao leitor'),
        ('Prepeg', 'prepreg', 'grafia do termo "prepreg"'),
        ('0,21040mm', '0,21040 mm', 'espaço antes da unidade'),
    ):
        n = texto.count(antigo)
        texto = texto.replace(antigo, novo)
        print(f"  {'OK ' if n else '-- '} {rotulo}: {n}")

    caminho.write_text(texto, encoding='utf-8')


def indice_figuras() -> None:
    """O manifesto repete a legenda de cada figura, então precisa acompanhar."""
    caminho = RAIZ / 'indice-figuras.md'
    texto = caminho.read_text(encoding='utf-8')

    print('indice-figuras.md')
    for n, legenda in LEGENDAS.items():
        texto, _ = _sub(
            texto,
            rf'^(\| {n} \| [^|]*\| `[^`]*` \|).*\|$',
            rf'\1 {legenda} |',
            f'legenda da figura {n}',
            flags=re.M,
        )

    caminho.write_text(texto, encoding='utf-8')


def main() -> None:
    figuras_url()
    indice_figuras()
    capitulo_9()
    print('\nconcluído.')


if __name__ == '__main__':
    main()
