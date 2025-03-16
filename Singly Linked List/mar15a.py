#!/usr/bin/python3

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        new_node = Node(value)
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
        self.head= new_node


    def findnode(self,input):
        cur = self.head
        while cur:
            if cur.data == input:
                return cur
            cur = cur.next
        return None

    def insertafter(self,prev,data):
        prev_node = self.findnode(prev)
        if prev_node is None:
            print(f"The previous node \"{prev}\" does not exist.")

        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def delnode(self,key):
        # val = self.findnode(key)
        # if value to delete is the head
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node  = None #it is optional as Python automatically handles this in oop
            return
        
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            print(f"The target node {key} does not exists.")
            return
        else:
            prev.next = cur_node.next
            cur_node = None #optional once again
        


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
ll.prepend("1")
ll.insertafter("D", "2")
ll.printlist()



