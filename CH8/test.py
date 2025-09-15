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
    
    def add(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.data:
            node.left = self.add(node.left, key)
        elif key > node.data:
            node.right = self.add(node.right, key)
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
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)   
    
    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
            
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')
            
    def printTree(self):
        self._printTree(self.root)
        print()

    def _printTree(self, node, level=0):
        if not node is None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self._printTree(node.left, level + 1)
            
avl1 = AVL()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AD":
        avl1.add(i[3:])

    elif i[:2] == "PR":
        avl1.printTree()

    elif i[:2] == "PO":

        avl1.postOrder()