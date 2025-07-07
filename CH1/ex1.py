pi = 3.14159
def area_of_circle(radius):
    return pi * radius ** 2

def main():
    radius = float(input("r : "))
    area = area_of_circle(radius)
    print(f"Area={area}")
    
if __name__ == "__main__":
    main()