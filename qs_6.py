class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertion_at_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertion_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insertion_at_index(self,data,index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for i in range(index-1):
            if current is None:
                print("invalid")
                return
            current = current.next
        if current is None:
            print("invalid")
            return
        new_node.next = current.next
        current.next = new_node

    def serching(self,key):
        temp = self.head
        index = 0
        while temp:
            if temp.data==key:
                print("found")
                return
            temp = temp.next
            index +=1
        print("not found")

    def reverse(self):
        previous = None
        current = self.head 
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def deletion_at_begining(self):
        if self.head is None:
            print("list is empty")
            return
        self.head = self.head.next

    def deletion_at_end(self):
        if self.head is None:
            print("empty")
            return 
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def deletion_at_index(self,index):
        if self.head is None:
            print("invalid")
            return

        if index ==0:
            self.head = self.head.next
            return

        temp = self.head
        for i in range(index-1):
            if temp is None or temp.next is None:
                print("invalid")
                return 
            temp = temp.next

        if temp.next is None:
            print("invalid")
            return
        temp.next = temp.next.next





    def display(self):
        temp = self.head
        print("head->", end ="")
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")


ll = LinkedList()
ll.insertion_at_begining(60)
ll.insertion_at_begining(6)
ll.insertion_at_begining(90)
ll.insertion_at_begining(33)
ll.display()
# ll.insertion_at_begining(0)
# ll.display()
# ll.insertion_at_end(87)
# ll.display()
# ll.insertion_at_index(100,2)
# ll.display()
# ll.serching(6)

# ll.reverse()
# ll.display()
# ll.deletion_at_begining()
# ll.deletion_at_end( )
ll.deletion_at_index(2)
ll.display()