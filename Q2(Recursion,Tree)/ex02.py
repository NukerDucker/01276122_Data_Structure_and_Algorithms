def pyramid_recursion(height: int, row: int = 0) -> str:
    if row >= height:
        return ""

    spaces = " " * (height - row - 1) * 2
    digit = str(row % 10)
    line = spaces + " ".join([digit] * (2 * row + 1))

    remaining = pyramid_recursion(height, row + 1)
    return line + ("\n" + remaining if remaining else "")

def main() -> None:
    height = int(input('Enter number of rows: '))
    print(pyramid_recursion(height))

if __name__ == '__main__':
    main()