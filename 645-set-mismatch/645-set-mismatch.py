class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i<len(nums):
            j = nums[i] - 1
            if nums[i]!=nums[j]:
                nums[j],nums[i] = nums[i],nums[j]
            else:
                i+=1
        arr=[]
        for i in range(0,len(nums)):
            if nums[i]!=i+1:
                arr.append(nums[i])
                arr.append(i+1)   
        return arr

        
      
                
        
        