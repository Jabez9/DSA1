#!/usr/bin/python3

class STC:
    def __init__(self):
        self.stack = []



    def isempty(self):
        return self.stack == []
    
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        return "Stack is empty"
    def peek(self):
        if not self.isempty():
            return self.stack[-1]
        return "Stack is empty"
        
    def getstack(self):
        return self.stack

stack1 = STC()

stack1.push("A")
stack1.push("b")
stack1.push("C")
stack1.push("d")
stack1.pop()
print(stack1.isempty())
print(stack1.getstack())
