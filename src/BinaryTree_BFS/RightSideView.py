"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []
"""
from collections import deque
from src.helper.create_binary_tree import list_to_tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = None
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == level_len -1:
                    res.append(node.val)
        return res

    def rightSideView2(self, root):
        if not root:
            return []
        next_level = deque()
        next_level.append(root)
        res = []
        while next_level:
            curr_level = next_level
            next_level = deque()
            while curr_level:
                node = curr_level.popleft()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(node.val)
        return res

    def rightSideView3(self, root):
        if not root:
            return []
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res

sol = Solution()
root = [1,2,3,None,5,None,4]
# root = [1,2,3,4,None,None,None,5]
# root = [1,None,3]
# root = []
print(sol.rightSideView(list_to_tree(root)))
print(sol.rightSideView2(list_to_tree(root)))
print(sol.rightSideView3(list_to_tree(root)))