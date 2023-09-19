class Solution:
    def addBinary(self, a: str, b: str) -> str:

    #### 1st Approach ####
        
        output = ''
        carry = 0

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0:
            
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            output += str(sum % 2)
            carry = sum // 2
        if carry == 1:
            output += str(carry)
            
        return output[::-1]

     #### 2nd Approach ####
        
        decimal_a = int(a, 2)
        decimal_b = int(b, 2)
        summation = decimal_a + decimal_b
        dec_to_binary = bin(summation)[2:]
        return (dec_to_binary)
