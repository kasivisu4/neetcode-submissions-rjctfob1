class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        distinct = set(nums)
        for num in nums:
            if num - 1 not in distinct:
                curr_streak = 1
                curr_num = num

                while curr_num + 1 in distinct:
                    curr_num += 1
                    curr_streak += 1
                max_length = max(max_length, curr_streak)

        return max_length