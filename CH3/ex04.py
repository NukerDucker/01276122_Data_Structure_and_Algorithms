class Stack:
    def __init__(self):
        self.items = []
    def __getitem__(self, index):
        return self.items[index]
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
    
class Calculator:
    OPERATIONS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b if b != 0 else None,
        'DUP': lambda stack: stack.push(stack.peek()),
        'POP': lambda stack: stack.pop()
    }
    
    def __init__(self):
        self.stack = Stack()
        
    def _perform_operation(self, operator, a, b):
        return self.OPERATIONS[operator](a, b)

    def run(self, s):
        instructions = s.split()
        
        for instruction in instructions:
            if not instruction.isdigit() and (instruction not in self.OPERATIONS):
                return f"Invalid instruction: {instruction}"
            elif instruction.isdigit():
                self.stack.push(int(instruction))

            elif instruction in ('+', '-', '*', '/'):
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(self.OPERATIONS[instruction](a, b))
            else:
                self.OPERATIONS[instruction](self.stack)
            
        return self.stack.peek() if not self.stack.is_empty() else 0

def main():
    print("* Stack Calculator *")
    usr_input = input("Enter arguments : ")
    calculator = Calculator()
    result = calculator.run(usr_input)
    print(result)

if __name__ == "__main__":
    main()