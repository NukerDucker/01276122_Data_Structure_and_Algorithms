def operators_idx(o):
    if o == '^':
        return 3
    elif o in '*/':
        return 2
    elif o in '+-':
        return 1
    else:
        return -1
    
def infix_to_postfix(s):
    stack = []
    result = ''
    
    for char in s:
        if char.isalnum():
            result += char
            
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
            
        else:
            while (stack and operators_idx(stack[-1]) >= operators_idx(char)):
                result += stack.pop()
            stack.append(char)
            
    while stack:
        result += stack.pop()
        
    return result

def main():
    usr_input = input("Enter Infix : ")
    postfix = infix_to_postfix(usr_input)
    print(f"Postfix : {postfix}")
    
if __name__ == "__main__":
    main()