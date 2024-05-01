class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
    #     # DFS

    #     height = len(image)
    #     width = len(image[0])
    #     starting_pixel = image[sr][sc]
    #     self.dfs(sr, sc, image, color, starting_pixel, height, width)
    #     return image

    
    # def dfs(self, sr, sc, image, color, starting_pixel, height, width):

    #     # base condition
    #     if (sr not in range(height)) or (sc not in range(width)) or image[sr][sc] == color or image[sr][sc] != starting_pixel:
    #         return

    #     image[sr][sc] = color

    #     self.dfs(sr+1, sc, image, color, starting_pixel, height, width) # right
    #     self.dfs(sr-1, sc, image, color, starting_pixel, height, width) # left
    #     self.dfs(sr, sc+1, image, color, starting_pixel, height, width) # down
    #     self.dfs(sr, sc-1, image, color, starting_pixel, height, width) # up


    ## BFS

        height = len(image)
        width = len(image[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        q.append((sr,sc))
        starting_pixel = image[sr][sc]

        if starting_pixel == color:
            return image

        image[sr][sc] = color

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (new_row in range(height)) and (new_col in range(width)) and image[new_row][new_col] == starting_pixel and (new_row, new_col) not in q:

                    image[new_row][new_col] = color
                    q.append((new_row, new_col))

        return image 


