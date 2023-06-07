""" This module contains
the MatrixApp class with al the internal app logic
"""
import numpy as np
from model.parser import parse_expression
from pyparsing import ParseResults
import ast


class MatrixApp:
    """ Main application class """

    def __init__(self):
        self.values = dict()
        self.expression = ""
        self.result = None

    def set_variable(self, name: str, value):
        """ Adds a name-value pair into
        application storage
        """
        try:
            self.values[name] = float(value)
        except ValueError:
            try:
                self.values[name] = np.array(ast.literal_eval(value))
            except ValueError as e:
                self.result = e
                print(str(e))
                raise e

    def del_variable(self, name: str):
        """ Deletes the name-value pair from
        application storage
        """
        del (self.values[name])

    def update(self):
        """ Updates the result of expression.
        A wrapper for a .solve() method
        """
        try:
            self.solve()
        except BaseException as e:
            self.result = str(e)

    def solve(self) -> float | np.ndarray:
        """ Updates the result
        of the stored expression
        """
        expr = parse_expression(self.expression, self.values)
        res = self.__compute(expr)
        self.result = res
        return res

    def __compute(self, expression: ParseResults):
        """ Recursively computes a value of each opeartion"""
        if not isinstance(expression, ParseResults):
            return expression
        if len(expression) == 0:
            return None
        elif len(expression) == 1:
            return self.__compute(expression[0])

        if expression.operator == "*":
            return self.__compute(expression[0]) \
                * self.__compute(expression[2])
        if expression.operator == "/":
            return self.__compute(expression[0]) \
                / self.__compute(expression[2])
        if expression.operator == "+":
            return self.__compute(expression[0]) \
                + self.__compute(expression[2])
        if expression.operator == "-":
            if len(expression) == 2:
                return -self.__compute(expression[1])
            else:
                return self.__compute(expression[0]) \
                    - self.__compute(expression[2])
        if expression.operator == "^":
            if isinstance(self.__compute(expression[0]),
                          np.ndarray | np.generic):
                if self.__compute(expression[2]) is -1:
                    return np.linalg.inv(self.__compute(expression[0]))
                elif self.__compute(expression[2]) == "T":
                    return np.transpose(self.__compute(expression[0]))
                elif self.__compute(expression[2]) == "det":
                    return np.linalg.det(self.__compute(expression[0]))

            return self.__compute(expression[0]) \
                ** self.__compute(expression[2])
