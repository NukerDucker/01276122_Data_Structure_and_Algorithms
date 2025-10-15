# ex01.py for Q3(Sort,Search)

def merge(array, start, middle, end, temp):
    left, right, pos = start, middle + 1, start
    while left <= middle and right <= end:
        if array[left] <= array[right]:
            temp[pos] = array[left]
            left += 1
        else:
            temp[pos] = array[right]
            right += 1
        pos += 1

    while left <= middle:
        temp[pos] = array[left]
        left, pos = left + 1, pos + 1

    while right <= end:
        temp[pos] = array[right]
        right, pos = right + 1, pos + 1

    array[start:end + 1] = temp[start:end + 1]

def merge_sort_recursive(array, start, end, temp):
    if start < end:
        middle = (start + end) // 2
        merge_sort_recursive(array, start, middle, temp)
        merge_sort_recursive(array, middle + 1, end, temp)
        merge(array, start, middle, end, temp)

def merge_sort(array):
    if len(array) <= 1:
        return array
    temp = [0] * len(array)
    merge_sort_recursive(array, 0, len(array) - 1, temp)
    return array

def main():
#   inp = "1 3 2 4 6 7 8 5 9"
    nums = list(map(int, input("Enter Input : ").split()))
    print(merge_sort(nums))

if __name__ == "__main__":
    main()
