class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(-1, head)
        while head:
            # if the replicate occurs
            if head.next and head.next.val == head.val:
                # send the head to the last occurence of replicate
                while head.next and head.next.val == head.val:
                    head = head.next
                prev.next = head.next
                head = head.next
            else:
                prev = prev.next
                head = head.next
        return dummy.next
                