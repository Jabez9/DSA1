#!/usr/bin/python3

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def findnode(self,input):
        cur = self.head
        while cur:
            if cur.data == input:
                return cur
            cur = cur.next
        else:
            return None
    
    def insertafter(self,prev,new):
        prev = self.findnode(prev)
        if not prev:
            print(f"The previous node \n{prev}\n does not exist." )

        else:
            new_node = Node(new)
            new_node.next = prev.next
            prev.next = new_node

    def delnode(self,key):
        # if self.head is what we want to remove
        cur = self.head
        if cur.next and cur.data == key:
            self.head = cur.next
            cur = None 
            return
        
        prev = None
        while cur.next and cur.data != key:
            prev = cur
            cur = cur.next
        
        if cur is None:
            return
        
        prev = cur.next
        cur = None


    def printlist(self):
        cur = self.head
        while cur:
            print(cur.data, end="->" if cur.next else "\n")
            cur = cur.next


ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
ll.printlist()
ll.prepend("1")
ll.insertafter("D", "2")
ll.printlist()

print(ll.findnode("t"))