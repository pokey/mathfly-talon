from typing import Optional
from talon import Module, Context, actions, app

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vscode
tag: user.cursorless
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
        actions.user.cursorless_wrap_with_custom_snippet(
            get_environment_snippet(name), target, "body"
        )

    def fraction_snippet() -> str:
        """Get the fraction snippet"""
        return "\\frac{$numerator}{$denominator}"


@ctx.action_class("user")
class Actions:
    def latex_insert_environment(name: str):
        actions.user.cursorless_insert_custom_snippet(get_environment_snippet(name))

    def maths_matrix(rows: int, columns: int, matrix_type: str):
        matrix_snippet = get_matrix_snippet(rows, columns, matrix_type)
        actions.user.cursorless_insert_custom_snippet(matrix_snippet)

    def maths_fraction():
        actions.user.cursorless_insert_custom_snippet(actions.user.fraction_snippet())


def get_matrix_snippet(rows: int, columns: int, matrix_type: str):
    matrix_snippet = f"\\begin{{{matrix_type}}}\n"
    # NB: We need 8 backslashes here because we want 2, and we need to escape in
    # Python, and also for our snippet parser
    matrix_snippet += " \\\\\\\\\n".join(
        [get_matrix_row(row_idx, columns) for row_idx in range(rows)]
    )
    matrix_snippet += f"\n\\end{{{matrix_type}}}"
    return matrix_snippet


def get_matrix_row(row_idx: int, columns: int):
    content = " & ".join(
        [f"$cell_{row_idx}_{column_idx}" for column_idx in range(columns)]
    )
    return f"\t{content}"
