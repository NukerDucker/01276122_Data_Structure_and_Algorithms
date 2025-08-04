class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        current = self.head
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
            
        return 'linked list : '+ '->'.join(elements)
    
    def str_reverse(self) -> str:
        current = self.tail
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.previous
            
        return 'reverse : '+ '->'.join(elements)
    
    def isEmpty(self) -> bool:
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def insert(self, index, data):
        if index < 0:
            print("Data cannot be added")
            return
        
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.previous = new_node
                
            self.head = new_node
            
            if self.tail is None:
                self.tail = new_node
                
            print(f'index = {index} and data = {data}')
            return
        
        current = self.head
        
        for _ in range(index - 1):
            if current is None:
                break
            current = current.next
        
        if current is None:
            print("Data cannot be added")
            return
            
        new_node.next = current.next
        new_node.previous = current
        
        if current.next:
            current.next.previous = new_node
            
        current.next = new_node
        
        if new_node.next is None:
            self.tail = new_node
        
        print(f'index = {index} and data = {data}')
    
    def remove(self, data):
        current = self.head
        index = 0
        
        while current:
            if current.data == data:
                found_index = index
                    
                if current.previous: 
                    current.previous.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                    
                print(f'removed : {data} from index : {found_index}')
                return
            
            current = current.next
            index += 1
            
        print("Not Found!")
            
    def index(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return 0
    
    def add_before(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

def main():
    ll = LinkedList()
    usr_input = input("Enter Input : ")
    commands = usr_input.split(',')
    
    for command in commands:
        parts = command.split()
        action = parts[0]
        value = parts[1] if len(parts) > 1 else None

        if action == 'A':
            ll.append(value)
        elif action == 'I':
            index, val = value.split(':')
            ll.insert(int(index), val)
        elif action == 'Ab':
            ll.add_before(value)
        elif action == 'R':
            ll.remove(value)
            
        print(ll)
        print(ll.str_reverse())

if __name__ == "__main__":
    main()