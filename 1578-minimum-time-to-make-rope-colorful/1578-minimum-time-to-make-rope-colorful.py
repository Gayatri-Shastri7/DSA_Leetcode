class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev=0
        curr=1

        minTime=0
        while curr!=len(colors):
            if colors[curr]!=colors[prev]:
                prev=curr
                curr=curr+1
            else:
                if neededTime[prev]<neededTime[curr]:
                    minTime=minTime+neededTime[prev]
                    prev=curr
                    curr=curr+1
                else:
                    minTime=minTime+neededTime[curr]
                    curr=curr+1

        return minTime
