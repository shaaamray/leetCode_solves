class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mydict = {}
        output = []

        for i in nums1:
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] = mydict[i] + 1

        for j in nums2:
            if j in mydict and mydict[j] >= 1:
                output.append(j)
                mydict[j] = mydict[j] - 1

        return output