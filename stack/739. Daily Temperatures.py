class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        n= len(T)
        ans = [0] * n
        stack = []
        
        for i in reversed(range(n)):
            
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans