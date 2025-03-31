def merge_sorted(self, llist):

    p = self.head
    q = llist.head
    s = None

    if not p :
        return q
    if not q:
        return p
    
    if p and q:
        if p.data <= q.data:
            s = p
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
        
    if not q:
        return p
    if not p:
        return q
    
    self.head = new_head
    return self.head

from mar26 import length_recursive
def find_nth_from_last(self, n):
    total = self.length_recursive()

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
            # return q.data
        
            while q:
                print(q.data, end="-->")
                q = q.next
            print() 

        
    else:
        return "Invalid n"
    

def get_nth_to_last(self,n):
    p = self.head
    q = self.head

    if n > 0:
        count = 0
        while p and count < n:
            p = p.next
            count +=1

        if not p:
            print(n, " is not in the range of the list")
            return
        
        else:
            while q and p.next:
                q = q.next
                p  = p.next
            # return q.data
        
            while q:
                print(q.data, end="-->")
                q = q.next
            print() 

    else:
        return "Invalid n"



    


        