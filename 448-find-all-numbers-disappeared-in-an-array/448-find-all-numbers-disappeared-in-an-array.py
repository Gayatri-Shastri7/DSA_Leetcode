class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i=0
        while(i<len(nums)):
            correct_id=nums[i]-1

            if nums[i]!=nums[correct_id]:
                nums[i],nums[correct_id]=nums[correct_id],nums[i]
            else:
                i=i+1
        arr=[]    
        for i in range(len(nums)):
            if i!=nums[i]-1:
                arr.append(i+1)
        return arr
    
#         n = len(nums)
#         i=0
#         while i < n: 
#             if nums[i]<n and nums[i]!=i: 
#                 s = nums[i]
#                 nums[i], nums[s] = nums[s], nums[i]
#             else:
#                 i += 1
                
#         arr=[]    
#         for i in range(len(nums)):
#             if i!=nums[i]-1:
#                 arr.append(i+1)

#         return arr
