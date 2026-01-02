"""
236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
"""

"""
Algorithm:
1. We create a function dfs to traverse through the tree. This function takes 1 argument Node
2. If the node is none, return False
3. Calculate left variable by calling dfs(node.left)
4. Calculate right variable by calling dfs(node.right)
5. Calculate mid variable value (mid = node == p or node == q)
6. If any two of the three mid, left, right are true, then we found the LCA.
7. Return mid or left or right
8. Call dfs(root)
"""
from src.helper.create_binary_tree import list_to_tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node.val == p or node.val == q
            if mid + left + right >= 2:
                self.ans = node
            return mid or left or right
        dfs(root)
        return self.ans

    def lowestCommonAncestor2(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

    def lca_node_doesnot_exist(self, root, p, q):
        result = {"lca": None, "pfound": False, "qfound": False}
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            mid = False
            if node == p:
                result["pfound"] = True
                mid = True
            if node == q:
                result["qfound"] = True
                mid = True

            if mid + left + right >= 2:
                result["lca"] = node
            return mid or left or right
        dfs(root)
        return result["lca"] if result["pfound"] and result["qfound"] else None



sol = Solution()
root = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 1
root = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 4
root = [1,2]
p = 1
q = 2
print(sol.lowestCommonAncestor(list_to_tree(root), p, q).val)
print(sol.lowestCommonAncestor2(list_to_tree(root), p, q).val)