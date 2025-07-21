class Stack:
    def __init__(self, items=None): self._items = [] if items is None else list(items)
    def __str__(self): return ' '.join(str(element) for element in self._items)
    def __len__(self): return len(self._items)
    def __getitem__(self, index): return self._items[index]
    
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
def parentheses_checker(s):
    stack = Stack()
    parentheses = {'(': ')', '{': '}', '[': ']'}
    missing = 0

    for char in s:
        if char in parentheses:
            stack.push(char)
        elif char in parentheses.values():
            if not stack or parentheses[stack[-1]] != char:
                missing += 1
            else:
                stack.pop()

    missing += len(stack)
    return missing

def main():
    usr_input = input("Enter Input : ")
    missing = parentheses_checker(usr_input)
    print(missing)
    if missing == 0:
        print("Perfect ! ! !")

if __name__ == "__main__":
    main()