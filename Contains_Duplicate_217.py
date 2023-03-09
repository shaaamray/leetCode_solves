class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = dict()
        for i in nums:
            if not i in dic:
                dic[i] = 1
            else:
                return True
        return False
