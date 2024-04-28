numbers = [5, 0, 4,4,1,0, 1, 3,5,2]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
