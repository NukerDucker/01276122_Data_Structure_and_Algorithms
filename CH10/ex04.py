class HashTable:
    def __init__(self, size, max_col, threshold):
        self.size = size
        self.max_col = max_col
        self.threshold = threshold
        self.table = [None] * size
        self.count = 0

    def insert(self, key, rehash=False):
        key = int(key)

        if key < 0:
            return

        if self._over_threshold(rehash):
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
            self.insert(key)
            return

        if not self._probe(key):
            print("****** Max collision - Rehash !!! ******")
            self.rehash()
            self.insert(key)

    def _over_threshold(self, rehash):
        if rehash:
            return False
        load = (self.count + 1) / self.size * 100
        return load > self.threshold

    def _probe(self, key):
        for i in range(self.max_col):
            idx = (key + i ** 2) % self.size

            if self.table[idx] is None:
                self.table[idx] = key
                self.count += 1
                return True

            print(f"collision number {i + 1} at {idx}")

        return False

    def rehash(self):
        old = [x for x in self.table if x is not None]

        self.size = self._next_prime(self.size * 2)
        self.table = [None] * self.size
        self.count = 0

        for x in reversed(old):
            self.insert(x, rehash=True)

    def _next_prime(self, n):
        p = n + 1
        while not self._is_prime(p):
            p += 1
        return p

    def _is_prime(self, n):
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

    def is_full(self):
        return all(self.table)

    def show(self):
        for i, item in enumerate(self.table):
            print(f"#{i + 1}\t{item}")
        print("----------------------------------------")

def main():
    print(" ***** Rehashing *****")
    inp = input("Enter Input : ")

    cfg, data = inp.split("/")
    size, max_col, threshold = map(int, cfg.split())
    keys = data.split()

    ht = HashTable(size, max_col, threshold)
    print("Initial Table :")
    ht.show()

    for key in keys:
        if ht.is_full():
            print("This table is full !!!!!!")
            break

        print("Add :", key)
        ht.insert(key)
        ht.show()

if __name__ == "__main__":
    main()