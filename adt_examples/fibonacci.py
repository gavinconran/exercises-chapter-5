"""Contains the class Fib for Ex 5 of OOP4Maths."""

class Fib:
    """The Fib class represents a fibonacci number."""

    def __init__(self, next=None):
        """Fib class constructor method."""
        self.value1 = 0
        self.value2 = 1
        self.next = next

    def __iter__(self):
        return FibIterator(self)

    def __next__(self):
        return next(FibIterator(self))


class FibIterator:
    """Concrete implementation of the iterator protocol"""
    def __init__(self, link):
        self.here = link

    def __iter__(self):
        return self

    def __next__(self):
        if self.here:
            next = self.here
            #self.here = self.here.next
            f_1 = next.value1
            f_2 = next.value2
            next.value1 = f_2
            next.value2 = f_1 + f_2
            #print(f_1 + f_2)
            return f_1 + f_2 
        else:
            raise StopIteration
