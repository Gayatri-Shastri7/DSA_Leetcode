class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance=[float('inf')]*n
        distance[k-1]=0
        visited=[False]*n
        heap=[(0,k-1)]
        adj=defaultdict(list)
        for u,v,w in times:adj[u-1].append((v-1,w))
        while heap:
            mi,u=heapq.heappop(heap)
            visited[u]=True
            for v,w in adj[u]:
                if not visited[v]:
                    if mi+w<distance[v]:
                        distance[v]=mi+w
                        heapq.heappush(heap,(mi+w,v))
        ans=max(distance)
        #print(distance)
        #print(adj)
        return ans if ans!=float('inf') else -1