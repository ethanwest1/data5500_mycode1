# import numpy as np

# name = "Andy"
# age = 44
# major = ["cs", "finance", "data"]
# grades = [93.4, 95.5, 89.5, 98.5]

# def calc_avg_grade(grades):
#     return np.mean(grades)

# print("andy's grades: ", calc_avg_grade)

# print(id(name))
# name = 35

# print(id(name))

# name = "andy"
# print(id(name))




## Example of class and object from ChatGPT ##
# Define a class
class Dog:
    # (init) = Constructor method (runs when a new Dog object is created) 
    def __init__(self, name, age):
        self.name = name   # assign dog's name
        self.age = age     # assign dog's age

    # Method for barking
    def bark(self):
        print(f"{self.name} says woof!")

# Create an object (an instance of Dog)
my_dog = Dog("Buddy", 3)

# Call different methods
my_dog.bark()         # Output: Buddy says woof!

your_dog = Dog("Winnie", 5)
your_dog.bark()
