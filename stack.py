#!/usr/bin/python3
#stack data structure

class Stack():
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

i = Stack()
i.push("A")
i.push(4)
print(i.get_stack())
i.pop()
print(i.get_stack())
print(i.peek())
print(i.is_empty())