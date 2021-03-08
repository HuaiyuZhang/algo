class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        running = head = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                running.next = l1
                l1 = l1.next
            else:
                running.next = l2
                l2 = l2.next
            running = running.next
        if l1:    
            running.next = l1 
        if l2:
            running.next = l2 
        return head.next