class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        elements.append('None')
        return ' -> '.join(elements)

def main():
    ll = LinkedList()
    usr_input = input("Enter Commands: ")
    commands = usr_input.split()
    for i in range(len(commands)):
        if commands[i] in ['insert_head', 'append', 'delete']:
            value = commands[i + 1]
            if commands[i] == 'insert_head':
                ll.insert_head(value)
            elif commands[i] == 'append':
                ll.append(value)
            elif commands[i] == 'delete':
                ll.delete(value)
        elif commands[i] == 'print':
            print(ll.print_list())

if __name__ == "__main__":
    main()