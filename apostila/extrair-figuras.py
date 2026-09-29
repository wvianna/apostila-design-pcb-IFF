#!/usr/bin/env python3
"""Extrai figuras de um PDF cujas legendas sejam do tipo "Figura N: ...".

Estrategia validada: a caixa da imagem termina exatamente no topo da legenda.
- caixas: `mutool trace` (y medido do topo da pagina)
- legendas: `pdftotext -bbox`
- recorte: `pdftoppm -r 300` + Pillow

Uso: extrair_figuras.py <pdf> <dir_saida> [--report <json>]
Nao substitui figura ausente por outra: legendas sem imagem vao para o relatorio.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

DPI = 300
SCALE = DPI / 72.0
PAD = 2          # pt de folga no recorte
Y_BAND = 25.0    # pt acima da legenda onde a imagem pode terminar
Y_TOL = 3.0      # caixas que terminam na mesma linha = mesma figura
MIN_H = 12.0     # descarta filetes/linhas decorativas
MIN_W = 24.0

IMG_RE = re.compile(
    r'transform="([-\d.eE]+) ([-\d.eE]+) ([-\d.eE]+) ([-\d.eE]+) '
    r'([-\d.eE]+) ([-\d.eE]+)" width="(\d+)" height="(\d+)"'
)
WORD_RE = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" '
                     r'yMax="([\d.]+)">(.*?)</word>')
CAP_RE = re.compile(r'^\**\s*Figura\s+(\d+)\s*:')
LEADER_RE = re.compile(r'\.{4,}')   # pontos de preenchimento = linha de indice/sumario


def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def page_count(pdf):
    out = sh(["pdfinfo", str(pdf)])
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    return int(m.group(1))


def image_boxes(pdf, page):
    """Caixas de imagem da pagina, em pt, com y medido do topo."""
    trace = sh(["mutool", "trace", str(pdf), str(page)])
    boxes = []
    for line in trace.splitlines():
        m = IMG_RE.search(line)
        if not m:
            continue
        a, _b, _c, d, e, f = (float(m.group(i)) for i in range(1, 7))
        x0, x1 = sorted((e, e + a))
        y0, y1 = sorted((f, f + d))
        if (y1 - y0) < MIN_H or (x1 - x0) < MIN_W:
            continue
        boxes.append({"x0": x0, "y0": y0, "x1": x1, "y1": y1})
    return boxes


def _group_lines(words, tol):
    """Agrupa palavras em linhas por proximidade vertical (tol em pt)."""
    lines = []
    for w in sorted(words, key=lambda w: w["y0"]):
        for ln in lines:
            if abs(ln["y"] - w["y0"]) <= tol:
                ln["ws"].append(w)
                break
        else:
            lines.append({"y": w["y0"], "ws": [w]})
    return [(" ".join(w["t"] for w in sorted(ln["ws"], key=lambda w: w["x0"])),
             ln["ws"]) for ln in lines]


def _words(pdf, page):
    """Palavras da pagina com caixa em pt (pdftotext -bbox)."""
    xml = sh(["pdftotext", "-bbox", "-f", str(page), "-l", str(page), str(pdf), "-"])
    out = []
    for m in WORD_RE.finditer(xml):
        out.append({"x0": float(m.group(1)), "y0": float(m.group(2)),
                    "x1": float(m.group(3)), "y1": float(m.group(4)),
                    "t": m.group(5)})
    return out


def captions(pdf, page):
    """Legendas 'Figura N: ...' da pagina.

    Usa tres tolerancias de agrupamento: a exata separa a legenda do rodape
    quando os dois correm na mesma faixa vertical; a frouxa cobre o caso normal.
    """
    words = _words(pdf, page)
    out = {}
    for tol in (0.5, 1.6, 4.5):
        for text, ws in _group_lines(words, tol):
            m = re.search(r'Figura\s+(\d+)\s*:', text)
            if not m:
                continue
            n = int(m.group(1))
            if n in out:
                continue
            out[n] = {"n": n, "y": min(w["y0"] for w in ws),
                      "y1": max(w["y1"] for w in ws),
                      "x0": min(w["x0"] for w in ws),
                      "x1": max(w["x1"] for w in ws),
                      "indice": bool(LEADER_RE.search(text))}
    return sorted(out.values(), key=lambda c: c["y"])


def all_lines(pdf, page, tol=4.5):
    """Todas as linhas de texto da pagina, com caixa em pt."""
    out = []
    for text, ws in _group_lines(_words(pdf, page), tol):
        out.append({"t": text,
                    "y0": min(w["y0"] for w in ws), "y1": max(w["y1"] for w in ws),
                    "x0": min(w["x0"] for w in ws), "x1": max(w["x1"] for w in ws)})
    return out


def _caption_blocks(caps, lines):
    """Legendas com suas linhas de continuacao (legenda quebrada em varias linhas).

    O rodape nao entra: so legendas delimitam o corte."""
    blocks = []
    for cap in caps:
        y1 = cap["y1"]
        for _ in range(2):
            nxt = None
            for ln in lines:
                if not (y1 - 2 <= ln["y0"] <= y1 + 8):
                    continue
                if re.search(r'Figura\s+\d+\s*:', ln["t"]):
                    continue
                if ln["x1"] < cap["x0"] or ln["x0"] > cap["x1"]:
                    continue
                if nxt is None or ln["y0"] < nxt["y0"]:
                    nxt = ln
            if nxt is None:
                break
            y1 = nxt["y1"]
        blocks.append({"y": cap["y"], "y1": y1,
                       "x0": cap["x0"], "x1": cap["x1"]})
    return blocks


def _top_limit(cap, blocks):
    """Y abaixo do qual o corte pode comecar: nao invadir a legenda anterior
    da mesma coluna (a caixa da imagem pode se sobrepor a ela na origem)."""
    lim = 0.0
    for b in blocks:
        if b["y"] >= cap["y"] - 2:
            continue
        if b["x1"] < cap["x0"] or b["x0"] > cap["x1"]:
            continue
        lim = max(lim, b["y1"] + 2)
    return lim


def main():
    pdf = Path(sys.argv[1])
    outdir = Path(sys.argv[2])
    report = Path(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[3] == "--report" else None
    outdir.mkdir(parents=True, exist_ok=True)

    found, missing, used_boxes = {}, [], []
    indice = set()
    resume = "--resume" in sys.argv
    total = page_count(pdf)

    for page in range(1, total + 1):
        all_caps = captions(pdf, page)
        if not all_caps:
            continue
        for c in all_caps:
            if c["indice"]:
                indice.add(c["n"])
        caps = [c for c in all_caps if not c["indice"]]
        if resume:
            caps = [c for c in caps
                    if not (outdir / f"figura-{c['n']:02d}.png").exists()]
        if not caps:
            continue
        boxes = image_boxes(pdf, page)
        lines = all_lines(pdf, page)
        blocks = _caption_blocks(caps, lines)
        assigned = {}
        for cap in caps:
            cand = [b for b in boxes if 0 <= cap["y"] - b["y1"] <= Y_BAND]
            if not cand:
                missing.append({"figura": cap["n"], "pagina": page,
                                "legenda_y": cap["y"]})
                continue
            best = min(cand, key=lambda b: cap["y"] - b["y1"])
            band = [b for b in cand if abs(b["y1"] - best["y1"]) <= Y_TOL]
            same_line = [c for c in caps if abs(c["y"] - cap["y"]) < 6]
            if len(same_line) > 1:
                cx = (cap["x0"] + cap["x1"]) / 2
                band = [min(band, key=lambda b: abs((b["x0"] + b["x1"]) / 2 - cx))]
            assigned[cap["n"]] = (cap, band)

        if not assigned:
            continue

        # renderiza a pagina uma unica vez
        prefix = outdir / f".page-{page:03d}"
        sh(["pdftoppm", "-r", str(DPI), "-png", "-f", str(page), "-l", str(page),
            str(pdf), str(prefix)])
        renders = sorted(outdir.glob(f".page-{page:03d}*.png"))
        if not renders:
            continue

        from PIL import Image
        img = Image.open(renders[0])
        W, H = img.size

        for n, (cap, band) in assigned.items():
            x0 = min(b["x0"] for b in band)
            y0 = max(min(b["y0"] for b in band), _top_limit(cap, blocks))
            x1 = max(b["x1"] for b in band)
            y1 = min(max(b["y1"] for b in band), cap["y"] - 0.7)
            box = (max(0, int((x0 - PAD) * SCALE)), max(0, int((y0 - PAD) * SCALE)),
                   min(W, int((x1 + PAD) * SCALE)), min(H, int((y1 + PAD) * SCALE)))
            if box[2] - box[0] < 8 or box[3] - box[1] < 8:
                missing.append({"figura": n, "pagina": page, "motivo": "caixa degenerada"})
                continue
            dest = outdir / f"figura-{n:02d}.png"
            img.crop(box).save(dest)
            found[n] = {"figura": n, "pagina": page, "arquivo": dest.name,
                        "pt": [round(x0, 1), round(y0, 1), round(x1, 1), round(y1, 1)],
                        "px": list(box)}
            used_boxes.append((page, box))
        for r in renders:
            r.unlink()

    arquivos = sorted(p.name for p in outdir.glob("figura-*.png"))
    print(json.dumps({
        "pdf": str(pdf), "paginas": total, "dpi": DPI,
        "extraidas_nesta_execucao": len(found),
        "arquivos_no_dir": len(arquivos),
        "entradas_de_indice": len(indice),
        "sem_imagem": len(missing),
        "max_figura": max(found) if found else 0,
        "faltantes": sorted(set(range(1, (max(found) if found else 0) + 1)) - set(found)),
        "detalhe_faltantes": missing,
        "figuras": [found[k] for k in sorted(found)],
    }, ensure_ascii=False, indent=1))
    if report:
        report.write_text(json.dumps({"figuras": [found[k] for k in sorted(found)],
                                      "faltantes": missing}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
