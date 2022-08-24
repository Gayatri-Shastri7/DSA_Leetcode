# BFS --> Queue
# left, right, top, bottom 
# if its not possible to rot an orange ; return -1
# 


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh, rotten = set(), deque()

        # iterate through the grid to get all the fresh and rotten oranges
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if we see a fresh orange, put its position in fresh
                if grid[row][col] == 1:
                    fresh.add((row, col))

                # if we see a rotten orange, put its position in rotten
                elif grid[row][col] == 2:
                    rotten.append((row, col))

        minutes = 0
        while fresh and rotten:

            minutes += 1

            # iterate through rotten, popping off the (row, col) that's currently in rotten
            # we don't touch the newly added (row, col) that are added during the loop until the next loop
            for rot in range(len(rotten)):
                row, col = rotten.popleft()

                for direction in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if direction in fresh:
                        # if the (row, col) is in fresh, remove it then add it to rotten
                        fresh.remove(direction)
                        # we will perform 4-directional checks on each (row, col)
                        rotten.append(direction)

        # if fresh is not empty, then there is an orange we were not able to reach 4-directionally    
        return -1 if fresh else minutes

        # Time Compelxity: O(m * n)
        # Space Complexity: O(m * n)