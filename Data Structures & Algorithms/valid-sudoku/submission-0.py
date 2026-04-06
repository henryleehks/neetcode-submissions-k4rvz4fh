class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                
                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                box_key = (r // 3, c // 3)
                if box_key not in boxes:
                    boxes[box_key] = set()
                if val in boxes[box_key]:
                    return False
                boxes[box_key].add(val)
            
        return True