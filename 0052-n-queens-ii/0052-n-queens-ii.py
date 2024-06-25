class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diagonals, antidiagonals):
            if row == n:
                return 1

            solutions = 0
            for col in range(n):
                curr_diagonal = row - col
                curr_antidiagonal = row + col

                if col in cols or curr_diagonal in diagonals or curr_antidiagonal in antidiagonals:
                    continue

                cols.add(col)
                diagonals.add(curr_diagonal)
                antidiagonals.add(curr_antidiagonal)

                solutions += backtrack(row+1, cols, diagonals , antidiagonals)

                cols.remove(col)
                diagonals.remove(curr_diagonal)
                antidiagonals.remove(curr_antidiagonal) 

            return solutions

        return backtrack(0, set(), set(), set())
