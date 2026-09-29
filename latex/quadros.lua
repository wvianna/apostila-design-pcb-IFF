-- quadros.lua — converte divs marcados em caixas de destaque do LaTeX.
--
-- No markdown da apostila:
--
--   ::: {.quadro tipo="dica" titulo="Dica"}
--   Texto do quadro.
--   :::
--
-- `tipo` define a cor (nota, dica, atencao, importante) e `titulo` o rótulo.
-- O ambiente `quadro` está definido em apostila.tex (tcolorbox, quebrável).

local CORES = {
  nota      = 'blue!55!black',
  dica      = 'green!50!black',
  atencao   = 'orange!85!black',
  importante = 'red!65!black',
}

function Div(el)
  if not el.classes:includes('quadro') then
    return nil
  end
  local tipo = el.attributes['tipo'] or 'nota'
  local titulo = el.attributes['titulo'] or 'Nota'
  local corpo = pandoc.write(pandoc.Pandoc(el.content), 'latex')
  return pandoc.RawBlock('latex', string.format(
    '\\begin{quadro}{%s}{%s}\n%s\n\\end{quadro}',
    CORES[tipo] or CORES['nota'], titulo, corpo))
end
