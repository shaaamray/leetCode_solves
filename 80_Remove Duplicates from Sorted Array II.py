class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        if k < 3:
            return k
        i, j = 1, 2
        while j < k:
            if nums[j] != nums[i - 1]:
                i += 1
            nums[i] = nums[j]
            j += 1
        return i + 1

#do it with for loop also