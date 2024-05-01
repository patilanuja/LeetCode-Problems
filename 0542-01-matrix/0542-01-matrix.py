class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        height = len(mat)
        width = len(mat[0])
        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for row in range(height):
            for col in range(width):
                if mat[row][col] == 0:
                    q.append((row,col))
                else:
                    mat[row][col] = inf


        while q:
            cur_row, cur_col = q.popleft()

            for dr, dc in directions:
                new_row, new_col = cur_row + dr, cur_col + dc

                if (new_row in range(height)) and (new_col in range(width)) and mat[new_row][new_col] > mat[cur_row][cur_col]:
                    mat[new_row][new_col] = mat[cur_row][cur_col] + 1
                    q.append((new_row,new_col))

        return mat