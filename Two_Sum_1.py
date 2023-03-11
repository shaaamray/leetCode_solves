class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}  # here key:value = value:index
        for i in range(len(nums)):
            find_at_hashMap = target - nums[i]
            if find_at_hashMap in hashMap:
                return (hashMap[find_at_hashMap], i)
            hashMap[nums[i]] = i
