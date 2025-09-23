
rods = [[], [], []]

def display(n):
    if n == 0:
        return
    row = [str(rods[i][n-1]) if n-1 < len(rods[i]) else '|' for i in range(3)]
    print(f"{row[0]}{row[1]:^5}{row[2]}")
    display(n-1)

def rod_name(rod):
    return 'ABC'[rods.index(rod)]

def hanoi(n, src, dest, aux):
    if n == 1:
        disk = src.pop()
        dest.append(disk)
        print(f"move {disk} from  {rod_name(src)} to {rod_name(dest)}")
        display(len(rods[0]) + len(rods[1]) + len(rods[2])+1)
        print(src)
        print(aux)
        print(dest)
        return
    print(src)
    print(aux)
    print(dest)
    hanoi(n-1, src, aux, dest)
    hanoi(1, src, dest, aux)
    hanoi(n-1, aux, dest, src)

def main():
    n = int(input("Enter Input : "))
    rods[0], rods[1], rods[2] = list(range(n, 0, -1)), [], []
    display(n + 1)
    hanoi(n, rods[0], rods[2], rods[1])

if __name__ == "__main__":
    main()
