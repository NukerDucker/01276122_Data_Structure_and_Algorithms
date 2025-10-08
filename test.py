def some_fibonacci(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    return some_fibonacci(n - 1) + some_fibonacci(n - 2) + 1

test= int(input("enter : "))
print(some_fibonacci(test))