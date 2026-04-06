class Solution:
    def isValid(self, s: str) -> bool:
        dict_1 = {'}' : '{', ']' : '[', ')' : '('}
        stack = []
        for c in s:
            if c not in dict_1:
                stack.append(c)
                continue
            if not stack or stack[-1] != dict_1[c]:
                return False
            stack.pop()
        return not stack 