"""
1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
"""
from collections import defaultdict, deque


class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        routes = defaultdict(list)
        orig_routes = set()
        for a, b in connections:
            routes[a].append(b)
            routes[b].append(a)
            orig_routes.add((a,b))
        visited = [False] * n
        def dfs(node):
            visited[node] = True
            count = 0
            for neighbour in routes[node]:
                if not visited[neighbour]:
                    if (node, neighbour) in orig_routes:
                        count += 1
                    count += dfs(neighbour)
            return count
        return dfs(0)

    def minReorder2(self, n, connections):
        routes = defaultdict(list)
        orig_routes = set()
        for a, b in connections:
            routes[a].append(b)
            routes[b].append(a)
            orig_routes.add((a,b))
        visited = [0] * n
        queue = deque()
        queue.append(0)
        count = 0
        while queue:
            node = queue.popleft()
            for nei in routes[node]:
                if not visited[nei]:
                    visited[node] = 1
                    if (node,nei) in orig_routes:
                        count += 1
                    queue.append(nei)
        return count

sol = Solution()
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
n = 3
connections = [[1,0],[2,0]]
print(sol.minReorder(n, connections))
print(sol.minReorder2(n, connections))