def parentheses_checker(s):
    stack = []
    parentheses = {'(': ')', '{': '}', '[': ']'}
    error = None

    for char in s:
        if char in parentheses:
            stack.append(char)
        elif char in parentheses.values():
            if not stack:
                error = "close paren excess"
                break
            elif parentheses[stack[-1]] != char:
                error = "Unmatch open-close"
                break
            else:
                stack.pop()

    if error:
        print(f"{s} {error}")
    elif stack:
        print(f"{s} open paren excess   {len(stack)} : {''.join(stack)}")
    else:
        print(f"{s} MATCH")

def main():
    usr_input = input("Enter expresion : ")
    parentheses_checker(usr_input)

if __name__ == "__main__":
    main()