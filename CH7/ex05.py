# ex05.py for Chapter 7
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  
    
    def __str__(self):
        return str(self.data)

class ExpressionTree:
    def __init__(self):
        self.root = None

    def insert_tree(self, expression):
        stack = []
        operators = set(['+', '-', '*', '/', '^'])
        for char in expression:
            if char not in operators:
                node = Node(char)
                stack.append(node)
            else:
                operator_node = Node(char)
                if stack:
                    operator_node.right = stack.pop()
                else:
                    print("Invalid Postfix Expression")
                    return
                if stack:
                    operator_node.left = stack.pop()
                else:
                    print("Invalid Postfix Expression")
                    return
                stack.append(operator_node)
        if len(stack) == 1:
            self.root = stack.pop()
        else:
            print("Invalid Postfix Expression")
            
    def Inorder(self, node):
        if node is not None:
            if node.left or node.right:
                print('(', end='')
            self.Inorder(node.left)
            print(node.data, end='')
            self.Inorder(node.right)
            if node.left or node.right:
                print(')', end='')
                
    def Preorder(self, node):
        if node is not None:
            print(node.data, end='')
            self.Preorder(node.left)
            self.Preorder(node.right)
    
    def Postorder(self, node):
        if node is not None:
            self.Postorder(node.left)
            self.Postorder(node.right)
            print(node.data, end='')
        
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
def main():
    tree = ExpressionTree()
    postfix = input("Enter Postfix : ")
    tree.insert_tree(postfix)
    
    print("Tree :")
    tree.printTree(tree.root)
    
    print('--------------------------------------------------')
    
    print("Infix : ", end='')
    tree.Inorder(tree.root)
    print()
    
    print("Prefix : ", end='')
    tree.Preorder(tree.root)
    print()

if __name__ == "__main__":
    main()