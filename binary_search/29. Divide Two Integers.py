class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        index = 1
        max_divisor = divisor
        while (max_divisor<<1) <= dividend:
            max_divisor <<= 1
            index <<= 1
        output = 0
        while max_divisor >= 1:
            if dividend >= max_divisor:
                dividend -= max_divisor
                output += index
            max_divisor >>= 1
            index >>= 1
        output *= sign
        return max(min(output, 2**31-1), -2**31)