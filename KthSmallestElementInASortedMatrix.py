################################################# Binary Search ##########################################################
########## Time Complexity: O(n*log(max-min)) ########## Space Complexity: O(1) ##########

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        lo, hi = matrix[0][0], matrix[-1][-1]
   
        def findIndex(matrxi, val):

            count = 0
            row, col = 1, len(matrix[0])

            while row < len(matrix) + 1 and col > 0:

                if matrix[row - 1][col - 1] >= val:
                    col -= 1
                else:
                    count += col
                    row += 1

            count += 1
            return count

        while lo < hi:

            mid = (lo + hi) // 2

            if findIndex(matrix, mid) > k:
                hi = mid
            else:
                lo = mid + 1

        if findIndex(matrix, lo) <= k:
            return lo
        
        return lo - 1