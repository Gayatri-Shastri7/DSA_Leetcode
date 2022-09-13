
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        [1,2,3,1] 
         0 1 2 3
         0+2 = 4
         1+3 = 3
        '''
        for i in range(1,len(nums)):
            if(i==1):
                nums[i] = max(nums[i],nums[i-1])
            else:
                nums[i]=max(nums[i]+nums[i-2],nums[i-1])
        return nums[-1]
    