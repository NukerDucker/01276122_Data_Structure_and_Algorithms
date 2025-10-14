class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)

class AVL:
    def __init__(self):
        self.root = None

    def search(self, node, key):
        if node is None or node.data == key:
            return node
        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = (1 + max(self.get_height(node.left), self.get_height(node.right)))
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
            return Node(key)
        elif key < node.data:
            node.left = self.insert_node(node.left, key)
        elif key > node.data:
            node.right = self.insert_node(node.right, key)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and key < node.left.data:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.data:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def delete_node(self, node, key):
        if node is None:
            return node
        elif key < node.data:
            node.left = self.delete_node(node.left, key)
        elif key > node.data:
            node.right = self.delete_node(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.get_min_value_node(node.right)
            node.data = temp.data
            node.right = self.delete_node(node.right, temp.data)

        if node is None:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def delete_root(self):
        """Delete the root node and return the new root"""
        if self.root is None:
            return None
        root_value = self.root.data
        self.root = self.delete_node(self.root, root_value)
        return self.root

def print_levels(root):
    if not root:
        return

    levels = root.height
    queue = [root]

    for level in range(1, levels + 1):
        next_queue = []
        left_pad = 1 + ((1 << (levels - level + 1)) - 1) * 2
        between = 1 + ((1 << (levels - level + 2)) - 1) * 2

        for node in queue:
            next_queue.append(node.left if node else None)
            next_queue.append(node.right if node else None)

        printable_nodes = [node for node in queue if node]
        if not printable_nodes:
            break

        line = " " * left_pad
        first = True

        for node in printable_nodes:
            if not first:
                line += " " * (between - 1)
            first = False

            line += str(node.data)
            if node.data < 10:
                line += " "

        print(line)
        queue = next_queue

        if all(node is None for node in queue):
            break

myTree = AVL()
root = None
print(' *** AVL Tree ***')
data = input("Enter numbers to insert: ").split()

for e in data:
    root = myTree.insert_node(root, int(e))

myTree.root = root

print_levels(root)
print("------------------------------")

while myTree.root is not None:
    myTree.delete_root()
    if myTree.root is not None:
        print_levels(myTree.root)
        print("------------------------------")

print("===== End of program =====")