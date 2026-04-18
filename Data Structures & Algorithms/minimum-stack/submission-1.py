class MinStack:

    def __init__(self):
        self.stk = []
        self.heap = []
        self.counter = defaultdict(int)
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        heapq.heappush(self.heap, val)
        self.counter[val] += 1

    def pop(self) -> None:
        val = self.stk.pop()
        if val in self.counter:
            self.counter[val] -= 1
        

    def top(self) -> int:
        return self.stk[-1] if self.stk else -1
        

    def getMin(self) -> int:
        while self.heap:
            top = heapq.heappop(self.heap)
            if self.counter[top] > 0:
                heapq.heappush(self.heap, top)
                return top
        return -1  
