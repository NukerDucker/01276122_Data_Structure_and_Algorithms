def find_max(lst: list) -> int:
    if not lst:
        raise ValueError("Cannot find max of empty list")
    if len(lst) == 1:
        return lst[0]
    rest_max = find_max(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max

def main() -> None:
    numbers = [int(x) for x in input('Enter number: ').split()]
    print('Max:', find_max(numbers))

if __name__ == '__main__':
    main()