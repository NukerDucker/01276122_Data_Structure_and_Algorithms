class AVLTree:
    class AVLNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
            self.height = 0

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            left_height = self.getHeight(self.left)
            right_height = self.getHeight(self.right)
            self.height = 1 + max(left_height, right_height)

        def getHeight(self, node):
            return -1 if node is None else node.height

        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)

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

        root.setHeight()

        balance = root.balanceValue()

        if balance > 1:
            if root.right.balanceValue() < 0:
                root.right = AVLTree.rotateRightChild(root.right)
            return AVLTree.rotateLeftChild(root)

        if balance < -1:
            if root.left.balanceValue() > 0:
                root.left = AVLTree.rotateLeftChild(root.left)
            return AVLTree.rotateRightChild(root)

        return root

    @staticmethod
    def rotateLeftChild(root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        root.setHeight()
        new_root.setHeight()
        return new_root

    @staticmethod
    def rotateRightChild(root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        root.setHeight()
        new_root.setHeight()
        return new_root

    def postOrder(self):
        print("AVLTree post-order : ", end='')
        AVLTree._postOrder(self.root)
        print()

    @staticmethod
    def _postOrder(root):
        if root is not None:
            AVLTree._postOrder(root.left)
            AVLTree._postOrder(root.right)
            print(root.data, end=' ')

    def printTree(self):
        AVLTree._printTree(self.root)

    @staticmethod
    def _printTree(node, level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

if __name__ == "__main__":
    avl1 = AVLTree()
    inp = input('Enter Input : ').split(',')
    for i in inp:
        parts = i.strip().split()
        command = parts[0]
        if command == "AD":
            value = int(parts[1])
            avl1.add(value)
        elif command == "PR":
            avl1.printTree()
            print()
        elif command == "PO":
            avl1.postOrder()