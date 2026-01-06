"""
547. Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""
from collections import deque
class Solution(object):
    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] and not visit[i]:
                self.dfs(i, isConnected, visit)
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        size = len(isConnected)
        visit = [False] * size
        num_of_prov = 0
        for i in range(size):
            if not visit[i]:
                num_of_prov += 1
                self.dfs(i, isConnected, visit)
        return num_of_prov

    def bfs(self, node, isConnected, visit):
        queue = deque()
        visit[node] = True
        queue.append(node)
        while queue:
            node = queue.popleft()
            for i in range(len(isConnected)):
                if isConnected[node][i] and not visit[i]:
                    queue.append(i)
                    visit[i] = True


    def findCircleNum2(self, isConnected):
        size = len(isConnected)
        visit = [False] * size
        num_of_prov = 0
        for i in range(size):
            if not visit[i]:
                num_of_prov += 1
                self.bfs(i, isConnected, visit)
        return num_of_prov

sol = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(sol.findCircleNum(isConnected))
print(sol.findCircleNum2(isConnected))