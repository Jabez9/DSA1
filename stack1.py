#!/usr/bin/python3

class Stack1():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items
    
s = Stack1()
s.push("A")
s.push("B")
s.push({"A":1, "B":2})
s.push([1,2,3])
s.peek()
print(s.get_stack())
