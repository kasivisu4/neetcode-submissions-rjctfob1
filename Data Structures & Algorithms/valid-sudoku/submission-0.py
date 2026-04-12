class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_duplicate_values(nums):
            visited = set()
            for num in nums:
                if num == ".":
                    continue
                if num in visited:
                    return True
                visited.add(num)
            return False

        # check row/column
        for i in range(len(board)):
            if check_duplicate_values(board[i]) or check_duplicate_values(list(zip(*board))[i]):
                return False
        
        # check sub_grid
        for i in range(0,9,3):
            for j in range(0,9,3):
                values = []
                for r1 in range(i, i+3):
                    for c1 in range(j, j+3):
                        values.append(board[r1][c1])
                if check_duplicate_values(values):
                    return False
        return True