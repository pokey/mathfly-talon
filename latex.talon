title: /.Overleaf./
title: /\.tex/
not app: scinoteb.exe
-
document class {user.tex_document_classes}:
    user.cursorless_insert_snippet("\\documentclass{{{tex_document_classes}}}\n")
use package {user.tex_packages}:
    user.cursorless_insert_snippet("\\usepackage{{{tex_packages}}}\n")
use package bib latex:
    user.cursorless_insert_snippet("\\usepackage[style=authoryear]{{biblatex}}\n")

begin {user.tex_environments}: user.latex_insert_environment(tex_environments)
insert {user.tex_commands}: user.insert_between("\\{tex_commands}{{", "}}")
insert {user.tex_commands_noarg}: user.cursorless_insert_snippet("\\{tex_commands_noarg} ")
greek {user.greek_letters}: user.cursorless_insert_snippet("\\{greek_letters} ")
symbol {user.tex_symbols}: user.cursorless_insert_snippet("\\{tex_symbols} ")

template {user.tex_templates}: user.paste(tex_templates)
