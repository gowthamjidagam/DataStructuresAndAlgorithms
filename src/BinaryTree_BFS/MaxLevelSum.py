"""
1161. Maximum Level Sum of a Binary Tree
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
"""
from collections import deque, defaultdict
from src.helper.create_binary_tree import list_to_tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        max_sum = float("-inf")
        level = 1
        max_sum_level = 0
        while queue:
            level_len = len(queue)
            level_sum = 0
            for _ in range(level_len):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if max_sum < level_sum:
                max_sum = level_sum
                max_sum_level = level
            level += 1
        return max_sum_level

    def maxLevelSum2(self, root):
        if not root:
            return 0
        level_sum = defaultdict(int)
        def dfs(node, level):
            if not node:
                return
            level_sum[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 1)
        max_sum = float("-inf")
        max_sum_level = 0
        for level in level_sum.keys():
            if max_sum < level_sum[level]:
                max_sum = level_sum[level]
                max_sum_level = level
        return max_sum_level

sol = Solution()
root = [1,7,0,7,-8,None,None]
# root = [989,None,10250,98693,-89388,None,None,None,-32127]
print(sol.maxLevelSum(list_to_tree(root)))
print(sol.maxLevelSum2(list_to_tree(root)))
