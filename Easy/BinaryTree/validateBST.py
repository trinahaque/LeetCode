# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode, min=float('-inf'), max=float('inf')) -> bool:
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)