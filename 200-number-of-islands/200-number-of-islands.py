class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def erase(i, j) -> None:
            grid[i][j] = "0"
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for move in moves:
                next_i = i + move[0]
                next_j = j + move[1]
                if 0 <= next_i < h and 0 <= next_j < w and grid[next_i][next_j] == "1":
                    erase(next_i, next_j)

        h = len(grid)
        w = len(grid[0])
        island_num = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    island_num += 1
                    erase(i, j)

        return island_num
