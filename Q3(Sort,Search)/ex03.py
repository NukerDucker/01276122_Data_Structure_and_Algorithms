# ex03.py for Chapter Q3(Sort,Search)

class HashTable:
    def __init__(self, size, max_collision):
        self.size = size
        self.max_collision = max_collision
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        original_index = index
        collision_count = 0

        if self.table[index] is None:
            self.table[index] = key
            return True

        i = 1
        while collision_count < self.max_collision:
            print(f"collision number {collision_count + 1} at {index}")
            collision_count += 1

            index = (original_index + i * i) % self.size

            if self.table[index] is None:
                self.table[index] = key
                return True

            i += 1

        print("Max of collisionChain")
        return False

    def display(self):
        for i in range(self.size):
            print(f"#{i + 1}\t{self.table[i]}")
        print("---------------------------")

def main():
    inp = input("Enter Input : ").split("/")
    size, max_col = map(int, inp[0].split())
    keys = list(map(int, inp[1].split()))

    ht = HashTable(size, max_col)

    for key in keys:
        ht.insert(key)
        ht.display()

if __name__ == "__main__":
    main()
