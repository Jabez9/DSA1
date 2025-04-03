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

        while cur.next:
            print(cur.data, end="-->" if cur.next and cur.next != self.head else "\n")
            cur = cur.next
            if cur.next == self.head:
                break
    
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node

        else:
            last = self.head
            while last.next != self.head:
                last = last.next

            new_node.next = self.head
            last.next = new_node
            self.head = new_node




