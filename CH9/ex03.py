# ex03.py for Chapter 9

def get_sorted_type(arr: list) -> str:
    if len(set(arr)) == 1:
        return "Repdrome"

    is_ascending: bool = True
    is_descending: bool = True
    has_duplicates: bool = len(set(arr)) < len(arr)
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            is_ascending = False
        if arr[i-1] < arr[i]:
            is_descending = False

    if is_ascending:
        return "Plaindrome" if has_duplicates else "Metadrome"
    elif is_descending:
        return "Nialpdrome" if has_duplicates else "Katadrome"
    else:
        return "Nondrome"
def main():
    arr: list = list(input('Enter Input : '))
    arr: list = [int(i) for i in arr]
    print(get_sorted_type(arr))

if __name__ == "__main__":
    main()
