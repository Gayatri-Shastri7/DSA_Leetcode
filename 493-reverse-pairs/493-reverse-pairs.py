class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        sorted_arr = []
        for i in range( len(nums)-1, -1, -1):
            x = nums[i]//2
            if( x == nums[i]/2 ):
                x -= 1
            
            insertion_index_of_number_less_than_half = bisect.bisect_right(sorted_arr, x)
            res += insertion_index_of_number_less_than_half
            insertion_index = bisect.bisect_left(sorted_arr, nums[i])
            sorted_arr.insert(insertion_index, nums[i])
        return res
