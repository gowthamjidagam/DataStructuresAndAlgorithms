"""
62. Unique Paths
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

class Solution(object):
    #DFS Approach Top-Down Without memoization
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)

    #Top-up with Memoization
    def uniquePaths_TD(self, m, n):
        memo = {}
        def dfs(row,col):
            if row == 0 or col == 0:
                return 1
            if (row,col) in memo:
                return memo[(row,col)]
            memo[(row,col)] = dfs(row-1,col) + dfs(row,col-1)
            return memo[(row,col)]
        return dfs(m-1,n-1)

    #Bottom-Up
    def uniquePaths2(self, m, n):
        dp = [[1] * n for _ in range(m)]
        for col in range(1,n):
            for row in range(1, m):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[m-1][n-1]

    def uniquePaths2_BU(self, m, n):
        dp = [1] * n
        for row in range(1, m):
            for col in range(1, n):
                dp[col] += dp[col-1]
        return dp[n-1]

sol = Solution()
m = 3
n = 7
m = 3
n = 7
print(sol.uniquePaths(m,n))
print(sol.uniquePaths2(m,n))
print(sol.uniquePaths_TD(m,n))
print(sol.uniquePaths2_BU(m,n))