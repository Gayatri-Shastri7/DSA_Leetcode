'''
Shortest Path in a Grid With Obstacle Elimination
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/1771716/Python-Simple-BFS 
    
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/2171080/Simplest-BFS-Approach 
    
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/2100345/Python3%3A-Customized-BFS 
    
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/1817855/Optimized-Python3-code-with-lots-of-comment-explations 
    
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/1424448/Python%3A-BFS   
'''    
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M,N=len(grid),len(grid[0])

        steps=0
        q,seen=[(0,0,0)],set()
        while q:
            for _ in range(len(q)):
                r,c,used=q.pop(0)
                if (r,c)==(M-1,N-1):
                    return steps
                for x,y in [(r-1,c),(r,c-1),(r,c+1),(r+1,c)]:
                    if 0<=x<M and 0<=y<N and (x,y,used) not in seen:
                        if grid[x][y]==0:
                            q.append((x,y,used))
                            seen.add((x,y,used))
                        elif grid[x][y]==1 and used<k:
                            seen.add((x,y,used))
                            q.append((x,y,used+1))
            steps+=1
        return -1
        