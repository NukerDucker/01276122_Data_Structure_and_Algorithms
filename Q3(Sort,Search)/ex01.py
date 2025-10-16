# ex01.py for Q3(Sort,Search)
def merge_sort(array):
    if len(array) <= 1:
        return array

    temp = [0] * len(array)

    def merge(start, middle, end):
        left, right, pos = start, middle + 1, start
        while left <= middle and right <= end:
            temp[pos] = array[left] if array[left] <= array[right] else array[right]
            left, right = (left + 1, right) if array[left] <= array[right] else (left, right + 1)
            pos += 1
        temp[pos:end + 1] = array[left:middle + 1] if left <= middle else array[right:end + 1]
        array[start:end + 1] = temp[start:end + 1]

    def sort_recursive(start, end):
        if start < end:
            middle = (start + end) // 2
            sort_recursive(start, middle)
            sort_recursive(middle + 1, end)
            merge(start, middle, end)

    sort_recursive(0, len(array) - 1)
    return array

if __name__ == "__main__":
    print(merge_sort(list(map(int, input("Enter Input : ").split()))))
