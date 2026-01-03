class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_bst(root, val):
    """Insert value into BST"""
    if not root:
        return TreeNode(val)

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


if __name__ == "__main__":
    # Example usage
    nums = [5, 3, 8, 1, 4, 7, 9]
    root = list_to_bst(nums)
    print(root)
