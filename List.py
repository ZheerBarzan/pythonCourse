numbers = [5, 0, 4, 1, 3]

max = numbers[0]
min = numbers[0]

for x in numbers:
    if max < x:
        max = x
print(max)

for x in numbers:
    if min > x:
        min = x
print(min)





