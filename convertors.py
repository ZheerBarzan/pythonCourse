def kg_to_lbs(weight):
    return weight / 0.453592


def lbs_to_kg(weight):
    return weight * 0.453592


def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number> max:
            max = number
    return max

def find_min(numbers):
    min = numbers[0]
    for number in numbers:
        if number< min:
            min = number
    return min

def find_avg(numbers):
    sum = 0
    for number in numbers:
        sum+=number
    return sum/numbers.__len__()