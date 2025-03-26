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
        if not cur:
            print("Empty list")
            return
        while cur:
            print(cur.data, end="-->" if cur.next else "\n")
            cur = cur.next
        
    
    def length_iterative(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count
    
    def length_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1+ self.length_iterative(node.next)
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next :
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def findnode(self, value):
        cur = self.head
        while cur:
            if cur.data == value:
                return cur
            cur = cur.next
        return
    
    def insert_after(self,prev,key):
        prev = self.findnode(prev)

        if not prev:
            print(f"The previous node {prev } does not exist")
           
        else:
            new_node = Node(key)
            new_node.next = prev.next
            prev.next = new_node
    

    def delbypos(self, pos):
        if pos < 0:
            print("The negative indices are not allowed.")

        if self.head is None:
            print("The linked list is empty")

        curr = self.head
        if curr:
            if pos == 0:
                self.head = curr.next
                return
        
        count = 0
        prev = None
        while curr and count < pos:
            prev = curr
            curr= curr.next
            count+= 1

        if prev:
            print(f"The position {pos} is out of range")

        else:
            prev.next = curr.next
            curr = None

    def delbyvalue(self,val):
        curr = self.head

        if not curr:
            print("Empty list.")
            return
        
        if curr and curr.data == val:
            self.head = curr.next
            curr = None
            return
        
        prev = None
        while curr and curr.data != val:
            prev = curr
            curr = curr.next

        if not prev:
            print(f"The node of value{val} does not exist.")

        prev.next = curr.next
        curr = None

    def swapnodes(self,node1,node2):
        if node1 == node2:
            return
        
        curr1 = self.head
        prev1 = None

        while curr1 and curr1.data != node1:
            prev1 = curr1
            curr1 = curr1.next

        
        curr2 = self.head 
        prev2 = None

        while curr2 and curr2.data != node2:
            prev2 = curr2
            curr2 = curr2.next

        
        if not curr1 or not curr2:
            print("Either of the nodes , does not exist.")
            return
        
        if  prev1 is None:
            self.head = curr2
        else:
            prev1.next = curr2

        if  prev2 is None:
            self.head = curr1
        else:
            prev2.next = curr1


        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp


    def print_helper(self,node,name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":", node.data)


    def reverse_iterative(self):
        curr = self.head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            self.print_helper(prev, "PREV")
            self.print_helper(curr, "CURR")
            self.print_helper(temp,"TEMP")
            print("\n")
            prev = curr
            curr = temp
        self.head = prev

    def merged_list(self, llist2):
        p = self.head
        q = llist2.head
        s = None

        if not p:
            return q
        if not q:
            return  p
        
        if p and q:
            if p.data <= q.data:
                s= p
                p = s.next
            
            else:
                s= q
                q = s.next
            
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    # def remove_duplicates(self):
    #     dup_values = dict()  # Dictionary to track seen values
    #     curr = self.head
    #     prev = None

    #     while curr:
    #         if curr.data in dup_values:
    #             # Remove the duplicate node
    #             prev.next = curr.next
    #             curr = None  # Free memory (optional in Python)
    #         else:
    #             dup_values[curr.data] = 1  # Mark value as seen
    #             prev = curr  # Move prev forward
            
    #         curr = prev.next  # Move curr forward (fixes bug)


    def remove_duplicates(self):
        if self.head is None:
            print("Empty linked list")
            return
        
        dup_values = dict()  # Dictionary to store seen values
        curr = self.head  # Start from the head
        prev = None  # Previous node tracker

        while curr:
            if curr.data in dup_values:
                # Duplicate found, remove the node
                prev.next = curr.next  # Skip the duplicate node
                curr = curr.next  # Move to the next node
            else:
                dup_values[curr.data] = 1  # Mark value as seen, I can also use true or even None, as this ensures the key:value is already in the dictionary
                prev = curr  # Move previous pointer forward
                curr = curr.next  # Move current pointer forward

    # def print_nth_to_last(self,n, method):
    #     # method 1 is mostly useful for a doubly linked list 
    #     if method == 1:
    #         total_len = self.length_iterative()

    #         cur = self.head

    #         while cur:
    #             if total_len == n:
    #                 print(cur.data)
    #                 return cur.data
    #             total_len -=1
    #             cur = cur.next

    #         if cur is None:
    #             return
            

    #     elif method ==2:
    #         p = self.head
    #         q = self.head

    #         if n >0:
    #             count = 0
    #             while q:
    #                 count += 1
    #                 if (count>= n):
    #                     break
    #                 q = q.next

    #             if not q:
    #                 print(str(n) + ' is greater than the number of nodes in the list.')  
    #                 return
                
    #             while p and q.next:
    #                 p = p.next
    #                 q = q.next

    #             return p.data
    #         else:
    #             return None
            
    def get_nth_to_last(self,n):
        p = self.head
        q = self.head

        if n > 0:
            count = 0
            while q:
                count +=1
                if count >= n:
                    break
                q = q.next

            if not q:
                print(str(n) + " is greater than the number of nodes in the list")
                return
            
            while p and q:
                p = p.next 
                q = q.next
            return p.data
        else:
            return None
            #will return this if the value entered is out of range
     
    def count_occurences(self, node):
        curr = self.head
        count = 0
        while curr:
            if curr.data == node:
                count += 1
            curr = curr.next
            
        return f"The node '{node }' appears '{count}' times in the  linked list."

    # def countocc_rec(self,node,data):
    #     if not node:
    #         return 0
    #     if node.data == data:
    #         return 1+self.countocc_rec(node.next,data)
    #     else:
    #         return self.countocc_rec(node.next,data)

    #ROTATING A LIST
    def rotate(self,k):
        if k > self.length_iterative():
            print(f"{k} exceeds the size of the linked list")
            return
        
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

        while p and count  < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev

        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None


    #IS PALINDROME
    # def is_palindrome1(self):
    #     #soln one
    #     s = ''
    #     p = self.head
    #     while p:
    #         s += p.data
    #         p = p.next
    #     return ''.join(s) == ''.join(s[::-1])
    
    def is_palindrome2(self):
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next

        
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next

        return True
    
    # def is_palindrome3(self):
    #     if self.head :
    #         p = self.head
    #         q = self.head
    #         prev = []

    #         i = 0
    #         while q:
    #             prev.append(q)
    #             q = q.next
    #             i += 1
    #         q = prev[i-1]

    #         count = 1

    #         while count <= i//2 + 1:
    #             if prev[-count].data != p.data:
    #                 return False
    #             p = p.next
    #             count +=1

    #         return True
    #     else:
    #         return True
    
    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head 
            second_to_last = None
            while last.next:
                second_to_last = last
                last = last.next
            last.next = self.head 
            second_to_last.next = None 
            self.head = last



llist_1 = LinkedList()
llist_2 = LinkedList()
llist_3 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(5)
llist_1.append(10)

print("------------------")
llist_1.reverse_iterative()
llist_1.print_list()
print("--------------------")
llist_1.swapnodes(10, 1)
llist_1.print_list()
print("-----------------")
llist_1.remove_duplicates()
llist_1.print_list()
print("------------------------")
print(llist_1.get_nth_to_last(8))
print("-----------------")
print(llist_1.get_nth_to_last(4))
print("-----------------")
llist_1.append(5)
print(llist_1.count_occurences(5))
# print(llist_1.countocc_rec(llist_1.head, 5))
print('----------------------------')
llist_3.append(1)
llist_3.append(2)
llist_3.append(3)
llist_3.append(4)
llist_3.append(5)
llist_3.rotate(2)
llist_3.print_list()

print('---------------')
print('------------------')
llist4 = LinkedList()

llist4.append(1)
llist4.append(2)
llist4.append(1)
llist4.append('cat')
llist4.prepend('cat')
print(llist4.is_palindrome2())
llist4.print_list()
llist4.move_tail_to_head()
llist4.print_list()