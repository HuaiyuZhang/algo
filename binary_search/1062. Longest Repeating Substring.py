class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        def f(s, length):
            seen = set()
            for l_end in range(len(s) - length + 1):
                r_end = l_end + length
                h = hash( s[l_end:r_end]) # reduce memory use
                if h in seen:
                    return True
                else:
                    seen.add(h)
            return False
            
            
        l = 0
        r = len(S) - 1
        while l < r:
            mid = l + int((r - l + 1) / 2)
            if f(S, mid):
                l = mid
            else:
                r = mid - 1
        return l