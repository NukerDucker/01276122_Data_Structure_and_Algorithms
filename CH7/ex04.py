class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
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
            node.left = Node(data) if node.left is None else self._insert(node.left, data)
        else:
            node.right = Node(data) if node.right is None else self._insert(node.right, data)
        return node

    def find_node(self, node, data):
        if node is None or data == node.data:
            return node
        return self.find_node(node.left if data < node.data else node.right, data)

    def get_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self.get_min_node(node.right)
            node.data = successor.data
            node.right = self.delete(node.right, successor.data)
        return node

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print('     ' * level, node)
        print_tree(node.left, level + 1)

tree = BinarySearchTree()
commands = input("Enter Input : ").split(",")

for cmd in commands:
    action, value = cmd[0], int(cmd[2:])

    if action == 'i':
        print("insert", value)
        tree.insert(value)
        print_tree(tree.root)
    elif action == 'd':
        print("delete", value)
        if tree.find_node(tree.root, value):
            tree.root = tree.delete(tree.root, value)
        else:
            print("Error! Not Found DATA")
        print_tree(tree.root)