#!/usr/bin/python3
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
        
    
#     def append(self,data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return
        
#     #appending the new node to the empty linked list

class Node:
    def __init__(self, data):
        self.data = data  # Stores the actual data
        self.next = None  # Stores a reference to the next node

# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking nodes
node1.next = node2  # node1's "next" stores a reference to node2
node2.next = node3
print(node1.data)    # 10
print(node1.next)    # Memory reference to node2
print(node1.next.data)  # 20
print(node1.next.next.data)
