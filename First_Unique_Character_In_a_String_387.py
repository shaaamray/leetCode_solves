class Solution:
    def firstUniqChar(self, s: str) -> int:

        my_dict = collections.defaultdict(int)

        for i in s:  # i = value
            my_dict[i] += 1

        for j, i in enumerate(s):  # j = index, i = value in enumerate
            if my_dict[i] == 1:
                return j

        return -1
