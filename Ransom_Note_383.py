class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # we will use Counter from collections
        # The keys in a Counter are the unique elements in the collection, and the values are the counts of each element.

        counter = collections.Counter(magazine)

        for i in ransomNote:
            if counter[i]:  # counter of element i here
                # Each letter in magazine can only be used once in ransomNote
                counter[i] = counter[i] - 1
            else:
                return False

        return True
