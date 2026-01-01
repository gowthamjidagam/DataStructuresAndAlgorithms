"""
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
"""
from collections import defaultdict
from src.helper.create_binary_tree import list_to_tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def preorder(node, curr_sum):
            nonlocal count
            if not node:
                return
            curr_sum += node.val
            if curr_sum == targetSum:
                count += 1
            count += hashmap[curr_sum - targetSum]
            hashmap[curr_sum] += 1
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            hashmap[curr_sum] -= 1

        count = 0
        hashmap = defaultdict(int)
        preorder(root, 0)
        return count

    def pathSum2(self, root, targetSum):
        def preorder(node, curr_sum):
            if not node:
                return 0
            count = 0
            curr_sum += node.val
            if curr_sum == targetSum:
                count += 1
            count += hashmap[curr_sum - targetSum]
            hashmap[curr_sum] += 1
            count += preorder(node.left, curr_sum)
            count += preorder(node.right, curr_sum)

            hashmap[curr_sum] -= 1
            return count
        hashmap = defaultdict(int)
        return preorder(root, 0)

sol = Solution()
# root = [10,5,-3,3,2,None,11,3,-2,None,1]
# targetSum = 8
root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
targetSum = 22
print(sol.pathSum(list_to_tree(root), targetSum))
print(sol.pathSum2(list_to_tree(root), targetSum))