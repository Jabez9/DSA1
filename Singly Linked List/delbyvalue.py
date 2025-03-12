#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def find_node(self, value):
        """Find a node by its value and return the node object."""
        cur_node = self.head
        while cur_node:
            if cur_node.data == value:
                return cur_node  # Return the node object if found
            cur_node = cur_node.next
        return None  # Return None if not found


    def insert_after_node(self, prev_node, data):
        prev_node = self.find_node(prev_node)
        if not prev_node:
            print("Previous node does not exist.")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

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


llist = LinkedList()

llist.append("B")
llist.append("C")
llist.append("E")
llist.print_list()
print("---------------------")
llist.prepend("A")
llist.print_list()
print("---------------------")
llist.insert_after_node("C", "D")
llist.print_list()
print("---------------------")
llist.delete_node("B")
llist.delete_node("E")

llist.print_list()
print("---------------------")

print("Onto the second object")

l = LinkedList()


l.append(20)
l.append(30)
l.append(50)
l.print_list()
print("---------------------")
l.insert_after_node(60,40)
l.print_list()
print("---------------------")
l.prepend(10)
l.print_list()