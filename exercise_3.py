import math
weightInLBS = float(input("Enter weight in pounds: "))
weightInKG = weightInLBS * 0.453592
print(f"Weight in KG: {weightInKG}")

name = "python for biginners"
print(name[1:-1])


# string methods
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
print(name.find("p"))
print(name.replace("p", "j"))
print("python" in name)
print("python" not in name)
print(len(name))
print(name.split(" "))
print(name.split("i"))

#math functions
x = 2.9
print(round(x))
print(abs(-2.9))
print(math.ceil(x))
print(math.floor(x))





