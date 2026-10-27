#encapsulation

# class Factory:
#     __a ="Pune"
#     def show(self):
#         print(Factory.__a)
        
# obj = Factory()
# obj.show()


# Abstraction
# from abc import ABC, abstractmethod

# class Abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass
    
#     @abstractmethod
#     def area(self):
#         pass


# class Square(Abstract):
#     def __init__(self,side):
#         self.side = side
#     def perimeter(self):
#         print("i have created")
                
#     def area(self):
#         print("i have area")
            
            
# class Circle(Abstract):
#     def __init__(self,radius):
#         self.radius = radius
        
#     def perimeter(self):
#         print("i have created")
        
#     def area(self):
#         print("i have area")

# obj = Circle()
# obj1 = Square()

# Dunder Methods

# class Animal:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return("Hello how are you")
    
#     def __add__(self, other):
#         return(f"your sum of ages are {self.age + other.age}")    
        
# obj = Animal("Lion", 12)
# obj2 = Animal("dolphin", 14)
# print(obj + obj2)

