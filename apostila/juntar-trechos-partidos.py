#!/usr/bin/env python3
"""
Rejunta trechos que a conversão do PDF separou indevidamente.

Três famílias de defeito, todas com a mesma origem — a quebra de linha do PDF
virando estrutura no markdown:

1. **Parágrafo partido no meio da frase.** O PDF quebra a frase entre páginas e a
   conversão transforma a quebra em fim de parágrafo: a frase fica interrompida
   por uma linha em branco e um recuo novo.
2. **Espaço depois de hífen legítimo.** Em `curtos- circuitos` o hífen faz parte
   da palavra; o que sobra é o espaço que a quebra de linha introduziu.
3. **Palavras transpostas.** A conversão troca a ordem de duas palavras vizinhas.

Os casos estão fixados um a um, de propósito. O critério de detecção foi aplicado
sobre todo o `apostila/*.md` e devolveu exatamente esta lista; uma correção
automática poderia emendar parágrafos ou palavras legítimos.

Uso:  python3 apostila/juntar-trechos-partidos.py
Idempotente: não faz nada quando o trecho já foi corrigido.
"""
from __future__ import annotations

import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

# 1. (arquivo, fim do parágrafo, início do parágrafo seguinte)
QUEBRAS = [
    ('02-principios-elementos.md',
     'Disponível em várias cores, como verde,',
     'vermelho e azul, essa camada contribui'),
    ('04-fabricacao-pcb.md',
     'tintas resistentes à corrosão é outra alternativa, onde a',
     'tinta é aplicada diretamente sobre a placa de cobre'),
    ('05-prototipo-pcb.md',
     'Dessa forma, os engenheiros e designers',
     'podem ter maior confiança de que o produto final'),
    ('07-kicad.md',
     'lista de bibliotecas de símbolos',
     'sym-lib-table disponíveis no editor de esquemáticos.'),
    ('07-kicad.md',
     'Entretanto, conforme o desejo do',
     'projetista, algumas etapas do workflow podem ser alteradas'),
    ('08-projetos-kicad.md',
     'permite o desenvolvimento futuro de',
     'gabinetes de usuário e novas integrações.'),
    ('10-interfaceamento-io.md',
     'proporcional ao número de chaveamentos e à',
     'corrente que passa pelos contatos.'),
]

# 2. (arquivo, trecho com espaço indevido, trecho correto) — aplicado a todas as
#    ocorrências, porque o mesmo termo se repete no texto.
HIFENIZACOES = [
    ('02-principios-elementos.md', 'curtos- circuitos', 'curtos-circuitos'),
    ('04-fabricacao-pcb.md', 'foto- resistente', 'foto-resistente'),
    ('08-projetos-kicad.md', 'add- on', 'add-on'),
    ('08-projetos-kicad.md', 'espectrômetro- dosímetro', 'espectrômetro-dosímetro'),
]

# 3. (arquivo, trecho transposto, trecho na ordem correta)
TRANSPOSICOES = [
    ('07-kicad.md', 'o fp- info-cachearquivo', 'o arquivo fp-info-cache'),
]


def _agrupar(lista) -> dict[str, list[tuple[str, str]]]:
    agrupado: dict[str, list[tuple[str, str]]] = {}
    for arquivo, antigo, novo in lista:
        agrupado.setdefault(arquivo, []).append((antigo, novo))
    return agrupado


def _aplicar(nome: str, itens: list[tuple[str, str]], por_quebra: bool) -> None:
    """`por_quebra=True` exige que os trechos estejam separados por parágrafo."""
    caminho = RAIZ / nome
    texto = caminho.read_text(encoding='utf-8')
    alterou = False
    for antigo, novo in itens:
        if por_quebra:
            padrao = re.escape(antigo) + r'\s*\n\s*\n\s*' + re.escape(novo)
            texto, n = re.subn(padrao, antigo + ' ' + novo, texto, count=1)
        else:
            n = texto.count(antigo)
            texto = texto.replace(antigo, novo)
        print(f"  {'OK ' if n else '-- '} {antigo[:46]!r}")
        alterou = alterou or bool(n)
    if alterou:
        caminho.write_text(texto, encoding='utf-8')


def main() -> None:
    # Os modos são explícitos: inferir o modo a partir da pontuação do trecho fez
    # entradas de QUEBRAS caírem na substituição simples e duplicarem frases.
    for nome, itens in _agrupar(QUEBRAS).items():
        print(f'{nome} [parágrafo partido]')
        _aplicar(nome, itens, por_quebra=True)

    for nome, itens in _agrupar(HIFENIZACOES + TRANSPOSICOES).items():
        print(f'{nome} [hífen / ordem]')
        _aplicar(nome, itens, por_quebra=False)

    print('\nconcluído.')


if __name__ == '__main__':
    main()
