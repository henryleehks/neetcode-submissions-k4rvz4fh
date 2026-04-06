class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                expression = a + b
                stack.append(expression)
            elif token == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                expression = a - b
                stack.append(expression)
            elif token == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                expression = a * b
                stack.append(expression)
            elif token == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                expression = a / b
                stack.append(expression)
            else:
                stack.append(int(token))
        return int(stack.pop())
