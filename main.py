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


# class Animal:
#     @property
#     def show(self):
#         print("hello how are you")

# obj = Animal()
# obj.show


# def decorater(func):
#     def wrapper(a,b):
#         print("I will print myself before the function")
#         func(a,b)
#         print("I will print after the function ")
#     return wrapper
    

# @decorater
# def addition(a,b):
#     print(f"you total is {a+b}")
# addition(12,67)

# def addtion(*args):
#     sum =0
#     for i in args:
#         sum =sum+i
#     print(sum)
# addtion(12+12+23+56+17889+13678+128663+218563+589565+56689+2659)
    
# def information(**kwargs):
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name = "rakshit" , age = 20 , designation ="AI/ML")
    
# l = [i for i in range(1,21) if i % 2 == 0]

# l = {i : i**2 for i in range(1,21)}

# l = {i**2 for i in range(1,21) if i%2==0}

# print(l)

# addtion = lambda a,b : a+b 
# print(addtion(12,13)) 

# a = [1,2,3,4,5,6,7]

# result = map(lambda x : x*2 , a) 
# print(list(result))

a = [1,2,3,4,5,6,7]

result = filter(lambda x : x / 2 , a) 
print(list(result))