class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) 
        left_border, right_border = -2147483648, 2147483647
        dividend, divisor = abs(dividend), abs(divisor)
        
        """
        Instead of dividing, we will subtract to the maximum of divisor
        """
        
        res = 0
        while dividend >= divisor:

            divisor_cp, divisor_cnt = divisor, 1
            while dividend >= divisor_cp:
                dividend -= divisor_cp
                res += divisor_cnt
                divisor_cnt <<= 1 # divisor_cnt *= 2
                divisor_cp <<= 1
    
        if is_negative:
            res = -res
        
        return min(max(left_border, res), right_border)