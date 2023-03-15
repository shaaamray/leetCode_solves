class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # time complexity is = O(log(m * n)) = O(logm + logn)
        # binary search time complexity is logn, so we have to use 2 binary searches here
        # first one to find the target value row, second to find the target itself

        # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

        rows, columns = len(matrix), len(matrix[0])

        top_row, bottom_row = 0, rows - 1
        while top_row <= bottom_row:
            mid_row = (top_row + bottom_row) // 2
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom_row = mid_row - 1
            else:
                break

        if top_row <= bottom_row:
            row = (top_row + bottom_row) // 2
        else:
            return False

        left = 0
        right = columns - 1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False
