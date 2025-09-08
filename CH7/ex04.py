class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        return str(self.data)

class BinarySearchTree:
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
    
    def find_node(self, node, data):
        if node is None:
            return None
        if data == node.data:
            return node
        elif data < node.data:
            return self.find_node(node.left, data)
        else:
            return self.find_node(node.right, data)

    def get_inorder_successor(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

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
            elif node.right is None:
                return node.left
            temp = self.get_inorder_successor(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)
        return node

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
        
tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
    if i[0] == 'i':
        print("insert", i[2:])
        root = tree.insert(int(i[2:]))
        printTree90(tree.root)
    elif i[0] == 'd':
        val_to_delete = int(i[2:])
        print("delete", val_to_delete)
        if tree.find_node(tree.root, val_to_delete):
            tree.root = tree.delete(tree.root, val_to_delete)
        else:
            print("Error! Not Found DATA")
        printTree90(tree.root)