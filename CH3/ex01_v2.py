class Stack:
    def __init__(self, items=None):
        self._items = [] if items is None else list(items)

    def __str__(self):
        return ' '.join(str(element) for element in self._items)
    
    def __repr__(self):
        return f"Stack({self._items})"
    
    def __len__(self):
        return len(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop() if  not self.is_empty() else None

    def peek(self):
        return self._items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

def stack_controller(command_string):
    stack = Stack()
    commands = command_string.split(',')
    
    for command in commands:
        cmd = command.strip()
        
        if cmd.startswith('A'):
            parts = cmd.split()
            if len(parts) < 2:
                print(f"Warning: Invalid add command '{cmd}'. Expected format: 'A value'")
                continue
                
            value = parts[1]
            stack.push(value)
            print(f"Add = {value} and Size = {stack.size()}")
            
        elif cmd.startswith('P'):
            if stack.is_empty():
                print("Warning: Cannot pop from empty stack")
                continue
                
            popped_value = stack.peek()
            index = stack.size() - 1
            print(f"Pop = {popped_value} and Index = {index}")
            stack.pop()
            
        else:
            print(f"Warning: Unknown command '{cmd}'. Use 'A value' or 'P'")
    
    return f"Value in Stack = {stack}"

def main():
    user_input = input("Enter Input: ")
    result_stack = stack_controller(user_input)
    print(result_stack)


if __name__ == "__main__":
    main()