# ex02.py for Chapter 10
def list_ceiling(lst, target):
    lst = sorted(lst)
    for num in lst:
        if num > target:
            return num
    return 'No First Greater Value'

def main():
    parts = input('Enter Input : ').split('/')
    numbers = [int(i) for i in parts[0].split()]
    targets = [int(i) for i in parts[1].split()]
    for num in targets:
        print(list_ceiling(numbers, num))

if __name__ == "__main__":
    main()