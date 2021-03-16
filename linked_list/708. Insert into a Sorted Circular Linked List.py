class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        new = Node(insertVal)
        if not head:
            new.next = new
            return new
        p = head
        while True:
            if p.val <= p.next.val: # not really needed
                if p.val <= insertVal and p.next.val >= insertVal:
                    break
            elif p.val > p.next.val:
                if insertVal >= max(p.val, p.next.val):
                    break
                elif insertVal <= min(p.val, p.next.val):
                    break
            p = p.next
            # this is a little tricky. 
            if p == head:
                break
        new.next = p.next
        p.next = new
        return head