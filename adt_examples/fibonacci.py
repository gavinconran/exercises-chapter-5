"""Contains the class Fib for Ex 5 of OOP4Maths."""
import pytest-timeout


class Fib:
    """The Fib class represents a fibonaci number."""

    def __init__(self, fib_o=0, fib_1=1, next=None):
        """Fib class constructor method."""
        self.value = value
        self.next = next

    def __iter__(self):
        return FibIterator(self)


class FibIterator:
        """Concrete implementation of the iterator protocol"""
    def __init__(self, link):
        self.here = link

    def __iter__(self):
        return self

    def __next__(self):
        next = self.here
        f_1 = next.fib_0
        f_2 = next.fib_1
        next.fib_0 = f_1
        next.fib_1 = f_1 + f_2
        return next.fib_0 + next.fib_1
            