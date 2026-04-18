class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        stk = []
        for token in tokens:
            if token in operators:
                b = int(stk.pop())
                a = int(stk.pop())
                res = 0
                if token == '+': res = a + b
                if token == '-' : res = a - b
                if token == '*' : res = a * b
                if token == '/' : res = int(a / b)
                token = res
            stk.append(int(token))
        return stk[-1]