#!/usr/bin/python3


from stack import Stack

binary = Stack()


def d2b(n):
    while n > 0:
        rem = n % 2
        binary.push(rem)
        n = n // 2

    bin_str = ""
    while not binary.is_empty():
        bin_str += str(binary.pop())

    return bin_str

n =int(input("Enter a decimal number: "))

d2b(n)
print(f"Binary representation of {n} is {d2b(n)}")