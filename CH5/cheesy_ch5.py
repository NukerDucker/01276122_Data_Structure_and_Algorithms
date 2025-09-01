import timeit
class SingleLinkedNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node: SingleLinkedNode = next_node
    def __str__(self) -> str:
        return str(self.value)
        
class SingleLinkedList:
    def __init__(self):
        self.first_node = None
    
    def __str__(self) -> str:
        output = str()
        node: SingleLinkedNode = self.first_node
        while node is not None:
            output += f"{node.value} "
            node = node.next_node
        return output
    
    def append_node(self, node: SingleLinkedNode):
        if self.first_node is None:
            self.first_node = node
            return
        iterating_node: SingleLinkedNode = self.first_node
        while iterating_node is not None:
            if iterating_node.next_node is None:
                iterating_node.next_node = node
                return
            iterating_node = iterating_node.next_node
                
    def delete_node(self, node: SingleLinkedNode):
        if self.first_node is None: return
        if self.first_node is node: 
            self.first_node = self.first_node.next_node
            return
        
        iterating_node: SingleLinkedNode = self.first_node
        while iterating_node.next_node is not None:
            if iterating_node.next_node is node:
                iterating_node.next_node = iterating_node.next_node.next_node
                return
            iterating_node = iterating_node.next_node
    
def get_radix_at_digit(i: int, digit_base: int) -> int:
    positive_i: int = i if i >= 0 else -i
    return (positive_i % (digit_base*10)) // digit_base



def main():
    concatenated_list = SingleLinkedList()
    unsorted_list: list[int] = []
    usr_input = "170 45 75 90 802 24 2 66 80 22 787 989 34 22 40 1 2 -1 -677 -9 -55 1000 4874 7348 -3849 34"
    all_zeros = True
    for e in usr_input.split():
        if all_zeros: all_zeros = int(e) == 0
        
        concatenated_list.append_node(SingleLinkedNode(int(e)))
        unsorted_list.append(int(e))
    print("------------------------------------------------------------")
    
    if all_zeros:
        print(f"0 Time(s)")
        print("Before Radix Sort : 0", end='')
        for e in unsorted_list[1:]:
            print(" -> 0", end='')
        print()
        print("After  Radix Sort : 0", end='')
        for e in unsorted_list[1:]:
            print(" -> 0", end='')
        print()
        return

    radix_pointers: list[SingleLinkedList] = []
    for i in range(10):
        radix_pointers.append(SingleLinkedList())

    has_next_digit = True
    round_count = int(0)

    while has_next_digit:
        digit_base = 10**round_count
        has_next_digit = False
        
        for i in reversed(range(10)):
            node: SingleLinkedNode = concatenated_list.first_node
            while node is not None:
                radix: int = get_radix_at_digit(i=node.value, digit_base=digit_base)
                if not has_next_digit:
                    positive_int: int = node.value if node.value >= 0 else -node.value
                    has_next_digit = positive_int//(digit_base*10) > 0
                
                if radix != i or node.value < 0:
                    node = node.next_node
                    continue
                
                deleting_node: SingleLinkedNode = node
                node = node.next_node
                radix_pointers[i].append_node(SingleLinkedNode(deleting_node.value))
                concatenated_list.delete_node(deleting_node)

        for i in reversed(range(10)):
            node: SingleLinkedNode = concatenated_list.first_node
            while node is not None:
                radix: int = get_radix_at_digit(i=node.value, digit_base=digit_base)
                if not has_next_digit:
                    positive_int: int = node.value if node.value >= 0 else -node.value
                    has_next_digit = positive_int//(digit_base*10) > 0
                
                if radix != i:
                    node = node.next_node
                    continue
                
                deleting_node: SingleLinkedNode = node
                node = node.next_node
                radix_pointers[i].append_node(SingleLinkedNode(deleting_node.value))
                concatenated_list.delete_node(deleting_node)
        
        print(f"Round : {round_count+1}")
        for i, radix_pointer in enumerate(radix_pointers):
            print(f"{i} : {radix_pointer}")
        print("------------------------------------------------------------")
        
        for radix_pointer in reversed(radix_pointers):
            node: SingleLinkedNode = radix_pointer.first_node
            while node is not None:
                if node.value > 0:
                    concatenated_list.append_node(SingleLinkedNode(node.value))
                    radix_pointer.delete_node(node)
                node = node.next_node

        for radix_pointer in radix_pointers:
            node: SingleLinkedNode = radix_pointer.first_node
            while node is not None:
                concatenated_list.append_node(SingleLinkedNode(node.value))
                radix_pointer.delete_node(node)
                node = node.next_node               
        round_count += 1
        
    print(f"{round_count} Time(s)")
        
    print(f"Before Radix Sort : {unsorted_list[0]}", end='')
    for e in unsorted_list[1:]:
        print(f" -> {e}", end='')
    print()

    node: SingleLinkedNode = concatenated_list.first_node
    print(f"After  Radix Sort : {node}", end='')
    node = node.next_node
    while node is not None:
        print(f" -> {node}", end='')
        node = node.next_node
    print()
    
if __name__ == "__main__":
    execution_time = timeit.timeit(lambda: main(), number=1)
    print(f"Execution time: {execution_time:.6f} seconds")