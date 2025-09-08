# ex03.py for Chapter 7
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if data == node.data:
            return node
        elif data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else: 
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
        return node
    
    def Inorder(self, node):
        if node is not None:
            self.Inorder(node.left)
            print(node.data, end=' ')
            self.Inorder(node.right)
    
    def Preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.Preorder(node.left)
            self.Preorder(node.right)
    
    def Postorder(self, node):
        if node is not None:
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
        