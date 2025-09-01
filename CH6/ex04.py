
A = []
B = []
C = []

def display_rods(n):
    if n == 0:
        return
    a = str(A[n-1]) if n-1 < len(A) else '|'
    b = str(B[n-1]) if n-1 < len(B) else '|'
    c = str(C[n-1]) if n-1 < len(C) else '|'
    print(f"{a}{b:^5}{c}")
    display_rods(n - 1)

def source_name(rod):
    if rod is A:
        return 'A'
    elif rod is B:
        return 'B'
    else:
        return 'C'

def move(n, A, B, C):
    if n == 1:
        disk = A.pop()
        B.append(disk)
        print(f"move {disk} from  {source_name(A)} to {source_name(B)}")
        display_rods(len(A)+len(B)+len(C)+1)
        return
    move(n-1, A, C, B)
    move(1, A, B, C)
    move(n-1, C, B, A)

def main():
    global A, B, C
    n = int(input("Enter Input : "))
    A = list(range(n, 0, -1))
    B = []
    C = []

    display_rods(n + 1)
    move(n, A, C, B)

if __name__ == "__main__":
    main()
