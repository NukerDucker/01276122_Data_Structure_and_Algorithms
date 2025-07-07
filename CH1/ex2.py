def wind_classification(wind_speed):
    if 0 <= wind_speed <= 51.99:
        return "Breeze"
    elif 52.00 <= wind_speed <= 55.99:
        return "Depression"
    elif 56.00 <= wind_speed <= 101.99:
        return "Tropical Storm"
    elif 102.00 <= wind_speed <= 208.99:
        return "Typhoon"
    elif 209 <= wind_speed:
        return "Super Typhoon"
    
def main():
    print(' *** Wind classification ***')
    wind_speed = float(input("Enter wind speed (km/h) : "))
    classification = wind_classification(wind_speed)
    if classification:
        print(f"Wind classification is {classification}.")

if __name__ == "__main__":
    main()