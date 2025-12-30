class Solution:
    def reverse(self, x: int) -> int:
        MinVal = -2**31
        MaxVal = 2**31 - 1
        
        revNum = 0
        sign = -1 if x < 0 else 1
        num = abs(x)
        
        while num != 0:
            digit = num % 10
            revNum = (revNum * 10) + digit
            num //= 10
            
        revNum *= sign
        
        if not (MinVal <= revNum <= MaxVal):
            return 0

        return revNum

 
        