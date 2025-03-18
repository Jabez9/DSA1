#!/usr/bin/python3
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        cur_node = self.head 
        while cur_node:
            print(cur_node.data, end="->" if cur_node.next else "\n")
            cur_node = cur_node.next

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = None
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def findnode(self,value):
        cur_node = self.head
        while cur_node :
            if cur_node.data == value:
                return cur_node
            cur_node = cur_node.next
        else:
            return None
        
    def insertafter(self,prev,key):
        prev = self.findnode(prev)
        

        if not prev:
            print("The previous node does not exist.")

        else:
            new_node = Node(key)
            new_node.next = prev.next
            prev.next = new_node

    def delval(self,val):
        # deleting if it is head
        cur = self.head
        if cur and cur.data ==  val:
            self.head = cur.next
            cur = None
            return
        
        prev = None
        while cur and cur.data != val:
            prev = cur
            cur = cur.next
            
        
        if cur is None:
            print("Previous key to delete does not exist.")

        else:
            prev.next = cur.next
            cur = None

    def delpos(self, pos):
        if pos < 0:
            print("Negative indices not allowed")

        if self.head:
            cur = self.head
            if pos == 0:
                self.head = cur.next
                cur = None

        count = 0
        prev = None
        while cur and count != pos:
            prev = cur
            count += 1
            cur = cur.next

        if  cur is None:
            print("The position is out of scope.")

        else:
            prev.next = cur.next
            cur = None

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next
            print(f"The length of this linked list is {count}")

    def lenght_rec(self, node):
        if node is None:
            return 0
        else:
            return 1+(self.lenghtrec(node.next))



