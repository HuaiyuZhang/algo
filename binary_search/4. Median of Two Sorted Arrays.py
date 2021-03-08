class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m = len(nums1), len(nums2)
        if n > m:
            n, m, nums1, nums2 = m, n, nums2, nums1   
        
        if (n+m) % 2 == 0:
            oddeven = "even"
        else:
            oddeven = 'odd'
            
        for i in range(n+1):
            j = int((m+n+1)/2 - i)
           
            max_left_1 = float('-inf') if i == 0 else nums1[i-1]
            max_left_2 = float('-inf') if j == 0 else nums2[j-1]
            min_right_1 = float('inf') if i == n else nums1[i]
            min_right_2 = float('inf') if j == m else nums2[j]
            
            if max_left_1 <= min_right_2  and max_left_2 <= min_right_1:
                if oddeven == 'odd':
                    return max(max_left_1, max_left_2)
                elif oddeven == 'even':
                    return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2))/2.0
        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            n, m, nums1, nums2 = m, n, nums2, nums1
        odd = ((m+n)%2==1)
        l = 0
        r = n
        while l <= r:
            # i is the mid of the first array search, j is the mid of the second array search.
            i = (l + r) // 2
            j = (m + n + 1)//2 - i
            max_left_1 = float('-inf')  if i == 0 else nums1[i-1]
            max_left_2 = float('-inf')  if j == 0 else nums2[j-1]
            min_right_1 = float('inf')  if i == n else nums1[i]
            min_right_2 = float('inf')  if j == m else nums2[j]
            
            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if odd:
                    return max(max_left_1, max_left_2)
                else:
                    return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2))/2.0
            elif max_left_1 > min_right_2:
                r = i - 1
            else:
                l = i + 1