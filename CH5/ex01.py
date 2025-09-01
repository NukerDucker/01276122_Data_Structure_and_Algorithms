class Node:
    """
    Node class for a singly linked list.
    Each node contains data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data  # The value stored in this node
        self.next = None  # Reference to the next node, initially None

class LinkedList:
    """
    Singly linked list implementation.
    Provides operations for inserting, deleting, and traversing nodes.
    """
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # Reference to the first node in the list
        self.next = None  # This seems redundant and unused
        self.tail = None  # Reference to the last node (not fully implemented)

    def append(self, data):
        """
        Add a new node with the given data to the end of the list.
        
        Args:
            data: The value to be stored in the new node
        """
        # Create a new node with the provided data
        new_node = Node(data)
        
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
            
        # Otherwise, traverse to the end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            
        # Link the last node to the new node
        last_node.next = new_node

    def insert_head(self, data):
        """
        Insert a new node with the given data at the beginning of the list.
        
        Args:
            data: The value to be stored in the new node
        """
        # Create a new node with the provided data
        new_node = Node(data)
        
        # Set the new node's next pointer to the current head
        new_node.next = self.head
        
        # Update the head to be the new node
        self.head = new_node

    def delete(self, data):
        """
        Delete the first node containing the specified data.
        
        Args:
            data: The value to search for and delete
        """
        # Start at the head
        current = self.head
        
        # Special case: head node contains the target data
        if current and current.data == data:
            self.head = current.next  # Update head to skip the first node
            current = None  # Allow the node to be garbage collected
            return
            
        # Track the previous node to relink the list when we find the target
        prev = None
        
        # Traverse until we find the target data or reach the end
        while current and current.data != data:
            prev = current
            current = current.next

        # If we reached the end without finding the data, exit
        if current is None:
            return

        # Relink the list to skip over the node with the target data
        prev.next = current.next
        current = None  # Allow the node to be garbage collected

    def print_list(self):
        """
        Create a string representation of the linked list.
        
        Returns:
            str: A string showing all elements connected by arrows
        """
        # Start at the head
        current = self.head
        elements = []
        
        # Traverse the list and collect all elements
        while current:
            elements.append(str(current.data))
            current = current.next
            
        # Add 'None' at the end to indicate the end of the list
        elements.append('None')
        
        # Join all elements with arrows
        return ' -> '.join(elements)

def main():
    """
    Main function to run the linked list program.
    Processes user commands to manipulate the linked list.
    """
    # Create a new linked list
    ll = LinkedList()
    
    # Get user commands
    usr_input = input("Enter Commands: ")
    commands = usr_input.split()
    
    # Process each command
    for i in range(len(commands)):
        # Check if the command is one that requires a value
        if commands[i] in ['insert_head', 'append', 'delete']:
            value = commands[i + 1]  # Get the value from the next command
            
            # Execute the appropriate operation
            if commands[i] == 'insert_head':
                ll.insert_head(value)
            elif commands[i] == 'append':
                ll.append(value)
            elif commands[i] == 'delete':
                ll.delete(value)
        # Print command doesn't need a value
        elif commands[i] == 'print':
            print(ll.print_list())

if __name__ == "__main__":
    main()