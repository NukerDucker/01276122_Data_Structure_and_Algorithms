# ex03.py for Chapter 7
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

    def Inorder(self, node):
        if not node:
            self.Inorder(node.left)
            print(node.data, end=' ')
            self.Inorder(node.right)

    def Preorder(self, node):
        if not node:
            print(node.data, end=' ')
            self.Preorder(node.left)
            self.Preorder(node.right)

    def Postorder(self, node):
        if not node:
            self.Postorder(node.left)
            self.Postorder(node.right)
            print(node.data, end=' ')

T = BST()
inp = input('Enter Input : ').split()
for i in inp:
    if i == 'Inorder':
        T.Inorder(root)
        print()
    elif i == 'Preorder':
        T.Preorder(root)
        print()
    elif i == 'Postorder':
        T.Postorder(root)
        print()
    else:
        root = T.insert(int(i))
