numbers = [5, 0, 4, 1, 3,5]

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


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#first element
print(matrix[0][0])
#second element
print(matrix[0][1])

#list methods
numbers.append(20)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(5)
print(numbers)
#numbers.clear() removes all elements
numbers.pop()
print(numbers)
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)



