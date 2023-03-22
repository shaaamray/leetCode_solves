class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        div = 1
        while x >= 10* div:
            div *= 10

        while x:
            right = x % 10
            left = x // div
            
            if right != left:
                return False
            x = x % div # remove left digit
            x = x // 10 # remove right digit
            div = div / 100
        return True
            
