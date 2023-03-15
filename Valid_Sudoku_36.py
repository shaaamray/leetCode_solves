class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        columns = set()
        boxes = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    current_row_value = (i, board[i][j])
                    current_col_value = (j, board[i][j])
                    current_box_value = (i//3, j//3, board[i][j])
                    if (current_row_value in rows or current_col_value in columns or current_box_value in boxes):
                        return False
                    rows.add(current_row_value)
                    columns.add(current_col_value)
                    boxes.add(current_box_value)
        return True
