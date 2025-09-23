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

    def inorder(self, node):
        print('Inorder: ', end='')
        self.Inorder(node)
        print()

    def Inorder(self, node):
        if node:
            self.Inorder(node.left)
            print(node.data, end=' ')
            self.Inorder(node.right)

    def preorder(self, node):
        print('Preorder: ', end='')
        self.Preorder(node)
        print()

    def Preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.Preorder(node.left)
            self.Preorder(node.right)

    def postorder(self, node):
        print('Postorder: ', end='')
        self.Postorder(node)
        print()

    def Postorder(self, node):
        if node:
            self.Postorder(node.left)
            self.Postorder(node.right)
            print(node.data, end=' ')

    def printTree(self, node, level=0):
        if node:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split()
for i in inp:
    root = T.insert(int(i))

T.preorder(T.root)
T.inorder(T.root)
T.postorder(T.root)
T.printTree(T.root)
