from datetime import date
birth_year = input('What year were you born? ')



age = date.today().year - int(birth_year)

print(f'You are {age} years old.')