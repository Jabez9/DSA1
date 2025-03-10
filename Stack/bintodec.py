#!/usr/bin/python3

#to convert the binary number to decimal number
# from stack import Stack

# deci = Stack()

# def b2d(mystr):
    
#     dec = 0
#     v=0
#     for i in mystr:
#         deci.push(i)

#         while not deci.is_empty:
#             n=deci.pop()
#             dec += (n*2**v)
#             n+=1
#             v+=1
#     return dec
        
    

# mystr = input("Enter a binary number: ")
# print(f"Decimal representation of {mystr} is {b2d(mystr)}")
from stack import Stack

deci = Stack()

def b2d(mystr):
    dec = 0
    v = 0

    # Push all characters to the stack
    for i in mystr:
        deci.push(int(i))  # Convert to int before pushing

    # Pop from stack and calculate decimal value
    while not deci.is_empty():  # Correct method call
        n = deci.pop()
        dec += (n * 2**v)
        v += 1  # Move to the next power of 2

    return dec

mystr = input("Enter a binary number: ")
print(f"Decimal representation of {mystr} is {b2d(mystr)}")
