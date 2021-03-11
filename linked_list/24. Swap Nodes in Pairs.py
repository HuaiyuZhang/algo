class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1, head)
        prev = dummy
        while head and head.next:
            first = head
            second = head.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
            head = prev.next
        return dummy.next

# iterative
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second