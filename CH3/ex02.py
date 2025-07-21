class Stack:
    def __init__(self, items=None):
        self._items = [] if items is None else list(items)
    
    def __str__(self):
        return ' '.join(map(str, self._items))
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop() if not self.is_empty() else None
    
    def peek(self):
        return self._items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return not self._items
    
    def size(self):
        return len(self._items)

def parentheses_checker(expression):
    stack = Stack()
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in expression:
        if char in pairs:
            stack.push(char)
        elif char in pairs.values():
            if not stack:
                return f"{expression} close paren excess"
            if pairs[stack[-1]] != char:
                return f"{expression} Unmatch open-close"
            stack.pop()
    
    return (f"{expression} MATCH" if not stack 
            else f"{expression} open paren excess {len(stack)} : {stack}")

def main():
    user_input = input("Enter expression : ")
    print(parentheses_checker(user_input))

if __name__ == "__main__":
    main()