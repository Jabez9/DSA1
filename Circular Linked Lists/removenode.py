#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # def print_list(self):
    #     cur = self.head
    #     while cur:
    #         print(cur.data , end='--> ' if cur.next else '\n')
    #         if cur.next == self.head:
    #             break
    #         cur = cur.next
    def print_list(self):
        if not self.head:
            print("List is empty.")
            return

        cur = self.head
        while True:
            # Print the current node's data
            print(cur.data, end=' -> ')

            # Move to the next node
            cur = cur.next

            # Break if we've returned to the head (end of the circular list)
            if cur == self.head:
                break

        # Print the head node again to show the circular connection
        print(self.head.data, end=' (circular)\n')
    
    def prepend(self, node):
        new_node = Node(node)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return

        cur = self.head
        while cur.next != self.head:
            cur = cur.next

        new_node.next = self.head
        self.head= new_node
        cur.next = self.head

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next =self.head

        cur = self.head
        while cur.next != self.head:
            cur = cur.next

        cur.next = new_node
        new_node.next= self.head



    def remove(self,key):

        if self.head:
            if self.head.data == key:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head =self.head.next
            else:
                cur= self.head
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next

                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next

cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")

cllist.remove("A")
cllist.remove("C")
cllist.print_list()