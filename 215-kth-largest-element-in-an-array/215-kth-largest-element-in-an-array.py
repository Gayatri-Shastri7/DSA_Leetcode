
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        nums.sort(reverse=True)
        return(nums[k-1])        
        '''
#         Min Heap
    # Implementation using
    # a Priority Queue
        N=len(nums)
        pq = []
        heapq.heapify(pq)
 
        for i in range(N):
 
        # Insert elements into
        # the priority queue
            heapq.heappush(pq, nums[i])
 
        # If size of the priority
        # queue exceeds k
            if (len(pq) > k):
                heapq.heappop(pq)
 
    # Print the k largest element
        while(len(pq) != 0):
            return(heapq.heappop(pq))
 
