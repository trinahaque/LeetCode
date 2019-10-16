# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(n) --> because the tree has to traverse every node to determine 
# if it's symmetric

# Space Complexity: O(n) --> height of the tree --> for linear tree --> 
#  don't understand why O(n) since there is a null check

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self._isSymmetric(root.left, root.right)
    def _isSymmetric(self, left, right):
        # leaf node
        if left == None and right == None:
            return True
        # one is none, other is not
        elif left == None or right == None:
            return False
        elif left.val == right.val:
            # will it check for mirror twice?
            outer = self._isSymmetric(left.left, right.right)
            inner = self._isSymmetric(left.right, right.left)
            return outer and inner
        else: