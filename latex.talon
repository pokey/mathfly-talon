title: /\.tex/
and not app: scinoteb.exe
-
document class {user.tex_document_classes}:
    insert("\\documentclass{{{tex_document_classes}}}\n")
use package {user.tex_packages}:
    insert("\\usepackage{{{tex_packages}}}\n")
use package bib latex:
    insert("\\usepackage[style=authoryear]{{biblatex}}\n")

begin {user.tex_environments}: user.latex_insert_environment(tex_environments)
insert {user.tex_commands}: user.insert_between("\\{tex_commands}{{", "}}")
insert {user.tex_commands_noarg}: insert("\\{tex_commands_noarg} ")
greek {user.greek_letters}: insert("\\{greek_letters} ")
symbol {user.tex_symbols}: insert("\\{tex_symbols} ")

template {user.tex_templates}: user.paste(tex_templates)