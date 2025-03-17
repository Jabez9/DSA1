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
    def delval(self,val):
        #for the case of the head
        cur_node = self.head
        if cur_node and cur_node.data == val:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.data != val:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            print("The value to delete does not exist.")
            return
        
        prev.next = cur_node.next
        cur_node = None

    def delpos(self,pos):
        if pos<0:
            print("Invalid position: Negative indices not allowed.")
            return
        
        if self.head:
            cur_node = self.head
            if pos ==0:
                self.head = cur_node.next
                cur_node = None
                return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next 
            count += 1   

        if cur_node is None:
            print(f"The position \"{pos}\" is out of the scope. No changes to the linked list.")
            return

        prev.next =cur_node.next
        cur_node = None
    
    #This is iterative
    def length(self):
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        print(f"The lenght of this linked list is {count}.")
    #Recursive calling of the length
    def length_rec(self, node):
        if node is None:
            return 0
        else:
            return 1+self.length_rec(node.next)




    def printlist(self):
        cur = self.head
        while cur:
            print(cur.data , end="->" if cur.next else "\n")
            cur = cur.next


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