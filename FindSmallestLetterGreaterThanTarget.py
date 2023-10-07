#################################################  Binary Search ##########################################################
########## Time Complexity: O(logn) ########## Space Complexity: O(1) #########

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left, right = 0, len(letters) - 1
        res = letters[0]

        while left <= right:

            mid = (left + right) // 2

            if ord(letters[mid]) == ord(target):
                left = mid + 1
            
            if ord(letters[mid]) > ord(target):
                res = letters[mid]
                right = mid - 1

            if ord(letters[mid]) < ord(target):
                left = mid + 1

        return res
