class Stack:
    def __init__(self, items=None):
        self._items = [] if items is None else list(items)

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()

class Queue:
    def __init__(self, items=None):
        self._items = [] if items is None else list(items)

    def __str__(self):
        return f"{self._items}"

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

employee_lists, command_lists = input("Enter Input : ").split('/')
employee_lists = employee_lists.split(',')
command_lists = command_lists.split(',')
employee_dept_map = {}
queue = Queue()

for employee in employee_lists:
    department, employee_id = employee.split()
    employee_dept_map[employee_id] = department

for command in command_lists:
    if command.startswith('E'):
        _, employee_id_to_add = command.split()
        dept_to_add = employee_dept_map[employee_id_to_add]

        temp_stack = Stack()
        insert_pos = -1
        dept1_last_pos = -1

        q_size = queue.size()
        for i in range(q_size):
            emp = queue.dequeue()
            emp_dept = employee_dept_map[emp]

            if emp_dept == dept_to_add:
                insert_pos = i
            if emp_dept == '1':
                dept1_last_pos = i

            temp_stack.push(emp)

        # Rebuild the queue
        while not temp_stack.is_empty():
            queue.enqueue(temp_stack.pop())

        # Decide insert position
        temp_queue = Queue()
        insert_at = 0

        if dept_to_add == '1':
            insert_at = insert_pos + 1 if insert_pos != -1 else 0
        else:
            insert_at = max(insert_pos, dept1_last_pos) + 1

        for i in range(queue.size()):
            if i == insert_at:
                temp_queue.enqueue(employee_id_to_add)
            temp_queue.enqueue(queue.dequeue())

        if insert_at >= queue.size():  # If not inserted inside the loop
            temp_queue.enqueue(employee_id_to_add)

        queue = temp_queue

    elif command.startswith('D'):
        if not queue.is_empty():
            print(queue.dequeue())
        else:
            print("Empty")
