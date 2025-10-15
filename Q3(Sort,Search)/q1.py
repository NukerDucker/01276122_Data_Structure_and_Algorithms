"""
Find the peak of a unimodal array using Binary Search

A unimodal array is an array that:
- Increases monotonically up to a certain index (the peak)
- Then decreases monotonically after that index

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def is_unimodal(arr):
    """
    Check if an array is unimodal (increases then decreases).

    Args:
        arr: An array of integers

    Returns:
        True if the array is unimodal, False otherwise
    """
    if len(arr) < 3:
        return False

    # Find the peak
    peak_idx = 0
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            peak_idx = i
            break
    else:
        # Array is strictly increasing (peak at end)
        peak_idx = len(arr) - 1

    # Check if elements before peak are strictly increasing
    for i in range(peak_idx):
        if arr[i] >= arr[i + 1]:
            return False

    # Check if elements after peak are strictly decreasing
    for i in range(peak_idx, len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            return False

    return True


def find_peak_binary_search(arr):
    """
    Find the peak element in a unimodal array using binary search.

    Args:
        arr: A unimodal array of integers

    Returns:
        The index of the peak element, or -1 if not enough elements or not unimodal
    """
    if not arr or len(arr) <= 2:
        print("not enough")
        return -1

    if not is_unimodal(arr):
        print("not a unimodal array")
        return -1

    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # If the middle element is less than the next element,
        # the peak must be in the right half
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        # Otherwise, the peak is in the left half (including mid)
        else:
            right = mid

    # At the end, left == right, which points to the peak
    return left


def find_peak_value(arr):
    """
    Find the peak value in a unimodal array.

    Args:
        arr: A unimodal array of integers

    Returns:
        The peak value
    """
    peak_index = find_peak_binary_search(arr)
    return arr[peak_index] if peak_index != -1 else None


# Test cases
if __name__ == "__main__":
    # Test case 1: Standard unimodal array
    arr1 = [1, 3, 5, 7, 9, 8, 6, 4, 2]
    peak_idx1 = find_peak_binary_search(arr1)
    if peak_idx1 != -1:
        print(f"Array: {arr1}")
        print(f"Peak index: {peak_idx1}, Peak value: {arr1[peak_idx1]}")
    print()

    # Test case 2: Peak at the beginning (NOT unimodal - only decreasing)
    arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Array: {arr2}")
    peak_idx2 = find_peak_binary_search(arr2)
    if peak_idx2 != -1:
        print(f"Peak index: {peak_idx2}, Peak value: {arr2[peak_idx2]}")
    print()

    # Test case 3: Peak at the end (NOT unimodal - only increasing)
    arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Array: {arr3}")
    peak_idx3 = find_peak_binary_search(arr3)
    if peak_idx3 != -1:
        print(f"Peak index: {peak_idx3}, Peak value: {arr3[peak_idx3]}")
    print()

    # Test case 4: Peak in the middle (valid unimodal)
    arr4 = [1, 5, 10, 15, 20, 18, 12, 8, 3]
    peak_idx4 = find_peak_binary_search(arr4)
    if peak_idx4 != -1:
        print(f"Array: {arr4}")
        print(f"Peak index: {peak_idx4}, Peak value: {arr4[peak_idx4]}")
    print()

    # Test case 5: Single element (not enough)
    arr5 = [42]
    print(f"Array: {arr5}")
    peak_idx5 = find_peak_binary_search(arr5)
    print()

    # Test case 6: Two elements (not enough)
    arr6 = [5, 3]
    print(f"Array: {arr6}")
    peak_idx6 = find_peak_binary_search(arr6)
    print()

    # Test case 7: Not unimodal (has multiple peaks)
    arr7 = [1, 3, 2, 5, 4, 6, 3]
    print(f"Array: {arr7}")
    peak_idx7 = find_peak_binary_search(arr7)
    print()

    # Test case 8: Valid unimodal array
    arr8 = [2, 4, 6, 8, 10, 12, 11, 9, 7, 5]
    peak_idx8 = find_peak_binary_search(arr8)
    if peak_idx8 != -1:
        print(f"Array: {arr8}")
        print(f"Peak index: {peak_idx8}, Peak value: {arr8[peak_idx8]}")
    print()

    # Test case 9: Empty array
    arr9 = []
    print(f"Array: {arr9}")
    peak_idx9 = find_peak_binary_search(arr9)
    print()
