#Ethan Westenskow

# 1.    Create a class called Rectangle with attributes length and width. 
# Implement a method within the class to calculate the area of the rectangle. 
# Instantiate an object of the Rectangle class with length = 5 and width = 3, and print its area.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

test = Rectangle(3,5)
print(test.area())

# ChatGPT session transcript (Problem 1: Rectangle)
#
# Me: What are the basic steps for problem 1?
# ChatGPT: Define Rectangle class → init with length/width → area() method → test with Rectangle(5,3).
#
# Me: This is what I have so far:
#   class Rectangle:
#       def_init_(self, length, width):
#           self.length = length
#           self.width = width
#       def area(self):
#           area = length * width
#           return print("The area is: ", area)
#   test = Rectangle(3,5)
#   test.area()
# ChatGPT: Explained that the constructor needed `__init__` with double underscores, 
#          methods must use `self.length` and `self.width` (not bare variables),
#          and recommended returning values instead of printing inside the method.
#
# Me: How about now? (after fixing)
#   class Rectangle:
#       def__init__(self, length, width):
#           self.length = length
#           self.width = width
#       def area(self):
#           return self.length * self.width
#   test = Rectangle(3,5)
#   print(test.area())
# ChatGPT: ✅ Correct, except noted a small typo: need a space after `def`.
#
# Me: Fixed it with `def __init__`, tested again, and it worked.
# ChatGPT: Confirmed final version was correct and prints 15.
