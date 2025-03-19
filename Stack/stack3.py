#!/usr/bin/python3

class Stack:
    def __init__(self):
        self.items = []

    def getstack(self):
        return self.items

    def push(self,val):
        self.items.append(val)

    def isempty(self):
        return self.items == []

    def pop(self):
        if self.isempty():
            return "Empty stack"
        else:
            self.items.pop()
        
    def peek(self):
        if self.isempty():
            return "Empty stack"
        else:
            return self.items[-1]
        
stack1 = Stack()
stack1.push("A")
stack1.push("B")
stack1.push("C")
stack1.push("D")
stack1.push("E")
print(stack1.getstack())
print(stack1.isempty())
stack1.pop()
print(stack1.getstack())
print(stack1.peek())

