class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
        return self.root

    def _insert(self, node, data):
        if data == node.data:
            return
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def print_levels(self, node=None, level=0, levels=None):
        if levels is None:
            levels = {}
        if node is None:
            node = self.root

        if node:
            if level not in levels:
                levels[level] = []
            levels[level].append(node.data)
            self.print_levels(node.left, level + 1, levels)
            self.print_levels(node.right, level + 1, levels)

        if level == 0:
            for lvl in sorted(levels.keys()):
                print(f"Level {lvl} : {' '.join(map(str, sorted(levels[lvl])))}")

def main():
    tree = BST()
    values = input('Enter Input : ').split()
    for value in values:
        tree.insert(int(value))

    tree.print_levels()

if __name__ == '__main__':
    main()