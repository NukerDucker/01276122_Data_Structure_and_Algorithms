def natural_sum(n: int) -> int:
    if n == 1:
        return 1
    return natural_sum(n-1) + n

def formula_sum(n: int) -> str:
    if n == 1:
        return '1'
    return f'{formula_sum(n-1)} + {n}'

print(" *** Natural sum ***")
num = int(input("Enter number : "))
formula, result = formula_sum(num), natural_sum(num)
print(f"{formula} = {result}")
print("===== End of program =====")