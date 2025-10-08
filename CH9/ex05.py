# ex05.py for Chapter 9

def quick_sort(arr, pivot_strategy):
    comparisons = [0]
    arr_copy = arr.copy()

    def partition(low, high, pivot_index):
        pivot = arr_copy[pivot_index]
        arr_copy[pivot_index], arr_copy[high] = arr_copy[high], arr_copy[pivot_index]

        i = low
        for j in range(low, high):
            comparisons[0] += 1
            if arr_copy[j] <= pivot:
                arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
                i += 1

        arr_copy[i], arr_copy[high] = arr_copy[high], arr_copy[i]
        return i

    def sort(low, high):
        if low < high:
            if pivot_strategy == 'first':
                pivot_index = low
            elif pivot_strategy == 'last':
                pivot_index = high
            else:
                pivot_index = (low + high) // 2

            pivot_pos = partition(low, high, pivot_index)

            sort(low, pivot_pos - 1)
            sort(pivot_pos + 1, high)

    if len(arr_copy) > 1:
        sort(0, len(arr_copy) - 1)

    return comparisons[0]

def main():
    print(" *** Quick sort ***")
    input_str = input("Enter a sequence of integers : ")

    numbers = [int(x) for x in input_str.split()]

    first_pivot = quick_sort(numbers, 'first')
    last_pivot = quick_sort(numbers, 'last')
    middle_pivot = quick_sort(numbers, 'middle')

    print("\nNumber of comparisons for each pivot strategy:")
    print(f"First Pivot: {first_pivot} comparisons")
    print(f"Last Pivot: {last_pivot} comparisons")
    print(f"Middle Pivot: {middle_pivot} comparisons")
    print("===== End of program =====")

if __name__ == "__main__":
    main()