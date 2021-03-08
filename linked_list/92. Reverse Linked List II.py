# see the chart here: https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left==right: 
            return head
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(left-1): 
            p = p.next
        tail = p.next
        for i in range(right-left):
            temp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = temp
        return dummy.next
