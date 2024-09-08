class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        max_row = len(board)
        max_col = len(board[0])
        path = set()


        def dfs(row, col, curr_idx):

            if curr_idx == len(word):
                return True

            if (row not in range(max_row)) or (col not in range(max_col)) or board[row][col] != word[curr_idx] or (row, col) in path:
                return False

            path.add((row, col))
            res =  dfs(row, col-1, curr_idx+1) or dfs(row-1, col, curr_idx+1) or dfs(row+1, col, curr_idx+1) or dfs(row, col+1, curr_idx+1)
            path.remove((row,col))

            return res


        for row in range(max_row):
            for col in range(max_col):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0): return True

        return False