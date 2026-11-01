class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Last in, first out (LIFO)."""

    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise IndexError("Cannot pop from an empty stack")

        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            raise IndexError("Cannot peek at an empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None


class Queue:
    """First in, first out (FIFO)."""

    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, data):
        """Add an item to the rear of the queue."""
        node = Node(data)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def pop(self):
        """Remove and return the item at the front."""
        if self.front is None:
            raise IndexError("Cannot pop from an empty queue")

        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        """Return the item at the front without removing it."""
        if self.front is None:
            raise IndexError("Cannot peek at an empty queue")
        return self.front.data

    def is_empty(self):
        return self.front is None


# Example
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())  # 20
print(stack.pop())   # 20

queue = Queue()
queue.push(10)
queue.push(20)
print(queue.peek())  # 10
print(queue.pop())   # 10