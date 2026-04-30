class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}': '{', ']': '[', ')': '('}
        stack = [] # only to store opening brackets

        for c in s:
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop() # use closing bracket to pop corresponding opening bracket
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False