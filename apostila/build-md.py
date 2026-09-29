#!/usr/bin/env python3
"""Migração (uso único): reescreve `apostila/*.md` a partir do PDF convertido.

ATENÇÃO: **sobrescreve** os arquivos de `apostila/`. Depois da migração inicial, a
fonte de verdade passa a ser `apostila/*.md` — correções editoriais feitas à mão
nelas se perdem se este script for rodado de novo. Rode apenas para refazer a
migração do zero (e reaplique as correções registradas em
`docs/auditoria-apostila-pcb.md`).

- Legenda completa: vem do Indice de figuras do documento original (fonte de verdade).
- Ordem: pares A/B (que a conversao devolveu invertidos) sao renumerados em ordem.
- Imagem: apostila/figuras/figura-NN.png extraida do PDF.
"""
import json
import re
from pathlib import Path

SRC = Path('/tmp/apostila-src.md')   # gerado por: npx -y @firecrawl/anydoc docs/materialApoioKicad_Optativa_R9.pdf -o /tmp/apostila-src.md
REPORT = Path('/tmp/figuras-report.json')
OUT = Path('/home/william/Documentos/cursoKicad/novaApostila/apostila')

lines = SRC.read_text(encoding='utf-8').split('\n')

CAP_NUM = re.compile(r'^\s*[•\s]*\**\s*Figura\s+(\d+)\s*:')
CHAP = {
    '1. Introdução': '01-introducao',
    '2. Princípios e elementos básicos das PCBs': '02-principios-elementos',
    '3. Boas Práticas de Design': '03-boas-praticas-design',
    '4. Processo básico de fabricação de PCB': '04-fabricacao-pcb',
    '5. Protótipo de PCB': '05-prototipo-pcb',
    '6. Opções de "EDA"': '06-opcoes-eda',
    '7. KiCad': '07-kicad',
    '8. Diversos projetos feitos com KiCAD': '08-projetos-kicad',
    '9. Controle de impedância': '09-controle-impedancia',
    '10. Circuitos para interfaceamento': '10-interfaceamento-io',
    'Referências WEB': '99-referencias-web',
}

# ---------- 1. legendas completas a partir do Indice de figuras ----------
i_idx = next(i for i, l in enumerate(lines) if l.startswith('### Índice de figuras'))
i_body = next(i for i, l in enumerate(lines) if l.startswith('# 1. Introdução'))

captions, ordem, cur = {}, [], None
for raw in lines[i_idx + 1:i_body]:
    m = CAP_NUM.match(raw)
    if m:
        cur = int(m.group(1))
        ordem.append(cur)
        captions[cur] = raw[m.end():].strip()
    elif cur is not None:
        captions[cur] = (captions[cur] + ' ' + raw.strip()).strip()


def limpar(txt):
    txt = re.sub(r'\.{3,}\s*\d*\s*$', '', txt)          # pontos de preenchimento + pagina
    txt = re.sub(r'\s+', ' ', txt).strip(' .*')
    return txt


captions = {n: limpar(t) for n, t in captions.items()}
# legendas 1 e 2 sao URLs de origem (defeito do material): registra o link como credito,
# sem inventar texto de legenda que nao existe no documento.
creditos = {}
for n, t in captions.items():
    u = re.search(r'https?://\S+', t)
    if u:
        creditos[n] = u.group(0).rstrip('*.,')

# ---------- 2. capitulos ----------
marcos = [(i, l) for i, l in enumerate(lines) if re.match(r'^# ', l) and i >= i_body]


def nome_arquivo(titulo):
    titulo = titulo.lstrip('#').strip()
    for chave, arq in CHAP.items():
        if titulo.startswith(chave):
            return arq
    return 'zz-' + re.sub(r'\W+', '-', titulo.lower())[:40].strip('-')


# ---------- 3. transforma blocos de figura em imagem + legenda ----------
def blocos(ls):
    """Devolve [(n, i, j)] para cada legenda (j exclusivo)."""
    res, i = [], 0
    while i < len(ls):
        m = CAP_NUM.match(ls[i])
        if not m:
            i += 1
            continue
        # legenda ja acompanhada da imagem (veio da linearizacao de tabela)
        ant = [x for x in ls[max(0, i - 3):i] if x.strip()]
        if ant and ant[-1].startswith(f'![Figura {m.group(1)}:'):
            i += 1
            continue
        j = i + 1
        while j < len(ls):
            nxt = ls[j].strip()
            if nxt == '':
                prox = ls[j + 1].strip() if j + 1 < len(ls) else ''
                if re.fullmatch(r'\*[^*]+\*', prox) and not CAP_NUM.match(ls[j + 1]):
                    j += 1
                    continue
                break
            # só linha INTEIRAMENTE em itálico é continuação da legenda; bolinha
            # em negrito (- **X**) e parágrafo em negrito (**N.. PASSO** ...)
            # são conteúdo e não podem ser consumidos.
            if re.fullmatch(r'\*[^*]+\*', nxt) and not CAP_NUM.match(ls[j]):
                j += 1
                continue
            break
        res.append((int(m.group(1)), i, j))
        i = j
    return res


def reordenar_pares(bs):
    """Pares A/B vieram como (n+1) antes de (n): devolve a lista de numeros
    reordenada, mantendo as posicoes fisicas originais."""
    bs = sorted(bs, key=lambda b: b[1])
    nums = [n for n, _i, _j in bs]
    for k in range(len(nums) - 1):
        if nums[k + 1] == nums[k] - 1:
            nums[k], nums[k + 1] = nums[k + 1], nums[k]
    return bs, nums


def linearizar_tabelas_com_figuras(ls):
    """A galeria do cap. 8 veio do PDF como tabela de 2 colunas (imagem+legenda
    a esquerda, descricao a direita) e chegou corrompida, sem as imagens.

    Regiao de tabela que contenha legenda de figura e linearizada: imagem +
    legenda + texto das demais celulas, na mesma ordem. Nenhum texto e perdido;
    o que se perde e o enquadramento em duas colunas, que no markdown ja nao
    existia. Tabelas sem figura (ex.: capacidades do cap. 7) ficam intactas.
    """
    saida, i = [], 0
    while i < len(ls):
        if not ls[i].lstrip().startswith('|'):
            saida.append(ls[i])
            i += 1
            continue
        j = i
        while j < len(ls) and ls[j].lstrip().startswith('|'):
            j += 1
        run = ls[i:j]
        if not any(re.match(r'^\s*\|\s*\**\s*Figura\s+\d+\s*:', l) or
                   re.search(r'\|\s*\**\s*Figura\s+\d+\s*:', l) for l in run):
            saida.extend(run)
            i = j
            continue
        for l in run:
            if re.fullmatch(r'\s*\|[\s|:-]*\|\s*', l):
                continue
            celulas = [c.strip() for c in l.strip().strip('|').split('|')]
            n, texto = None, []
            for c in celulas:
                m = re.match(r'^\**\s*Figura\s+(\d+)\s*:', c)
                if m and n is None:
                    n = int(m.group(1))
                elif c:
                    texto.append(c)
            if n is not None:
                leg = captions.get(n) or '[VERIFICAR: legenda ausente no índice]'
                saida += [f'![Figura {n}: {leg}](figuras/figura-{n:02d}.png)', '',
                          f'*Figura {n}: {leg}*', '']
            if texto:
                saida += [' '.join(texto), '']
        i = j
    return saida


ORD_PASSO = re.compile(r'\*\*(\d)\.{1,2}\s*PASSO\*\*')


def limpar_marcadores(ls):
    """O conversor extrai o indicador ordinal de `1.º PASSO` como um `**o**`
    solto e escreve o numero como `1..`. O `**o**` fica preso ao fim do
    paragrafo anterior e o passo perde o titulo — foi assim que o bloco do
    3.º passo do capitulo 9 sumiu na primeira migracao (achado A-12)."""
    saida = []
    for l in ls:
        l = ORD_PASSO.sub(lambda m: f'**{m.group(1)}º PASSO**', l)
        l = re.sub(r'\s*\*\*o\*\*\s*', ' ', l).rstrip()
        if not l.strip() and saida and not saida[-1].strip():
            continue
        saida.append(l)
    return saida


def transformar(corpo):
    corpo = limpar_marcadores(corpo)
    bs, nums = reordenar_pares(blocos(corpo))
    saida, pos = [], 0
    for (_n_orig, i, j), n in zip(bs, nums):
        saida.extend(corpo[pos:i])
        # a legenda pode estar colada no item de lista anterior: sem a linha em
        # branco, a imagem viraria continuacao do item em vez de figura propria
        if saida and saida[-1].strip():
            saida.append('')
        leg = captions.get(n) or '[VERIFICAR: legenda ausente no índice de figuras]'
        saida.append(f'![Figura {n}: {leg}](figuras/figura-{n:02d}.png)')
        saida.append('')
        saida.append(f'*Figura {n}: {leg}*')
        saida.append('')
        pos = j
    saida.extend(corpo[pos:])
    return saida


# ---------- 4. escreve ----------
OUT.mkdir(parents=True, exist_ok=True)
manifesto, usados = [], set()
for k, (ini, titulo) in enumerate(marcos):
    fim = marcos[k + 1][0] if k + 1 < len(marcos) else len(lines)
    corpo = transformar(linearizar_tabelas_com_figuras(lines[ini:fim]))
    arq = OUT / f'{nome_arquivo(titulo)}.md'
    arq.write_text('\n'.join(corpo).rstrip() + '\n', encoding='utf-8')

# capa
capa_fim = next(i for i, l in enumerate(lines) if l.startswith('### Sumário'))
(OUT / 'indice.md').write_text(
    '\n'.join(lines[:capa_fim]).rstrip() + '\n', encoding='utf-8')

# manifesto de figuras (rastreabilidade)
rep = json.loads(REPORT.read_text(encoding='utf-8'))
por_pagina = {f['figura']: f for f in rep['figuras']}
linhas = ['# Índice de figuras (manifesto)',
          '',
          'Rastreabilidade das figuras extraídas de `docs/materialApoioKicad_Optativa_R9.pdf`.',
          'Arquivos em `apostila/figuras/`.',
          '',
          '| Figura | Página no PDF | Arquivo | Legenda |',
          '|---|---|---|---|']
for n in sorted(captions):
    f = por_pagina.get(n, {})
    linhas.append(f"| {n} | {f.get('pagina','—')} | `figuras/figura-{n:02d}.png` | "
                  f"{captions.get(n,'[VERIFICAR]')} |")
(OUT / 'indice-figuras.md').write_text('\n'.join(linhas) + '\n', encoding='utf-8')

print('capítulos:', len(marcos))
print('legendas:', len(captions), '| figuras com arquivo:', len(por_pagina))
print('sem legenda:', sorted(set(por_pagina) - set(captions)))
print('sem arquivo:', sorted(set(captions) - set(por_pagina)))
