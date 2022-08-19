'''

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5

'''
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        end = defaultdict(int)
        for num in nums:
            if counter[num]:
                counter[num] -= 1
                
                if end[num-1]:
                    end[num] += 1
                    end[num-1] -= 1
                elif counter[num+1] and counter[num+2]:
                    counter[num+1] -= 1
                    counter[num+2] -= 1
                    end[num+2] += 1
                else:
                    return False
        return True
                    
        