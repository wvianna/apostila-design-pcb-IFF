#!/usr/bin/env python3
"""Consolida `apostila/*.md` no LaTeX de `latex/build/`.

Normalizações aplicadas — todas com evidência em `docs/auditoria-apostila-pcb.md`:

1. Junta títulos que a conversão quebrou em duas linhas (`#### ENEPIG ...` +
   `#### Palladium Immersion Gold)`).
2. Promove `#### N.N.N.` para `###` — no original 7.7.1..7.7.3 são subseções de
   7.7, mas saíram do conversor com um nível a mais.
3. Converte linhas de comando em `####` para bloco de código literal (no PDF
   original, pág. 41–42, são texto monoespaçado, não títulos).
4. Remove a legenda em itálico duplicada: o pandoc já usa o texto alternativo da
   imagem como `\\caption`.
5. Junta as quebras de linha do PDF dentro do parágrafo; hífen no fim de linha
   seguido de minúscula é mantido colado (`foto-` + `resistente`).
6. Ajusta a largura das imagens e reduz o corpo das tabelas largas.
7. Numera legendas fora do contador do LaTeX: o material já traz o próprio
   número ("Figura N:") e a numeração não é sequencial por capítulo.

Não reescreve conteúdo. O que não pôde ser resolvido por regra fica registrado
em `docs/auditoria-apostila-pcb.md`.
"""
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
APOSTILA = RAIZ / 'apostila'
BUILD = Path(__file__).resolve().parent / 'build'

H_NUM = re.compile(r'^(#{1,6}) (\d+(?:\.\d+)*)\.\s+')
CMD = re.compile(r'^(pip|npm|python3?|sudo|apt|git|easyeda2kicad|choco|pacman)\b')
CAMINHO = re.compile(r'(C:/|/home/|\$\{KIPRJMOD\})')
IMG = re.compile(r'^!\[Figura \d+')
LEG = re.compile(r'^\*Figura \d+:.*\*$')
ESTRUTURAL = re.compile(r'^(#{1,6} |\||!\[|>|```|:::|\s*$|\s*([-*+]|\d+\.)\s)')


def normalizar(linhas):
    saida, i, anterior_imagem = [], 0, False
    while i < len(linhas):
        linha = linhas[i]
        prox = linhas[i + 1] if i + 1 < len(linhas) else ''

        # 1. titulo quebrado em duas linhas de nivel 4
        if linha.startswith('#### ') and prox.startswith('#### '):
            saida.append(linha + ' ' + prox[5:])
            i += 2
            continue

        # 3. linha de comando virou titulo
        if linha.startswith('#### ') and (CMD.match(linha[5:]) or CAMINHO.search(linha)):
            saida.append('    ' + linha[5:].strip())
            i += 1
            continue

        # 2. o nivel do titulo vem da profundidade do proprio numero
        #    (1 -> #, 9.1 -> ##, 7.5.2 -> ###, 7.7.1 -> ###). O conversor
        #    errou a profundidade em 7 titulos; o numero sai porque o LaTeX
        #    numera a partir do nivel.
        m = H_NUM.match(linha)
        if m:
            nivel = min(m.group(2).count('.') + 1, 6)
            linha = '#' * nivel + ' ' + linha[m.end():]

        # 4. legenda duplicada: o pandoc ja usa o alt da imagem como \caption
        if LEG.match(linha) and anterior_imagem:
            anterior_imagem = False
            i += 1
            continue

        saida.append(linha)
        if linha.strip():          # linha em branco nao apaga o estado
            anterior_imagem = bool(IMG.match(linha))
        i += 1

    # 5. junta quebras de linha do PDF dentro de cada paragrafo
    final, buf = [], []
    for linha in saida:
        if ESTRUTURAL.match(linha):
            if buf:
                final.append(_juntar(buf))
                buf = []
            final.append(linha)
        else:
            buf.append(linha)
    if buf:
        final.append(_juntar(buf))
    return final


def _juntar(buf):
    txt = buf[0].rstrip()
    for nxt in buf[1:]:
        nxt = nxt.strip()
        if not nxt:
            continue
        if txt.endswith('-') and nxt[:1].islower():
            txt += nxt
        else:
            txt += ' ' + nxt
    return txt


def capa_tex():
    linhas = [l.rstrip() for l in (APOSTILA / 'indice.md').read_text(encoding='utf-8').split('\n')]
    titulo = [l[2:].strip() for l in linhas if l.startswith('# ')]
    # "sinais discretos" vem em linha propria, em negrito: faz parte do titulo
    for l in linhas:
        if l.startswith('**') and l.endswith('**') and 'sinais discretos' in l:
            titulo.append(l.strip('*'))
    profs = [l[2:].strip() for l in linhas if l.startswith('- ')]
    inst = next((l.lstrip('# ').strip() for l in linhas if 'Instituto' in l), '')
    data = next((l.strip() for l in linhas if re.match(r'^[a-zç]+/\d{4}$', l.strip())), '')
    titulo_txt = ' '.join(titulo).replace('&', r'\&')
    # Filete duplo (grosso + fino) em azul: abre e fecha o bloco do título.
    # \hrule em vez de \rule para não consumir uma linha de texto inteira.
    abre = [
        '  {\\color{azulCap}\\hrule height 2.4pt}',
        '  \\vspace{2.4pt}',
        '  {\\color{azulSub}\\hrule height 0.6pt}',
    ]
    fecha = [
        '  {\\color{azulSub}\\hrule height 0.6pt}',
        '  \\vspace{2.4pt}',
        '  {\\color{azulCap}\\hrule height 2.4pt}',
    ]
    corpo = '\n'.join([
        '% Gerado por build-tex.py a partir de apostila/indice.md — não editar.',
        '% Capa: título e filetes em azul, no mesmo esquema de cores das seções.',
        '\\begin{titlepage}',
        '  \\centering',
        '  \\vspace*{2.3cm}',
        '',
    ] + abre + [
        '',
        '  \\vspace{1.8cm}',
        '  {\\color{azulCap}\\huge\\bfseries ' + titulo_txt + '\\par}',
        '  \\vspace{1.3cm}',
        '',
    ] + fecha + [
        '',
        '  \\vfill',
        '',
        '  {\\large Professores\\par}',
        '  \\vspace{0.5cm}',
    ] + ['  {\\large ' + p.replace('&', r'\&') + '\\par}' for p in profs] + [
        '',
        '  \\vspace{1.4cm}',
        '  {\\color{azulSub}\\rule{0.42\\linewidth}{0.9pt}}',
        '  \\vspace{1.4cm}',
        '',
        '  {\\Large\\scshape\\color{azulCap} ' + inst + '\\par}',
        '  \\vspace{0.35cm}',
        '  {\\large\\color{azulSec} ' + data + '\\par}',
        '',
        '  \\vfill',
        '',
    ] + fecha + [
        '\\end{titlepage}',
        '',
    ])
    (BUILD / 'capa.tex').write_text(corpo, encoding='utf-8')


def escapar_latex(t):
    for a, b in (('\\', r'\textbackslash{}'), ('&', r'\&'), ('%', r'\%'),
                 ('$', r'\$'), ('#', r'\#'), ('_', r'\_'),
                 ('{', r'\{'), ('}', r'\}'), ('~', r'\textasciitilde{}'),
                 ('^', r'\textasciicircum{}')):
        t = t.replace(a, b)
    return t


def com_urls(t):
    """Escapa o texto e envolve URLs em \\url{} para poderem quebrar linha."""
    partes = re.split(r'(https?://\S+)', t)
    return ''.join(f'\\url{{{p.rstrip(".,;)")}}}' if k % 2 else escapar_latex(p)
                   for k, p in enumerate(partes))


def indice_figuras_tex():
    """Indice de figuras do original: figura, legenda e pagina (via \\pageref)."""
    linhas = []
    for l in (APOSTILA / 'indice-figuras.md').read_text(encoding='utf-8').split('\n'):
        if not l.startswith('| ') or l.startswith('| Figura') or set(l) <= set('|- '):
            continue
        c = [x.strip() for x in l.strip('|').split('|')]
        if len(c) < 4 or not c[0].isdigit():
            continue
        n, leg = int(c[0]), c[3]
        leg = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', leg)      # link -> texto
        linhas.append(f'{n} & {com_urls(leg)} & \\pageref{{fig:{n:02d}}} \\\\')
    corpo = '\n'.join([
        '% Gerado por build-tex.py a partir de apostila/indice-figuras.md.',
        '\\begingroup\\small',
        '\\begin{longtable}{@{}r>{\\raggedright\\arraybackslash}p{0.68\\linewidth}r@{}}',
        '\\toprule',
        'Figura & Legenda & Página \\\\',
        '\\midrule',
        '\\endhead',
        '\\bottomrule',
        '\\endfoot',
    ] + linhas + [
        '\\end{longtable}',
        '\\endgroup',
        '',
    ])
    (BUILD / 'indice-figuras.tex').write_text(corpo, encoding='utf-8')


def separar_blocos(ls):
    """O leitor markdown do pandoc só reconhece título ou início de tabela se a
    linha vier depois de uma linha em branco; sem isso o bloco é absorvido pelo
    parágrafo anterior.

    A linha em branco entra apenas no início da tabela: inserir entre as linhas
    de uma tabela a desmonta em tabelas de uma linha (que não são tabelas)."""
    out = []
    for l in ls:
        if out and out[-1].strip():
            if l.startswith('#') or l.startswith(':::') or \
                    (l.startswith('|') and not out[-1].startswith('|')):
                out.append('')
        out.append(l)
    return out


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    capa_tex()
    indice_figuras_tex()

    fontes = sorted(p for p in APOSTILA.glob('[0-9]*.md'))
    if not fontes:
        sys.exit('nenhum capítulo em apostila/')

    corpo = []
    for f in fontes:
        corpo.extend(normalizar(f.read_text(encoding='utf-8').split('\n')))
        corpo.append('')
    corpo = separar_blocos(corpo)
    (BUILD / 'corpo.md').write_text('\n'.join(corpo), encoding='utf-8')

    subprocess.run([
        'pandoc', str(BUILD / 'corpo.md'),
        '-f', 'markdown',
        '-t', 'latex',
        '--top-level-division=chapter',
        '--wrap=preserve',
        '--lua-filter', str(Path(__file__).resolve().parent / 'quadros.lua'),
        '-o', str(BUILD / 'corpo.tex'),
    ], check=True)

    tex = (BUILD / 'corpo.tex').read_text(encoding='utf-8')

    # imagens: nunca passar da largura da linha nem da altura da pagina
    tex = texto_imagens(tex)

    # tabelas grandes: corpo menor para caber na mancha
    tex = tex.replace('\\begin{longtable}', '\\begingroup\\scriptsize\\begin{longtable}')
    tex = tex.replace('\\end{longtable}', '\\end{longtable}\\endgroup')

    # Referencias WEB nao tem numero no original
    tex = re.sub(r'\\chapter\{Referências WEB\}',
                 lambda _m: '\\chapter*{Referências WEB}\n'
                            '\\addcontentsline{toc}{chapter}{Referências WEB}', tex)
    tex = re.sub(r'(\\chapter\*\{Referências WEB\}\n\\addcontentsline\{toc\}'
                 r'\{chapter\}\{Referências WEB\}\n?)(\\label\{[^}]*\}\n?)?',
                 lambda m: m.group(1), tex)

    (BUILD / 'corpo.tex').write_text(tex, encoding='utf-8')
    print(f'corpo.md: {len(corpo)} linhas | capítulos: {len(fontes)}')


def texto_imagens(tex):
    """Limita o tamanho de toda imagem e rotula cada figura.

    A maioria vem como ambiente `figure` (pandoc, a partir do texto alternativo).
    Uma imagem que o pandoc deixou fora de `figure` recebe o mesmo limite e um
    rotulo, para o indice de figuras nao ficar com referencia pendente."""
    limite = ('max width=\\linewidth,max height=0.82\\textheight')

    def repl(m):
        n = int(m.group(1))
        return ('\\begin{figure}[H]\n\\centering\n'
                f'\\includegraphics[{limite}]{{figuras/figura-{n:02d}.png}}\n'
                f'\\label{{fig:{n:02d}}}')

    tex = re.sub(r'\\begin\{figure\}\n\\centering\n'
                 r'\\includegraphics\{figuras/figura-(\d+)\.png\}', repl, tex)

    def repl_solto(m):
        n = int(m.group(1))
        return (f'\\par\\noindent\\makebox[\\linewidth][c]{{'
                f'\\includegraphics[{limite}]{{figuras/figura-{n:02d}.png}}}}\\par'
                f'\\label{{fig:{n:02d}}}')

    tex = re.sub(r'\\includegraphics\{figuras/figura-(\d+)\.png\}', repl_solto, tex)
    return tex


if __name__ == '__main__':
    main()
