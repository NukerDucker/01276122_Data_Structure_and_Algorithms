class Queue:
    def __init__(self):
        self._items = []

    def __str__(self):
        return f"{self._items}"

    def __getitem__(self, index):
        return self._items[index]
    
    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._items.pop(0)
    
    def popleft(self):
        self.dequeue()
        
    def peek(self):
        if self.is_empty():
            return None
        return self._items[0]
    
def has_bomb(stack):
    return len(stack) >= 3 and stack[-1] == stack[-2] == stack[-3]

def bomb(stack):
    for _ in range(3):
        stack.pop()
    
def process_mirror(mirror_side):
    mirror_reversed = list(reversed(mirror_side))
    stack = []
    blocking_queue = Queue()
    explosions = 0

    for char in mirror_reversed:
        stack.append(char)
        while has_bomb(stack):
            bomb_char = stack[-1]
            bomb(stack)
            explosions += 1
            blocking_queue.enqueue(bomb_char)
            
    return list(reversed(stack)), blocking_queue, explosions

def process_normal(normal_side, blocking_queue):
    stack = []
    explosions = 0
    failed_blocks = 0
    for char in normal_side:
        stack.append(char)
        while has_bomb(stack):
            if not blocking_queue.is_empty():
                blocked_char = blocking_queue[0] 
                if blocked_char == stack[-1]:
                    stack.pop()
                    stack.pop()
                    failed_blocks += 1
                else:
                    temp = stack.pop()
                    stack.append(blocked_char)
                    stack.append(temp)
                blocking_queue.popleft()
            else:
                bomb(stack)
                explosions += 1

    return stack, explosions, failed_blocks

def main():
    usr_input = input("Enter Input (Normal, Mirror) : ").split()
    if len(usr_input) != 2:
        print("Please enter exactly two strings")
        return

    normal_side, mirror_side = usr_input

    mirror_result, blocking_queue, mirror_explosions = process_mirror(mirror_side)

    normal_result, normal_explosions, failed_blocks = process_normal(normal_side, blocking_queue)

    print("NORMAL :")
    print(len(normal_result))
    print(''.join(reversed(normal_result)) if normal_result else "Empty")
    print(f"{normal_explosions} Explosive(s) ! ! ! (NORMAL)")
    if failed_blocks > 0:
        print(f"Failed Interrupted {failed_blocks} Bomb(s)")
        
    print("------------MIRROR------------")
    print(": RORRIM")
    print(len(mirror_result))
    print(''.join(mirror_result) if mirror_result else "ytpmE")
    print(f"(RORRIM) ! ! ! (s)evisolpxE {mirror_explosions}")

if __name__ == "__main__":
    main()
