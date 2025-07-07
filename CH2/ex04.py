def sum_3_array(n):
    array = n.split(" ")
    array = [int(i) for i in array]
    arr_len = len(array)
    res = []
    
    if len(array) < 3:
        return "Array Input Length Must More Than 2"
    
    for i in range(arr_len - 2):
        for j in range(i + 1, arr_len - 1):
            for k in range(j + 1, arr_len):
                if array[i] + array[j] + array[k] == 0:
                    res_array = [array[i], array[j], array[k]]
                    if res_array not in res:
                        res.append([array[i], array[j], array[k]])
    return res

def main():
    n = input("Enter Your List : ")
    result = sum_3_array(n)
    if isinstance(result, str):
        print(result)
    else:
        print(f"{result}")
        
if __name__ == "__main__":
    main()