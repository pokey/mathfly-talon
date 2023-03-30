tag: user.maths
-
tag(): user.maths
help (math | maths): user.maths_help_show()
show (math | maths) help: user.maths_help_show()
hide maths help: user.maths_help_hide()

# Basic symbols
(greek | creek) {user.greek_letters}: user.maths_greek_letter(greek_letters)
{user.tex_symbols}: user.maths_tex_symbol(tex_symbols)

# Matrices
[{user.bracket_type}] [{user.matrix_type}] matrix <number_small> [by <number_small>]:
    user.maths_matrix(number_small, number_small_2 or number_small, bracket_type or "bmatrix", matrix_type or "full")

# Fractions
fraction: user.maths_fraction()
over:
    key(shift-left)
    user.maths_fraction()
    key(down)
<number> {user.maths_fractions}:
    user.maths_fraction()
    insert(number)
    key(down)
    insert(maths_fractions)
    key(right)

# Sub/Superscript
(super script | to the power): user.maths_begin_superscript()
inverse: user.maths_superscript("-1")
squared: user.maths_superscript("2")
cubed: user.maths_superscript("3")
sub script: user.maths_begin_subscript()
