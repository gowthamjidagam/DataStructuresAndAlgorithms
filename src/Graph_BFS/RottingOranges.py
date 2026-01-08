"""
994. Rotting Oranges
You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""
from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_oranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        if fresh_oranges == 0:
            return 0
        if not queue:
            return -1
        dirs = ((1,0),(0,1),(-1,0),(0,-1))
        minutes_elapsed = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_row, curr_col = queue.popleft()
                for d in dirs:
                    next_row = curr_row + d[0]
                    next_col = curr_col + d[1]
                    if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        queue.append((next_row, next_col))
                        fresh_oranges -= 1
            minutes_elapsed += 1
        return minutes_elapsed - 1 if fresh_oranges == 0 else -1

sol = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]
print(sol.orangesRotting(grid))


