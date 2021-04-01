class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        item_remove = set()
        stack = []
        
        for i, c in enumerate(S):
            if c == "(":
                if not stack:
                    item_remove.add(i)
                stack.append(i)
            else:
                # handle the ")"
                if len(stack) == 1:
                    item_remove.add(i)
                stack.pop()     

        result = []
        for i, c in enumerate(S):
            if i not in item_remove:
                result.append(c)
        return ''.join(result)
                
                
# solution 2
# using "balance"
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        balance = 0
        i = 0
        for j in range(len(S)):
            if S[j] == "(":
                balance += 1
            elif S[j] == ")":
                balance -= 1
            if balance == 0:
                result.append(S[i+1 : j])
                i = j + 1
        return ''.join(result)
        