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
        if not self.root:
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

    def printTree(self, node, level=0):
        if node:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

tree = BST()
numbers = [int(i) for i in input('Enter Input : ').split()]
for num in numbers:
    root = tree.insert(num)
tree.printTree(root)
