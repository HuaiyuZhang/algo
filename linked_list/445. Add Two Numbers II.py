class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return head
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        carry = 0 
        prev = None
        while l1 or l2:
            x1 = l1.val if l1 else None
            x2 = l2.val if l2 else None
            total = x1 + x2 + carry
            curr = ListNode(total % 10)
            # in the result we want the most significant digit to be presented first.
            curr.next = prev
            prev = curr
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            carry = total // 10
        if carry != 0:
            curr = ListNode(carry)
            curr.next = prev
            prev = curr

        return prev