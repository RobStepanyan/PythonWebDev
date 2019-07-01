"""
 Create three new objects(dogs), each with a different age, and
 determine the oldest dog
"""
class Dog:
    oldest = 0
    oldest_name = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        if age > Dog.oldest:
            Dog.oldest = age
            Dog.oldest_name = name


jake = Dog("Jake", 7)
doug = Dog("Doug", 9)
william = Dog("William", 5)

print(f"The oldest dog is {Dog.oldest_name}. It is {Dog.oldest} years old.")
# The oldest dog is Doug. It is 9 years old


"""
Instance Methods

Instance methods are defined inside a class and are used to get the contents of an instance. 
They can also be used to perform operations with the attributes of our objects. 
Like the __init__ method, the first argument is always self:
"""


class Animal:

    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age

    def description(self):
        print(f"{self.name} is a {self.type}, and its age is {self.age}.")

    def speak(self, sound):
        print(f"{self.name} says: {sound}.")

puss_in_boots = Animal("cat", "Puss_in_boots", 2)

puss_in_boots.description()
puss_in_boots.speak("Meow")
# Puss_in_boots is a cat, and its age is 2.
# Puss_in_boots says: Meow.