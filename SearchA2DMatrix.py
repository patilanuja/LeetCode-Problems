################################################# Binary Search ##########################################################
########## Time Complexity: O(log(m*n)) ########## Space Complexity: O(1) ##########
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row, col = 1, len(matrix[0])

        while row < len(matrix) + 1 and col > 0:

            if matrix[row - 1][col - 1] == target:
                return True

            elif matrix[row - 1][col - 1] > target:
                col -= 1
            
            else:
                row += 1
                
        return False