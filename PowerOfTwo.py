class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Approach 1 (Time complexity: O(log n), Space Complexity: O(log n))
        # if n == 1:
        #     return True
        # elif n % 2 != 0 or n == 0:
        #     return False
        # else:
        #     return self.isPowerOfTwo(n/2)

        # Approach 2 (Time complexity: O(log n), Space Complexity: O(1))
        # if n == 0:
        #     return False
        # while n % 2 == 0:
        #     n /= 2
        # return n == 1 


        # Approach 3 (Time complexity:O(1) , Space Complexity:O(1)) 
        # Bitwise operation:  n & (-n) gives rightmost 1-bit.
         """Intuition: In binary representation, a power of two is one 1-bit followed by some zeros (example: 1 = 0001, 2 = 0010, 4 = 0100, 8 = 1000, 16 = 00010000) and any other number which is not a power of two, has more that 1-bit in its binary representation (example: 5 = 0101, 6 = 0110, 18 = 00010010 )."""

        #  if n == 0:
        #      return False
        #  return n & (-n) == n

        # Approach 4 (Time complexity:O(1) , Space Complexity:O(1)) 
        # Bitwise operation: n & (n - 1) sets rightmost 1-bit to 0.
         """Intuition: when we substract 1 from a given number, it changes the rightmost 1-bit to 0 and to sets all the lower bits to 1. Now because of AND operator rightmost 1-bit and all the lower bits will turn 0, making ouput 0."""
         
         if n == 0:
            return False
         return n & (n - 1 ) == 0


      