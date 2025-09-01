def display(towers, n):
    for level in range(n-1, -1, -1):  # print from top to bottom
        row = []
        for rod in "ABC":
            if level < len(towers[rod]):
                row.append(str(towers[rod][level]))
            else:
                row.append("|")
        print("  ".join(row))
    print()
    
def move(n,A,B,C,maxn):
    if n==1:
        print ("move 1 from ",A,"to",C)
        return
    move(n-1, A, B, C, maxn)
    print ("move",n,"from ",A,"to",C)
    move(n-1, B, C, A, maxn)

n = int(input("Enter Input : "))
move(n, "A", "B", "C", n)