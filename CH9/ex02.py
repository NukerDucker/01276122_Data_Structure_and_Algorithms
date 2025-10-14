# ex02.py for Chapter 9
def bubble_sort(array):
    indices = [i for i, v in enumerate(array) if v >= 0]

    if not indices:
        print(*array)
        return

    n = len(indices)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            idx_j = indices[j]
            idx_j_plus_1 = indices[j + 1]

            if array[idx_j] > array[idx_j_plus_1]:
                array[idx_j], array[idx_j_plus_1] = array[idx_j_plus_1], array[idx_j]
                swapped = True

        if not swapped:
            break

    print(*array)

def main():
    input_array = input('Enter Input : ').split()
    if not input_array:
        return

    input_array = [int(i) for i in input_array]
    bubble_sort(input_array)

if __name__ == "__main__":
    main()