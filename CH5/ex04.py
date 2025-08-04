class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class VimClone:
    def __init__(self):
        self.head = None
        self.tail = None
        self.pointer_position = 0
        self.cursor = '|'
        
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.pointer_position = 1
            return
        
        if self.pointer_position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(self.pointer_position - 1):
                if current.next is None:
                    break
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            
        if new_node.next is None:
            self.tail = new_node
        
        self.pointer_position += 1
    
    def pointer_left(self):
        if self.pointer_position > 0:
            self.pointer_position -= 1
            
    def pointer_right(self):
        if self.pointer_position < self.size():
            self.pointer_position += 1
    
    def delete_left(self):
        if self.pointer_position == 0:
            return
        
        current = self.head
        if self.pointer_position == 1:
            self.head = current.next
        else:
            for _ in range(self.pointer_position - 2):
                current = current.next
            current.next = current.next.next
        
        self.pointer_position -= 1
    
    def delete_right(self):
        if self.head is None or self.pointer_position >= self.size():
            return

        if self.pointer_position == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        current = self.head
        for _ in range(self.pointer_position - 1):
            if current is None:
                return
            current = current.next

        if current.next is None:
            self.tail = current
        else:
            current.next = current.next.next
    
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def display(self):
        if not self.head:
            print(self.cursor)
            return
            
        result = ""
        position = 0
        current = self.head
        
        if self.pointer_position == 0:
            result += f' {self.cursor}'
            
        while current:
            result += f' {current.data}'
            position += 1
            
            if position == self.pointer_position:
                result += f' {self.cursor}'
                
            current = current.next
            
        print(result.strip())
    
vim = VimClone()
usr_input = input("Enter Input : ")
commands = usr_input.split(',')
for command in commands:
    if command.startswith('I'):
        _, value = command.split()
        vim.insert(value)
    elif command.startswith('B'):
        vim.delete_left()
    elif command.startswith('D'):
        vim.delete_right()
    elif command.startswith('L'):
        vim.pointer_left()
    elif command.startswith('R'):
        vim.pointer_right()
    
vim.display()



