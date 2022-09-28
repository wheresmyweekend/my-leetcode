class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create the hashsets for rows, cols, sections
        rows = defaultdict(set)
        cols = defaultdict(set)
        sections = defaultdict(set) # key is (r/3,c/3)

        # check each cell against hashsets
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in sections[(r//3,c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sections[(r//3,c//3)].add(board[r][c])

        return True
