class Calculator:
    def __init__(self):
        self.stack = []

    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    def push(self, value):
        if isinstance(value, int):
            self.stack.append(value)

    def run(self, s):
        instructions = s.split()
        i = 0
        while i < len(instructions):
            instruction = instructions[i]
            if instruction.isdigit():
                self.push(int(instruction))

            elif instruction in ('+', '-', '*', '/'):

                a = self.stack.pop()
                b = self.stack.pop()
                
                if instruction == '+':
                    self.push(self.plus(a, b))
                elif instruction == '-':
                    self.push(self.minus(a, b))
                elif instruction == '*':
                    self.push(self.multiply(a, b))
                elif instruction == '/':
                    try:
                        self.push(int(self.divide(a, b)))
                    except ValueError as e:
                        print(e)
                        return
            elif instruction == 'DUP':
                self.push(self.stack[-1])
            elif instruction == 'POP':
                self.stack.pop()
            else:
                print(f"Invalid instruction: {instruction}")
                return
            i += 1
        if self.stack:
            print(self.stack[-1])
        else:
            print("0")

def main():
    print("* Stack Calculator *")
    usr_input = input("Enter arguments : ")
    calculator = Calculator()
    calculator.run(usr_input)

if __name__ == "__main__":
    main()