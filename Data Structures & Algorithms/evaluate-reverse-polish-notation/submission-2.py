import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if not c in ["+","*","-","/"]:
                stack.append(int(c))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if c == "+":
                    stack.append(op1+op2)
                elif c =="-":
                    stack.append(op1-op2)
                elif c == '*':
                    stack.append(op1*op2)
                elif c == '/':
                    stack.append(int(op1/op2))
        return stack[0]