class Solution:
    def reinitializePermutation(self, n: int) -> int:
        A = list(range(n))
        init = A[:]
        counter = 0
        while A != init or counter == 0:
            A = [A[int(n / 2 + (i - 1) / 2)] if i%2 else A[int(i/2)] for i in range(n)]
            counter += 1
        return counter