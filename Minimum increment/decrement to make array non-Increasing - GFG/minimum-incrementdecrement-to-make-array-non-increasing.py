#User function Template for python3
import heapq
class Solution:
    def minOperations(self,a,n):
        # code here
        heap = []
        count = 0
        for i in range(n):
            if heap and heap[0] < a[i]:
                count += a[i] - heap[0]
                heapq.heappush(heap,a[i])
                heapq.heappop(heap)
            heapq.heappush(heap,a[i])
        return count


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[int(x) for x in input().strip().split()]
        obj=Solution()
        print(obj.minOperations(a,n))


# } Driver Code Ends