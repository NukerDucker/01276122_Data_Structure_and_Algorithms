def staircase(n):
    if n > 0:
        return staircase_positive(n, 1)
    elif n < 0:
        return staircase_negative(abs(n), 1)
    else:
        return "Not Draw!"

def staircase_positive(n, count):
    if count > n:
        return ""
    result = "_" * (n - count) + "#" * count + ("\n" if count < n else "")
    return result + staircase_positive(n, count + 1)

def staircase_negative(n, count):
    if count > n:
        return ""
    result = "_" * (count - 1) + "#" * (n - count + 1) + ("\n" if count < n else "")
    return result + staircase_negative(n, count + 1)

print(" *** Stair case ***")
print(staircase(int(input("Enter Input : "))))
print("===== End of program =====")
