def gcd(a, b):
    if a == 0:
        return abs(b)
    return gcd(b % a, a)

def main():
    usr = input("Enter Input : ")
    a, b = map(int, usr.split()) 
    if a == 0 and b == 0:
        print("Error! must be not all zero.")
        return
    
    larger, smaller = max(a, b), min(a, b)

    result = gcd(abs(larger), abs(smaller))
    print(f"The gcd of {larger} and {smaller} is : {result}")
    
if __name__ == "__main__":
    main()