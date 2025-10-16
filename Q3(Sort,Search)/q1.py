def is_unimodal(arr):
    if len(arr) < 3:
        return False
    peak_idx = next((i for i in range(len(arr) - 1) if arr[i] >= arr[i + 1]), len(arr) - 1)
    return (all(arr[i] < arr[i + 1] for i in range(peak_idx)) and
            all(arr[i] > arr[i + 1] for i in range(peak_idx, len(arr) - 1)))

def find_peak_binary_search(arr):
    if len(arr) < 3 or not is_unimodal(arr):
        print("not enough" if len(arr) < 3 else "not a unimodal array")
        return -1
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        left, right = (mid + 1, right) if arr[mid] < arr[mid + 1] else (left, mid)
    return left

def find_peak_value(arr):
    peak_index = find_peak_binary_search(arr)
    return arr[peak_index] if peak_index != -1 else None

def main():
    inp = input('Enter numbers : ').split()
    numbers = list(map(int, inp))
    peak_idx = find_peak_binary_search(numbers)
    if peak_idx != -1:
        print(f"Peak index: {peak_idx}, Peak value: {numbers[peak_idx]}")
    print()

if __name__ == "__main__":
    main()