# LOGIC: We are supposed to find the first and last index of the array             

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        start = 0
        end = len(nums)-1
        ans =[-1,-1]
        while(start <= end):            
            mid = start + (end - start) // 2
            if nums[mid] == target:
                i = mid 
                j = mid 
                while i >= 0 and nums[mid] == nums[i]: i -= 1
                while j < n and nums[mid] == nums[j]: j+= 1
                return [i+1,j-1]

            elif target < nums[mid]: end = mid-1
            else: start = mid + 1 
        return [-1,-1]

