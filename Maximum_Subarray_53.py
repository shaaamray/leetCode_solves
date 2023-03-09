class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # float('-inf') is the lowest possible number in python
        current_max_sum, overall_max_sum = 0, float('-inf')

        for i in nums:
            current_max_sum = max(current_max_sum+i, i)
            overall_max_sum = max(overall_max_sum, current_max_sum)

        return overall_max_sum
