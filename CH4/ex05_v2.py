# TODO THIS CODE IS NOT FINISHED
class Queue:
    def __init__(self):
        self._items = []

    def __str__(self):
        return str([(c, r) for (r, c), dist in self._items])

    def __getitem__(self, index):
        return self._items[index]
    
    @property
    def is_empty(self):
        return len(self._items) == 0

    @property
    def size(self):
        return len(self._items)

    @property
    def peek(self):
        return self._items[0] if not self.is_empty else None

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0) if not self.is_empty else None
    
    def popleft(self):
        self.dequeue()
        
usr_input = input("Enter Input : ").split(',')
first_line = usr_input.pop(0).split()
width = int(first_line[0])
height = int(first_line[1])
room = [first_line[2]] + usr_input
room = [list(row) for row in room]

if len(room) != height or any(len(row) != width for row in room):
    print("Invalid map input.")
    exit()

start_pos = None
for r, row in enumerate(room):
    for c, char in enumerate(row):
        if char == 'F':
            start_pos = (r, c)
            break
    if start_pos:
        break

if not start_pos:
    print("Invalid map input.")
    exit()

q = Queue()
q.enqueue((start_pos, 0))
visited = {start_pos}
found = False
checking_path = [[-1, 0], [0, 1], [1, 0], [0, -1]] 

while not q.is_empty:
    front = q.peek
    if front and room[front[0][0]][front[0][1]] != 'O':
        print(f"Queue: {q}")
    item = q.dequeue()
    if item is None:
        break
    (r, c), dist = item
    
    if room[r][c] == 'O':
        print("Found the exit portal.")
        found = True
        break
        
    for dr, dc in checking_path:
        nr, nc = r + dr, c + dc

        if 0 <= nr < height and 0 <= nc < width and room[nr][nc] in ['_', 'O'] and (nr, nc) not in visited:
            visited.add((nr, nc))
            q.enqueue(((nr, nc), dist + 1))
    
if not found:
    print("Cannot reach the exit.")
