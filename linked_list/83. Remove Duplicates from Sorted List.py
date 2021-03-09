# one pointer jump
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p = head
        while p.next:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head

# recursive
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val != head.next.val:
            return head
        else:
            return head.next