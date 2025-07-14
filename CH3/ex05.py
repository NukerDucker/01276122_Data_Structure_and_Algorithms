def car_parking(s):
    instructions = s.strip().split('/')
    max_car = int(instructions[0].strip())
    parked = [int(x) for x in instructions[1].strip().split(',') if x.strip().isdigit()]
    action, car = instructions[2].strip().split()
    car = int(car)

    stack = parked.copy()

    if action == "arrive":
        if len(stack) >= max_car:
            print(f"car {car} cannot arrive : Soi Full")
            print(stack)
        elif car in stack:
            print(f"car {car} already in soi")
            print(stack)
        else:
            stack.append(car)
            print(f"car {car} arrive! : Add Car {car}")
            print(stack)
            
    elif action == "depart":
        if car not in stack:
            print(f"car {car} cannot depart : Dont Have Car {car}")
            print(stack)
        else:
            temp = []
            while stack and stack[-1] != car:
                temp.append(stack.pop())
            stack.pop()
            while temp:
                stack.append(temp.pop())
            print(f"car {car} depart ! : Car {car} was remove")
            print(stack)

def main():
    print("******** Parking Lot ********")
    usr_input = input("Enter max of car / car in soi / operation : ")
    car_parking(usr_input)

if __name__ == "__main__":
    main()