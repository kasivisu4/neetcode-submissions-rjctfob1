class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = [] # monotonically_decreasing
        for i in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                top = stk.pop()
                res[top] = i - top
            stk.append(i)
        return res

