#!/usr/bin/python3
class A:
    name = "Jabez"
    @staticmethod
    def greet():
        return "Hello"
    
    @classmethod
    def reply(cls,name):
        cls.name = name
        return f"The name is {cls.name}"

# print(A.__dict__)
a = A()
print(a.greet())
# A.reply("Melvine")
print(A.reply("Melvine"))

# class Car:
#     manufacturer = "Unknown"  # Class attribute (shared by all instances)

#     def __init__(self, brand):
#         self.brand = brand

#     @classmethod
#     def set_manufacturer(cls, name):
#         cls.manufacturer = name  # Modifies class attribute

# # Before changing
# print(Car.manufacturer)  # Output: Unknown

# Car.set_manufacturer("Toyota")

# # After changing
# print(Car.manufacturer)  # Output: Toyota

# car1 = Car("Corolla")
# print(car1.manufacturer)  # Output: Toyota (affected all instances)
