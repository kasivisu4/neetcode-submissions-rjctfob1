class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1
            heapq.heappush(heap,(-freq[num], num))
        res = []
        while k and heap:
            count, val = heapq.heappop(heap)
            if freq[val] == -count:
                res.append(val)
                k -= 1
        return res