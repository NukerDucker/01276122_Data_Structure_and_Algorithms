symbol = '*'

def length(txt):
    global symbol
    if not txt:
        return 0, ""

    current = symbol
    symbol = "~" if symbol == "*" else "*"

    remaining_len, remaining_txt = length(txt[1:])
    return 1 + remaining_len, txt[0] + current + remaining_txt

def main():
    print(' *** Length of string (Recursion) ***')
    user_input = input('Enter Input : ')
    text_len, text = length(user_input)
    print(text)
    print(f"length of '{user_input}' is {text_len}")

if __name__ == '__main__':
    main()