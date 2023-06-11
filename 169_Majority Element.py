class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majorElement = 0
        for i in nums:
            if count == 0: #if count is 0; we need to assign new major element
                majorElement = i
            if majorElement == i:
                count += 1
            else:
                count -= 1
        return majorElement
