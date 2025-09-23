class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)

class AVL:
    def __init__(self):
        self.root = None

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
        if not node:
            return Node(key)

        if key < node.data:
            node.left = self.insert_node(node.left, key)
        elif key > node.data:
            node.right = self.insert_node(node.right, key)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and key < node.left.data:
            print('Right Right Rotation')
            return self.right_rotate(node)
        if balance < -1 and key > node.right.data:
            print('Left Left Rotation')
            return self.left_rotate(node)
        if balance > 1 and key > node.left.data:
            print('Left Right Rotation')
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.data:
            print('Right Left Rotation')
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

def print_tree_90(node, level=0):
    if node is not None:
        print_tree_90(node.right, level + 1)
        print('     ' * level, node)
        print_tree_90(node.left, level + 1)

def main() -> None:
    tree = AVL()
    root = None
    print(' *** AVL Tree Insert Element ***')
    values = input("Enter Input : ").split()
    for value in values:
        print("insert :", value)
        root = tree.insert_node(root, int(value))
        print_tree_90(root)
        print("===============")

if __name__ == '__main__':
    main()