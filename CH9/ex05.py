print(" *** Quick sort ***")
nums = list(map(int, input("Enter a sequence of integers : ").split()))

def qsort(arr, ptype):
    count = [0]

    def part(a, lo, hi):
        count[0] += (hi - lo - 1)

        if ptype == "first":
            pv = a[lo]
        elif ptype == "last":
            a[lo], a[hi-1] = a[hi-1], a[lo]
            pv = a[lo]
        elif ptype == "middle":
            mid = lo + (hi - lo - 1) // 2
            a[lo], a[mid] = a[mid], a[lo]
            pv = a[lo]

        i = lo + 1
        for j in range(lo+1, hi):
            if a[j] < pv:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[lo], a[i-1] = a[i-1], a[lo]
        return i-1

    def sort(a, lo, hi):
        if lo < hi:
            p = part(a, lo, hi)
            sort(a, lo, p)
            sort(a, p+1, hi)

    sort(arr[:], 0, len(arr))
    return count[0]

first = qsort(nums, "first")
last = qsort(nums, "last")
mid = qsort(nums, "middle")

print("\nNumber of comparisons for each pivot strategy:")
print(f"First Pivot: {first} comparisons")
print(f"Last Pivot: {last} comparisons")
print(f"Middle Pivot: {mid} comparisons")
print("===== End of program =====")
