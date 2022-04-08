class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []                             # Using heap to keep kth largest number alway at self.h[0] 
        self.k = k
        
        for n in nums:
            if len(self.h) < k:                 # Only keep k number in self.h
                heapq.heappush(self.h, n)
            elif n > self.h[0]:
                heapq.heapreplace(self.h, n)
            elif n <= self.h[0]:
                continue

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heapreplace(self.h, val)
        return self.h[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)