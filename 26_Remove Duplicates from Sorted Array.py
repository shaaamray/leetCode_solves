class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k

#alternate solution; not for leetcode

nums = [1, 2, 2, 3, 4, 5, 5]
print(nums)

visited = []

for i in range(len(nums)):

    if nums[i] not in visited:
        visited.append(nums[i])
    else:
        continue

print(visited)