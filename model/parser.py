""" Parser module. Contains functions to help break down
a string expression into operations
"""
import pyparsing as pp


def parse_expression(string: str, variables: dict) -> pp.ParseResults:
    """ Parses a string into a nested array of operations """
    atom = pp.Word(pp.alphanums + "_")

    operators = [
        (pp.Literal("-").setResultsName("operator"), 1, pp.opAssoc.RIGHT),
        (pp.Literal("^").setResultsName("operator"), 2, pp.opAssoc.LEFT),
        (pp.Literal("*").setResultsName("operator"), 2, pp.opAssoc.RIGHT),
        (pp.Literal("/").setResultsName("operator"), 2, pp.opAssoc.LEFT),
        (pp.Literal("+").setResultsName("operator"), 2, pp.opAssoc.LEFT),
        (pp.Literal("-").setResultsName("operator"), 2, pp.opAssoc.LEFT),
    ]

    expr = pp.infix_notation(atom, operators)

    return evaluate_input(expr.parse_string(string), variables)


def evaluate_input(expression: pp.ParseResults | list, variables: dict):
    """ Inserts values of the variables in expression """
    for num in range(len(expression)):
        if isinstance(expression[num], pp.ParseResults) or \
                isinstance(expression[num], list):
            expression[num] = evaluate_input(expression[num], variables)
        elif expression[num] in variables:
            expression[num] = variables[expression[num]]
        elif expression[num] is not expression.operator:
            try:
                expression[num] = float(expression[num])
            except (ValueError, TypeError):
                if expression.operator == "^" and (
                        expression[2] == "det" or
                        expression[2] == "T"
                ):
                    pass  # reserved for determinant and transposition operations
                else:
                    raise TypeError(f'No variable named {expression[num]}')

    return expression


print(parse_expression("A*B*C", {"A": 5, "B": 4, "C": 3}))
