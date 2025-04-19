#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end ='--> ' if cur.next ==self.head else '\n')
            
            if cur.next == self.head:
                break
            cur = cur.next
    
    def prepend(self, node):
        new_node = Node(node)

        #for an empty list
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        #for a non_empty list
        cur = self.head
        while cur.next != self.head:
            cur = cur.next

        #update the pointers
        new_node.next = self.head
        self.head = new_node
        cur.next = self.head
        

    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        

        cur = self.head
        while cur.next != self.head:
                cur = cur.next
        
        cur.next = new_node
        new_node.next = self.head

    
cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()

        

                

        
            