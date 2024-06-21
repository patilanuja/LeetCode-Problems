class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return arr
        
        res = [-1] * n
        
        # Start from the second last element and move to the left
        max_from_right = arr[-1]
        for i in range(n - 2, -1, -1):
            res[i] = max_from_right
            if arr[i] > max_from_right:
                max_from_right = arr[i]
        
        return res
            
