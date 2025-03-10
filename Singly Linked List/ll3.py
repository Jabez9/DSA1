#!/usr/bin/python3
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        node1 = Node(val)
        if self.head is None:
            self.head = node1
        return
    
#this is for an empty list


