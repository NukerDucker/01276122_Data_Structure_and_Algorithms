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

class Customer:
    def __init__(self, cid, arrival, prep):
        self.cid = cid
        self.arrival = arrival
        self.prep = prep
        self.start = None
        self.end = None
        self.wait = 0

def parse_input(log):
    entries = log.split('/')
    customers = []
    for idx, entry in enumerate(entries):
        arrival, prep = map(int, entry.split(','))
        customers.append(Customer(idx + 1, arrival, prep))
    return customers

def simulate(log):
    customers = parse_input(log)
    queue = Queue()
    baristas = [0, 0]
    timeline = []

    time = 0
    i = 0
    total_customers = len(customers)
    completed = []

    while len(completed) < total_customers:
        while i < total_customers and customers[i].arrival <= time:
            queue.enqueue(customers[i])
            i += 1

        for b in range(2):
            if baristas[b] <= time and not queue.is_empty():
                customer = queue.dequeue()
                customer.wait = max(0, time - customer.arrival)
                customer.start = time
                customer.end = time + customer.prep
                baristas[b] = customer.end
                timeline.append((customer.end, customer.cid))
                completed.append(customer)

        time += 1
    timeline.sort()

    for t, cid in timeline:
        print(f"Time {t} customer {cid} get coffee")

    max_wait = max(c.wait for c in completed)
    if max_wait == 0:
        print("No waiting")
    else:
        for c in completed:
            if c.wait == max_wait:
                print(f"The customer who waited the longest is : {c.cid}")
                print(f"The customer waited for {c.wait} minutes")
                break

def main():
    print(" ***Cafe***")
    log = input("Log : ")
    simulate(log)
    
if __name__ == "__main__":
    main()
