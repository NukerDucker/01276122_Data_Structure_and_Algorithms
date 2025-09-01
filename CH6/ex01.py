def natural_sum(n):
    if n == 1:
        return '1'
    return f'{natural_sum(n-1)} + {n}'

print(" *** Natural sum ***")
num = int(input("Enter number : ")) 
print(f"{natural_sum(num)} = {sum(range(1, num+1))}")
print("===== End of program =====")