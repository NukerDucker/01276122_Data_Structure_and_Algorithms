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
        else:
            self._insert(self.root, data)
        return self.root

    def _insert(self, node, data):
        if data == node.data:
            return
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def preorder(self, node):
        print('Preorder: ', end='')
        self._preorder(node)
        print()

    def _preorder(self, node):
        if node:
            print(node.data, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def inorder(self, node):
        print('Inorder: ', end='')
        self._inorder(node)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)

    def postorder(self, node):
        print('Postorder: ', end='')
        self._postorder(node)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data, end=' ')

    def print_tree(self, node, level=0):
        if node:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

def main() -> None:
    tree = BST()
    values = input('Enter Input : ').split()
    for value in values:
        tree.insert(int(value))
    tree.preorder(tree.root)
    tree.inorder(tree.root)
    tree.postorder(tree.root)
    tree.print_tree(tree.root)

if __name__ == "__main__":
    main()
