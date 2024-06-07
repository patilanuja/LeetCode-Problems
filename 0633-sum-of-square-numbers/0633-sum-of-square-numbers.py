class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(sqrt(c))

        if high**2 == c:
            return True

        while low <= high:

            exp = low**2 + high**2

            if exp < c:
                low += 1

            elif exp > c:
                high -= 1

            else:
                return True

        return False 