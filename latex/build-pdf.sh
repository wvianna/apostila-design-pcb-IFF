#!/usr/bin/env bash
# Consolida apostila/*.md e compila latex/apostila.pdf.
# Gate do projeto: 0 erros LaTeX ("! ") e 0 Overfull (hbox/vbox).
set -euo pipefail
cd "$(dirname "$0")"

python3 build-tex.py
mkdir -p build

for passada in 1 2 3; do
  pdflatex -interaction=nonstopmode -file-line-error \
           -output-directory=build apostila.tex > "build/passada${passada}.log" 2>&1 || true
done

erros=$(grep -c '^! ' build/passada3.log || true)
over=$(grep -c '^Overfull' build/passada3.log || true)
echo "---------------------------------------------"
echo "erros LaTeX : ${erros}"
echo "Overfull    : ${over}"
if [ "${erros}" != "0" ]; then
  echo "--- primeiros erros ---"
  grep -n -A3 '^! ' build/passada3.log | head -60
  exit 1
fi
cp build/apostila.pdf apostila.pdf
echo "PDF: latex/apostila.pdf ($(du -h apostila.pdf | cut -f1))"
if [ "${over}" != "0" ]; then
  echo "--- overfull remanescentes ---"
  grep -n '^Overfull' build/passada3.log | head -20
fi
