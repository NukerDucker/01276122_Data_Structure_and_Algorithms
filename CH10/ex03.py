# ex03.py for Chapter 10
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, size, max_collision):
        self.size = int(size)
        self.max_collision = int(max_collision)
        self.table = [None] * self.size
        self.table_full_shown = False

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def is_full(self):
        return all(item is not None for item in self.table)

    def display(self):
        for i in range(self.size):
            print(f"#{i + 1}\t{self.table[i]}")
        print("---------------------------")

    def insert(self, data):
        if self.is_full():
            if not self.table_full_shown:
                print("This table is full !!!!!!")
                self.table_full_shown = True
            return

        index = self.hash_function(data.key)
        original_index = index
        collision_count = 0

        if self.table[index] is None:
            self.table[index] = data
            self.display()
            return

        i = 1
        while collision_count < self.max_collision:
            print(f"collision number {collision_count + 1} at {index}")
            collision_count += 1

            index = (original_index + i * i) % self.size

            if self.table[index] is None:
                self.table[index] = data
                self.display()
                return

            i += 1

        print("Max of collisionChain")
        self.display()

def process_data(lst):
    data = []
    for s in lst:
        key, value = s.split()
        data.append(Data(key, value))
    return data

def main():
    print(' ***** Fun with hashing *****')
    s = input('Enter Input : ').split("/")
    tsize, max_collision = s[0].split()
    data = s[1].split(',')
    processed = process_data(data)

    hash_table = Hash(tsize, max_collision)
    for item in processed:
        hash_table.insert(item)

if __name__ == "__main__":
    main()