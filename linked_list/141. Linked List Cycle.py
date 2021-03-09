class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            else:
                seen.add(head)
            head = head.next
        return False
# solution 2
# two pointers. Given the presence of a cycle, fast pointer will catch the slow pointer.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        prev = head
        head = head.next
        while head != prev:
            if not head or not head.next:
                return False
            head = head.next.next
            prev = prev.next
        return True