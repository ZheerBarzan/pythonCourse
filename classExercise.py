class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")




person1 = Person("Zheer", 23)

person1.talk()