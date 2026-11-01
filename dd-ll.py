class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_end(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def delete_beginning(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")

        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return value

    def delete_end(self):
        if self.tail is None:
            raise IndexError("Cannot delete from an empty list")

        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return value

    def traverse_forward(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

    def traverse_backward(self):
        values = []
        current = self.tail
        while current:
            values.append(current.data)
            current = current.prev
        return values


# Example
dll = DoublyLinkedList()
dll.insert_beginning(20)
dll.insert_beginning(10)
dll.insert_end(30)

print(dll.traverse_forward())   # [10, 20, 30]
print(dll.traverse_backward())  # [30, 20, 10]

print(dll.delete_beginning())   # 10
print(dll.delete_end())         # 30
print(dll.traverse_forward())   # [20]