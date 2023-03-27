from typing import Callable, Optional
from talon import Module, Context, actions, app

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
tag: user.cursorless
title: /\.tex/
"""

mod.list("math_big_operator", "Big operators such as sum, product, integral, etc.")

ctx.lists["user.math_big_operator"] = {
    "some": "sum",
    "product": "prod",
    "integral": "int",
    "double integral": "iint",
    "triple integral": "iiint",
}


@mod.capture(rule="[short | nude] {user.math_big_operator}")
def big_operator_snippet(m) -> str:
    name = m.math_big_operator

    if m[0] == "short":
        return f"\\{name}_{{$lower}} $body"
    if m[0] == "nude":
        return f"\\{name} $body"
    return f"\\{name}_{{$lower}}^{{$upper}} $body"


def get_environment_snippet(name: str):
    indentation = "" if name == "document" else "\t"
    return f"\\begin{{{name}}}\n{indentation}$body\n\\end{{{name}}}"


@mod.action_class
class Actions:
    def latex_wrap_with_environment(name: str, target: dict):
        """Insert a latex environment"""
        actions.user.cursorless_wrap_with_snippet(
            get_environment_snippet(name), target, "body"
        )

    def fraction_snippet() -> str:
        """Get the fraction snippet"""
        return "\\frac{$numerator}{$denominator}"

    def identity_matrix_snippet(size: int, bracket_type: str) -> str:
        """Get the identity matrix snippet"""
        return get_matrix_snippet(
            size, size, bracket_type, identity_matrix_get_cell_content
        )

    def scalar_matrix_snippet(size: int, bracket_type: str) -> str:
        """Get the scalar matrix snippet"""
        return get_matrix_snippet(
            size, size, bracket_type, scalar_matrix_get_cell_content
        )

    def diagonal_matrix_snippet(rows: int, columns: int, bracket_type: str) -> str:
        """Get the diagonal matrix snippet"""
        return get_matrix_snippet(
            rows, columns, bracket_type, diagonal_matrix_get_cell_content
        )

    def full_matrix_snippet(rows: int, columns: int, bracket_type: str) -> str:
        """Get the full matrix snippet"""
        return get_matrix_snippet(rows, columns, bracket_type, default_get_cell_content)


@ctx.action_class("user")
class Actions:
    def latex_insert_environment(name: str):
        actions.user.cursorless_insert_snippet(get_environment_snippet(name))

    def maths_matrix(rows: int, columns: int, bracket_type: str):
        matrix_snippet = actions.user.full_matrix_snippet(rows, columns, bracket_type)
        actions.user.cursorless_insert_snippet(matrix_snippet)

    def maths_fraction():
        actions.user.cursorless_insert_snippet(actions.user.fraction_snippet())


def identity_matrix_get_cell_content(row_idx: int, column_idx: int) -> str:
    return "1" if row_idx == column_idx else "0"


def scalar_matrix_get_cell_content(row_idx: int, column_idx: int) -> str:
    return "$constant" if row_idx == column_idx else "0"


def diagonal_matrix_get_cell_content(row_idx: int, column_idx: int) -> str:
    return f"$cell_{row_idx}_{column_idx}" if row_idx == column_idx else "0"


def default_get_cell_content(row_idx: int, column_idx: int) -> str:
    return f"$cell_{row_idx}_{column_idx}"


def get_matrix_snippet(
    rows: int,
    columns: int,
    bracket_type: str,
    get_cell_content: Callable[[int, int], str],
):
    matrix_snippet = f"\\begin{{{bracket_type}}}\n"
    # NB: We need 8 backslashes here because we want 2, and we need to escape in
    # Python, and also for our snippet parser
    matrix_snippet += " \\\\\\\\\n".join(
        [get_matrix_row(row_idx, columns, get_cell_content) for row_idx in range(rows)]
    )
    matrix_snippet += f"\n\\end{{{bracket_type}}}"
    return matrix_snippet


def get_matrix_row(
    row_idx: int,
    columns: int,
    get_cell_content: Callable[[int, int], str],
):
    content = " & ".join(
        [get_cell_content(row_idx, column_idx) for column_idx in range(columns)]
    )
    return f"\t{content}"
