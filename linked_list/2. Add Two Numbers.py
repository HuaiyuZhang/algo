class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        carry = 0
        result = head = ListNode(-1)
        while p1 or p2:
            first = p1.val if p1 else 0
            second = p2.val if p2 else 0
            temp = first + second + carry
            result.next = ListNode(temp % 10)
            carry = temp // 10
            
            result = result.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        if carry > 0:
            result.next = ListNode(carry)
        return head.next
        
        