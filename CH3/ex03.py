class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

def get_precedence(operator):
    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    return precedence.get(operator, -1)

def infix_to_postfix(expression):
    stack = Stack()
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop() 
        else:
            while (not stack.is_empty() and 
                   get_precedence(stack.peek()) >= get_precedence(char)):
                postfix.append(stack.pop())
            stack.push(char)
    
    while not stack.is_empty():
        postfix.append(stack.pop())
    
    return ''.join(postfix)

def main():
    infix_expression = input("Enter Infix : ")
    print(f"Postfix : {infix_to_postfix(infix_expression)}")

if __name__ == "__main__":
    main()