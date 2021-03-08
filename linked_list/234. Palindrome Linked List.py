# recursive: O(n) time O(n) space
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front = head
        
        def check(current):
            if current:
                # recursive call will dig to the last node.
                # at the end, current is null, return True
                
                # if any step not satisfy the matching, return False till the bottom of the call stack
                if not check(current.next):
                    return False
                # check condition
                if self.front.val != current.val:
                    return False
                # move the pointer at the front.
                self.front = self.front.next
            return True
                
        return check(head)

# two-pointers: O(n) time, O(1) space
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = curr2 = head
        # curr moves 1 step each time, curr2 moves 2 steps.
        while curr2 and curr2.next:
            curr = curr.next
            curr2 = curr2.next.next
        # if length is odd, curr is at the center, eg, 1,2,3,2,1, curr is at 3
        # if length is even, curr is at the head of second half, eg, 1,2,3,4,2,1, curr is at 4
        
        # a standard reverse linked list code for the second half
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # the second half has been reversed, prev is the head of the second half
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

# hash
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        seed = 3
        hash1 = hash2 = 0
        h = 1
        
        while head!=None:
            hash1 = hash1 * seed + head.val
            hash2 = hash2 + head.val * h
            h *= seed
            head = head.next
        return hash1 == hash2