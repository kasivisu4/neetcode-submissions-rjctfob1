class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                
                box_location = (i //3 , j //3)
                if val in rows[i] or val in cols[j] or val in boxes[box_location]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_location].add(val)
        return True