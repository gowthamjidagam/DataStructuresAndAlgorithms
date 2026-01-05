class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_bst(root, val):
    """Insert value into BST"""
    if not root:
        return TreeNode(val)
    if val is None:
        return root

    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)

    return root


def list_to_bst(nums):
    """
    Convert list to BST by sequential insertion
    Time: O(N log N) average, O(N²) worst
    Space: O(N) for tree + O(H) for recursion

    :param nums: List of integers (can be unsorted)
    :return: Root of BST
    """
    if not nums:
        return None

    root = None
    for val in nums:
        root = insert_into_bst(root, val)

    return root


def bst_to_list_preorder(root):
    """
    Convert BST to list using preorder traversal
    Root → Left → Right

    Time: O(N), Space: O(N)
    """
    result = []

    def preorder(node):
        if node:
            result.append(node.val)  # Visit root first
            preorder(node.left)  # Visit left
            preorder(node.right)  # Visit right

    preorder(root)
    return result


def bst_to_list_inorder(root):
    """
    Convert BST to sorted list using inorder traversal
    Left → Root → Right

    Time: O(N), Space: O(N)
    """
    result = []

    def inorder(node):
        if node:
            inorder(node.left)  # Visit left
            result.append(node.val)  # Visit root
            inorder(node.right)  # Visit right

    inorder(root)
    return result


def bst_to_list_postorder(root):
    """
    Convert BST to list using postorder traversal
    Left → Right → Root

    Time: O(N), Space: O(N)
    """
    result = []

    def postorder(node):
        if node:
            postorder(node.left)  # Visit left
            postorder(node.right)  # Visit right
            result.append(node.val)  # Visit root last

    postorder(root)
    return result

if __name__ == "__main__":
    # Example usage
    nums = [5, 3, 8, 1, 4, 7, 9]
    root = list_to_bst(nums)
    print(root)
