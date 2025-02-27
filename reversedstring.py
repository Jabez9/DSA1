#!/usr/bin/python3
# input_str = "Educative"
# print(input_str[::-1])

from stack import Stack

stack = Stack()

def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    # for x in input_str:
    #     stack.push(x)
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str

input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))