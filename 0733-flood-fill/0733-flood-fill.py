class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # DFS

        height = len(image)
        width = len(image[0])
        starting_pixel = image[sr][sc]
        self.dfs(sr, sc, image, color, starting_pixel, height, width)
        return image

    
    def dfs(self, sr, sc, image, color, starting_pixel, height, width):

        # base condition
        if (sr not in range(height)) or (sc not in range(width)) or image[sr][sc] == color or image[sr][sc] != starting_pixel:
            return

        image[sr][sc] = color

        self.dfs(sr+1, sc, image, color, starting_pixel, height, width) # right
        self.dfs(sr-1, sc, image, color, starting_pixel, height, width) # left
        self.dfs(sr, sc+1, image, color, starting_pixel, height, width) # down
        self.dfs(sr, sc-1, image, color, starting_pixel, height, width) # up