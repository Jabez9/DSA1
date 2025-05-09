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
            print(cur.data , end='-->' if cur.next else '\n')
            cur =cur.next

    def length_iterative(self):
        count = 0
        cur = self.head

        while cur:
            count+= 1
            cur = cur.next

        return count
    

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def findnode(self,val):
        cur = self.head
        while cur :
            if cur.data == val:
                return cur
            cur = cur.next
        return None
    
    def insert_after(self,prev, node):
        prev = self.findnode(prev)

        if not prev:
            print(f"The previous node \"{prev}\" does not exist.")

        else:
            new_node = Node(node)
            new_node.next = prev.next
            prev.next = new_node
            

    def delete_by_position(self,pos):
        cur = self.head

        if pos < 0:
            print("Negative positions not allowed.")
            return
        
        if self.head is None:
            print("empty linked list")
            return
        
        if pos == 0:
            self.head = cur.next
            # cur = None
            return
        
        
        prev = None
        count = 0

        while cur and count < pos:
            prev = cur
            count += 1
            cur = cur.next

        if not cur:
            print("The position is out or range")
            return

        prev.next = cur.next
        cur = None

    def delete_by_value(self,value):
        if not self.head:
            print("The linked list is empty.")
            return
        
        cur = self.head

        if cur and cur.data == value:
            self.head = cur.next
            return
        
        prev = None
        while cur and cur.data != value:
            prev = cur
            cur = cur.next
        
        if not cur:
            print("The  node \"{value}\" is not in the linked list.")
        
        prev.next = cur.next
        cur = None

    
    def swap_nodes(self,node1,node2):
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

        if not curr1 or not curr2:
            print("Either of the nodes '{node1}' of '{node2}' does not exist.")
            return

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
        # curr1.next , curr2.next = curr2.next, curr1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next  
            cur.next = prev
            prev = cur
            cur = nxt
        
        self.head = prev


    def count_occurence(self, value):
        cur = self.head 
        count = 0
        while cur and cur.data == value:
            count += 1
            cur = cur.next
        return count
    

    def is_palindrome(self):
        cur = self.head
        stack = []
        while cur:
            stack.append(cur.data)
            cur = cur.next

        cur = self.head
        while cur:
            if cur.data != stack.pop():
                print("The linked list is not a palindrome.")
                return False
            cur = cur.next
        return True
    
    def remove_duplicate(self):
        
        cur = self.head
        if not cur:
            print("The linked list is empty.")
            return
        

        prev = None
        dup_values = dict()

        while cur:
            if cur and cur.data in dup_values:
                prev.next = cur.next
                cur = prev.next
            else:
                dup_values[cur.data] = True
                prev = cur
                cur = cur.next


    def find_nth_from_last(self, n):
        total = self.length_iterative()

        cur = self.head
        while cur:
            if total == n:
                print(cur.data)
                return cur.data
            total -=1
            cur = cur.next

        if not cur:
            return
        
    def get_nth_from_last(self,n):
        p = self.head
        q = self.head

        if n > 0:
            count = 0
            while p:
                count +=1
                if count >= n:
                    break
                p = p.next

            if not p:
                print(n, " is not in the range of the list")
                return
            
            else:
                while q and p.next:
                    q = q.next
                    p  = p.next
                print(q.data)

        else:
            return "Invalid n"
        

    def get_nth_to_last(self,n):
        p = self.head
        q = self.head

        if n > 0:
            count = 0
            while p and count < n: #move p exactly n steps ahead
                p = p.next
                count +=1

            if not p:
                print(n, " is not in the range of the list")
                return
            
            else:
                while p: # mv p and q together
                    q = q.next
                    p  = p.next
            
                while q:
                    print(q.data, end="-->" if q.next else "\n")
                    q = q.next
                print() 

        else:
            return "Invalid n"
        
    def print_nth_to_last(self, n):
        p = self.head
        count = 0

        # Move p to the nth index position
        while p and count < n:
            p = p.next
            count += 1

        # If n is out of range
        if not p:
            print(n, "is out of the range of the list")
            return

        # Print from the nth node to the last
        while p:
            print(p.data, end=" --> " if p.next else "\n")
            p = p.next


    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
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
            if p.data <= q.data :
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
    
    def rotate(self,k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

        while p and count < k:
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
        p.next =  None

    def move_tail_to_head(self):
        
        if not self.head or not  self.head.next :
            return
        
        prev = None
        p = self.head

        while p.next :
            prev = p
            p = p.next

        prev.next = None
        p.next = self.head
        self.head = p




        
        
    

        


llist = LinkedList()
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("G")
llist.print_list()
print("-----------------------")
llist.prepend("A")
llist.print_list()
print("-------------------")
llist.insert_after("A", "B")
llist.print_list()
print("-----------------")
llist.delete_by_position(9)
llist.print_list()
print("------------------")
llist.delete_by_value("A")
llist.print_list()
print("------------------------")
print("Swapping of nodes")
llist.swap_nodes("B", "D")
llist.print_list()

print("------------------------")
llist.append("B")
llist.print_list()
print("------------------------")
llist.remove_duplicate()
llist.print_list()
print("------------------------")
llist.append("E")
llist.append("B")   
llist.append("C")
llist.append("D")
print("------------------------")
llist.print_list()
print("------------------------")
if llist.is_palindrome():
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
print("------------------------")
llist.print_list()
print('------------------------------')
llist.find_nth_from_last(4)
print('--------------------------')
llist.get_nth_from_last(4)
print("--------------------")
llist.get_nth_to_last(4)
print("--------------------")
llist.print_nth_to_last(3)
print('-------------------')
llist1 = LinkedList()
llist1.append(1)
llist1.append(2)
llist1.append(3)            
llist1.append(4)
llist1.append(5)
llist1.append(6)
print('-------------')
llist1.print_list()
llist1.rotate(1)
print('-------------')
llist1.print_list()
print('--------------------')
llist1.move_tail_to_head()
llist1.print_list()


            

        

