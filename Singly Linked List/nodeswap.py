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
            return

        if self.head is None:
            print("The list is empty.")
            return

        
        cur = self.head

        if pos == 0:
            self.head = cur.next
            cur = None
            return

        count = 0
        prev = None
        while cur and count < pos:
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

    def length_rec(self, node):
        if node is None:
            return 0
        else:
            return 1+(self.length_rec(node.next))
        

    def swapnodes(self,node1,node2):

        if node1 == node2:
            return

        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != node1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != node2:
            # prev2,curr2 = curr2,curr2.next
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return
        
        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2
        
        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        temp = curr1.next
        curr1.next = curr2.next 
        curr2.next = temp

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
print("-----------------------")
llist.printlist()
print("-----------------------")  
llist.swapnodes("E","F")
llist.printlist()
print("-----------------------") 
llist.swapnodes("F", "E")
llist.printlist()


