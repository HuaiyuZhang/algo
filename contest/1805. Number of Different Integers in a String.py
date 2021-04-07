class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        res = []
        for c in word:
            if '0' <= c <= '9':
                res.append(c)
            else:
                res.append(' ')
        new_s = ''.join(res)
        
        return len(collections.Counter(map(int, new_s.split())))