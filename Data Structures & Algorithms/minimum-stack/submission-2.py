class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk= []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.minStk:
            val = min(val, self.minStk[-1])
        self.minStk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.minStk.pop()
        

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]
