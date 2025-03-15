#!/usr/bin/python3
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node=last_node.next 

        last_node.next = new_node


    def prepend(self,input):
        node1 = Node(input)
        node1.next = self.head
        self.head = node1

    def findnode(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next

        return None
    
    def insertafter(self,prev,data):
        prev_node = self.findnode(prev)
        if  prev_node is None:
            print(f"The previous node \"{prev}\" does not exits")
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next= new_node

        
    def printlist(self):
        cur = self.head
        while cur:
            print(cur.data, end='-->' if cur.next else "\n")
            cur = cur.next


l = LinkedList()

l.append("B")
l.append("C")
l.append("D")
l.printlist()
print("----------------")
l.prepend("A")
l.printlist()
print("------------")
l.insertafter("D", "E")
l.printlist()
print("-----------")
# l.insertafter("F", "G")
# l.printlist()
