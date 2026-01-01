"""
1372. Longest ZigZag Path in a Binary Tree

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
"""

"""
Algorithm:
1. Initialize the maximum path length variable to 0
2. Declare a function dfs which accepts node, isleft, steps as input parameters
3. inside the function, if the node is empty, return
4. Calculate the max path length till that node.
5. If isleft is true, call the dfs function again on node.left child, False and steps + 1
6. Onde the dfs call finishes, call the dfs function again on node.right child, True, 1
7. If isleft is False, call dfs function on node.left child, False, 1
8. call dfs on node.right, True, steps + 1
9. Outside dfs function, call the dfs function on root, True, 0
10. Return max path length
"""
from src.helper.create_binary_tree import list_to_tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.path_len = 0
        def dfs(node, goleft, steps):
            if not node:
                return
            self.path_len = max(self.path_len, steps)
            if goleft:
                dfs(node.left, False, steps + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.left, False, 1)
                dfs(node.right, True, steps + 1)
        dfs(root, True, 0)
        return self.path_len

sol = Solution()
root = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1]
root = [1,1,1,None,1,None,None,1,1,None,1]
root = [1]
print(sol.longestZigZag(list_to_tree(root)))