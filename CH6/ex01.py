# def natural_sum(n):
#     if n == 1:
#         return '1'
#     return f'{natural_sum(n-1)} + {n}'

# print(" *** Natural sum ***")
# num = int(input("Enter number : ")) 
# print(f"{natural_sum(num)} = {sum(range(1, num+1))}")
# print("===== End of program =====")

# def natural_sum(n):
#     s = n * (n + 1) // 2
#     return f"{' + '.join(map(str, range(1, n + 1)))} = {s}"

# print(" *** Natural sum ***")
# num = int(input("Enter number : ")) 
# print(f"{natural_sum(num)}")
# print("===== End of program =====")

def natural_sum(n):
    if n == 1:
        return '1 = 1'

    prev_result = natural_sum(n-1).split(' = ')
    sum_str = prev_result[0]
    prev_sum = int(prev_result[1])

    new_sum = prev_sum + n
    new_sum_str = f'{sum_str} + {n}'
    
    return f'{new_sum_str} = {new_sum}' 

print(" *** Natural sum ***")
num = int(input("Enter number : ")) 
print(f"{natural_sum(num)}")
print("===== End of program =====")