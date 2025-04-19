class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        postivediag = set()  # row + column 
        negativediag = set()  # row - column 
        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in postivediag or (r-c) in negativediag:
                    continue

                col.add(c)
                postivediag.add(r+c)
                negativediag.add(r-c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                postivediag.remove(r+c)
                negativediag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return result
