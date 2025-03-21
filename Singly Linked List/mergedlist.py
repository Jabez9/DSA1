#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printlist(self):
        cur = self.head

        while cur:
            print(cur.data,end="-->" if cur.next else "\n")
            cur = cur.next
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next :
            last_node = last_node.next
        last_node.next = new_node

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def findnode(self,key):
        cur = self.head
        while cur:
            if cur.data == key:
                return cur
            cur = cur.next
        return None
    
    def insertafter(self,prev, key):
        prev = self.findnode(prev)

        if not prev:
            print("The previous node does not exist.")
            return
        
        else:
            new_node = Node(key)
            new_node.next = prev.next
            prev.next = new_node
    
    def delbyval(self,val):
        cur = self.head
        if cur and cur.data == val:
            cur.next = self.head
            cur = None
            return
        
        prev = None
        while cur and cur.next != val:
            prev = cur
            cur = cur.next

        if not prev:
            print(f"The value {prev} does not exist.")

        prev.next = cur.next
        cur = None

    def delbypos(self,pos):
        if pos <  0 :
            print("No negative values are not allowed.")
            return
        
        cur = self.head
        if cur:
            if pos == 0:
                self.head = cur.next
                cur = None
        
        prev = None
        count = 0
        while cur and pos < 0:
            prev = cur
            count+= 1
            cur = cur.next

        if not prev:
            print(f"The position {pos} is out of range.")

        prev.next = cur.next
        cur = None

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count+=1
            cur = cur.next
        return count
    
    def lengthrec(self,node):
        if node is None:
            return 0
        return 1+self.lengthrec(node.next)
        
    def swapnodes(self,node1,node2):
        if node1 == node2:
            return
        if self.head is None:
            print("Linked list is empty")

        prev1 = None
        curr1 = self.head

        while curr1 and curr1.data != node1:
            prev1 = curr1
            curr1= curr1.next

        prev2 =  None
        curr2 = self.head
        while curr2 and curr2.data != node2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return "Either of the nodes does not exists"
        
        if not prev1:
            self.head = curr2
        prev1.next = curr2

        if not prev2:
            self.head = curr2
        prev2.next = curr1

        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur,prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

            return _reverse_recursive(cur,prev)
        
        self.head = _reverse_recursive(cur = self.head , prev = None)
        

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.reverse_recursive()

llist.printlist()
print("--------------------")
llist.reverse_iterative()
llist.printlist()
print("----------------------")
llist.swapnodes("B", "C")
llist.printlist()
print("----------------------")
print(llist.length())
