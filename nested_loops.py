for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'({x},{y},{z})')



numbers = [5, 2, 5, 2, 2]

for i in numbers:
    output = ''
    for j in range(i):
        output += 'x'
    print(output)