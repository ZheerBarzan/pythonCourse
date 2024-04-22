weight = float(input("Enter weight: "))

unit = input("(L)bs or (K)g: ")

if unit.lower() == "l" :
    weight = weight * 0.45
    print(f"Weight in kg: {weight}")
elif unit.lower() == "k":
    weight = weight / 0.45
    print(f"Weight in lbs: {weight}")