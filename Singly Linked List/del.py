#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        node1 = Node(val)
        if self.head is None:
            self.head = node1
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node1

    def prepend(self, val):
        node1 = Node(val)
        node1.next = self.head
        self.head = node1

    def find_node(self, value):
        """Find a node by its value and return the node object."""
        cur_node = self.head
        while cur_node:
            if cur_node.data == value:
                return cur_node  # Return the node object if found
            cur_node = cur_node.next
        return None  # Return None if not found

    def insert_after_value(self, target_value, data):
        """Find a node by its value and insert a new node after it."""
        prev_node = self.find_node(target_value)  # Find the node dynamically
        if not prev_node:
            print(f"Node with value '{target_value}' not found.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printlist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" --> " if cur_node.next else "\n")
            cur_node = cur_node.next

# Example Usage
ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
# ll.prepend("1")

# # Insert dynamically without manually traversing .next
# ll.insert_after_value("1", "2")

ll.printlist()
