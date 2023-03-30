app: vscode
tag: user.cursorless
title: /\.tex/
-
tag(): user.maths

{user.tex_environments} wrap <user.cursorless_target>:
    user.latex_wrap_with_environment(tex_environments, cursorless_target)
place <user.cursorless_target> over:
    user.cursorless_wrap_with_snippet(user.fraction_snippet(), cursorless_target, "numerator")
place <user.cursorless_target> under:
    user.cursorless_wrap_with_snippet(user.fraction_snippet(), cursorless_target, "denominator")

<user.big_operator_snippet> wrap <user.cursorless_target>:
    user.cursorless_wrap_with_snippet(big_operator_snippet, cursorless_target, "body")
<user.big_operator_snippet>: user.cursorless_insert_snippet(big_operator_snippet)

# Matrices
[{user.bracket_type}] scaler matrix <number_small> [by <number_small>] wrap <user.cursorless_target>:
    snippet = user.matrix_snippet(number_small, number_small_2 or number_small, bracket_type or "bmatrix", "scalar")
    user.cursorless_wrap_with_snippet(snippet, cursorless_target, "constant")

# TODO: Implement the stuff below this line

add matrix row: user.lyx_control_sequence("m", "w i")
(delete | remove) matrix row: user.lyx_control_sequence("m", "w d")
add matrix column: user.lyx_control_sequence("m", "c i")
(delete | remove) matrix column: user.lyx_control_sequence("m", "c d")

square root: user.lyx_control_sequence("m", "s")
generic root: user.lyx_control_sequence("m", "r")

brackets: user.lyx_control_sequence("m", "(")
square brackets: user.lyx_control_sequence("m", "[")
curly brackets: user.lyx_control_sequence("m", "{")
angle brackets: user.lyx_control_sequence("m", "<")
absolute: user.lyx_control_sequence("m", "|")

accent hat: user.lyx_control_sequence("m", "h")
accent tilde: user.lyx_control_sequence("m", "&")
accent dot: user.lyx_control_sequence("m", ".")
accent double dot: user.lyx_control_sequence("m", '"')
accent bar: user.lyx_control_sequence("m", "-")
accent vector: user.lyx_control_sequence("m", "v")

blank limit: "\\lim "
limit:
    insert("\\underset \\lim ")
    key(down)
label above: "\\overset "
label below: "\\underset "
prime: user.maths_superscript("\\prime")
degrees: user.maths_superscript("\\degrees")
exponential:
    insert("\\exp ")
    user.lyx_control_sequence("m", "(")
expectation:
    insert("E")
    user.lyx_control_sequence("m", "(")
variance:
    insert("Var")
    user.lyx_control_sequence("m", "(")
#
real numbers:
    insert("\\mathbb R")
    key(right)
complex numbers:
    insert("\\mathbb C")
    key(right)
integer numbers:
    insert("\\mathbb Z")
    key(right)
rational numbers:
    insert("\\mathbb Q")
    key(right)
natural numbers:
    insert("\\mathbb N")
    key(right)

text roman: "\\mathrm "
text bold: "\\mathbf "
text sans serif: "\\mathsf "
text italic: "\\mathit "
text typewriter: "\\mathtt "
text (beebee | blackboard bold | blackboard): "\\mathbb "

#
# Program control
#
new file: key(ctrl-n)
open file: key(ctrl-o)
save as: key(ctrl-shift-s)
(math | maths) mode: user.lyx_control_sequence("m", "m")
display mode: key(ctrl-shift-m)
normal mode: user.lyx_control_sequence("p", "s")
view PDF: key(ctrl-r)
update PDF: key(ctrl-shift-r)
next tab: key(ctrl-pgdown)
(prior | previous) tab: key(ctrl-pgup)
close tab: key(ctrl-w)
move line up: key(alt-up)
move line down: key(alt-down)
#
insert (in line formula | in line): user.lyx_control_sequence("i", "h i")
insert (numbered formula): user.lyx_control_sequence("i", "h n")
insert (display formula | display): user.lyx_control_sequence("i", "h d")
insert equation array: user.lyx_control_sequence("i", "h e")
#
insert [bulleted] list: user.lyx_control_sequence("p", "b")
insert numbered list: user.lyx_control_sequence("p", "e")
insert description: user.lyx_control_sequence("p", "d")
insert part: user.lyx_control_sequence("p", "0")
insert (section | heading): user.lyx_control_sequence("p", "2")
insert sub (section | heading): user.lyx_control_sequence("p", "3")
insert sub sub (section | heading): user.lyx_control_sequence("p", "4")
insert paragraph: user.lyx_control_sequence("p", "5")
insert sub paragraph: user.lyx_control_sequence("p", "6")
insert title: user.lyx_control_sequence("p", "t")
insert author: user.lyx_control_sequence("p", "shift-a")
insert date: user.lyx_control_sequence("p", "shift-d")
insert abstract: user.lyx_control_sequence("p", "a")
insert address: user.lyx_control_sequence("p", "alt-a")
insert bibliography: user.lyx_control_sequence("p", "shift-b")
insert quotation: user.lyx_control_sequence("p", "alt-q")
insert quote: user.lyx_control_sequence("p", "q")
insert verse: user.lyx_control_sequence("p", "v")
