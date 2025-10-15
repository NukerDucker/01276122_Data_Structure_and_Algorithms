# ex04.py for Chapter Q3(Sort,Search)

class HashTable:
    def __init__(self, size, max_collision, threshold):
        self.size = size
        self.max_collision = max_collision
        self.threshold = threshold
        self.table = [None] * size
        self.count = 0

    def hash_function(self, key):
        return key % self.size

    def is_prime(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def next_prime(self, n):
        p = n + 1
        while not self.is_prime(p):
            p += 1
        return p

    def over_threshold(self, rehash):
        if rehash:
            return False
        load = (self.count + 1) / self.size * 100
        return load > self.threshold

    def probe(self, key):
        index = self.hash_function(key)
        original_index = index
        for i in range(self.max_collision):
            idx = (original_index + i ** 2) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                self.count += 1
                return True

            print(f"collision number {i + 1} at {idx}")

        return False

    def rehash(self):
        old = [x for x in self.table if x is not None]

        self.size = self.next_prime(self.size * 2)
        self.table = [None] * self.size
        self.count = 0

        for x in reversed(old):
            self.insert(x, rehash=True)

    def insert(self, key, rehash=False):
        if self.over_threshold(rehash):
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
            self.insert(key)
            return

        if not self.probe(key):
            print("****** Max collision - Rehash !!! ******")
            self.rehash()
            self.insert(key)

    def display(self):
        for i in range(self.size):
            print(f"#{i + 1}\t{self.table[i]}")
        print("----------------------------------------")

def main():
    inp = input("Enter Input : ").split("/")
    size, max_col, threshold = map(int, inp[0].split())
    keys = inp[1].split()

    ht = HashTable(size, max_col, threshold)
    print("Initial Table :")
    ht.display()

    for key in keys:
        key = int(key)
        print("Add :", key)
        ht.insert(key)
        ht.display()

if __name__ == "__main__":
    main()
