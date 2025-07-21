from collections import deque

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
    
    def enqueue(self, item):
        self.push(item)
        
    def popleft(self):
        return self._items.pop(0) if not self.is_empty() else None
        
    def dequeue(self):
        return self.popleft() if not self.is_empty() else None
    
    def insert(self, index, item):
        self._items.insert(index, item)
        

        