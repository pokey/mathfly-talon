from talon import Context, Module

mod = Module()
ctx = Context()

# Defined in sn55, lyx.py
mod.list("greek_letters", desc="TeX greek letters")
mod.list("tex_symbols", desc="TeX mathematical symbols")

ctx.lists["user.tex_symbols"] = {
    "binomial": "binom",
    # operators
    "times": "times",
    "divide": "div",
    "C dot": "cdot",
    "plus or minus": "pm",
    "partial": "partial",
    "infinity": "infty",
    "vector nabla": "nabla",
    # accents
    "accent hat": "hat",
    "accent tilde": "tilde",
    "accent dot": "dot",
    "accent double dot": "ddot",
    "accent bar": "bar",
    "accent vector": "vec",
    # trig
    "sine": "sin",
    "cosine": "cos",
    "tangent": "tan",
    "secant": "sec",
    "cosecant": "csc",
    "cotangent": "cot",
    "arc sine": "arcsin",
    "arc cosine": "arccos",
    "arc tan": "arctan",
    "hyperbolic sine": "sinh",
    "hyperbolic cosine": "cosh",
    "hyperbolic cotangent": "coth",
    "hyperbolic tangent": "tanh",
    # functions
    "argument": "arg",
    "degree": "deg",
    "determinant": "det",
    "dimension": "dim",
    "natural log": "ln",
    "logarithm": "log",
    "maximum": "max",
    "minimum": "min",
    "modulus": "bmod",
    "infimum": "inf",
    "supremum": "sup",
    "probability": "Pr",
    # relations
    "not equal to": "neq",
    "greater than or equal to": "geq",
    "less than or equal to": "leq",
    "approximately equal to": "approx",
    "proportional to": "propto",
    "preference less than": "prec",
    "preference less equals": "preceq",
    "preference greater than": "succ",
    "preference greater equal": "succeq",
    # logic
    "logic and": "land",
    "logic or": "lor",
    "logic not": "lnot",
    "logic exists": "exists",
    "logic member": "in",
    "logic for all": "forall",
    #
    "left arrow": "leftarrow",
    "right arrow": "rightarrow",
    "up arrow": "uparrow",
    "down arrow": "downarrow",
    "left right arrow": "leftrightarrow",
    "maps to": "mapsto",
    "oh plus": "oplus",
    "oh times": "otimes",
    "big oh plus": "bigoplus",
    "big oh times": "bigotimes",
    #
    "dot dot dot": "dots",
    "diagonal dots": "ddots",
    "horizontal dots": "cdots",
    "vertical dots": "vdots",
    # sets
    "empty set": "emptyset",
    "subset": "subset",
    "superset": "supset",
    "strict subset": "subsetneq",
    "strict superset": "supsetneq",
    "intersection": "cap",
    "union": "cup",
}
