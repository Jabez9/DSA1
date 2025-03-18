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
            print(cur.data, end="-->" if cur.next else "\n")
            cur = cur.next

    def append(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            return
        
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def prepend(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def findnode(self, value):
        cur = self.head
        while cur:
            if cur.data == value:
                return cur
            cur = cur.next
        else:
            return None
        
    def insertafter(self,prev,key):
        prev = self.findnode(prev)

        if not prev:
            print ("The previous node does not exists")

        else:
            new_node = Node(key)
            new_node.next = prev.next
            prev.next = new_node
            
    def delval(self,val):
        # if the head node
        cur = self.head 
        if cur and cur.data == val:
            self.head = cur.next
            cur = None
            return
        
        else:
            prev = None
            while cur and cur.data != val:
                prev = cur
                cur = cur.next

            if cur is None:
                print("The value to delete does not exist.")

            else:
                prev.next = cur.next
                cur = None

    def delpos(self,pos):
        if pos < 0:
            print("No negative index allowed")
            return

        cur = self.head

        if self.head is None:
            print("Empty list")
            return

        if pos == 0:
            self.head = cur.next
            cur = None
            return

        prev  = None
        count = 0

        while cur and count < pos:
            prev = cur
            count +=1
            cur = cur.next
        
        if cur is None:
            print("The position to delete is out of range")
            return

        
        prev.next = cur.next
        cur = None

    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        print(f"The length of the linked list is {count}")

    def length_rec( self, node):
        if node is None:
            return 0
        return 1+self.length_rec(node.next)
    

    def swapnodes(self, node1, node2):
        if node1 == node2 :
            return
        
        if self.head is None:
            print("The list is empty")
            return
        
        #finding node1
        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != node1:
            prev1 = curr1
            curr1 = curr1.next
        
        #checking for node2
        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != node2:
            prev2 = curr2
            curr2 = curr2.next

        # if either does not exists 
        if not curr1 or not curr2:
            return
        
        # if they are found , we move on to this
        #node one is the head, update head to node2
        if prev1 is None:
            self.head = curr2

        else:
            prev1.next = curr2

        #if node2 is the head , update head to node1
        if prev2 is None:
            self.head = curr1
        
        else:
            prev2.next = curr1

        # curr1.next, curr2.next = curr2.next, curr1.next
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
llist.delval("D")
llist.printlist()
print("-----------------------")
llist.delpos(1)
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




        
    
    
        