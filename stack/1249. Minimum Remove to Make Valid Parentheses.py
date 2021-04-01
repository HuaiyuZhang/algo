class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_item = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == '(':
                stack.append(i)
            else:
                if not stack:
                    remove_item.add(i)
                else:
                    stack.pop()
        # collect the remaining ( in the stack
        remove_item = remove_item.union(set(stack))            
        result = []
        for i in range(len(s)):
            if i not in remove_item:
                result.append(s[i])
        return "".join(result)