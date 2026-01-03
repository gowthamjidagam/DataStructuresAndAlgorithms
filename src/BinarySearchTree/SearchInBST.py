"""
700. Search in a Binary Search Tree
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []
"""
from src.helper.create_binary_search_tree import list_to_bst
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root or root.val == val:
            return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)

    def searchBST2(self, node, val):
        while node and node.val != val:
            node = node.left if val < node.val else node.right
        return node

sol = Solution()
root = [4,2,7,1,3]
val = 2
root = [4,2,7,1,3]
val = 5
print(sol.searchBST(list_to_bst(root), val))
print(sol.searchBST2(list_to_bst(root), val))

