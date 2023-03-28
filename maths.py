from talon import Context, Module, actions
from typing import NamedTuple, Optional

fractions = {
    "half": "2",
    "halve": "2",
    "third": "3",
    "quarter": "4",
    "fourth": "4",
    "fifth": "5",
    "sixth": "6",
    "seventh": "7",
    "eighth": "8",
    "ninth": "9",
    "tenth": "10",
}

mod = Module()
ctx = Context()

mod.tag("maths")

mod.list("bracket_type", "Matrix bracket types, eg parenthesized, brackets, etc.")
mod.list("matrix_type", "Matrix types, eg full, diagonal, etc.")

ctx.lists["user.matrix_type"] = {
    "identity": "identity",
    "scaler": "scalar",
    "diagonal": "diagonal",
    "full": "full",
}

mod.list("maths_fractions", "Fractions")
ctx.lists["user.maths_fractions"] = {
    **fractions,
    **{f"{k}s": v for k, v in fractions.items()},
}


@mod.action_class
class Actions:
    def maths_greek_letter(letter: str):
        """Insert a greek letter (one of those in the greek_letters list)"""
        actions.insert("\\" + str(letter))
    def maths_tex_symbol(symbol: str):
        """Insert a TeX symbol (one of those in the tex_symbols list)"""

    def maths_matrix(rows: int, columns: int, bracket_type: str, matrix_type: str):
        """Insert a matrix (rows x columns)"""

    def maths_fraction():
        """Begin a fraction"""

    def maths_begin_subscript():
        """Begin subscript"""
        actions.key("_ { } left")
    def maths_end_subscript():
        """End subscript"""
        actions.key("right")
    def maths_subscript(label: str):
        """Subscript"""
        actions.user.maths_begin_subscript()
        actions.insert(label)
        actions.user.maths_end_subscript()

    def maths_begin_superscript():
        """Begin superscript"""
        actions.key("^ { } left")
    def maths_end_superscript():
        """End superscript"""
        actions.key("right")
    def maths_superscript(exponent: str):
        """Superscript"""
        actions.user.maths_begin_superscript()
        actions.insert(exponent)
        actions.user.maths_end_superscript()
