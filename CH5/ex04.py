class Node:
    """
    Node class for the linked list implementation.
    Each node stores data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class VimClone:
    """
    A simplified VIM text editor clone implemented using a linked list.
    Supports basic operations like insertion, deletion, and cursor movement.
    """
    def __init__(self):
        """
        Initialize an empty editor with no text and cursor at position 0.
        """
        self.head = None        # First node of the linked list
        self.tail = None        # Last node of the linked list
        self.pointer_position = 0  # Current cursor position (0 = before first character)
        self.cursor = '|'       # Symbol representing the cursor
        
    def insert(self, data):
        """
        Insert a character at the current cursor position.
        
        Args:
            data: The character to insert
        """
        # Create a new node with the provided data
        new_node = Node(data)
        
        # If the list is empty, make the new node both head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.pointer_position = 1  # Move cursor after the inserted character
            return
        
        # Insert at the beginning if cursor is at position 0
        if self.pointer_position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            # Traverse to the node just before the cursor position
            current = self.head
            for _ in range(self.pointer_position - 1):
                if current.next is None:
                    break
                current = current.next
            
            # Insert the new node
            new_node.next = current.next
            current.next = new_node
            
        # Update tail if inserted at the end
        if new_node.next is None:
            self.tail = new_node
        
        # Move cursor position forward
        self.pointer_position += 1
    
    def pointer_left(self):
        """Move the cursor one position to the left if possible."""
        if self.pointer_position > 0:
            self.pointer_position -= 1
            
    def pointer_right(self):
        """Move the cursor one position to the right if possible."""
        if self.pointer_position < self.size():
            self.pointer_position += 1
    
    def delete_left(self):
        """Delete the character to the left of the cursor (backspace)."""
        # Can't delete if at the beginning
        if self.pointer_position == 0:
            return
        
        current = self.head
        # If deleting the first element
        if self.pointer_position == 1:
            self.head = current.next
        else:
            # Traverse to the node just before the one to delete
            for _ in range(self.pointer_position - 2):
                current = current.next
            # Skip the node to be deleted
            current.next = current.next.next
        
        # Move cursor position back
        self.pointer_position -= 1
    
    def delete_right(self):
        """Delete the character to the right of the cursor (delete key)."""
        # Can't delete if list is empty or cursor is at the end
        if self.head is None or self.pointer_position >= self.size():
            return

        # If deleting from position 0, update head
        if self.pointer_position == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        # Find the node just before the one to delete
        current = self.head
        for _ in range(self.pointer_position - 1):
            if current is None:
                return
            current = current.next

        # Update tail if deleting the last node
        if current.next is None:
            self.tail = current
        else:
            # Skip the node to be deleted
            current.next = current.next.next
    
    def size(self):
        """
        Calculate the size of the linked list.
        
        Returns:
            int: The number of characters in the editor
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def display(self):
        """Display the current content of the editor with the cursor position."""
        # If the list is empty, just show the cursor
        if not self.head:
            print(self.cursor)
            return
            
        result = ""
        position = 0
        current = self.head
        
        # Add cursor at the beginning if position is 0
        if self.pointer_position == 0:
            result += f' {self.cursor}'
            
        # Traverse the list and build the display string
        while current:
            result += f' {current.data}'
            position += 1
            
            # Add cursor after the current position if needed
            if position == self.pointer_position:
                result += f' {self.cursor}'
                
            current = current.next
            
        print(result.strip())

def main():
    """
    Main function to run the VIM clone.
    Processes user input and executes corresponding commands.
    """
    vim = VimClone()
    usr_input = input("Enter Input : ")
    # Split the input into individual commands
    commands = usr_input.split(',')
    
    # Process each command
    for command in commands:
        if command.startswith('I'):
            # Insert command: I <character>
            _, value = command.split()
            vim.insert(value)
        elif command.startswith('B'):
            # Backspace command: delete character to the left
            vim.delete_left()
        elif command.startswith('D'):
            # Delete command: delete character to the right
            vim.delete_right()
        elif command.startswith('L'):
            # Move cursor left
            vim.pointer_left()
        elif command.startswith('R'):
            # Move cursor right
            vim.pointer_right()
        
    # Display the final state
    vim.display()
    
if __name__ == "__main__":
    main()


