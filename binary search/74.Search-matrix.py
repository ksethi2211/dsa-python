class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        def getPosition(row: int, col: int) -> int:
            return (row * num_cols) + col
        
        def getCoordinates(position: int) -> List[int]:
            return [position // num_cols, position % num_cols]
        
        lower = getPosition(0, 0)
        upper = getPosition(num_rows - 1, num_cols - 1)

        while lower <= upper:
            mid = (lower + upper) // 2
            mid_position = getCoordinates(mid)
            mid_row = mid_position[0]
            mid_col = mid_position[1]

            if matrix[mid_row][mid_col] == target:
                return True
            if matrix[mid_row][mid_col] < target:
                lower = mid + 1
            else:
                upper = mid - 1
        
        return False