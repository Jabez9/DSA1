#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end="-->" if cur.next else "\n")
            cur = cur.next
        return
    
    def length_iterative(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return f"The length of the linked list recursively is {count} "
    
    def length_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1+ self.length_iterative(node.next)
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next :
            last_node = last_node.next
        last_node.next = new_node

    def append(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def findnode(self, value):
        cur = self.head
        while cur:
            if cur.data == value:
                return cur
            cur = cur.next
        return
    
    def insert_after(self,prev,key):
        prev = self.findnode(prev)

        if not prev:
            print(f"The previous node {prev } does not exist")
           
        else:
            new_node = Node(key)
            new_node.next = prev.next
            prev.next = new_node
    

    def delbypos(self, pos):
        if pos < 0:
            print("The negative indices are not allowed.")

        if self.head is None:
            print("The linked list is empty")

        curr = self.head
        if curr:
            if pos == 0:
                self.head = curr.next
                return
        
        count = 0
        prev = None
        while curr and count < pos:
            prev = curr
            curr= curr.next
            count+= 1

        if prev:
            print(f"The position {pos} is out of range")

        else:
            prev.next = curr.next
            curr = None

    def delbyvalue(self,val):
        curr = self.head

        if not curr:
            print("Empty list.")
            return
        
        if curr and curr.data == val:
            self.head = curr.next
            curr = None
            return
        
        prev = None
        while curr and curr.data != val:
            prev = curr
            curr = curr.next

        if not prev:
            print(f"The node of value{val} does not exist.")

        prev.next = curr.next
        curr = None

    def swapnodes(self,node1,node2):
        if node1 == node2:
            return
        
        curr1 = self.head
        prev1 = None

        while curr1 and curr1.data != node1:
            prev1 = curr1
            curr1 = curr1.next

        
        curr2 = self.head 
        prev2 = None

        while curr2 and curr2.data != node2:
            prev2 = curr2
            curr2 = curr2.next

        
        if not curr1 or not curr2:
            print("Either of the nodes , does not exist.")
            return
        
        if not prev1:
            self.head = curr2
        prev1.next = curr2

        if not prev2:
            self.head = curr1
        prev2.next = curr1

        # if prev2:
        #     prev2.next = curr1
        # else:
        #     self.head = prev2

        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp


    def print_helper(self,node,name):
        if node is None:
            return "None"
        else:
            return name, ":", node


    def reverse_iterative(self):
        curr = self.head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            self.print_helper(prev, "PREV")
            self.print_helper(curr, "CURR")
            self.print_helper(temp,"TEMP")
            print("\n")
            prev = curr
            curr = temp
        self.head = prev


