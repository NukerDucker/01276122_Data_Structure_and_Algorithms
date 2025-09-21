class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.next = None

    def __str__(self):
        return str(self.data)

class ExpressionTree:
    def __init__(self):
        self.root = None

    def insert_tree(self, expression):
        stack = []
        for char in expression:
            if char not in '+-*/^':
                stack.append(Node(char))
            else:
                if len(stack) < 2:
                    print("Invalid Postfix Expression")
                    return
                operator_node = Node(char)
                operator_node.right = stack.pop()
                operator_node.left = stack.pop()
                stack.append(operator_node)

        if len(stack) == 1:
            self.root = stack.pop()
        else:
            print("Invalid Postfix Expression")

    def inorder(self, node):
        if node:
            if node.left or node.right:
                print('(', end='')
            self.inorder(node.left)
            print(node.data, end='')
            self.inorder(node.right)
            if node.left or node.right:
                print(')', end='')

    def preorder(self, node):
        if node:
            print(node.data, end='')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end='')

    def print_tree(self, node, level=0):
        if node:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)
def main():
    tree = ExpressionTree()
    postfix = input("Enter Postfix : ")
    tree.insert_tree(postfix)

    print("Tree :")
    tree.print_tree(tree.root)

    print('--------------------------------------------------')

    print("Infix : ", end='')
    tree.inorder(tree.root)
    print()

    print("Prefix : ", end='')
    tree.preorder(tree.root)
    print()

if __name__ == "__main__":
    main()