class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
            
        ans = 1
        i = n
        current_product = x
        while i > 0:
            if i % 2 == 1:
                ans *= current_product
            current_product *= current_product
            i //= 2
        return ans
               