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
            print(cur.data , end="->" if cur.next else "\n")
            cur = cur.next

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def findnode(self,key):
        cur = self.head
        # while cur:
        #     if cur.data == key:
        #         return cur
        #     cur = cur.next
        # return None
    
        while cur and cur.data != key:
            cur = cur.next
        return cur
        

    def insertafter(self,prev,key):
        prev = self.findnode(prev)

        if not prev:
            print("The previous node does not exist.")
            return
  
        else:
            new_node= Node(key)
            new_node.next = prev.next
            prev.next = new_node

    def delval(self,val):
        cur = self.head 
        if cur is None:
            print("The linked list is empty.")
            return
        
        if cur.data == val:
            self.head == cur.next
            cur = None
            return

        prev = None
        while cur and cur.data != val:
            prev = cur
            cur = cur.next

        if prev :
            print("The value does not exist")

        prev.next = cur.next
        cur = None

    def delpos(self,pos):
        if pos < 0:
            print("Negative indices not allowed")
            return
        
        cur = self.head
        if cur is None:
            print("The linked list is empty")
            return

        if pos == 0:
            self.head = cur.next
            cur = None
            return
        
        prev = None
        count = 0
        while cur and count < pos:
            prev = cur
            cur = cur.next
            count +=1
        
        if prev :
            print(f"The position {pos} is out or range.")

        prev = cur.next
        cur = None

    def length(self):
        cur = self.head
        count = 0

        while cur:
            count +=1
            cur = cur.next
            return f"The length of the linked list is {count}"
        
    def length_rec( self, node):
        if node is None:
            return 0
        return 1+self.length_rec(node.next)

    def swapnodes(self,node1, node2):
        if node1 == node2:
            return
        
        if self.head is None:
            return "The linked list is currently empty."
        
        #finding node1
        prev1 = None
        cur1 = self.head

        while cur1 and cur1.data != node1:
            prev1 = cur1
            cur1 = cur1.next

        # finding node2 
        prev2 = None
        cur2 = self.head
        while cur2 and cur2.data != node2:
            prev2 = cur2
            cur2 = cur2.next

        #either key not found
        if not cur2 or not cur1:
            print("Either of the keys does not exist.")
            return
        
        if prev1 is None:
            self.head = cur2
        prev1.next = cur2

        if prev2 is None:
            self.head = cur1
        prev2.next = cur1

        
        # if both are found 
        temp = cur1.next
        cur1.next = cur2.next
        cur2.next = temp

    def reverse_iterative(self):

        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
        self.head = prev

        

llist = LinkedList()
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("G")
llist.printlist()
print("-----------------------")
llist.insertafter("E", "F")
llist.printlist()
print("-----------------------")
llist.prepend("B")
llist.prepend("A")
llist.printlist()
print("-----------------------")
llist.delval("D")
llist.printlist()
print("-----------------------")
llist.delpos(6)
llist.printlist()
print("-----------------------")
llist.length()
print("-----------------------") 
print(f"The length by recursive counting is {llist.length_rec(llist.head)}.")
print("-----------------------")
llist.printlist()
print("-----------------------")  
llist.swapnodes("E","F")
llist.printlist()
print("-----------------------") 
llist.swapnodes("F", "E")
llist.printlist()
print("-----------------------") 
print("Reversed List")
print("               ")
llist.reverse_iterative()
llist.printlist()

def mergedsorted(self,llist):
    p = self.head
    q = llist.head
    s = None

    if not p:
        return q
    if not q:
        return p
    
    if p and q:
        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head = s
    while p and q:
        if p.data <= q.data:
            s.next = p
            s= p
            p  = s.next
        else:
            s.next = q
            s = q
            q = s.next
    if not p:
        s.next = q
    if not q:
        s.next = p
    
    self.head = new_head
    return self.head




        
    
    
        


    