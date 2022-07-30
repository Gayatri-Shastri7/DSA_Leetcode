class Solution:
    def mySqrt(self, x: int) -> int:
        
#  Brute force approach : Let us consider x as 16, now to find the square root we will take 16 nos. in the array [1,2,3,4,5,6,7,8,9, ... 16] and will check 
#         if  1*1 == 16
#             2*2 == 16
#             3*3 == 16
#             4*4 == 16 -> found our answer  
        

        low = 0
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
            
                
            
        