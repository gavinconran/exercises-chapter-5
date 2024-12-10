"""Contains the class Deque for Ex 5 of OOP4Maths."""
import numpy as np # noqa F401


class Deque:
    """The Deque class represents a deque ADT."""

    def __init__(self, n, next=None):
        """Class constructor method."""
        self.list = [None] * n
        self.length = 0
        self.next = next

    def append(self, x):
        """Return a deque with x appended to the right."""
        self.list[self.length] = x
        self.length += 1
        return self.list

    def appendleft(self, x):
        """Return a deque with x appended to the left."""
        copied_list = self.list[:self.length]
        self.list[0] = x
        self.list[1:self.length + 1] = copied_list
        self.length += 1
        return self.list

    def pop(self):
        """Remove the value from the right of the deque."""
        x = self.list[self.length - 1]
        self.list[self.length - 1] = None
        self.length -= 1
        return x

    def popleft(self):
        """Remove the value from the left of the deque."""
        copied_list = self.list[1: self.length]
        x = self.list[0]
        self.length -= 1
        self.list[0: self.length] = copied_list
        return x

    def peek(self):
        """Return the value at the top of the deque."""
        if self.length == 0:
            return 'Exception: deque is empty'
        return self.list[self.length - 1]

    def peekleft(self):
        """Return the value at the top of the stack."""
        return self.list[0]

    def __len__(self):
        """Return the length of the deque."""
        return self.length

    def __iter__(self):
        return DequeIterator(self)


class DequeIterator:
    """Concrete implementation of the iterator protocol."""

    def __init__(self, link):
        self.here = link

    def __iter__(self):
        return self

    def __next__(self):
        if self.here:
            next = self.here
            self.here = self.here.next
            return next.list[:next.length][0]
        else:
            raise StopIteration
