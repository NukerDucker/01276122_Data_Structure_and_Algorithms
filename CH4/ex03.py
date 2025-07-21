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


def parse_command(command):
    command = command.strip()
    if len(command) < 2 or not command[1:].isdigit():
        return None, None
    return command[0], int(command[1:])


def process_enqueue(queue, count, enqueue_count):
    for _ in range(count):
        queue.enqueue(f'*{enqueue_count}')
        enqueue_count += 1
    return enqueue_count


def process_dequeue(queue, count):
    errors = 0
    for _ in range(count):
        if queue.is_empty():
            errors += 1
        else:
            queue.dequeue()
    return errors


def command_handler(user_commands, queue):
    error_dequeue_count = 0
    error_input_count = 0
    enqueue_count = 0

    for command in user_commands:
        print(f"Step : {command}")
        action, count = parse_command(command)

        if action == 'E':
            enqueue_count = process_enqueue(queue, count, enqueue_count)
            print(f"Enqueue : {queue}")

        elif action == 'D':
            error_dequeue_count += process_dequeue(queue, count)
            print(f"Dequeue : {queue}")

        else:
            error_input_count += 1
            print(queue)

        print(f"Error Dequeue : {error_dequeue_count}")
        print(f"Error input : {error_input_count}")
        print('--------------------')


def main():
    user_commands = input("input : ").split(',')
    queue = Queue()
    command_handler(user_commands, queue)


if __name__ == "__main__":
    main()
