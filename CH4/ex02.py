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
    
    def items(self):
        return self._items
    
def cashier_queue(usr_input):
    people = list(usr_input)
    main_queue = Queue(people)
    cashier1_queue = Queue()
    cashier2_queue = Queue()
    cashier1_time = 3  
    cashier2_time = 2 
    time = 0

    while not main_queue.is_empty():
        time += 1
        
        if time % cashier1_time == 1 and not cashier1_queue.is_empty():
            cashier1_queue.dequeue()
        
        if time % cashier2_time == 0 and not cashier2_queue.is_empty():
            cashier2_queue.dequeue()
        
        if not main_queue.is_empty():
            if cashier1_queue.size() < 5:
                person = main_queue.dequeue()
                cashier1_queue.enqueue(person)
            elif cashier2_queue.size() < 5:
                person = main_queue.dequeue()
                cashier2_queue.enqueue(person)
        
        print(f"{time} {main_queue} {cashier1_queue} {cashier2_queue}")

def main():
    usr_input = input("Enter people : ")
    cashier_queue(usr_input)
    
if __name__ == "__main__":
    main()