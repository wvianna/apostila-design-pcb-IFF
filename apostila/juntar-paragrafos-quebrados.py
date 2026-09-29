#!/usr/bin/env python3
"""
Junta parágrafos que a conversão do PDF partiu no meio de uma frase.

O PDF de origem quebra a frase entre duas páginas (ou entre figura e texto) e a
conversão transforma essa quebra em **fim de parágrafo**. O resultado, no PDF
final, é uma frase interrompida por uma linha em branco e um recuo novo.

O critério de detecção — parágrafo que não termina em pontuação final seguido de
parágrafo que começa em minúscula — foi aplicado sobre todo o `apostila/*.md` e
produziu exatamente os casos abaixo. Eles estão fixados aqui, um a um, de
propósito: uma junção automática poderia emendar parágrafos legítimos.

Uso:  python3 apostila/juntar-paragrafos-quebrados.py
Idempotente: não faz nada quando a quebra já foi corrigida.
"""
from __future__ import annotations

import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

# (arquivo, fim do parágrafo, início do parágrafo seguinte)
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


def main() -> None:
    por_arquivo: dict[str, list[tuple[str, str]]] = {}
    for arquivo, fim, inicio in QUEBRAS:
        por_arquivo.setdefault(arquivo, []).append((fim, inicio))

    for nome, pares in por_arquivo.items():
        caminho = RAIZ / nome
        texto = caminho.read_text(encoding='utf-8')
        print(nome)
        alterou = False
        for fim, inicio in pares:
            # Quebra de parágrafo = duas ou mais linhas em branco entre os trechos.
            padrao = re.escape(fim) + r'\s*\n\s*\n\s*' + re.escape(inicio)
            novo, n = re.subn(padrao, fim + ' ' + inicio, texto, count=1)
            print(f"  {'OK ' if n else '-- '} {' '.join(inicio.split())[:45]!r}")
            if n:
                texto = novo
                alterou = True
        if alterou:
            caminho.write_text(texto, encoding='utf-8')
    print('\nconcluído.')


if __name__ == '__main__':
    main()
