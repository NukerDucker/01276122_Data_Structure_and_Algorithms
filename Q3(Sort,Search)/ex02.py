# ex02.py for Chapter Q3(Sort,Search)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    nums = list(map(int, input("Enter Input : ").split()))
    sorted_nums = insertion_sort(nums)
    print(sorted_nums)

if __name__ == "__main__":
    main()
