class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}
        for val in arr:
            if val in freq.keys():
                freq[val] += 1
            else:
                freq[val] = 1
        
        heap = []
        for key, val in freq.items():
            heap.append((-val, key))
            
        heapq.heapify(heap)
        count, total = 0, 0
        while total<len(arr)/2:
            total += -heapq.heappop(heap)[0]
            count += 1
        return count


        # a=[]
        # for i in arr:
        #     if i not in a:
        #         a.append(i)
        # if(len(a)>=2):
        #     return(len(a)//2)
        # else:
        #     return(len(a))
