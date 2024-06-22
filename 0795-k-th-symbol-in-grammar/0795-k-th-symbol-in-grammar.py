class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1 and k == 1: # 1st row
            return 0

        mid =  ( 2 ** (n-1) ) // 2 # mid point

        if k <= mid:
            return self.kthGrammar(n-1, k)
        else:
            return   1 - self.kthGrammar(n-1, k-mid)