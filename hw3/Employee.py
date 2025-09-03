# Ethan Westenskow

# Create a class called Employee with attributes name and salary. 
# Implement a method within the class that increases the salary of the employee by a given percentage. 
# Instantiate an object of the Employee class with name = "John" and salary = 5000, increase the salary by 10%, and print the updated salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_ten(self):
        self.salary = self.salary * 1.1
        return self.salary 

John = Employee("John", 5000)
print(John.increase_ten())


# ChatGPT session transcript (Problem 2: Employee)
#
# Me: Let's move onto problem 2.
# ChatGPT: Broke it down — create class with name & salary, add a method to raise salary 
#          by percentage, test with John at 5000 salary and raise by 10%.
#
# Me: First attempt:
#   class Employee:
#       def __init__(self, name, salary):
#           self.name = name
#           self.salary = salary
#       def increase_ten(self):
#           return salary * 1.1
#   John = Employee("John", 5000)
#   print(increase_ten.John())
# ChatGPT: Explained issues — needed to use `self.salary` not `salary`, update the attribute 
#          permanently, and call method with `John.increase_ten()` not flipped syntax.
#
# Me: Fixed version:
#   def increase_ten(self):
#       self.salary = self.salary * 1.1
#       return self.salary
#   John = Employee("John", 5000)
#   print(John.increase_ten())
# ChatGPT: ✅ Correct — raises salary to 5500.0 and prints it.
#
# Me: Asked: why does `self.salary = self.salary * 1.1` update permanently?
# ChatGPT: Explained that `self.salary` is stored on the object, so once reassigned, 
#          the object remembers the new value until changed again.
