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
    
    def second_reply(self,name):
        self.name = name
        return f"The name is {self.name}"

# print(A.__dict__)
a = A()
print(a.greet())
# A.reply("Melvine")
print(A.reply("Melvine"))
b = a.second_reply("Braden")
print(b)
