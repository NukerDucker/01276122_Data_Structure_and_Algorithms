def parentheses_checker(s):
    stack = []
    parentheses = {'(': ')', '{': '}', '[': ']'}
    missing = 0

    for char in s:
        if char in parentheses:
            stack.append(char)
        elif char in parentheses.values():
            if not stack or parentheses[stack[-1]] != char:
                missing += 1
            else:
                stack.pop()

    missing += len(stack)
    return missing

def main():
    usr_input = input("Enter Input : ")
    missing = parentheses_checker(usr_input)
    if missing == 0:
        print(missing)
        print("Perfect ! ! !")
    else:
        print(missing)
        
if __name__ == "__main__":
    main()