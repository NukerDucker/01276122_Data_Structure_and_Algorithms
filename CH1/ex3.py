def summation_of_each_digits(n):
    return sum(int(digit) for digit in str(n))

def main():
    print(' *** Summation of each digit ***')
    n = int(input("Enter a positive number : "))
    result = summation_of_each_digits(n)
    print(f"Summation of each digit =  {result}")
    
if __name__ == "__main__":
    main()