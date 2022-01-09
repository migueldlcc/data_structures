class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        value = self.items[self.size() - 1]
        del self.items[-1]
        return value

    def peek(self):
        return self.items[self.size() - 1]

class Deque:
    def __init__(self):
        self.items) []

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
    def append(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

    def appendLeft(self, item):
        self.items.insert(0, item)

    def popLeft(self):
        return self.items.pop(0)

    def extend(self, iterable):
        sel.items.extend(iterable)

    def extendLeft(self, iterable):
        rev = list(iterable)
        rev.reverse()
        rev.extend(self.items)
        self.items = rev

    def rotate(self, n):
        if n > 0:
            for i in range(n):
                self.appendLeft(self, pop())
        if n < o:
            for i in range(n * -1):
                self.append(popLeft())

    def __str__(self):
        return str(self.items)

class Queue:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.size() == 0
    def clear(self):
        self.items = []
    def append(self, item):
        slef.items.append(item)
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.size > o:
            return self.items.pop(0)
        else:
            raise Exception("Cannot call dequeue() on an empty queue.")
    def clear(self):
        self.items = []
    def __str__(self):
        return str(self.items)
    def __add__(self, iterable):
        self.items.extend(iterable)
        return self
