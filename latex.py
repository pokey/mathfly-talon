from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = r"""
title: /Overleaf/
title: /\.tex/
and not app: scinoteb.exe
"""

mod.list("tex_document_classes", desc="TeX document classes")
ctx.lists["user.tex_document_classes"] = {
    "article": "article",
    "beamer": "beamer",
    "book": "book",
    "letter": "letter",
    "proceedings": "proc",
    "report": "report",
}

mod.list("tex_packages", desc="TeX packages")
ctx.lists["user.tex_packages"] = {
    "adjustbox": "adjust box",
    "after page": "afterpage",
    "AMS math": "amsmath",
    "appendix": "appendix",
    "array": "array",
    "BBM": "bbm",
    "book tabs": "booktabs",
    "bookmark": "bookmark", 
    "caption": "caption",
    "clever ref": "cleverref",
    "colour": "color",
    "comment": "comment",
    "E tool box": "etoolbox",
    "ellipses": "ellipsis",
    "fancy H D R": "fancyhdr",
    "float": "float",
    "font enc": "fontenc",
    "geometry": "geometry",
    "graphic X": "graphicx",
    "hyper ref": "hyperref",
    "if draft": "ifdraft", 
    "inputenc": "inputenc",
    "L modern": "lmodern",
    "long table": "longtable",
    "math tools": "mathtools",
    "math tools": "mathtools",
    "micro type": "microtype",
    "multi col": "multicol",
    "nat bib": "natbib",
    "PDF landscape": "pdflscape",
    "place ins": "placeins",
    "rotating": "rotating",
    "see unit X": "siunitx",
    "sub caption": "subcaption",
    "taboo": "tabu",
    "tabular X": "tabularx",
    "text comp": "textcomp",
    "three part tablex": "threeparttablex",
    "three part table": "threeparttable",
    "title seck": "titlesec",
    "title tock": "titletoc",
    "to do notes": "todonotes",
    "verbatim": "verbatim",
    "wrap figure": "wrapfig",
    "X color": "xcolor",
    "XR": "xr",
    # "bib latex"   = ["[style=authoryear]", "biblatex"]
}

mod.list("tex_environments", desc="TeX environments")
ctx.lists["user.tex_environments"] = {
    "abstract": "abstract",
    "add margin": "addmargin",
    "align": "align",
    "center": "center",
    "columns": "columns",
    # "column"                      = ["column", "{0.5\\textwidth}"]
    "column": "column",
    "comment": "comment",
    "cases": "cases",
    "display cases": "dcases",
    "definition": "definition",
    "description": "description",
    "document": "document",
    "enumerate": "enumerate",
    "equation": "equation",
    # "figure"                      = ["figure", "[h!]"]
    "figure": "figure",
    "flush left": "flushleft",
    "flush right": "flushright",
    "frame": "frame",
    "itemise": "itemize",
    "mini page": "minipage",
    # "multi (cols | columns)"      = ["multicols", "{2}"]
    "multi line": "multline",
    "proof": "proof",
    "quotation": "quotation",
    "quote": "quote",
    "split": "split",
    # "table"                       = ["table", "[h!]\n\\centering"]
    # "long table"                  = ["longtable", "{lll}"]
    # "tabular"                     = ["tabular", "{llll}"]
    # "tabular X"                   = ["tabular X", "{l X}"]
    "theorem": "theorem",
    "title page": "titlepage",
    "verbatim": "verbatim",
    "verse": "verse",
    "wrap figure": "wrapfigure",
}

mod.list("tex_commands", desc="TeX commands")
ctx.lists["user.tex_commands"] = {
    "author": "author",
    "add bib resource": "addbibresource",
    "caption": "caption",
    "chapter": "chapter",
    "cite text": "citet",
    "cite all text": "citet*",
    "cite paren": "citep",
    "site paren": "citep",
    "cite all paren": "citep*",
    "cite author": "citeauthor",
    "cite year": "citeyear",
    "clever ref": "cref",
    "simple citation": "cite",
    "frame title": "frametitle",
    "footnote": "footnote",
    "footnote text": "footnotetext[]",
    "graphics path": "graphicspath",
    "h space": "hspace",
    "horizontal space": "hspace",
    "include graphics": "includegraphics[width=1\\textwidth]",
    "label": "label",
    "new command": "newcommand{}[]",
    "paragraph": "paragraph",
    "paren cite": "parencite",
    "part": "part",
    "reference": "ref",
    "renew command": "renewcommand",
    "sub paragraph": "subparagraph",
    "section": "section",
    "sub section": "subsection",
    "sub sub section": "subsubsection",
    "text cite": "textcite",
    "bold": "textbf",
    "italics": "textit",
    "slanted": "textsl",
    "emphasis": "emph",
    "text color":"textcolor{}",
    "text color blue":"textcolor{blue}",
    "title": "title",
    "use theme": "usetheme",
    "v space": "vspace",
    "vertical space": "vspace",
    # Accents
    "accent grave": "`",
    "accent acute": "'",
    "accent dot": ".",
    "accent breve": "u",
    "circumflex": "^",
    "umlaut": '"',
    "tilde": "~",
    "macron": "=",
}

mod.list("tex_commands_noarg", desc="TeX commands without arguments")
ctx.lists["user.tex_commands_noarg"] = {
    "centering": "centering",
    "column": "column{0.5\\textwidth}",
    "footnote mark": "footnotemark[]",
    "h line": "hline",
    "horizontal line": "hline",
    "lay tech": "LaTeX~ ",
    "line break": "linebreak",
    "item": "item",
    "make title": "maketitle",
    "new page": "newpage",
    "no indent": "noindent",
    "page break": "pagebreak",
    "print bibliography": "printbibliography",
    "table of contents": "tableofcontents",
    "tech": "TeX~ ",
    "text backslash": "textbackslash",
    "text height": "textheight",
    "text width": "textwidth",
    "v line": "vline",
    "vertical line": "vline",
}

ctx.lists["user.greek_letters"] = {
    # Lowercase
    "alpha": "alpha",
    "beater": "beta",
    "gamma": "gamma",
    "delta": "delta",
    "epsilon": "varepsilon",
    "zita": "zeta",
    "eater": "eta",
    "theta": "theta",
    "iota": "iota",
    "kappa": "kappa",
    "lambda": "lambda",
    "mu": "mu",
    "new": "nu",
    "zee": "xi",
    "pie": "pi",
    "row": "rho",
    "sigma": "sigma",
    "tau": "tau",
    "upsilon": "upsilon",
    "phi": "phi",
    "chi": "chi",
    "sigh": "psi",
    "omega": "omega",
    # Capitals
    "big gamma": "Gamma",
    "big delta": "Delta",
    "big theta": "Theta",
    "big lambda": "Lambda",
    "big zee": "Xi",
    "big pie": "Pi",
    "big sigma": "Sigma",
    "big upsilon": "Upsilon",
    "big phi": "Phi",
    "big sigh": "Psi",
    "big omega": "Omega",
}

ctx.lists["user.bracket_type"] = {
    "nude": "matrix",
    "curly": "Bmatrix",
    "round": "pmatrix",
    "square": "bmatrix",
    "pipe": "vmatrix",
    "double pipe": "Vmatrix",
}

@mod.action_class
class Actions:
    def latex_insert_environment(name: str):
        """Insert a latex environment"""
        actions.insert(f"\\begin{{{name}}}")
        actions.key("enter:2")
        actions.insert(f"\\end{{{name}}}")
        actions.key("up")

@ctx.action_class("user")
class Actions:
    def maths_greek_letter(letter: str):
        actions.insert(f"\\{letter} ")

    def maths_tex_symbol(symbol: str):
        actions.insert(f"\\{symbol} ")

    def maths_begin_superscript():
        actions.user.insert_between("^{", "}")

    def maths_begin_subscript():
        actions.user.insert_between("_{", "}")


mod.list("tex_templates", desc="TeX templates")
ctx.lists["user.tex_templates"] = {
    "header": r'''
\documentclass[12pt, a4paper]{article}

\usepackage{graphicx}
\usepackage{hyperref}
\usepackage[utf8]{inputenc}
\usepackage{booktabs}
\usepackage[style=authoryear]{biblatex}
\addbibresource{}

\setlength{\parskip}{1em}
\renewcommand{\baselinestretch}{1.3}
''',
# ------------------------------------
    "beamer": r'''
\documentclass{beamer}
\usetheme{metropolis}
\usepackage{graphicx}
\usepackage[style=authoryear]{biblatex}
\addbibresource{}

\begin{document}
\begin{frame}
\frametitle{}

\end{frame}
\end{document}
''',
# ------------------------------------
    "figure": r'''
\begin{figure}[h!]
    \centering
    \includegraphics[width=1\textwidth]{}
    \caption{}
    \label{}
\end{figure}
''',
# ------------------------------------
    "wrap figure": r'''
\begin{wrapfigure}{l}{0.5\textwidth}
    \centering
    \includegraphics[width=0.4\textwidth]{}
    \caption{}
    \label{}
\end{wrapfigure}
''',
# ------------------------------------
    "table": r'''
\begin{table}[h!]
    \centering
    \begin{tabular}{ccccc}
    &  &  &  & \\
    \hline
    &  &  &  &  \\
    \end{tabular}
    \caption{}
    \label{}
\end{table}
''',
# ------------------------------------
    "three part table": r'''
\begin{table}[h!]
    \begin{threeparttable}[]
        \caption{}
        \label{}
        \begin{tabularx}{\linewidth}{Xcccc}
            \toprule
                      &  &  &  & \\
            \midrule
            \tnote{1} &  &  &  & \\
                      &  &  &  & \\
            \bottomrule
        \end{tabularx}
        \begin{tablenotes}
            \item [1]
        \end{tablenotes}
    \end{threeparttable}
\end{table}
''',
# ------------------------------------
"three part tablex": r'''
\begin{ThreePartTable}
    \begin{TableNotes}
        \item[a] A note
        \item[b] Another note
    \end{TableNotes}
    \begin{longtable}{l l}
        \caption{} \label{} \\
        \toprule
        Column 1   & Column 2   \\
        \midrule
        \endhead
        \cmidrule{2-2}
        \multicolumn{2}{r}{\textit{continued}}
        \endfoot
        \bottomrule
        \insertTableNotes
        \endlastfoot
        % the contents of the table
        A          & B\tnote{a} \\
        C\tnote{b} & D          \\
    \end{longtable}
\end{ThreePartTable}
'''
}
