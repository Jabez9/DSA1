#!/usr/bin/python3
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):

        new_node = Node(data)
        while self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head= new_node


    def insertafter(self,prev,data):
        if not prev:
            print(f"Previous node {prev} does not exist")
            return

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def delete_val (self,key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None

    def delpos(self,pos):
        if pos < 0:
            print("Negative indices not allowed.")
            return
        if self.head:
            cur_node = self.head
            if pos == 0:
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
            print("The index is out of range")
            return
        
        prev.next = cur_node.next
        cur_node = None

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        print(f"The lenght of this linked list is {count}.")



    def printlist(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

l = LinkedList()


l.append(20)
l.append(30)
l.append(50)
l.printlist()

l.insertafter(30,40)
l.printlist()
l.prepend(10)
l.printlist()



