#!/usr/bin/python3
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        cur = Node(data)
        if self.head is None:
            self.head = cur
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = cur

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def findnode(self,key):
        cur = self.head
        while cur:
            if cur.data == key:
                return cur
            cur = cur.next
        else:
            return None
        
    def insertafter(self,prev,key):
        prev = self.findnode(prev)
        if not prev:
            print(f"The previous node \"{prev}\" does not exist")
        
        else:
            new_node = Node(key)
            new_node.next = prev.next
            prev.next = new_node
    
    #deleting by value
    def delnode(self,val):
        #for the case of the head
        cur = self.head

        if cur and cur.data == val:
            self.head = cur.next
            cur = None
            return
        
        prev = None
        while cur and cur.data != val:
            prev = cur
            cur = cur.next

        if cur is None:
            print("The value to delete does not exist.")
            return
        
        prev.next = cur.next
        cur = None

    def printlist(self):
        cur = self.head
        while cur:
            print(cur.data , end="->" if cur.next else "\n")
            cur = cur.next

    
