# Count no. of components
# Use a dfs() 
# Initialize a adj list
# Convert the given adj matrix to list
# Then mark the visited array wiyj default 0
# Cnt -0
# Run a for loop, if its not visited, cnt++, dfs() 

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        
        if not M:
            return 0
        
        n = len(M)
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j]==1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visit = [False]*n
        
        def dfs(u):
            for v in graph[u]:
                if visit[v] == False:
                    visit[v] = True
                    dfs(v)
        
        count = 0
        for i in range(n):
            if visit[i] == False:
                count += 1
                visit[i] = True
                dfs(i)
        
        return count
        
