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

@mod.capture(
    rule="[short | bare] {user.math_big_operator}"
)
def big_operator_snippet(m) -> str:
    name = m.math_big_operator

    if m[0] == "short":
        return f"\\{name}_{{$lower}} $body"
    if m[0] == "bare":
        return f"\\{name} $body"
    return f"\\{name}_{{$lower}}^{{$upper}} $body"

def get_environment_snippet(name: str):
    return f"\\begin{{{name}}}\n\t$body\n\\end{{{name}}}"

@mod.action_class
class Actions:
    def latex_wrap_with_environment(name: str, target: dict):
        """Insert a latex environment"""
        actions.user.cursorless_wrap_with_custom_snippet(get_environment_snippet(name), target, "body")

    def fraction_snippet() -> str:
        """Get the fraction snippet"""
        return "\\frac{$numerator}{$denominator}"


@ctx.action_class("user")
class Actions:
    def latex_insert_environment(name: str):
        actions.user.cursorless_insert_custom_snippet(get_environment_snippet(name))

    def maths_greek_letter(letter: str):
        actions.insert(f"\\{letter} ")

    def maths_tex_symbol(symbol: str):
        actions.insert(f"\\{symbol} ")

    def maths_matrix(rows: int, columns: int):
        raise NotImplementedError()

    def maths_fraction():
        actions.user.cursorless_insert_custom_snippet(actions.user.fraction_snippet())

    def maths_begin_superscript():
        raise NotImplementedError()

    def maths_begin_subscript():
        raise NotImplementedError()
