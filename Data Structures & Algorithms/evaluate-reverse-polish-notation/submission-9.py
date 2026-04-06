class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        operator = '+-*/'

        for token in tokens:
            if token in operators:
                if token == operators[0]:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    expression = a + b
                    stack.append(expression)
                elif token == operators[1]:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    expression = a - b
                    stack.append(expression)
                elif token == operators[2]:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    expression = a * b
                    stack.append(expression)
                else:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    expression = a / b
                    stack.append(expression)
            else:
                stack.append(int(token))
        return int(stack.pop())
