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
            print (cur.data, end='-->' if cur.next else "\n")
            cur = cur.next

    def length_iterative(self) -> int:
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        return cur
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def find_node(self,node):
        if not self.head:
            return f"Empty linked list, '{node}' is therefore not part of the list"
        else:
            cur = self.head
            while cur:
                if cur.data == node:
                    return cur
                cur = cur.next
            return
        

    def insert_after(self,prev, data):
        prev = self.find_node(prev)
        if not prev:
            print("Previous node does not exist.")
        
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    
    def del_by_position(self, pos):
        if not self.head:
            print("Empty linked list")
            return
        
        if pos < 0:
            print("Invalid Position !!")
            return
        
        if pos == 0:
            self.head = cur.next
            return        
        
        cur = self.head
        prev = None
        count = 0
        while cur and count < pos:
            prev = cur
            cur = cur.next
        
        if not cur:
            return f"The position '{pos}' is out of range."
        
        prev.next = cur.next
        cur = None # this is optional


    def del_by_value(self, val):
        if not self.head:
            return "Emtpy linked list"
        
        cur = self.head

        if self.head:
            if self.head.data == val:
                self.head = cur.next

        prev = None
        while cur and cur.data != val:
            prev = cur
            cur = cur.next

        if not cur:
            print(f"The value {val} is not part of the list.")

        prev.next = cur.next

    
    def swap_nodes(self, node1, node2):
        if node1 == node2:
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

        if not curr2 or not curr1:
            return ("Either of the nodes does not exist.")
        

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1


        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp

    
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next= prev
            prev=cur
            cur = nxt
        self.head = prev

    def count_occurence(self, node) -> int:
        count = 0
        cur = self.head
        while cur:
            if cur.data == node:
                count +=1

            cur = cur.next
        
        return  count
    

    def palindrome(self) -> bool:
        cur = self.head
        palindrome_list = []

        while cur:
            palindrome_list.append(cur.data)
            cur = cur.next

        cur = self.head
        while cur:
            if palindrome_list.pop() != cur.data:
                print("Linked list is not a palindrome.")
                return False
            cur = cur.next
        return True

    def remove_duplicates(self):
        cur = self.head

        if not cur:
            return "Empty linked list."
        
        dup_values = dict()
        prev = None
        while cur:
            if cur and cur.data in dup_values:
                prev.next = cur.next
                cur = prev.next

            else:
                dup_values[cur.data] = True
                prev = cur
                cur = prev.next
    
    def get_nth_from_last(self, n):
        p = self.head
        q = self.head

        if n > 0:
            count += 1
            while count >= n:
                break
            p = p.next

            if not p:
                print(f"'{n}' is not in the part of the list.")
                return
            
            else:
                while q and p.next:
                    p = p.next
                    q = q.next
                print(q.data)
        else:
            return 'Invalid n.'
        
    
    def rotate(self, k):
        p = self.head
        q = self.head
         
        pass

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q :
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next

            else:
                s = q
                q = s.next

            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = s
                s = p
                p = s.next

            else:
                s.next = s
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p
            
        self.head = new_head
        return self.head
                





            












                  
            
            

        

        




            
                



