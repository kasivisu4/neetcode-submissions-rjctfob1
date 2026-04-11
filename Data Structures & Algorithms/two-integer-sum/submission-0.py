class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {} # key = ele, val = index
        for i, v in enumerate(nums):
            other_num = target - v
            if other_num in prev:
                return [prev[other_num], i]
            prev[v] = i
        return [-1, -1]