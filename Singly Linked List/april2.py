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
            print (cur.data, end='-->' if cur.next else "\n")
            cur = cur.next

    def length_iterative(self) -> int:
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        return cur
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def find_node(self,node):
        if not self.head:
            return f"Empty linked list, '{node}' is therefore not part of the list"
        else:
            cur = self.head
            while cur:
                if cur.data == node:
                    return cur
                cur = cur.next
            return
        

    def insert_after(self,prev, data):
        prev = self.find_node(prev)
        if not prev:
            print("Previous node does not exist.")
        
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    
    def del_by_position(self, pos):
        if pos < 0:
            print("Invalid Position !!")
            return
        
        cur = self.head
        prev = None
        count = 0

        while cur and count < pos:
            if pos == 0:
                self.head = cur.next
                return
            
            prev = cur
            


            
                



