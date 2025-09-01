def length(txt, symbol="*"):
    if txt == "":
        return 0, ""
    
    remaining_length, remaining_text = length(txt[1:], "~" if symbol == "*" else "*")
    transformed_txt = txt[0] + symbol + remaining_text
    
    return 1 + remaining_length, transformed_txt

print(" *** Length of string (Recursion) ***")
usr = input("Enter Input : ")
len_text, new_text = length(usr)
print(new_text)
print(f"length of '{usr}' is {len_text}")