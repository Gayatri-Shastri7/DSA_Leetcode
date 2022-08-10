# https://leetcode.com/problems/01-matrix/discuss/1994028/Python-BFS-Simple

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = list()
        visited = dict()
        for i in range(0, m):
            for j in range(0, n):
                if mat[i][j] == 0:
                    visited[(i, j)] = True
                    queue.append((i, j))
        
        while queue:
            si, sj = queue.pop(0)
            for di, dj in [(0,-1),(-1,0),(1,0),(0,1)]:
                ni, nj = si+di, sj+dj
                if 0 <= ni < m and 0 <= nj < n:
                    if (ni, nj) not in visited:
                        visited[(ni, nj)] = True
                        queue.append((ni, nj))
                        mat[ni][nj] = mat[si][sj] + 1
        return mat