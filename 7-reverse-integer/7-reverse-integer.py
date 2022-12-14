class Solution:
    def reverse(self, x: int) -> int:
        number = 0
        is_neg = False
        
        if x < 0:
            is_neg = True
            x = -x

        while x:
            digit = x % 10
            number = number * 10 + digit
            x //= 10
        
        if number < -2147483648 or number > 2147483647:
            return 0
        
        if is_neg:
            return -number
        
        return number