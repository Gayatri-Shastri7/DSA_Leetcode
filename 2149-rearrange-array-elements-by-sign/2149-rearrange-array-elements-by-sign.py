class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        newArray = [0] * len(nums)
        i, j = 0, 1
        for num in nums:
            if num > 0:
                newArray[i] = num
                i += 2
            else:
                newArray[j] = num
                j += 2
                
        return newArray      
  