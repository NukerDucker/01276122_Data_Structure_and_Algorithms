# ex04.py for Chapter 9

def list_median(arr):
    nums = []
    for num in arr:
        nums.append(num)
        array = nums.copy()
        n = len(array)

        for i in range(1, n):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

        if n % 2 == 1:
            median = array[n // 2]
        else:
            median = (array[n // 2 - 1] + array[n // 2]) / 2

        print(f'list = {nums} : median = {median:.1f}')

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "Insertion sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    list_median(l)