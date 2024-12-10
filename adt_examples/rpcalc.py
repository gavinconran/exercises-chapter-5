"""Contains the class RPCalc for Ex 5 of OOP4Maths."""
import numbers
import numpy as np


class RPCalc:
    """The RPCalc class represents a Reverse Polish Calculator."""

    def __init__(self):
        """RPCalc class constructor method."""
        self.stack = []

    def push(self, n):
        if isinstance(n, numbers.Number):
            return self.stack.append(n)
        elif n in ["+", "-", "*", "/", "sin", "cos"]:
            if n in ["+", "-", "*", "/"]:
                op1_str = str(self.stack.pop())
                op2_str = str(self.stack.pop())
                op_str = op2_str + n + op1_str
                return self.stack.append(eval(op_str))
            else:
                operand = str(self.stack.pop())
                op_str = 'np.' + n + '(' + operand + ')'
                return self.stack.append(eval(op_str))
        else:
            print("Can't push")

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)
