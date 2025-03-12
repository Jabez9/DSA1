#!/usr/bin/python3
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #adding an elemnt to the end of the list
    def append(self,val):
        node1 = Node(val)
        if self.head is None:
            self.head = node1
            return
    
        last_node = self.head #currently ensures that the last node is the first node
        while last_node.next: #while the last node  reference is not None
            last_node = last_node.next #it is assigned the value at the next one
        last_node.next = node1 #finally assigns the new node value of node1 to the last node for refenence
    
    #add at the beginning
    def prepend(self,val):
        node1 = Node(val) #takes a value

        node1.next = self.head #point to the next node, which should now be the self.head
        self.head = node1 #makes node1 to be self.head 

    #inserting after a node
    #first find the node
    def findnode(self, value):
        """Find a node by its value and return the node object."""
        cur_node = self.head
        while cur_node:
            if cur_node.data == value:
                return cur_node  # Return the node object if found
            cur_node = cur_node.next
        return None  # Return None if not found

        
    def insert_after_node(self, prev_node, data):
        prev_node = self.findnode(prev_node)
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node


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
ll.prepend("1")
ll.insert_after_node("D", "2")
ll.printlist()
