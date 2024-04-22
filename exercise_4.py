weight = float(input("Enter weight: "))

unit = input("(L)bs or (K)g: ").lower()

if unit == "l" :
    weight = weight * 0.45
    print(f"Weight in kg: {weight}")
elif unit == "k":
    weight = weight / 0.45
    print(f"Weight in lbs: {weight}")