"""Contains the class RPCalc for Ex 5 of OOP4Maths."""
import numbers


class RPCalc:
    """The RPCalc class represents a Reverse Polish Calculator."""

    def __init__(self):
        """Class constructor method."""
        self.stack = []

    def push(self, n):
        """Return the result of an operation."""
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
        """Remove the value from the top of the stack."""
        return self.stack.pop()

    def peek(self):
        """Return the value at the top of the stack."""
        return self.stack[-1]

    def __len__(self):
        """Return the length of the stack."""
        return len(self.stack)
