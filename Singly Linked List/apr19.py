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
            print(cur.data, end= "-->" if cur.next else '\n')
            cur = cur.next

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count+=1
            cur =cur.next
            return count
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head :
            self.head = new_node

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def find_node(self, data):
        cur = self.head
        while cur:
            if cur and cur.data ==data:
                return cur
            cur = cur.next

    def insert_after(self,node1, node2):
        prev = self.find_node(node1)
        
        if not prev:
            print(f"The previous node {node1} does not exist.")
        
        new_node = Node(node2)
        new_node.next = prev.next
        prev.next = new_node

    def del_by_position(self, pos):
        if not self.head:
            print("Empty linked list")
            return
        if pos < 0:
            print ("Invalid position, only positive indices are allowed.")
            return
        count = 0
        prev = None
        cur = self.head
        if pos == 0:
            self.head = cur.next
            cur = None

        while cur and count< pos:
            prev = cur
            count +=1
            cur = cur.next
        
        if not prev:
            print("The index is out of range.")
        
        prev.next = cur.next
        cur = None # can be assumed

    
    def del_by_value(self, val):
        if not self.head:
            print("Empty linked list.")
        
        prev = None
        cur = self.head

        while cur:
            if cur.data != val:
                prev = cur
            cur = cur.next
        
        if not prev:
            print(f"The value {val} is not part of the linked list")

        prev.next = cur.next

    
    def swap_nodes(self, node1, node2):
        if node1 != node2:
            return
        

        prev1 = None
        curr1 = self.head

        while curr1 and curr1.data != node1:
            prev1 = curr1
            curr1 = curr1.next

        
        prev2 = None
        curr2 = self.head 

        while curr2 and curr2.data != node2:
            prev2 = curr2
            curr2 = curr2.next
  
        if not prev1 and not prev2:
            print("Either of the nodes do not exist.")
            return
        

        if not prev1:
            curr2 = self.head
        else:
            prev1.next = curr2
        
        if not prev2:
            curr1 = self.head
        else:
            prev2.next = curr1
        
        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp

    def remove_duplicate(self):
        if not self.head:
            return
        cur = self.head
        duplicates = set()
        prev = None

        while cur:
            if cur.data  in duplicates:
                prev.next = cur.next
            
            else:
                duplicates.add(cur.data)
                prev = cur

            cur = cur.next


    def palindrome(self) -> bool:
        if not self.head:
            print("Empty linked list")
            return
        
        s = []
        cur = self.head

        while cur:
            s.append(cur.data)
            cur = cur.next

        cur = self.head
        while cur:
            if s.pop != cur.data:
                return False
            cur = cur.next

        return True
    

    def rotate(self, k):
        if  self.head and self.head .next:
            p = self.head
            q = self.head
            count = 0
            prev = None

        while p  and count< k:
            prev = p
            p = p.next 
            q = q.next 
            count +=1 
        
        p = prev

        while q:
            prev = q
            q = q.next

        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

    def get_nth_to_last(self, n):
        p = self.head 
        q= self.head

        if n >= 0:
            count = 0
            while p and count < n:
                p = p.next 
                count += 1

            if not p:
                print(n, " is not part of the list.")
                return
            
            else:
                while p:
                    p = p.next
                    q = q.next

                while q:
                    print(q.data, end= '-->' if q.next else '\n')
                    q = q.next

        else:
            print('n should be a positive integer.')

    def get_nth_from_last(self, n):
        p= self.head
        q = self.head

        if n >= 0:

            while p:
                count += 1
                if count >= n :
                    break
                p = p.next

            if not p:
                print(n, "is not in the range of the list.")
            
            while q and p.next:
                q = q.next
                p = p.next
            
            print(q.data)
        
        else:
            return "Invalid n"
                





    
    def move_tail_to_head(self):





        
        




