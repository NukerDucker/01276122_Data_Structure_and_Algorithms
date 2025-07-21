class Queue:
    def __init__(self, items=None):
        self._items = [] if items is None else list(items)

    def __str__(self):
        return f"Number in Queue is :   {self._items}"

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


def command_handler(usr_input, queue):
    for command in usr_input:
        if command.startswith('E'):
            _, item = command.strip().split()
            item = item.strip()
            queue.enqueue(item)
            print(f"Add {item} index is {queue.size() - 1}")
        elif command.startswith('D'):
            item = queue.dequeue()
            if item is not None:
                print(f"Pop {item} size in queue is {queue.size()}")
            else:
                print("-1")
    return "Empty" if queue.is_empty() else queue


def main():
    usr_input = input("Enter Input : ").split(',')
    queue = Queue()
    print(command_handler(usr_input, queue))

if __name__ == "__main__":
    main()