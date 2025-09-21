class BST:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def search(self, root, key):
        if not root or root.val == key:
            return root
        return self.search(root.left if key < root.val else root.right, key)

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root

    def _insert(self, node, data):
        if not node:
            return BST.Node(data)
        if data != node.val:
            if data < node.val:
                node.left = self._insert(node.left, data)
            else:
                node.right = self._insert(node.right, data)
        return node

    def delete_subtree(self, root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.delete_subtree(root.left, key)
        elif key > root.val:
            root.right = self.delete_subtree(root.right, key)
        else:
            return None
        return root

    def print_tree(self, root, indent=0):
        if root:
            self.print_tree(root.right, indent + 1)
            print("    " * indent, root.val)
            self.print_tree(root.left, indent + 1)

class AVLTree:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            self.height = 1

    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def insert(self, node, key):
        if not node:
            return self.Node(key)
        if key < node.val:
            node.left = self.insert(node.left, key)
        elif key > node.val:
            node.right = self.insert(node.right, key)
        else:
            return node

        self.update_height(node)
        balance = self.balance_factor(node)

        if balance > 1 and key < node.left.val:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.val:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.val:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.val:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def from_bst(self, bst_root):
        if not bst_root:
            return
        values = self.inorder(bst_root)
        self.root = None
        for val in values:
            self.root = self.insert(self.root, val)

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def print_tree(self, root, indent=0):
        if root:
            self.print_tree(root.right, indent + 1)
            print("    " * indent + str(root.val))
            self.print_tree(root.left, indent + 1)


values, cut_value = input("Enter the val of tree and node to cut: ").split("/")
bst = BST()
for val in values.split():
    bst.insert(int(val))

print("Before cut:")
bst.print_tree(bst.root)

avl1, avl2 = AVLTree(), AVLTree()

print("Cutted Tree:")
subtree = bst.search(bst.root, int(cut_value))
avl1.from_bst(subtree)
avl1.print_tree(avl1.root)

print("Left Tree:")
bst.root = bst.delete_subtree(bst.root, int(cut_value))
avl2.from_bst(bst.root)
avl2.print_tree(avl2.root)