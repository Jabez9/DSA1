#!/usr/bin/python3
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        node1 = Node(val)
        if self.head is None:
            self.head = node1
            return
    
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node1

    def printlist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=' --> ' if cur_node.next else '\n')
            cur_node = cur_node.next


ll = LinkedList()

ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")

ll.printlist()