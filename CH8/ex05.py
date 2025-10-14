class BST:
    class BSTNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, root=None) -> None:
        self.root = root

    def get_successor(self, curr):
        current = curr.right
        while current.left is not None:
            current = current.left
        return current

    def search_subtree(self, root, key):
        if root is None:
            return None
        if root.val == key:
            return root
        elif key < root.val:
            return self.search_subtree(root.left, key)
        else:
            return self.search_subtree(root.right, key)

    def insert_node(self, data):
        if self.root is None:
            self.root = BST.BSTNode(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if data == node.val:
            return node
        elif data < node.val:
            if node.left is None:
                node.left = BST.BSTNode(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = BST.BSTNode(data)
            else:
                self._insert(node.right, data)
        return node

    def delete_subtree(self, root, key):
        if root is None:
            return None

        if key < root.val:
            root.left = self.delete_subtree(root.left, key)
        elif key > root.val:
            root.right = self.delete_subtree(root.right, key)
        else:
            return None

        return root

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent, root.val)
            self.printTree90(root.left, indent + 1)


class AVLTree:
    class AVLNode:
        def __init__(self, val, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right
            self.height = 1

    def __init__(self, root=None) -> None:
        self.root = root

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def insert_node(self, node, key):
        if node is None:
            return self.AVLNode(key)
        elif key < node.val:
            node.left = self.insert_node(node.left, key)
        elif key > node.val:
            node.right = self.insert_node(node.right, key)
        else:
            return node  # Duplicate keys not allowed

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

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

    def bst_to_avl(self, bst_root):
        if bst_root is None:
            return

        sorted_values = self.inorder_traversal(bst_root)
        self.root = None

        for val in sorted_values:
            self.root = self.insert_node(self.root, val)

    def inorder_traversal(self, root):
        if root is None:
            return []
        return (
            self.inorder_traversal(root.left)
            + [root.val]
            + self.inorder_traversal(root.right)
        )

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.val))
            self.printTree90(root.left, indent + 1)


inp1, inp2 = input("Enter the val of tree and node to cut: ").split("/")
bst = BST()
for i in inp1.split():
    bst.root = bst.insert_node(int(i))
print("Before cut:")
bst.printTree90(bst.root)

avl1, avl2 = AVLTree(), AVLTree()

print("Cutted Tree:")
subtree_root = bst.search_subtree(bst.root, int(inp2))
avl1.bst_to_avl(subtree_root)
avl1.printTree90(avl1.root)

print("Left Tree:")
bst.root = bst.delete_subtree(bst.root, int(inp2))
avl2.bst_to_avl(bst.root)
avl2.printTree90(avl2.root)