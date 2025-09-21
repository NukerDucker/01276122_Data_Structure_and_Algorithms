class AVLTree:
    class AVLNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = self.right = None
            self.height = 0

        def __str__(self):
            return str(self.data)

        def set_height(self):
            self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))

        def get_height(self, node):
            return -1 if node is None else node.height

        def balance(self):
            return self.get_height(self.right) - self.get_height(self.left)

    def __init__(self, root=None):
        self.root = root

    def add(self, data):
        self.root = AVLTree._add(self.root, data)

    @staticmethod
    def _add(root, data):
        if root is None:
            return AVLTree.AVLNode(data)

        if data < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)

        root.set_height()
        balance = root.balance()

        if balance > 1:
            if root.right.balance() < 0:
                root.right = AVLTree.rotate_right(root.right)
            return AVLTree.rotate_left(root)

        if balance < -1:
            if root.left.balance() > 0:
                root.left = AVLTree.rotate_left(root.left)
            return AVLTree.rotate_right(root)

        return root

    @staticmethod
    def rotate_left(root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.set_height()
        new_root.set_height()
        return new_root

    @staticmethod
    def rotate_right(root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.set_height()
        new_root.set_height()
        return new_root

    def post_order(self):
        print("AVLTree post-order : ", end='')
        AVLTree._post_order(self.root)
        print()

    @staticmethod
    def _post_order(root):
        if root:
            AVLTree._post_order(root.left)
            AVLTree._post_order(root.right)
            print(root.data, end=' ')

    def print_tree(self):
        AVLTree._print_tree(self.root)

    @staticmethod
    def _print_tree(node, level=0):
        if node:
            AVLTree._print_tree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._print_tree(node.left, level + 1)

if __name__ == "__main__":
    avl = AVLTree()
    commands = input('Enter Input : ').split(',')

    for cmd in commands:
        parts = cmd.strip().split()
        operation = parts[0]

        if operation == "AD":
            avl.add(int(parts[1]))
        elif operation == "PR":
            avl.print_tree()
            print()
        elif operation == "PO":
            avl.post_order()