# ex02.py for Chapter 7
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        return self._insert(self.root, data)

    def _insert(self, node, data):
        if data == node.data:
            return node
        if data < node.data:
            if not node.left:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if not node.right:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
        return node

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Height of this tree is :", T.height(root)-1)
