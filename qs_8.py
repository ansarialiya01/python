from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self,root,data):
        if data < root.data:
            if root.left : self._insert(root.left, data)
            else:root.left = Node(data)
        elif data > root.data:
            if root.right:self._insert(root.right, data)
            else:root.right = Node(data)

    def search(self,root,data):
        if root is None or root.data == data:
            return root
        if data < root.data:
            return self.search(root.left,data)
        return self.search(root.right,data)

    def deletion(self,root,data):
        if root is None:
            print("invalid")
            return
        if data < root.data:
            root.left = self.deletion(root.left, data)
        elif data > root.data:
            root.right = self.deletion(root.right,data)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left
            root.data = temp.data
            root.right = self.deletion(root.right, temp.data)
        return root

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

bst = BST()
bst.insert(90)
bst.insert(67)
bst.insert(89)
bst.insert(56)
bst.insert(23)
bst.insert(9)

if bst.search(bst.root,89):
    print("found")
else:
    print("not found")

bst.root=bst.deletion(bst.root, 56)
bst.inorder(bst.root)
        
