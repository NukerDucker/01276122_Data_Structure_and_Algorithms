# ex01.py for Chapter 9
def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        swapped = False
        moved = None
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                moved = array[j + 1]

        step_label = "last" if i == (n - 2) or moved is None else str(i + 1)
        print(f'{step_label} step : {array} move[{moved}]')
        if not swapped:
            break

def main():
    input_array = input('Enter Input : ').split()
    input_array = [int(i) for i in input_array]
    bubble_sort(input_array)

if __name__ == "__main__":
    main()