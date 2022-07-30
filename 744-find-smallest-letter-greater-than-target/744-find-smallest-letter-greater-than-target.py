class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

#         left, right = 0, len(letters)-1
#         while left < right:
#             mid = left + (right - left) // 2
#             if (target< letters[mid]):
#                 right = mid-1
#             else:
#                 left = mid + 1
#         return letters[left% len(letters)]

        
        start = 0
        end = len(letters)-1

        while(start <= end):            
            mid = (start + end) // 2
            mid = start + (end - start) // 2

            if (target < letters[mid]):
                end = mid - 1;
            else: 
                start = mid + 1;

        return letters[start % len(letters)];
    