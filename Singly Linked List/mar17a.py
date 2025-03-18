#!/usr/bin/python3

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        cur = self.head 
        while cur:
            print(cur.data, end="->" if cur.next else "\n")
            cur = cur.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def findnode(self,key):
        cur = self.head
        while cur:
            if cur.data == key:
                return cur
        return None
    
    def insertafter(self,prev,key):
        prev = self.findnode(prev)
        if not prev:
            print(f"The value \"{prev}\" does not exist.")

        else:
            new_node = Node(key)
            new_node.next = prev.next
            prev.next = new_node

    def delval(self,value):
        cur = self.head
        if cur and cur.data ==value:
            self.head = cur.next
            cur = None
            return

        prev = None
        while cur and cur.data != value:
            prev =  cur
            cur = cur.next


        if cur is None:
            print("The value to delete does not exist.")
        else:
            prev.next = cur.next
            cur = None

    def delpos(self,pos):
        if pos < 0:
            print("Negative indices not allowed")
            return
        
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None

        count = 0
        prev = None
        while cur_node and count != pos:
            prev = cur_node
            count +=1
            cur_node = cur_node.next

        if cur_node is None:
            print(f"The position {pos} is out or range.")

        else:
            prev.next = cur_node.next
            cur_node = None

    def length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count +=1
            cur_node = cur_node.next

    def length_rec(self, node):
        if node is None:
            return 0
        else:
            return 1 +self.length_rec(node.next)

llist = LinkedList()
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("G")
llist.printlist()
print("-----------------------")
llist.insertafter("E", "F")
llist.printlist()
print("-----------------------")
llist.prepend("A")
llist.printlist()
print("-----------------------")
llist.delval("A")
llist.printlist()
print("-----------------------")
llist.delpos(6)
llist.printlist()
print("-----------------------")
llist.length()
print("-----------------------") 
print(f"The length by recursive counting is {llist.length_rec(llist.head)}.")

            

